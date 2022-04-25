import data
from data import MENU

WATER = 300
MILK = 200
COFFEE = 100
MONEY = 0.0


def report_print(water, milk, coffee, money):
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def check_sufficient(product="espresso", resource="water"):
    amount = int(data.MENU["" + product + ""]["ingredients"]["" + resource + ""])
    match resource:
        case "water":
            if WATER < amount:
                print(f"Sorry there is not enough {resource}.")
                return False
        case "coffee":
            if COFFEE < amount:
                print(f"Sorry there is not enough {resource}.")
                return False
        case "milk":
            if MILK < amount:
                print(f"Sorry there is not enough {resource}.")
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
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded, needed: {price} , paid: {total_paid}")
        return False


selection = "ON"
selection = input("What would you like? (espresso/latte/cappuccino):\n").upper()

while not selection == "OFF":
    match selection:
        case "REPORT":
            report_print(WATER, MILK, COFFEE, MONEY)
        case "ESPRESSO":
            if check_sufficient("espresso", "water"):
                if check_sufficient("espresso", "coffee"):
                    if process_coins("espresso"):
                        print("Here is your espresso ☕ Enjoy👍")
                        WATER -= int(data.MENU["espresso"]["ingredients"]["water"])
                        COFFEE -= int(data.MENU["espresso"]["ingredients"]["coffee"])
                        MONEY += float(data.MENU["espresso"]["cost"])
        case "LATTE":
            if check_sufficient("latte", "water"):
                if check_sufficient("latte", "coffee"):
                    if check_sufficient("latte", "milk"):
                        if process_coins("latte"):
                            print("Here is your latte ☕ Enjoy👍")
                            WATER -= int(data.MENU["latte"]["ingredients"]["water"])
                            MILK -= int(data.MENU["latte"]["ingredients"]["milk"])
                            COFFEE -= int(data.MENU["latte"]["ingredients"]["coffee"])
                            MONEY += float(data.MENU["latte"]["cost"])
        case "CAPPUCCINO":
            if check_sufficient("cappuccino", "water"):
                if check_sufficient("cappuccino", "coffee"):
                    if check_sufficient("cappuccino", "milk"):
                        if process_coins("cappuccino"):
                            print("Here is your cappuccino ☕ Enjoy👍")
                            WATER -= int(data.MENU["cappuccino"]["ingredients"]["water"])
                            MILK -= int(data.MENU["cappuccino"]["ingredients"]["coffee"])
                            MONEY += float(data.MENU["cappuccino"]["cost"])
        case _:
            print("Code not found")
    selection = input("What would you like? (espresso/latte/cappuccino):\n").upper()

print("Thank you, machine going Off")


