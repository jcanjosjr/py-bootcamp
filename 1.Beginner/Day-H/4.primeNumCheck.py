# Check a prime number xD


def primeNumber(number):
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
    if isPrime and number != 0 and number != 1:
        print(f"This {number} is prime.")
    else:
        print(f"This {number} is not a prime number.")


test = int(input("What is the number you want to check? "))
primeNumber(test)
