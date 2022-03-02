class User:
    # Initialize the attributes.
    def __init__(self, userId, username):
        self.id = userId
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        # this line introduces 1 on followers of the object that
        # receive the follow.
        user.followers += 1
        # this line introduces 1 on following of the object that
        # call the function and follow a new user.
        self.following += 1

userOne = User(1, "josec")

print(userOne.username)
print(userOne.followers)


userOne.follow(userTwo)


class Car:
    def __init__(self, seats):
        self.seats = seats


# userOne = User()
# userOne.id = "01"
# userOne.username = "josec"
# print(userOne.username)
# userTwo = User()
# userTwo.id = "02"
# userTwo.username = "vanessal"
# print(userTwo.id)

