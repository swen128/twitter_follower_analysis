import os
import time

from tweepy_wrapper import api, cursor
from dotenv import load_dotenv


load_dotenv()
data_dir = os.environ.get('DATA_DIR')
users_list_path = os.environ.get('USERS_LIST_PATH')

with open(users_list_path, 'r') as f:
    screen_names = [name.strip() for name in f.readlines()]

for screen_name in screen_names:
    print('fetching followers of ' + screen_name)
    with open(os.path.join(data_dir, screen_name), mode="w", encoding="utf-8") as f:
        for page in cursor(api.followers_ids, screen_name=screen_name):
            ids = [str(i) + '\n' for i in page]
            f.writelines(ids)
            f.flush()
