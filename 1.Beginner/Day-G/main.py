# Hangman Project
import random

from click import clear
from hangmanWords import wordList
from hangmanArt import logo
from hangmanArt import stages

# Starting the project:
print(logo)
finish = False
lives = len(stages) - 1

# Resolving the random word.
randWord = random.choice(wordList)
wordLength = len(randWord)

blank = []

for _ in range(wordLength):
    blank += "_"

while not finish:
    guess = input("Guess a letter: ").lower()

    # Using the clear() function to clear the output.
    clear()

    if guess in blank:
        print(f"You've already guessed {guess}")
    
    for position in range(wordLength):
        letter = randWord[position]
        if letter == guess:
            blank[position] = letter
    print(f"{' '.join(blank)}")

    if guess not in randWord:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            finish = True
            print("You lose.")
    
    if not "_" in blank:
        finish = True
        print("You win.")
    
    print(stages[lives])
