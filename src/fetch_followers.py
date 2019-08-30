import json
import os

from src.tweepy_wrapper import api, cursor


def main(data_dir: str, users_list_path: str):
    with open(users_list_path, 'r') as f:
        users = json.load(f)
        screen_names = [user['screen_name'] for user in users]

    for screen_name in screen_names:
        print('fetching followers of ' + screen_name)
        with open(os.path.join(data_dir, screen_name), mode="w", encoding="utf-8") as f:
            for page in cursor(api.followers_ids, screen_name=screen_name):
                ids = [str(i) + '\n' for i in page]
                f.writelines(ids)
                f.flush()


if __name__ == '__main__':
    main(data_dir='resources', users_list_path='resources/users.json')
