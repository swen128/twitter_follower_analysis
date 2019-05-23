import os

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

screen_name = "nijisanji_app"
for twilist in api.lists_all(screen_name=screen_name):
    print("slug="+twilist.slug)
    print("name="+twilist.name)


# slug=list
# name=【公式】にじさんじ統合以降
# slug=list1
# name=【公式・全体】にじさんじ
# slug=seeds1
# name=【公式】にじさんじSEEDs出身
# slug=list2
# name=【公式】にじさんじゲーマーズ出身
# slug=1-21
# name=【公式】にじさんじ1・2期出身