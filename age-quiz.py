# create a variable called age with an input of a user's age that is cast into an integer
# if the user's age >=40, print the statement "You're over the hill."
# elif the user's age >100, print the statement "Sorry, you're dead."
# elif the user's age >=65. print the statement "Enjoy your retirement!"
# elif the user's age <13, print the statement "You qualify for the kiddie discount"
# elif the user's age ==21, print the statement "Congrats on your 21st!"
# else, print the statement "Age is but a number."

# Order of conditions as follows:
# 1. if age <13
# 2. elif age == 21
# 3. elif age > 100
# 4. elif age >= 65
# 5. elif age >= 40
# 6. else

age = int(input("Enter your age:"))

if age <13:   #this must be checked first as it is the lowest variable and has the less than condition
    print("You qualify for the kiddie discount")
elif age ==21:   #this is the next logical check as it is older than 13 and is less than the other conditions
    print("Congrats on your 21st!")    
elif age >100:    #all remaining conditions before the else statement is checking an age greater than a condition
    print("Sorry, you're dead.")
elif age >=65:
    print("Enjoy your retirement!")
elif age >=40:
    print("You're over the hill.")
else:
    print("Age is but a number.") # the else statement covers any age 13-21, 22-39