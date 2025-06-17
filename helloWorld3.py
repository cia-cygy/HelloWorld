# # This example show the use of input() to get a response from the user and storing it in a variable and the displaying it back to the user.

# This line of code asks the user for input and stores it in the variable 'greetingName'.
greetingName = input("Please enter your first name: ")

# This line of code prints a greeting message to the user, using the value stored in 'greetingName'.
# The '+' operator is used to concatenate (combine) the strings 'Hello' and 'greetingName'.
# So, it says "Hello" followed by the name the user entered.
print('Hello', greetingName + '!')

# CHALLENGE 1 : Change the code so that the output always has the first letter capitalised and the rest in lowercase

capitalisedName = greetingName.casefold().capitalize()

print('Hello',capitalisedName + '!')
# Capitalizes your name and prints <Hello, 'Your Name'> it to the screen.

# CHALLENGE 2 : Change the code so that the prompt asks for the user First and Last Name and output the first letter of each word capitalised and the rest in lowercase

capitalisedName = greetingName.casefold().title()

print('Hello',capitalisedName + '!')

# Same as above but does not use a variable. Manipulate the output on the fly.
print('Hello',greetingName.casefold().title() + '!')
