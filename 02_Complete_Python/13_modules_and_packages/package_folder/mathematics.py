#pylint: disable = all

def addition(num1, num2):
    return num1 + num2

def substraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Enter a valid value"
    return num1 / num2