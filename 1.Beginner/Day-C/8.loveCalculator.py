# Link for the Algorithm:
# https://www.buzzfeed.com/ariannarebolini/what-are-the-chances-your-crush-is-actually-your-true-love

print('Welcome to the Love Calculator!')
name1 = input('What is your name? \n')
name2 = input('What is their name? \n')

combined_string = name1 + name2
lowerCase = combined_string.lower()

t = lowerCase.count("t")
r = lowerCase.count("r")
u = lowerCase.count("u")
e = lowerCase.count("e")

true = t + r + u + e

l = lowerCase.count("l")
o = lowerCase.count("o")
v = lowerCase.count("v")
e = lowerCase.count("e")

love = l + o + v + e

loveScore = str(true) + str(love)

intScore = int(loveScore)

print(loveScore)

if (intScore < 10) or (intScore > 90):
    print(f'Your love score is {intScore}, you go together, like coke and mentos.')
elif (intScore >= 40) and (intScore <= 50):
    print(f'Your score is {intScore}, your are alright together!')
else:
    print(f'Your score is {intScore}')