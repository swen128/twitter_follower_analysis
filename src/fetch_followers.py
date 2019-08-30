import json
from pathlib import Path

from tweepy import Cursor

from src.tweepy_wrapper import api


def main(users_list_path: str, out_dir: str):
    with open(users_list_path, 'r') as f:
        users = json.load(f)
        screen_names = [user['screen_name'] for user in users]

    Path(out_dir).mkdir(exist_ok=True)

    for screen_name in screen_names:
        print('fetching followers of ' + screen_name)

        cursor = Cursor(api.followers_ids, screen_name=screen_name, count=2048)
        out_path = Path(out_dir) / screen_name

        with open(out_path, mode="w", encoding="utf-8") as f:
            for user_id in cursor.items():
                f.write(f'{user_id}\n')
                f.flush()


if __name__ == '__main__':
    main(users_list_path='resources/users.json', out_dir='resources/followers')
