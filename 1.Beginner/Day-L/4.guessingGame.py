# Number Guessing Game!

from random import randint
from art import logo

# Generating the Random Number:
computer = randint(1, 100)

# Startint the game.
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Psst, the correct answer is {computer}")
dif = input("Choose a difficulty. Type [easy] or [hard]: ")


def diff(difficulty):
    """This function makes the game Guess the Word choosing by difficulty."""

    def check(number):
        """ This function checks if the Number is lower or high from the Guess."""
        if number > computer:
            print("Too high!")
            print("Guess again.")
            print(f"You have {i} attempts remaning to guess the number.")
        elif number < computer:
            print("Too low!")
            print("Guess again.")
            print(f"You have {i} attempts remaning to guess the number.")
        elif number == computer:
            print("Congratz! You're awesome!!!")
            exit()


    # Check the Difficulty, and give the total chances from player:
    if difficulty == "easy":
        for i in range(9, -1, -1):
            guess = int(input("Please guess a number between [1] and [100]: "))
            if i == 0:
                print("You've run out of guesses, you lose.")
            else:
                check(guess)
    elif difficulty == "hard":
        for i in range (4, -1, -1):
            guess = int(input("Please guess a number between [1] and [100]: "))
            if i == 0:
                print("You've run out of guesses, you lose.")
            else:
                check(guess)

# Calling the function xD
diff(dif)


# Angela make the program with a constant calling:
EASY_CHOICEE = 10
HARD_CHOICE = 5
# This make him don't need to put a function inside another
# function, my solution is great, but I dind't think on this
# and this turn my code less readable.
# This the more insane difference between his code and my code.
