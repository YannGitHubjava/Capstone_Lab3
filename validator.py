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
# def is_whole_number(message, valid_range = None):
#     while True:
#         user_input = input('{} :'.format(message))
def is_whole_number(number,valid_range = None):
    try:
        number_int = int(number)
        # if parsing as integer does not produce an error, check if it's in range if a range has been given
        if valid_range and number_int not in valid_range: # number >= min(valid_range) and number <= max(valid_range):
            _min = min(valid_range)
            _max = max(valid_range)
            # print('You must enter a number from {} to {}.'.format(_min, _max))
            return False
        # otherwise check that number and int are equal
        return number == number_int
    except ValueError:
        # also return False if an integer is not passed
        return False


        # All tests passed
        # return number