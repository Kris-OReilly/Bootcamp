<<<<<<< HEAD
# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") # Syntax error, print call needs parentheses surrounding it
print ("\n") # Syntax error, print has an unexpected indent and the call is not in parentheses

    # Variables declaring the user's age, casting the str to an int, and printing the result

age = 24 # this has multiple errors, the use of == is incorrect as it should be just one
# there is a syntax error for indentation, the variable name also ignores the naming convention by using str
# ValueError as the string "24 years old" cannot be turned into an integer

age_string = str(age) # syntax error for unexpected indent, runtime error as age variable needs to be a string
print(f"I'm " + age_string + " years old.") # syntax error for unexpected indent, 
# also a logical error as has not used an f string correctly

    # Variables declaring additional years and printing the total years of age
years_from_now = 3 # syntax error for indent, creating 3 as a string instead of an integer
total_years = age + years_from_now # runtime error as using age variable instead of age_string

print(f"The total number of years:" + str(total_years)) # syntax error as print call is not in parentheses
 # logical error as has not used an f string correctly and has the variable answer_years as a string
# runtime error as calling an undefined variable answer_years, runtime error as variable needs to be converted to str

# Variable to calculate the total amount of months from the total amount of years and printing the result
total = 27.5
total_months = total * 12 # runtime error, referring to undefined variable total
total_months = int(total_months) # casting the variable to int 
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")
# syntax error as print call is not in parentheses, logical error as not using f string correctly
# runtime error as total_months variable needs to be cast as a string

#HINT, 330 months is the correct answer

=======
# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") # Syntax error, print call needs parentheses surrounding it
print ("\n") # Syntax error, print has an unexpected indent and the call is not in parentheses

    # Variables declaring the user's age, casting the str to an int, and printing the result

age = 24 # this has multiple errors, the use of == is incorrect as it should be just one
# there is a syntax error for indentation, the variable name also ignores the naming convention by using str
# ValueError as the string "24 years old" cannot be turned into an integer

age_string = str(age) # syntax error for unexpected indent, runtime error as age variable needs to be a string
print(f"I'm " + age_string + " years old.") # syntax error for unexpected indent, 
# also a logical error as has not used an f string correctly

    # Variables declaring additional years and printing the total years of age
years_from_now = 3 # syntax error for indent, creating 3 as a string instead of an integer
total_years = age + years_from_now # runtime error as using age variable instead of age_string

print(f"The total number of years:" + str(total_years)) # syntax error as print call is not in parentheses
 # logical error as has not used an f string correctly and has the variable answer_years as a string
# runtime error as calling an undefined variable answer_years, runtime error as variable needs to be converted to str

# Variable to calculate the total amount of months from the total amount of years and printing the result
total = 27.5
total_months = total * 12 # runtime error, referring to undefined variable total
total_months = int(total_months) # casting the variable to int 
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")
# syntax error as print call is not in parentheses, logical error as not using f string correctly
# runtime error as total_months variable needs to be cast as a string

#HINT, 330 months is the correct answer

>>>>>>> a2a808354ee9571f3dc6a535263b0b26bc315446
