# Remember the logic game from before?
# In Python, and other programming languages, these are called conditional statements.
# They allow us to make decisions in our code based on certain conditions.
# Typically, we use if statements to check the value of a variable and then run different code depending on what that value is.

ph = 7.2 # try changing this number and re-running!

# With the ph variable, we can check if the water is safe to drink based on its pH level.
# For example, an if statement directly checks the provided condition and runs if the condition is true.
if ph < 6.5:
    print("Too acidic - NOT safe to drink.")
# In this case, elif (short for "else if") checks another condition if the first one was false.
elif ph > 8.5:
    print("Too basic - NOT safe to drink.")
# Lastly, else runs if all previously evaluated conditions were false.
# In this case, that means the pH is in the safe range.
else:
    print("pH is in the safe range. Good to go!")

# TODO: Change the value of the variable ph to test the other branches of the if/elif/else statement.