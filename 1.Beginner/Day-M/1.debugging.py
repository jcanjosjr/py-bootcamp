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

# Play Compute xD
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a Millenial!")
elif year > 1994:
    print("You are a Gen Z.")

# The problem from a input like 1994, it's this not resolves
# to any if statements, is simple resolve if put >= and <= on
# first if statement.

# Fix the Errors
age = int(input("How old are you?"))
if age > 18:
    print("You can drive at age {age}")

# This is a indent error, and is easy to resolve.
# Ever a line have the "refeson cobrinha" this is a error.
# The input is good to resolves a int too.

# Print is your friend xD
pages = 0
wordPerPage = 0
pages = int(input("Number of pages: "))
wordPerPage == int(input("Number of words per page: "))
totalWords = pages + wordPerPage
print(totalWords)


# Just print the variables and find what variable making
# the "false" output.
# Print always a good friend xD
# For correct the code, just make a adjust on "==", because
# with a correct logic, you want to add this input, not
# compare.

# Use a Debugger.
def mutate(aList):
    bList = []
    for item in aList:
        newItem = item * 2
    bList.append(newItem)
    print(bList)

mutate([1, 2, 3, 4, 5, 8, 13])

# This error occours because a identation, the append is
# outside the "for" statement, and don't add all the itens,
# just the last.
# Or i'm a Genious, or i don't need the debugger, lul

# Tips:
# 7. Take a Break, just have a cup of tea or have a nap.
# 8. Ask a friend, preferably a developer, but they don't have to be.
# 9. Run Often, don't wait until you've written loads of code to hit run.
# 10. Ask Google/StackOverflow.
