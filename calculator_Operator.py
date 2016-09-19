#nothing here yet, just firing it up


    #Lets create a calculator object that add, subtract, divide and multiply 2 values
class Calculator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2


    def addition(self):
        return self.value1 + self.value2

    def substraction(self):
        return self.value1 - self.value2

    def multiply(self):
        return self.value1 * self.value2

    def divide(self):
        try:
            return self.value1 / self.value2
        except ZeroDivisionError:
            return "[Unable to divide by zero.]"

