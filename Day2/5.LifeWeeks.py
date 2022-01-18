# Create a program using maths and f-Strings that tells
# us how many days, weeks, months we have left if we
# live until 90 years old.
age = input('What is your current age? ')
months = int(age) * 12
days = int(age) * 365
weeks = int(age) * 52

years_remaining = 90 - int(age)
days_remaining = 90 * 365 - days
months_remaining = 12 * 90 - months
weeks_remaining = 52 * 90 - weeks

print(f'Your enjoy {months} months, {days} days, {weeks} weeks.')
print(f'Your will enjoy {months_remaining} months, {days_remaining} days, {weeks_remaining} weeks')
