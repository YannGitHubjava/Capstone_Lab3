#nothing here yet, just firing it up


    #Lets create a calculator object that add, subtract, divide and multiply 2 values
# class Calculator:
#     def __init__(self, value1, value2):
#         self.value1 = value1
#         self.value2 = value2

# TODO code does not work with float numbers :(
def addition(value1, value2):
    if not (isinstance(value1,str) or isinstance(value2,str)):
        return value1 + value2
    else: return None

def substraction(value1, value2):
    if not (isinstance(value1,str) or isinstance(value2,str)):
        return value1 - value2
    else: return None

def multiply(value1, value2):
    return value1 * value2

def divide(value1, value2):
    return value1 / value2

# print(addition(4.7,3.5))