import json
from logging import getLogger, StreamHandler, INFO
from pathlib import Path
from time import sleep

from tweepy import Cursor

from src.tweepy_wrapper import api

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(INFO)
logger.setLevel(INFO)
logger.addHandler(handler)
logger.propagate = False


def main(users_list_path: str, out_dir: str):
    with open(users_list_path, 'r') as f:
        users = json.load(f)
        screen_names = [user['screen_name'] for user in users]

    Path(out_dir).mkdir(exist_ok=True)

    for screen_name in screen_names:
        out_path = Path(out_dir) / screen_name

        if not out_path.exists():
            logger.info(f'Fetching followers of: {screen_name}')

            cursor = Cursor(api.followers_ids, screen_name=screen_name, count=2048)
            out_path = Path(out_dir) / screen_name

            with open(out_path, mode="w", encoding="utf-8") as f:
                for page in cursor.pages():
                    for user_id in page:
                        f.write(f'{user_id}\n')
                        f.flush()
                    sleep(60)


if __name__ == '__main__':
    main(users_list_path='resources/users.json', out_dir='resources/followers')
