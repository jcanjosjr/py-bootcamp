# Make a random that means heads or tails.

from random import randint


randomInt = randint(0,1)

if randomInt == 1:
    print('Tails')
else:
    print('Head')