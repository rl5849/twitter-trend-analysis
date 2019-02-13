#Author: Robert Liedka
#
#Usage of twitters API
import requests
import twitter


class twitter:
    API = twitter.api(consumer_key=[consumer key],
                  consumer_secret=[consumer secret],
                  access_token_key=[access token],
                  access_token_secret=[access token secret])


    usage_url = "https://api.twitter.com/1.1/trends/place.json"

    def __init__(self):
        return


    def getTrends(self):
        data = requests.get("https://api.twitter.com/1.1/trends/place.json?id=1")
        if(data.status_code != 200):
            print("Error getting data")
        data.json()

        print(data)
        return

    def sendRequest(self, requestString):
