# Calculates the sum of all even numbers from 1 to 100.
total = 0

for number in range(0, 100):
    if number % 2 == 0:
        total += number

print(total)

# Other solution:
total2 = 0

for number2 in range(0, 100, 2):
    total2 += number2

print(total)
