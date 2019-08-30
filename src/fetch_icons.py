import json
import os
from urllib.request import urlretrieve
from pathlib import Path


def main(img_dir: str, users_list_path: str):
    with open(users_list_path, mode='r') as f:
        users = json.load(f)

    Path(img_dir).mkdir(exist_ok=True)

    for user in users:
        url = user['profile_image_url'].replace('_normal.jpg', '.jpg')
        path = os.path.join(img_dir, user['screen_name'] + '.jpg')
        urlretrieve(url, path)


if __name__ == '__main__':
    main(img_dir='img', users_list_path='resources/users.json')
