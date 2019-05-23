import os
import time

import tweepy
from dotenv import load_dotenv


load_dotenv()
data_dir = os.environ.get('DATA_DIR')
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

with open(os.path.join(data_dir, 'nijisanji_livers'), 'r') as f:
    screen_names = [name.strip() for name in f.readlines()]

for screen_name in screen_names:
    print('fetching followers of ' + screen_name)
    with open(os.path.join(data_dir, screen_name), mode="w", encoding="utf-8") as f:
        cursor = tweepy.Cursor(api.followers_ids, screen_name=screen_name)
        for page in cursor.pages():
            ids = [str(i) + '\n' for i in page]
            f.writelines(ids)
            f.flush()
            time.sleep(60)
