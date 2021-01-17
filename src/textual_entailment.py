from allennlp.predictors.predictor import Predictor
import allennlp_models.pair_classification


class TextualEntailment:
    def __init__(self):
        self.predictor = Predictor.from_path(
            "https://storage.googleapis.com/allennlp-public-models/mnli_roberta-2020.06.09.tar.gz",
            "textual_entailment")

    def calculate_entailment(self, premise: str, hypothesis: str):
        results = self.predictor.predict(hypothesis, premise).get('probs')
        e, c, n = results[0], results[1], results[2]
        return e, c, n
