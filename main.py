from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def start_machine():
    """Asks user for an option and starts transaction"""
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    machine_on = True
    while machine_on:

        menu_options = menu.get_items()
        choice = input(f" What would you like? ({menu_options}): ").lower()
        if choice == "off":
            machine_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if drink is not None:
                cost = drink.cost
                if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(cost):
                    coffee_maker.make_coffee(drink)


start_machine()
