from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

selection = "ON"
options = menu.get_items()

selection = input(f"What would you like? ({options}):\n").lower()
cost = float(menu.find_drink(selection).cost)
print(f"Selection dring cost: {cost}")

while not selection == "off":
    match selection:
        case "report":
            coffee_machine.report()
            money_machine.report()

        case _:
            if coffee_machine.is_resource_sufficient(menu.find_drink(selection)):
                if money_machine.make_payment(menu.find_drink(selection).cost):
                    coffee_machine.make_coffee(menu.find_drink(selection))
    selection = input(f"What would you like? ({options}):\n").lower()
#
print("Thank you, machine going Off")
