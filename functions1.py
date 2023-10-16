# # This is an example of creating a simple function and then calling the function in order to execute it.

# Define a function named 'myfunc'.
def myFunction():
    # Inside the function, create a variable 'rating' and assign the string "fantastic" to it.
    rating = "fantastic"
    
    # Print the string "Python is " concatenated with the value of variable 'rating'.
    print("Python is", rating)

# Call the 'myfunc' function to execute its code. 
# NOTE: If you omit the line below then the function will not run even though it exists.
myFunction()

# Explanation:
# We define a function named myfunc using the def keyword. This function doesn't take any parameter/arguments.
# Inside the function, we create a variable x and set it equal to the string "fantastic".
# We then print a message using the print function. The message consists of the string "Python is " concatenated with the value of the x variable. The + operator is used for concatenation.
# Finally, we call the myfunc function, which causes the code inside the function to be executed, resulting in the printed message: "Python is fantastic".