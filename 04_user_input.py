# In many programs, we want to get input from the user.
# In Python, we can simply use the input() function to get input from the user.
#
# It should be noted that the input() function will always return a string, so if you want the input to be a number, you will need to convert it to the appropriate type (like int or float).
# This is important because if you try to do math with a string, it will produce unexpected results or errors.

# For example, if we want to get a pH level from the user, we can use the following code:
ph = float(input("Enter a pH level: ")) # Note that since we are using float(), the input will be converted to a decimal number.

# Now that we have the pH level from the user, we can use conditional statements to check if it's safe to drink.
if ph < 6.5:
    print("Too acidic - NOT safe to drink.")
elif ph > 8.5:
    print("Too basic - NOT safe to drink.")
else:
    print("pH is in the safe range. Good to go!")

# TODO: Try adding a new input for the user to enter their name, and print a personalized message to the screen using that name.
