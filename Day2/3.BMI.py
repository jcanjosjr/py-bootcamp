# Write a program that calculates the Body Mass Index (BMI) from
# a user's weight and height.
# BMI = weight / height²
height = input('Enter your Height in m: ')
weight = input('Enter your weight in kg: ')
bmi = float(weight) / float(height) ** 2
print(int(bmi))
