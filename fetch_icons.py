import json
import os
from urllib.request import urlretrieve

from dotenv import load_dotenv

load_dotenv()
img_dir = os.environ.get('IMG_DIR')
users_list_path = os.environ.get('USERS_LIST_PATH')

with open(users_list_path, mode='r') as f:
    users = json.load(f)

for user in users:
    url = user['profile_image_url'].replace('_normal.jpg', '.jpg')
    path = os.path.join(img_dir, user['screen_name'] + '.jpg')
    urlretrieve(url, path)
