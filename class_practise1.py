from curses.ascii import US
from mimetypes import init


class User:
    def __init__(self, userid, username):
        self.userid = userid
        self.username = username
        self.followers = 10


user1 = User(username='james', userid=23)
print(user1.username)
print(user1.userid)
print(user1.followers)
