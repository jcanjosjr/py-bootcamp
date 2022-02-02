import random


nameString = input("Give me everybody's names, separeted by a comma. ")
names = nameString.split(', ')

numItems = len(names)
randomChoice = random.randint(0, numItems -1)

print(f'{names[randomChoice]} is pay the bill!')