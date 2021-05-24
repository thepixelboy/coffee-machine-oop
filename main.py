# Imports
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

# Variables and objects
turn_off = False
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Functions
def clrscr():
    """Clears the screen"""
    # Check if Operating System is Mac and Linux or Windows
    if os.name == 'posix':
      _ = os.system('clear')
    else:
      # Else Operating System is Windows (os.name = nt)
      _ = os.system('cls')


# Main program
clrscr() 

while not turn_off:
  menu_options = menu.get_items()
  selection = input(f"What would you like? ({menu_options}): ")

  if selection == "off":
    turn_off = True
    print("Switching off the coffee machine...")
  elif selection == "report":
    coffee_maker.report()
    money_machine.report()
  else:
    drink = menu.find_drink(selection)

    if coffee_maker.is_resource_sufficient(drink):
      if money_machine.make_payment(drink.cost):
        print("ok")
    