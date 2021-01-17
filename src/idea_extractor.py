import json

from src.definitions import SETTINGS
import requests


class IdeaExtractor:
    def __init__(self):
        self.base_url = "https://htn-poly-text.cognitiveservices.azure.com/text/analytics/v3.0/keyPhrases"

        self.headers = {
            'Ocp-Apim-Subscription-Key': SETTINGS["idea_extractor"]["api_key"],
            'Content-Type': "application/json",
            'Accept': "application/json",
            'Cache-Control': "no-cache",
            'Host': "htn-poly-text.cognitiveservices.azure.com",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

    def get_ideas(self, claims):
        body = {"documents": []}
        for key, claim in claims.items():
            body["documents"].append(
                {
                    "language": "en",
                    "id": key,
                    "text": claim
                }
            )

        payload = json.dumps(body)

        response = requests.request("POST", self.base_url, data=payload, headers=self.headers)
        resp_dict = json.loads(response.text)
        out_dict = dict()
        for idea in resp_dict["documents"]:
            out_dict[idea["id"]] = idea["keyPhrases"]
