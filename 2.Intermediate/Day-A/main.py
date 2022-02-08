MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}

profit = 0
resources = {
    "water": 500,
    "milk": 500,
    "coffee": 300
}

on = True


def resourceSufficiente(orderIngredients):
    """Validate if the resources of the coffee machine is sufficient to make a drink."""
    for item in orderIngredients:
        if orderIngredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def processCoins():
    """Return the total values for the coins input on coffee machine."""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def transactionSuccessful(moneyReceived, drinkCost):
    "Return True when the payment is accepted, or False if money is insufficient"
    if moneyReceived >= drinkCost:
        change = round(moneyReceived - drinkCost, 2)
        print(f"Here is ${change} in change.")
        # Indicates that profit, is a global variable.
        global profit
        profit += drinkCost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def makeCoffee(drinkName, orderIngredients):
    """Deduct the required ingredients from the resources."""
    for item in orderIngredients:
        resources[item] -= orderIngredients[item]
        print(f"Here is your {drinkName}")


while on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee :{resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if resourceSufficiente(drink["ingredients"]):
            payment = processCoins()
            if transactionSuccessful(payment, drink["cost"]):
                makeCoffee(choice, drink["ingredients"])
