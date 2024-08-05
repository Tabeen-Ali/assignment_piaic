'''Student Name: Iqra Tahir
Roll No: PIAIC234522
Assignment 1: Python Print Function Practice Questions'''

#1. Basic Printing:
#- Write a Python script to print the phrase 'Hello, World!'
print("Hello World!")
#- Print your first name.
first_name = "Iqra"
print(f"My first name is {first_name}")

#2. Printing Multiple Items:
# - Print your first name and last name in a single print statement
first_name = "iqra"
last_name = "Tahir"
full_name = f"{first_name} {last_name}"
print(f"My full name is {full_name}")
# - Print the numbers 1, 2, and 3 in a single print statement.
num_list = [1,2,3]
for x in num_list:
 print(x)

#3. Printing Special Characters:
#- Print a string that includes a newline character to display text on two lines. For example:HelloWorld
print("Hello\nWorld")
# - Print a string that includes a tab character. For example: Hello	World
print("\tHello World")

#4. Using the sep Parameter:
 #- Print three different words separated by commas. For example: 'apple, banana, cherry'
print('Apple','banana','orange',sep=',')
# - Print three different numbers separated by hyphens. For example: '1-2-3'.
print('1','2','3',sep='-')

#5. Using the end Parameter:
# - Print two words on the same line with a space in between. For example: 'Hello World'.
print('Happy', end=' ')
print('coding') 
# - Print the numbers 1 and 2 on the same line without a space in between. For example: '12'.
print('1',end='')
print('2')

#6. Escape Characters:
# - Print a string that includes double quotes. For example: He said, "Hello!".
print('He said,\"hello!\"')
# - Print a backslash character. For example: This is a backslash: \.
print('This is a backlash: \\')

#7. Combining Text and Numbers:
# - Print your age alongside a descriptive message. For example: 'I am 20 years old
my_age = 27
print(f"My age is {my_age} years.")
# - Print a number and a string together. For example: 'The number is 5'.
string = "The number is"
number = 5
print(f"{string} {number}")

#8. Basic Loop for Printing: - Print the numbers 1 to 5, each on a new line using separate print statements.
print(1)
print(2)
print(3)
print(4)
print(5)

#*************************************************************************************************