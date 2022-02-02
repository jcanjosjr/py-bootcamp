# A game with comparising instagram followers between persons.

from art import logo, vs
from data import data
import random


def randData(text):
    """Get a random metadata on the archive."""
    return random.choice(text)


def formatData(text):
    """Format the List[{Dict}] into a String."""
    name = text["name"]
    desc = text["description"]
    country = text["country"]
    return f"{name}, a {desc}, from {country}"


def game():
    """Start the game, and compare the stars!"""
    personA = randData(data)
    personB = randData(data)
    print(f"Compare A: {formatData(personA)}")
    print(f"Compare B: {formatData(personB)}")


game()
