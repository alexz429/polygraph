import requests
from src.definitions import SETTINGS


class FactChecker:
    def __init__(self):
        self.base_url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"

        self.params = {
            "languageCode": "en-US",
            "maxAgeDays": "10000",
            "key": SETTINGS["fact_checker"]["api_key"]
        }

        self.headers = {
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Host': "factchecktools.googleapis.com",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

    def check_fact(self, query):
        p = self.params
        p["query"] = query
        response = requests.request("GET", self.base_url, headers=self.headers, params=p)
        print(response.text)
