# Did you know 1 + 1 = 11 
input1 = input("Enter Input #1: ")
input2 = input("Enter Input #2: ")
print (input1 + input2)

# # Challenge: Change the code so that it gives the correct answers when adding two numbers instead of concatenating them. 
# # Challenge: Change the print line to be more descriptive when giving the answer. 
#              Example: If a user enters 1 and 2 then your print output should be as follows: 1 + 2 = 3
#              Hint: You cannot combine strings and numbers. Look for a solution for this.

answer = "{} + {} ="
print(answer.format(input1, input2), int(input1) + int(input2))