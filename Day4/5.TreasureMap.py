import random

print('Welcome to the Treasure Map.')

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# Defined the arguments passed to position:
horizontal = int(position[0]) # 2
vertical = int(position[1]) # 3

# Using the -1 condition to select the field.
selectRow = map[vertical - 1]
selectRow[horizontal - 1] = "X"

# Print the result:
print(f"{row1}\n{row2}\n{row3}")
