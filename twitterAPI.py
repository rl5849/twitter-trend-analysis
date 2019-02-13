#Author: Robert Liedka
#
#Usage of twitters API
import requests
import twitter
import credentials


creds = credentials.credentials

api = twitter.Api(consumer_key=creds.consumer_key,
              consumer_secret=creds.consumer_secret,
              access_token_key=creds.access_token_key,
              access_token_secret=creds.access_token_secret)


get_trends_url = "https://api.twitter.com/1.1/trends/place.json"

def __init__():
    return


def getTrends():
    trends = twitter.api.Api.GetTrendsCurrent(api)

    print(trends)
    return


