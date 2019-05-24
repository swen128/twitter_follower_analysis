import os
import time

from tweepy_wrapper import api, cursor
from dotenv import load_dotenv


load_dotenv()
data_dir = os.environ.get('DATA_DIR')
users_list_path = os.environ.get('USERS_LIST_PATH')

screen_name = "nijisanji_app"
list_name = "list1"

with open(users_list_path, mode="w", encoding="utf-8") as f:
    for page in cursor(api.list_members, slug=list_name, owner_screen_name=screen_name):
        names = [user.screen_name + '\n' for user in page]
        f.writelines(names)
        f.flush()