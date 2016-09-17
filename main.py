
from calculator_Operator import *
from validator import *

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
        print("Please make a valid selection from the menu.")
        menu_choice = input(menu_string)
    menu_choice = int(menu_choice)
    if menu_choice == 1:
        print("Your result is " + str(calculation.addition()))
        return True
    elif menu_choice == 2:
        print("Your result is " + str(calculation.substraction()))
        return True
    elif menu_choice == 3:
        print("Your result is " + str(calculation.multiply()))
        return True
    elif menu_choice == 4:
        print("Your result is " + str(calculation.divide()))
        return True
    elif menu_choice == 5:
        return True
    elif menu_choice == 6:
        return False


def main():
    """"
    Entry point get 2 numbers to work with and then go to the operation menue

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



