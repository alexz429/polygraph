from src.definitions import ROOT_PATH
from src.assertion_finder import AssertionFinder
from src.textual_entailment import TextualEntailment
from src.wolfram import WolframAPI
import json


class Polygraph:
    def __init__(self, top_n=10):
        self.top_n = top_n
        self.assertion_finder = AssertionFinder()
        self.wolfram_api = WolframAPI()
        self.hypothesis_tester = TextualEntailment()

    def run(self, captions: str) -> str:  # Both input and output strings must be valid JSON
        captions = json.loads(captions)
        assertion_scores = self.assertion_finder.parse_captions(captions)
        print(assertion_scores)
        assertions = sorted(assertion_scores.items(), key=lambda x: x[1], reverse=True)[:self.top_n]
        assertions = {k: {"score": v, "claim": captions[k]} for k, v in assertions}

        for timestamp, assertion in assertions.items():
            assertion["wolfram_response"] = self.wolfram_api.query(assertion)
            assertion["is_factual"] = self.hypothesis_tester.run(assertion["wolfram_response"],
                                                                 assertion["claim"])

        invalid_assertions = {k: v for k, v in assertions if not assertions["is_factual"]}
        return json.dumps(invalid_assertions)


if __name__ == "__main__":
    p = Polygraph()
    with open(str(ROOT_PATH / "data/sample.txt")) as file:
        print("".join(file.readlines()))
        p.run("".join(file.readlines()))
        file.close()

