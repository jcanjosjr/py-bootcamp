# Debugging, the process of removing bugs from you code.
# The first documented bug was actually found by this lady,
# Grace Hopper, she was probably one of the first programmers
# and one of the pioneers of the job that we're undertaking.


# Describe problem
def myFunction():
    for i in range(1, 20):
        if i == 20:
            print("You got it!")


myFunction()
# The for loop walks through a range between one and twenty, but
# when it reaches nineteen, automatically he scapes the loop and
# don't print the output information.
# To fix, just make the loop through a range between one and
# twenty-one.

# Reproduce the bug:
from random import randint

diceImgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
diceNum = randint(1, 6)
print(diceImgs[diceNum])

# The IndexError is because the list have the range between
# 0 and 5 index, and the randint walks between the 1-6,
# if the randint resolves to six, we get a IndexError.
# To fix, just make the loop through a range between zero and five.
