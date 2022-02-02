# Modifying Global Scope.
enemies = "Skeleton"


def increaseEnemies():
    enemies = "Zombie"
    print(f"Enemies inside function: {enemies}")


increaseEnemies()
print(f"Enemies outisde function: {enemies}")


increaseValue = 1


def modifyGlobal():
    global increaseValue
    increaseValue += 1


# Probably don't actually want to do this very often, because
# it's confusing and it's prone to creating bugs and errors.
# Because this variable with global scope could been created
# anywhere in your code.
# For modifying a Global Scope, this is the best practice:
friends = 1


def increaseFriends():
    print(f"Friends inside function: {friends}")
    return friends + 1


friends = increaseFriends()
print(f"Friends outisde function: {friends}")
