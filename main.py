# Imports
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

# Variables and objects
turn_off = False
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

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

coffee_maker.report()
money_machine.report()