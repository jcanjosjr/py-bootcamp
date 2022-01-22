# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00) * 1.12.
print('Welcome to the tip Calculator.')
bill = float(input('What is the total bill? $' ))
tip = int(input('What percentage tip would you like to give? %'))
split = int(input('How many people to split the bill? '))

bill_tip = (bill * (1 + tip / 100)) / 7

print(f'R$ {round(bill_tip, 2)}')