# valdidator for input

# need to verify input is numeric for calculator
def isNumeric(tocheck):
    # try casting as a float; if an error is generated, it's not numberlike and we can return false.
    try:
        float(tocheck)
        return True
    except:
        return False