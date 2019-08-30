import jsonstreams

from src.tweepy_wrapper import api, cursor


def main(users_list_path: str):
    screen_name = "nijisanji_app"
    list_name = "list1"

    with jsonstreams.Stream(jsonstreams.Type.array, users_list_path) as s:
        for page in cursor(api.list_members, slug=list_name, owner_screen_name=screen_name):
            for user in page:
                s.write(user._json)


if __name__ == '__main__':
    main(users_list_path='resources/users.json')
