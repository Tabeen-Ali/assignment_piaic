'''
Student Name: Iqra Tahir
Roll No: PIAIC234522
Assignment: Calculator using functions
'''
def calculator():
    x  = float(input("Please enter the first number:  "))
    y  = float(input("Please enter the second number:  "))
    z = input("Please enter the arithmetic operation you want to perform ('+','-','*','/'):  ")
    def addition(x,y): #function for addition
        return x+y
    def subtraction(x,y): #function for subtraction
        return x-y
    def multiplication(x,y): #function for multiplication
        return x*y
    def division(x,y): #function for division
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