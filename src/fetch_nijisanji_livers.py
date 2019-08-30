import jsonstreams
from tweepy import Cursor

from src.tweepy_wrapper import api


def main(users_list_path: str):
    screen_name = "nijisanji_app"
    list_name = "list1"
    cursor = Cursor(api.list_members, slug=list_name, owner_screen_name=screen_name)

    with jsonstreams.Stream(jsonstreams.Type.array, users_list_path) as s:
        for user in cursor.items():
            s.write(user._json)


if __name__ == '__main__':
    main(users_list_path='resources/users.json')
