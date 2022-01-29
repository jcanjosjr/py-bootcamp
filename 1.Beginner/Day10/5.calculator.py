# Calculator Program with Py.

from art import logo

print(logo)


def calculator(numOne, ope, numTwo):
    """Resolves basics calculation."""
    if ope == "/":
        return numOne / numTwo
    elif ope == "*":
        return numOne * numTwo
    elif ope == "-":
        return numOne - numTwo
    elif ope == "+":
        return numOne + numTwo
    else:
        return "Invalid input."


numberOne = float(input("What's the frist number? "))
print("+ - * /")
operator = str(input("Pick an operation: "))
numberTwo = float(input("What's the next number? "))

result = []
result.append(calculator(numberOne, operator, numberTwo))

while True:
    print(f"{numberOne} {operator} {numberTwo} = {result[-1]}")
    choose = input(f"Type 'y' to continue calculating with {result[-1]}, or type 'n' to start a new calculation: ")
    if choose == 'y':
        operator = str(input("Pick an operation: "))
        numberTwo = float(input("What's the next number: "))       
        result.append(calculator(result[-1], operator, numberTwo))
    else:
        print("Goodbye.")
        break

result = []

# Above have my solution, now, we have the solution of a Engineer from IBM, xD


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Making a dict with functions, lul, did this works???? wtf
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def recursive():
    num1 = float(input("What's is the first number? "))

    for symbol in operations:
        print(symbol)
    shouldContinue = True

    while shouldContinue:
        operationSymbol = input("Pick an operation: ")
        num2 = float(input("What's is the second number? "))
        # Resolving the calc with Dict.
        calcSymbol = operations[operationSymbol]
        answer = calcSymbol(num1, num2)
        # Output the results:
        print(f"{num1} {operationSymbol} {num2} = {answer}")

        # Learning another thing, this two lines: lol xD
        if input("Type 'yes' to continue calculating with {answer}, or type 'new' to restart calculation:  ") == "y":
            num1 = answer
        else:
            shouldContinue = False
            recursive()

recursive()

# Basically, recursive is a function that call's himself.
