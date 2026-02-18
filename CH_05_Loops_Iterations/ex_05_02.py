################################################################################
# Name: Brandon A Bustamante
# Chapter: 05
# Exercise: 02
# Description:  Write a program that repeatedly prompts a user for integer 
# numbers until the user enters 'done'. Once 'done' is entered, print out the 
# largest and smallest of the numbers. If the user enters anything other than 
# a valid number catch it with a try/except and put out an appropriate message 
# and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
# Input: 7, 2, bob, 10, 4
# Output: 
#       Invalid input
#       Maximum is 10
#       Minimum is 2
################################################################################

max = None
min = None

while True:

    user_input = input("Enter a number:")

    if user_input == "done":
        break
    
    try:
        user_input = int(user_input)

        if max == None:
            max = user_input
            min = user_input

    except:
        print("Invalid input")
        continue

    if user_input > max:
        max = user_input

    if user_input < min:
        min = user_input 

print("Maximum is", max)
print("Minimum is", min)

