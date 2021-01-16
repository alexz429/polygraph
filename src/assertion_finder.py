from src.definitions import ROOT_PATH, SETTINGS
import requests


class AssertionFinder:
    def __init__(self):
        import requests

        url = "https://idir.uta.edu/claimbuster/api/v2/score/text/Hello%20there"

        headers = {
            'x-api-key': SETTINGS["assertion_finder"]["api_key"],
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Host': "idir.uta.edu",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.text)

    def assertion_likelihood(self, sentence: str) -> float:
        return 0.5

    def parse_captions(self, captions: dict) -> dict:
        full_text = " ".join(captions.values())
        doc = self.nlp(full_text)
        return {k: self.assertion_likelihood(v) for k, v in captions.items()}
