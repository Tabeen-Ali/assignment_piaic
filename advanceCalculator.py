'''
Student Name: Iqra Tahir
Roll No: PIAIC234522
Assignment: Basic Calculator Operations in Python using functions
'''
def calculator():
    x  = float(input("Please enter the first number:  "))
    y  = float(input("Please enter the second number:  "))
    z = input("Please enter the arithmetic operation you want to perform ('+','-','*','/'):  ")
    def addition(x,y):
        return x+y
    def subtraction(x,y):
        return x-y
    def multiplication(x,y):
        return x*y
    def division(x,y):
        return x/y
    if z == '+':
        result = addition(x, y)
    elif z == '-':
        result = subtraction(x, y)
    elif z == '*':
        result = multiplication(x, y)
    elif z == '/':
        if y != 0:  # Check for division by zero
            result = division(x, y)
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operation"

    # Display the result
    print("The result is:", result)
    
calculator()