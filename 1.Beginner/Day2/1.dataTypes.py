# Strings 
print("Hello"[0])
print("123" +  "345")

# Integer
print(123 + 345)
123_456_789

# Float
3.14159

# Boolean
True
False

# TypeErrors:
num_char = len(input('What is your name?'))
# print('Your name has ' + num_char + ' characters.')
# Can only concatenate str(not "int") to str.

# The function called type, basecally check whatever you
# put between the parenteheses and give the type.
print(type(num_char))

# For convert this int, to a String:
new_num_char = str(num_char)
print('Your name has ' + new_num_char + ' characters.')

# We can convert any type.
a = 123
print(type(a))
a = str(123)
print(type(a))
a = float(123)
print(type(a))
print(70 + float("100.5"))
print(str(70) + str(100))


# Write a program that adds the digits in a 2 digit number,
# if the input was 35, then the output should be 3 + 5 = 8.
two_digit_number = input('Type a two digit numbers: ')
print(int(two_digit_number[0]) + int(two_digit_number[1]))
