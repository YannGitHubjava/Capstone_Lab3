# valdidator for input

# need to verify input is numeric for calculator
def isNumeric(tocheck):
    # try casting as a float; if an error is generated, it's not numberlike and we can return false.
    try:
        float(tocheck)
        return True
    except:
        return False

# verify input is a whole number
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