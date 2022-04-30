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
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

#TODO: quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

turned_on = True


def check_req():
    for req in resources:
        if resources[req] < 0:
            print(f"Sowwy, there is not enough {req}")
            return '1'


def report_status():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def change_or_nah(user_payment, coffee):
    if check_req() == '1':
        canceller(coffee)
        print("Your payment has been returned")
    elif user_payment >= MENU[coffee]['cost']:
        resources['money'] += MENU[coffee]['cost']
        change = user_payment - MENU[coffee]['cost']
        print(f"Your change is: ${round(change, 2)}")
        print(f"Please do enjoy your {coffee}")
    else:
        canceller(coffee)
        print("Sorry, your payment is not enough")
        return 1


def payment(pay_dimes, pay_quarters, pay_nickel, pay_pennies, coffee):
    pay_dimes = float(pay_dimes) * 0.1
    pay_quarters = float(pay_quarters) * 0.25
    pay_nickel = float(pay_nickel) * 0.05
    pay_pennies = float(pay_pennies) * 0.01
    total = pay_nickel + pay_dimes + pay_quarters + pay_pennies
    change_or_nah(total, coffee)


def canceller(coffee):
    resources['water'] = resources['water'] + MENU[coffee]['ingredients']['water']
    resources['coffee'] = resources['coffee'] + MENU[coffee]['ingredients']['coffee']
    if coffee != 'espresso':
        resources['milk'] = resources['milk'] + MENU[coffee]['ingredients']['milk']


def buy_a_coffee(dimes, quarters, nickles, pennies, coffee):
    resources['water'] = resources['water'] - MENU[coffee]['ingredients']['water']
    resources['coffee'] = resources['coffee'] - MENU[coffee]['ingredients']['coffee']
    if coffee != 'espresso':
        resources['milk'] = resources['milk'] - MENU[coffee]['ingredients']['milk']
    payment(dimes, quarters, nickles, pennies, coffee)


while turned_on:
    user_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_coffee == "report":
        report_status()
    elif user_coffee == "off":
        turned_on = False
    elif user_coffee == 'espresso' or user_coffee == 'latte' or user_coffee == 'cappuccino':
        user_quarters = input("Quarters: ")
        user_dimes = input("Dimes: ")
        user_nickles = input("Nickles: ")
        user_pennies = input("Pennies: ")
        buy_a_coffee(user_dimes, user_quarters, user_nickles, user_pennies, user_coffee)
