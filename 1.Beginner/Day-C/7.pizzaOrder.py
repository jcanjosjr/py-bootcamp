# Based on user's order, work out their final bill.


while True:
    print('Welcome to Python Pizza!')
    size = input('What size pizza do you want? [S, M or L]: ')
    if size == 'S':
        bill = 15
        break
    elif size == 'M':
        bill = 20
        break
    elif size == 'L':
        bill = 25
        break
    else:
        continue

while True:
    addPepperoni = input('Do you want pepperoni? [Y or N]: ')
    if addPepperoni == 'Y':
        if size == 'S':
            bill += 2
            break
        else:
            bill += 3
            break
    if addPepperoni == 'N':
        break
    else:
        continue

while True:
    extraCheese = input('Do you want extra cheese? [Y or N]: ')
    if extraCheese == 'Y':
        bill += 1
        break
    if extraCheese == 'N':
        break
    else:
        continue

print(f'The order came to you, the bill is ${bill}')