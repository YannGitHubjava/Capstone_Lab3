# valdidator for input

# need to verify input is numeric for calculator
def isNumeric(tocheck):
    # try casting as a float; if an error is generated, it's not numberlike and we can return false.
    try:
        float(tocheck)
        return True
    except:
        return False

def is_whole_number(number,valid_range = None):
    try:
        number_as_int = int(number)
        # if parsing as integer does not produce an error, check if it's in range if a range has been given
        if valid_range and number_as_int not in valid_range:
            _min = min(valid_range)
            _max = max(valid_range)
            return False
        # Check if it's a float:  convert to string and check if there's a period in it
        if len(str(number).split('.')) > 1:
            return False
        # if we get to here, we can return true
        return True
    except ValueError:
        # also return False if an integer is not passed
        return False
