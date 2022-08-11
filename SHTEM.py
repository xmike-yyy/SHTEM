import requests
import json
import os
import tweepy
import re
import wget
from bs4 import BeautifulSoup
consumer_key = "sBuVDXltogiJKX6FCaaugo9bL"
consumer_secret = "DVvQzj2HLj1YlafIbz2kXwlCvsVvd30KcZkpScbCcFLyRveSma"
access_token = "1442543873075527685-ejB1WfGT7rWLY6Qh1G6eUpwtLgwwX5"
access_token_secret = "BTo6jh8WTvioJwPA9YRkSILq3XlASCVgFONVM696Vy0E5"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

def download_tweets(twitter_links, directory):
  ids = get_ids(twitter_links)
  public_tweets = api.lookup_statuses(ids,tweet_mode="extended")  #used to be called statuses_lookup (AAAAAH)
  for tweet in public_tweets:
    media = (tweet.entities.get("media", []))
    if(len(media) > 0):
      img_links.append(media[0]["media_url"])
  for img_file in img_links:
    wget.download(img_file, out = "./" + directory + "/")
def get_ids(twitter_links):
  ids = []
  for link in twitter_links:
    ids.append(int(re.findall("[0-9]+",link.split("/status/")[1])[0]))
  return ids
client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAErZbAEAAAAAU2Dei6vGTecfREeXot8c7%2BEDrw4%3DOm2wluOZlb6c1cOLk8R6QbWzXAIRKNXpq2nQIGM3l1wZeqKYgV")
query = "climatechange"
tweet = client.search_recent_tweets(query= query)

for tweet in tweet.data:
    print(tweet.text)