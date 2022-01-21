print('Welcome to the Rollercoaster!')
height = int(input('What is your height in cm? '))

if height >= 120:
    print('You can ride!')
    age = int(input('What your age? '))
    if age < 12:
        print('Please, pay $5')
        pay = 5
    elif age > 18:
        print('Please, pay $12')
        pay = 12
    else:
        print('Please, pay $7')
        pay = 7
    photo = input('Want photos? [Y or N]: ')
    if photo == 'Y':
        pay += 3
        print('Please, pay $3')
        print(f'The total bill is ${pay}')    
    else:
        print(f'The total bill is ${pay}')    
else:
    print("You can't ride.")
