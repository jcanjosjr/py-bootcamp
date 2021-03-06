# A game with comparising instagram followers between persons.
from art import logo, vs
from data import data
import random
import click


# Getting a random data on archive.
def randData(text):
    """Get a random metadata on the archive."""
    return random.choice(text)


# Formating the output from the Dict format.
def formatData(text):
    """Format the {'Dict': Format} into a readable String."""
    name = text["name"]
    desc = text["description"]
    country = text["country"]
    return f"{name}, a {desc}, from {country}"


def game():
    """Start the game, and compare the stars!"""
    recursive = True
    i = 0
    # I like to use recursive for calling again the same "recurse"
    while recursive:
        # Basically, I just this to repeat one time.
        if i == 0:   
            score = 0
            personA = randData(data)
            print(logo)
        
        # Defining, person Two and printing the "menu".
        personB = randData(data)
        print(f"Compare A: {formatData(personA)}.")
        print(vs)
        print(f"Compare B: {formatData(personB)}.")
        guess = input("Who has more followers? Type [A] or [B]: ")
        # Comparising the persons, clear the Output and logic for results.
        if personA['follower_count'] > personB['follower_count'] and guess == 'A':
            click.clear()
            score += 1
            print(logo)
            print(f"        You're right! Current score: {score}!")
            i += 1
        elif personA['follower_count'] < personB['follower_count'] and guess == 'B':
            score += 1
            click.clear()
            print(logo)
            print(f"        You're right! Current score: {score}!")
            i += 1
            personA = personB
        else:
            click.clear()
            print(logo)
            print(f"        Sorry, that's wrong. Final score: {score}. :(")
            # Breaking the loop just where I want to finally.
            recursive = False


# Starting the game.
game()
