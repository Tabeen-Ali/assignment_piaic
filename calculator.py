'''
Student Name: Iqra Tahir
Roll No: PIAIC234522
Assignment(4): Basic Calculator Operations in Python
'''
#Simple Calculator Function
def calculator():
    x : int = input("Please enter the first number:  ")
    y : int = input("Please enter the second number:  ")
    z = input("Please enter the arithmetic operation ypu want to perform ('+','-','*','/'):  ")
    if z=='+':
     result = int(x)+int(y)
     print(f'The sum of {x} and {y} = {result}')
    elif z=='-':
     result = int(x)-int(y)
     print(f'The subtraction of {x} and {y} = {result}')
    elif z=='*':
     result = int(x)*int(y)
     print(f'The multiplication of {x} and {y} = {result}')
    elif z=='/':
     result = int(x)/int(y)
     print(f'The division of {x} and {y} = {result}')
    else:
     print('Please enter valid operator...')

calculator()