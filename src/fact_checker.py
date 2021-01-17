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

    def get_debunked_articles(self, query):
        # p = self.params
        # p["query"] = query
        # response = requests.request("GET", self.base_url, headers=self.headers, params=p)
        # print(response.text)
        articles = {
            "claims": [
                {
                    "text": "\"The Russian vaccine – it is now completely obvious … is the best one worldwide. [N]o other preparations of a similar kind demonstrate such a level of protection and such a degree of safety.”",
                    "claimant": "Vladimir Putin",
                    "claimDate": "2021-01-15T00:00:00Z",
                    "claimReview": [
                        {
                            "publisher": {
                                "name": "POLYGRAPH.info",
                                "site": "polygraph.info"
                            },
                            "url": "https://www.polygraph.info/a/putin-sputnik-coronavirus-vaccine/31048033.html",
                            "title": "Putin's Baseless Brag About Russian COVID-19 Vaccine",
                            "reviewDate": "2021-01-15T00:00:00Z",
                            "textualRating": "Unsubstantiated",
                            "languageCode": "en"
                        }
                    ]
                },
                {
                    "text": "A study found asymptomatic transmission of COVID-19 didnt occur at all.",
                    "claimant": "LifeSiteNews, Posts on Facebook and Instagram",
                    "claimDate": "2021-01-14T03:30:25Z",
                    "claimReview": [
                        {
                            "publisher": {
                                "name": "BOOM FACT Check",
                                "site": "boomlive.in"
                            },
                            "url": "https://www.boomlive.in/world/covid-19-asymptomatic-transmission-misleading-claim-11537",
                            "title": "Did A Study Find COVID-19 Asymptomatic Transmission Does Not Exist?",
                            "reviewDate": "2021-01-14T03:30:25Z",
                            "textualRating": "Misleading",
                            "languageCode": "en"
                        }
                    ]
                },
                {
                    "text": "Make sure you and your family all dig out your NHS number and have a copy of it immediately to hand for the Covid jab. NHS staff on the front line say this is the biggest bottleneck when it comes to administering the vaccine to as many people as quickly as possible.",
                    "claimReview": [
                        {
                            "publisher": {
                                "name": "Full Fact",
                                "site": "fullfact.org"
                            },
                            "url": "https://fullfact.org/online/nhs-number-coronavirus-vaccine/",
                            "reviewDate": "2021-01-12T00:00:00Z",
                            "textualRating": "You do not need to have your NHS number with you in order to receive the vaccine. A name and date of birth is all that is required, although some trusts have asked patients to bring their NHS numbers if possible.",
                            "languageCode": "en"
                        }
                    ]
                },
                {
                    "text": "Barack Obama has asked Africans not to accept vaccines that'll come from America and Europe, calling it \"an evil act white people want to do to Africans\".",
                    "claimant": "Social media users",
                    "claimDate": "2021-01-08T00:00:00Z",
                    "claimReview": [
                        {
                            "publisher": {
                                "name": "India Today",
                                "site": "indiatoday.in"
                            },
                            "url": "https://www.indiatoday.in/fact-check/story/fact-check-obama-never-warned-africans-against-covid-19-vaccines-from-us-europe-1757718-2021-01-10",
                            "title": "Fact Check: Obama never warned Africans against Covid-19 ...",
                            "reviewDate": "2021-01-10T00:00:00Z",
                            "textualRating": "False",
                            "languageCode": "en"
                        }
                    ]
                },
                {
                    "text": "Barack Obama has not warned against getting the COVID-19 vaccine.",
                    "claimant": "Posts on Facebook and Twitter",
                    "claimDate": "2021-01-08T13:55:29Z",
                    "claimReview": [
                        {
                            "publisher": {
                                "name": "BOOM FACT Check",
                                "site": "boomlive.in"
                            },
                            "url": "https://www.boomlive.in/world/barack-obama-covid-19-vaccine-11468",
                            "title": "Barack Obama Has Endorsed COVID-19 Vaccines",
                            "reviewDate": "2021-01-08T13:55:29Z",
                            "textualRating": "False",
                            "languageCode": "en"
                        }
                    ]
                },
                {
                    "text": "Justin Trudeau violated COVID-19 guidelines to go to Barbados.",
                    "claimant": "Conservative Beaver, Facebook posts",
                    "claimDate": "2021-01-08T13:48:57Z",
                    "claimReview": [
                        {
                            "publisher": {
                                "name": "BOOM FACT Check",
                                "site": "boomlive.in"
                            },
                            "url": "https://www.boomlive.in/world/justin-trudeau-did-not-go-to-barbados-violating-covid-19-guidlines-11467",
                            "title": "Justin Trudeau Did Not Violate COVID-19 Guidelines To Go To Barbados",
                            "reviewDate": "2021-01-08T13:48:57Z",
                            "textualRating": "False",
                            "languageCode": "en"
                        }
                    ]
                },
                {
                    "text": "Time Magazine did a feature on UPs response to the Covid-19 pandemic",
                    "claimant": "Zee News, ABP Ganga, News18 UP, TV9 Bharatvarsh, Patrika UP",
                    "claimDate": "2021-01-06T10:28:53Z",
                    "claimReview": [
                        {
                            "publisher": {
                                "name": "BOOM FACT Check",
                                "site": "boomlive.in"
                            },
                            "url": "https://www.boomlive.in/fact-check/time-magazine-up-government-praise-covid-yogi-adityanath-article-zee-news-abp-news-patrika-tv9bharatvarsh-news18-up-11416",
                            "title": "Did TIME Praise Yogi Adityanath's COVID-19 Management? A FactCheck",
                            "reviewDate": "2021-01-06T10:28:53Z",
                            "textualRating": "False",
                            "languageCode": "en"
                        }
                    ]
                },
                {
                    "text": "CNN story writes that Doctors encourage COVID-19 vaccine injections in penis",
                    "claimant": "Facebook and Twitter Users",
                    "claimDate": "2021-01-04T14:15:11Z",
                    "claimReview": [
                        {
                            "publisher": {
                                "name": "BOOM FACT Check",
                                "site": "boomlive.in"
                            },
                            "url": "https://www.boomlive.in/fact-check/fact-check-viral-news-doctors-covid-19-vaccine-injections-in-penis-cnn-news-11392",
                            "title": "Check: Did Doctors Encourage Covid19 Vaccine Injections In Penis?",
                            "reviewDate": "2021-01-04T14:15:11Z",
                            "textualRating": "False",
                            "languageCode": "en"
                        }
                    ]
                },
                {
                    "text": "Patients who were administered with the COVID-19 vaccine did not start eating each other.",
                    "claimant": "Posts on Facebook and Twitter",
                    "claimDate": "2020-12-30T07:26:41Z",
                    "claimReview": [
                        {
                            "publisher": {
                                "name": "BOOM",
                                "site": "boomlive.in"
                            },
                            "url": "https://www.boomlive.in/world/fake-news-covid-19-vaccine-patients-eat-each-other-11341",
                            "title": "No, Patients Did Not Eat Each Other After Getting COVID-19 Vaccine",
                            "reviewDate": "2020-12-30T07:26:41Z",
                            "textualRating": "False",
                            "languageCode": "en"
                        }
                    ]
                },
                {
                    "text": "Mike Pence faked getting the COVID-19 vaccine.",
                    "claimant": "Posts on Facebook and Twitter",
                    "claimDate": "2020-12-30T07:20:19Z",
                    "claimReview": [
                        {
                            "publisher": {
                                "name": "BOOM FACT Check",
                                "site": "boomlive.in"
                            },
                            "url": "https://www.boomlive.in/world/mike-pence-covid-19-vaccine-fake-news-11339",
                            "title": "US Vice President Mike Pence Did Not Fake Getting COVID-19 Vaccine",
                            "reviewDate": "2020-12-30T07:20:19Z",
                            "textualRating": "False",
                            "languageCode": "en"
                        }
                    ]
                }
            ],
            "nextPageToken": "CAo"
        }

        debunk_ratings = ["false", "misleading", "unsubstantiated", "inaccurate"]
        return [v for v in articles["claims"] if v["claimReview"][0]["textualRating"].lower() in debunk_ratings]

