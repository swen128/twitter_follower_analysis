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

screen_name = "nijisanji_app"
list_name = "list1"
cursor = tweepy.Cursor(
    api.list_members,
    slug=list_name,
    owner_screen_name=screen_name
)

with open(os.path.join(data_dir, "nijisanji_livers"), mode="w", encoding="utf-8") as f:
    for page in cursor.pages():
        names = [user.screen_name + '\n' for user in page]
        f.writelines(names)
        f.flush()
        time.sleep(60)