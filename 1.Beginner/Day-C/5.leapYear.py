# Write a program that works out wheter if a given year is
# a leap year.

year = int(input('What year you want to check? '))

# on every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap year.')
        else:
            print('Not a leap year.')
    else:
        print('Leap year.')
else:
    print('Not a leap year.')
