import os

import jsonstreams
from dotenv import load_dotenv

from tweepy_wrapper import api, cursor

load_dotenv()
data_dir = os.environ.get('DATA_DIR')
users_list_path = os.environ.get('USERS_LIST_PATH')

screen_name = "nijisanji_app"
list_name = "list1"

with jsonstreams.Stream(jsonstreams.Type.array, users_list_path) as s:
    for page in cursor(api.list_members, slug=list_name, owner_screen_name=screen_name):
        for user in page:
            s.write(user._json)
