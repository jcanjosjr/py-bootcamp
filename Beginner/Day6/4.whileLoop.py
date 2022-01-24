"""
# the For loop:
for item in listItems:
    # Do something to each item

for number in range(a, b):
    print(number)


# the While loop:
while somethingTrue:
    # Do something.
"""


def jump():
    print('Jump!')


numberHurdles = 6
while numberHurdles > 0:
    jump()
    numberHurdles -= 1


# Challeng: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

# Reeborg has entered a hurdle race:

"""
My solution:


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def path():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
     path()
"""
