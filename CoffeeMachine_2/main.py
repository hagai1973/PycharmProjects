import data
from data import MENU

resources = {"water": 300, "milk": 200, "coffee": 100}

MONEY = 0.0


def report_print():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${MONEY}")


def is_resource_sufficient(order_ingredients):
    print(order_ingredients)
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item} ")
            return False
    return True


def process_coins(product="espresso"):
    print("Please insert coins.")
    quarters = int(input("how many quarters? \n"))
    dimes = int(input("how many dimes? \n"))
    nickles = int(input("how many nickles? \n"))
    pennies = int(input("how many pennies? \n"))
    total_paid = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    price = float(data.MENU["" + product + ""]["cost"])
    if total_paid >= price:
        if total_paid > price:
            refund = round(total_paid - price, 2)
            print(f"Here is ${refund} dollars in change.")
        global MONEY
        MONEY += price
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded, needed: {price} , paid: {total_paid}")
        return False


def make_coffee(drink_name, order_ingredients):
    print(f"Here is your {drink_name} ☕ Enjoy👍")
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]


selection = "ON"
selection = input("What would you like? (espresso/latte/cappuccino):\n").upper()

while not selection == "OFF":
    match selection:
        case "REPORT":
            report_print()
        case "ESPRESSO":
            print(data.MENU["espresso"])
            if is_resource_sufficient(data.MENU["espresso"]["ingredients"]):
                if process_coins("espresso"):
                    make_coffee("espresso", data.MENU["espresso"]["ingredients"])
        case "LATTE":
            print(data.MENU["latte"])
            if is_resource_sufficient(data.MENU["latte"]["ingredients"]):
                if process_coins("latte"):
                    make_coffee("latte", data.MENU["latte"]["ingredients"])
        case "CAPPUCCINO":
            print(data.MENU["cappuccino"])
            if is_resource_sufficient(data.MENU["cappuccino"]["ingredients"]):
                if process_coins("cappuccino"):
                    make_coffee("cappuccino", data.MENU["cappuccino"]["ingredients"])
        case _:
            print("Code not found")
    selection = input("What would you like? (espresso/latte/cappuccino):\n").upper()

print("Thank you, machine going Off")
