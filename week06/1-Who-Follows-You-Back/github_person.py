import requests
from settings import ID, SECRET, GITHUB_API


class Person:

    def __init__(self, user_api_url):
        person_info = requests.get(
            user_api_url + "?client_id={}&client_secret={}".
            format(ID, SECRET)).json()

        self.url = person_info["url"]
        self.login = person_info["login"]

        self.following_url = self.url + "/following" + \
            "?client_id={}&client_secret={}". format(ID, SECRET)

        self.followers_url = self.url + "/followers" + \
            "?client_id={}&client_secret={}". format(ID, SECRET)

        self.followers_json = requests.get(self.followers_url).json()
        self.following_json = requests.get(self.following_url).json()

        self.followers = []
        self.following = []

    def __repr__(self):
        return str(self.login)

    def __str__(self):
        return str(self.login)

    def __eq__(self, other):
        return self.login == other.login

    def __hash__(self):
        return hash(self.url)

    def build_followers(self):
        for follower in self.followers_json:
            url = GITHUB_API + follower["login"] + \
                "?client_id={}&client_secret={}" . format(ID, SECRET)
            person = Person(url)
            self.followers.append(person)

    def build_following(self):
        for following in self.following_json:
            url = GITHUB_API + following["login"] + \
                "?client_id={}&client_secret={}" . format(ID, SECRET)
            person = Person(url)
            self.following.append(person)

    def get_followers(self):
        return self.followers

    def get_following(self):
        return self.following
