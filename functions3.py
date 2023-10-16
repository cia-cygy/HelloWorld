# # This is an example of Scoping.
# # This example is used to illustrate the effect of declaring a variable with the same outside of a function block and also within a function block

# Assign the string "a species of snake" to the GLOBAL variable 'rating'.
rating = "a species of snake"

# Define a function named 'myFunction'.
def myFunction():
    # Inside the function, create a new LOCAL variable 'rating' and assign it the string "fantastic".
    rating = "fantastic"
    
    # Print a message with the string "Python is" followed by the value of the 'rating' variable.
    print("Python is", rating)

# Call the 'myFunction' function to execute its code.
# NOTE: If you omit this line, the function will not run even though it exists.
myFunction()

# Print a message with the string "Python is" followed by the value of the 'rating' variable.
# This 'rating' variable is the one defined outside of the 'myFunction' function.
print("Python is", rating)

# Explanation:

# rating = "a species of snake": This line assigns the string "a species of snake" to the variable 'rating'. 
# This is a global variable because it's defined outside of any function.

# def myFunction():: This line defines a function called 'myFunction'. Functions in Python are blocks of code that can be called and executed later.

# rating = "fantastic": Inside the 'myFunction' function, this line creates a new variable also named 'rating' and assigns it the string "fantastic". 
# This 'rating' variable is local to the function and does not affect the global 'rating' variable defined earlier.

# print("Python is", rating): Inside the function, this line prints a message that combines the string "Python is" with the value of the local 'rating' variable, which is "fantastic". It will print "Python is fantastic" when the function is called.

# myFunction(): This line calls the 'myFunction' function, which executes the code inside it and prints "Python is fantastic."

# print("Python is", rating): This line prints a message that combines the string "Python is" with the value of the global 'rating' variable, which is still "a species of snake." 
# It will print "Python is a species of snake" because it's referencing the global variable defined outside the function.