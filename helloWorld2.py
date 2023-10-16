# # This example is to show the different way and effect of concatenating text.

# We create a variable called "greetingName" and assign it the value "World".
greetingName = "World"

# We use the 'print' function to display the text "Hello " followed by the value of the 'greetingName' variable.
# In Python, we can concatenate (join) strings together using the '+' operator.
# So, this line will display "Hello World" because it combines "Hello " and the value of 'greetingName'.
print("Hello " + greetingName)

# Similar to the previous line, this one also displays "Hello World."
# It uses single quotes (' ') instead of double quotes (" ") to define the string.
# In Python, you can use either single or double quotes to create strings.
print('Hello ' + greetingName)

# This line is different from the previous two.
# Instead of using the '+' operator, it uses a comma (',') to separate the two values.
# As a result, it will display "Hello World" with a space between "Hello" and "World."
print('Hello', greetingName)

# In summary, all three lines produce the same output, which is "Hello World." 
# They just use different ways to concatenate the string "Hello" and the value of the greetingName variable. 
# The first two lines use the + operator with either double or single quotes, 
# while the third line uses a comma to separate the values, which automatically adds a space.


# CHALLENGE: Change all 3 print statements in the script so the output shows "Hello World!" instead of "Hello World".

# CHALLENGE ANSWER:
print("Hello " + greetingName + "!")
print('Hello ' + greetingName + '!')
print('Hello', greetingName + '!')