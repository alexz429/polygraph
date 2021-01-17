from src.definitions import ROOT_PATH, SETTINGS
from src.assertion_finder import AssertionFinder
from src.textual_entailment import TextualEntailment
from src.fact_checker import FactChecker
from src.idea_extractor import IdeaExtractor
import json

from flask import Flask, request, jsonify


class Polygraph:
    def __init__(self, top_n=5):
        self.top_n = top_n
        self.assertion_finder = AssertionFinder()
        self.fact_checker = FactChecker()
        self.idea_extractor = IdeaExtractor()
        self.hypothesis_tester = TextualEntailment()

    def run(self, captions: dict) -> dict:  # Both input and output must be dicts
        # captions = json.loads(captions)
        assertion_scores = self.assertion_finder.parse_captions(captions)
        print(assertion_scores)
        assertions = sorted(assertion_scores.items(), key=lambda x: x[1]["claim_score"], reverse=True)[:self.top_n]
        assertions = \
            {
                k: {
                    "score": v,
                    "claim": v["claim"],
                    "claim_score": v["claim_score"]
                } for (k, v) in assertions
            }

        claims = {k: x["claim"] for k, x in assertions.items()}
        ideas = self.idea_extractor.get_ideas(claims)
        for key, idea in ideas.items():
            assertions[key]["ideas"] = ideas[key]

        out_assertions = dict()
        for timestamp, assertion in assertions.items():
            print(timestamp)
            articles = [self.fact_checker.get_debunked_articles(idea) for idea in assertion["ideas"][:4]]
            # Flatten 2d array
            articles = [article for idea_articles in articles for article in idea_articles]

            max_e = (0, 0, 0)
            closest_article = None
            for article in articles:
                e, c, n = self.hypothesis_tester.calculate_entailment(assertion["claim"], article["text"])
                if e > max_e[0]:
                    max_e = (e, c, n)
                    closest_article = article

            if closest_article is None:
                continue

            print(closest_article)

            print(max_e)
            print("\n\n\n")

            if max_e[0] < SETTINGS["polygraph"]["entailment_threshold"]:
                continue

            out_assertions[timestamp] = {
                "original_claim": assertion["claim"],
                "textual_rating": closest_article["claimReview"][0]["textualRating"],
                "title": closest_article["text"],
                "url": closest_article["claimReview"][0]["url"],
                "confidence": max_e[0]
            }

        return out_assertions

if __name__ == "__main__":
    p = Polygraph()
    with open(str(ROOT_PATH / "data/sample.json")) as file:
        p.run(json.load(file))
        file.close()


app = Flask(__name__)
print("Flask App Initialized")
p = Polygraph()


@app.route('/')
def hello_word():
    return 'Hello world'


@app.route('/analyze', methods=["POST"])
def get_polygraph():
    input_json = request.get_json(force=True)
    result = p.run(input_json)
    print(result)
    return jsonify(result)
