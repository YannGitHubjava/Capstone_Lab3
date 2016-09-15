
from calculator_Operator import *


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

    while True:
        menu_choice = is_whole_number(menu_string, range(1, 7))

        if menu_choice == 1:
            print("Your result is " + str(calculation.addition()))
        elif menu_choice == 2:
            print("Your result is " + str(calculation.substraction()))
        elif menu_choice == 3:
            print("Your result is " + str(calculation.multiply()))
        elif menu_choice == 4:
            print("Your result is " + str(calculation.divide()))
        elif menu_choice == 5:
            return True
            break
        elif menu_choice == 6:
            return False
            break





def is_whole_number(message, valid_range = None):
    while True:
        user_input = input('{} :'.format(message))
        try:
            number = int(user_input)
        except ValueError:
            print("Please enter a correct Value: ")
            continue
        if valid_range and number not in valid_range:
            _min = min(valid_range)
            _max = max(valid_range)
            print('You must enter a number from {} to {}.'.format(_min, _max))
            continue

        # All tests passed
        return number



def main():
    """"
    Entry point get 2 numbers to work with and then go to the operation menue

    """
    quit_operation = True
    while quit_operation:
        value1 = is_whole_number("Enter your first number number")
        value2 = is_whole_number("Enter your Second number number")
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



