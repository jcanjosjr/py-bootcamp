import random

rock = '''
Rock!
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper!
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors!
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gameImages = [rock, paper, scissors]
userChoice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: '))
print(gameImages[userChoice])

computerChoice = random.randint(0, 2)
print('Computer choice: ')
print(gameImages[computerChoice])

if userChoice >= 3 or userChoice < 0:
    print('Your typed an invalid number, you lose xD')
elif userChoice == 0 and computerChoice == 2:
    print('You win!')
elif computerChoice == 2 and userChoice == 0:
    print('You lose!')
elif computerChoice > userChoice:
    print('Your lose.')
elif userChoice > computerChoice:
    print('You win!')
elif computerChoice == userChoice:
    print("It's a draw...")
