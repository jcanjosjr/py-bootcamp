# Local vs Global Scope.

# Global Scope
enemies = 1


def increaseEnemies():
    enemies = 2
    # Local Scope
    print(f"Enemies inside, function: {enemies}")


increaseEnemies()
print(f"Enemies outside Function: {enemies}")
# Global Scope:
playerHealth = 20


# Local Scope existis within functions.
def drinkPotion():
    potionStrength = 2
    print(playerHealth)


drinkPotion()
#print(potionStrength)   # Variable is not defined.

# In python don't have block scope, like Java or C++.
gameLevel = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if gameLevel < 5:
    newEnemy = enemies[0]

print(newEnemy)

# Only inside a Function we have Scopes, on if statements or
# loops statements, are all Global Scope.
