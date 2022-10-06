
class User:
    def __init__(self, userid, username):
        self.userid = userid
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User(username='james', userid=23)
user2 = User(0, "Zion")

user1.follow(user2)
print(user2.followers)
print(user1.following)
