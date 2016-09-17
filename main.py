
from calculator_Operator import *
from validator import *

CHOICE_ADD = '1'
CHOICE_SUB = '2'
CHOICE_MUL = '3'
CHOICE_DIV = '4'
CHOICE_RESTART = '5'
CHIOCE_QUIT = '6'

def operation_menu(calculation):

    menu_string = (
        '\nOperands : {} and {}\n'
        '\nCalculator Menu:\n'
        '\t1) Addition\n'
        '\t2) Subtraction\n'
        '\t3) Multiplication\n'
        '\t4) Division\n'
        '\t5) Start Over\n'
        '\t6) Quit\n'
        '\nEnter Selection'
    ).format(calculation.value1, calculation.value2)

    menu_choice = input(menu_string)
    while not is_whole_number(menu_choice, range(1, 7)):
        menu_choice = input("Please make a valid selection from the menu.")

    if menu_choice == CHOICE_ADD:
        print("Your result is " + str(calculation.addition()))
        return True
    elif menu_choice == CHOICE_SUB:
        print("Your result is " + str(calculation.substraction()))
        return True
    elif menu_choice == CHOICE_MUL:
        print("Your result is " + str(calculation.multiply()))
        return True
    elif menu_choice == CHOICE_DIV:
        print("Your result is " + str(calculation.divide()))
        return True
    elif menu_choice == CHOICE_RESTART:
        return True
    elif menu_choice == CHIOCE_QUIT:
        return False


def main():
    """"
    Entry point get 2 numbers to work with and then go to the operation menu

    """
    quit_operation = True
    while quit_operation:
        value1 = input("Enter your first number\n")
        while not isNumeric(value1):
            value1 = input("You must enter a number.  Please enter a whole number.\n")
        value2 = input("Enter your Second number\n")
        while not isNumeric(value2):
            value2 = input("You must enter a number.  Please enter a whole number.\n")
        value1 = float(value1)
        value2 = float(value2)
        calculation = Calculator(value1, value2)

        if not calculation:
            print("Can't perform this calculation")
            continue
        if calculation:
            quit_operation = operation_menu(calculation)
            continue
        break

    print("We are all done!!!")



main()



