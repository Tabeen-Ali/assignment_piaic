'''
Student Name: Iqra Tahir
Roll No: PIAIC234522
Assignment: Python Basics Exercises

'''
'''1. Simple Message
Task: Assign a message to a variable and then print that message'''
x : str = "It's a message."
print(x)

'''2. Simple Messages
Task:
● Assign a message to a variable and print that message.
● Change the value of the variable to a new message, and print the new message.'''
x = "It's a message"
print(x)
x = "It's a new message."
print(x)

'''3. Personal Message
Task:
● Use a variable to represent a person’s name.
● Print a message to that person, such as, “Hello Eric, would you like to learn some
Python today?'''
a : str = "Iqra"
b : str = f"Hello {a}, would you like to learn some python today?"
print(b)

'''4. Name Cases
Task:
● Use a variable to represent a person’s name.
● Print the person’s name in lowercase, uppercase, and title case.'''
a : str = "iqra"
print(a.upper())
print(a.lower())
print(a.title())

'''5. Famous Quote
Task:
● Find a quote from a famous person you admire.
● Print the quote and the name of its author.'''
p : str = "Holy Prophet (SAW)"
q : str = "Kindness is a mark of faith, and whoever is not kind has no faith."
print(f"{p}said,'{q}'")

'''6. Famous Quote 2
Task:
● Use a variable called famous_person to represent the famous person’s name.
● Compose the message and represent it with a variable called message.
● Print the message.'''
famous_person : str = "Holy Prophet (SAW)"
message : str = "He who seeks knowledge, Allah will make his path to Paradise easy."
print(f"{famous_person}said,'{message}'")

'''7. Stripping Names
Task:
● Use a variable to represent a person’s name, and include some whitespace characters
at the beginning and end of the name.

'''
first_name : str = "   Ayaz  "
last_name : str = "Ali"
print(f"\t{first_name}\n{last_name}")
'''● Make sure you use each character combination, \t and \n, at least once.
● Print the name once, so the  around the name is displayed.
whitespace● Print the name using each of the three stripping functions: lstrip(), rstrip(), and
strip().'''
print(f"{first_name} {last_name}")
print(f"{first_name.strip()} {last_name}")
print(f"{first_name.lstrip()} {last_name}")
print(f"{first_name.rstrip()} {last_name}")

'''8. Variable Sum
Task: Assign the values 5, 10, and 15 to three variables x, y, and z. Print their sum.'''
x : int = 5
y : int = 10
z : int = 15
print(x+y+z)

'''9. Variable Swap
Task: Swap the values of two variables a and b. Print the values before and after the swap.'''
x : int = 5
y : int = 10
print(f"Before swapping x = {x} and y = {y}")
temp = x
x = y
y = temp
print(f"After swapping x = {x}and y = {y}")

'''10. Favorite Color
Task: Create a variable with your favorite color and print it. Then change the variable name to
something else and print the color again.'''
fav_color : str = "Lavender"
print(fav_color)
mfav_color = fav_color
print(mfav_color)

'''11. Changing Pet Name
Task: Create a variable pet_name and set it to "Buddy". Change the value of pet_name to
"Max" and print the new value.'''
pet_name : str = "Buddy"
pet_name : str = "Max"
print(pet_name)

'''12. Observing Name Error
Task: Assign the value "Sunshine" to a variable and print it. Then, mistakenly try to print a
variable with a different name (like sunsine) and observe the error.'''
sunshine : str = "something"
#print(sunsine)
print(sunshine)

'''13. Reassigning Score
Task: Assign the value 100 to a variable score and print it. Then assign a new value to score
and print it again.
'''
score : int = 100
print(score)
score = 150
print(score)

'''14. City Name
Task: Create a string variable city and assign it the name of a city you like. Print the city
name'''
city : str = "Lahore"
print(city)

'''15. Title Case Text
Task: Create a variable text with the value "python programming" and print it in title case.'''
course : str = "python programming"
print(course.title())

'''16. Lowercase Conversion
Task: Assign a string with mixed cases to a variable and print it in all lowercase letters.'''
string : str = "AssiGnmenT"
print(string.lower())

'''17. Uppercase Conversion
Task: Assign a string with mixed cases to a variable and print it in all uppercase letters'''
string : str = "pYthoN"
print(string.upper())

'''18. Current Temperature
Task: Create a variable temperature with the value 25. Print "The current temperature is
[temperature] degrees." using the variable.
'''
temperature : int = 25
print(f"The current temperature is {temperature}")

'''19. Printing a Poem
Task: Create a variable poem with a short poem that has multiple lines. Print the poem with
each line starting on a new line.'''
poem : str = "In the sky so vast and blue,\nDreams take flight, the old and new.\nWhispers of the wind's sweet song,\nGuide us gently, all day long."
print(poem)