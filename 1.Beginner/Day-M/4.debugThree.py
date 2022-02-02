for number in range(1, 101):
    # Use the "and" comparising statement.
    if number % 3 == 0 or number % 5 == 0:
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        # Retire [], is for print one by one.
        print([number])

