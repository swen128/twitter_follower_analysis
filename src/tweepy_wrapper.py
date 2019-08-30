import os
import time

import tweepy
from dotenv import load_dotenv

load_dotenv()
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def cursor(endpoint, *args, **kwargs):
    for page in tweepy.Cursor(endpoint, *args, **kwargs).pages():
        yield page
        time.sleep(60)
