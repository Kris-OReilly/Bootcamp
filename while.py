<<<<<<< HEAD

# defining a total variable that starts at 0 and will be updated each time a number is entered
total = 0

# defining a variable to count the number of inputs that are not -1
counter = 0

# defining the num variable as an integer starting at zero
num = 0

# while loop will run whilst the input is not -1, it will add the num to the total and increase the
# input counter by 1 each time
# if the input equals -1 the while loop will break and the next if condition will check if the input
# count is greater than 0 and will then print the average of the numbers

while num != -1:
    num = int(input("Enter another number or enter -1 to print the average of your total: "))
    if num == -1:
        break
    total += num
    counter += 1

# conditional to check that the user has entered values to be totalled and average
if counter > 0:

    # defining a variable for calculating the average of the entered numbers
    average = total / counter
    # will print the average of the total to 2 decimal places
    print(f"The average of your total is: {average:.2f}")

# if the user enters -1 on the first entry it will tell them they didn't enter any numbers
else:
    print("You didn't enter any numbers!")    
=======

# defining a total variable that starts at 0 and will be updated each time a number is entered
total = 0

# defining a variable to count the number of inputs that are not -1
counter = 0

# defining the num variable as an integer starting at zero
num = 0

# while loop will run whilst the input is not -1, it will add the num to the total and increase the
# input counter by 1 each time
# if the input equals -1 the while loop will break and the next if condition will check if the input
# count is greater than 0 and will then print the average of the numbers

while num != -1:
    num = int(input("Enter another number or enter -1 to print the average of your total: "))
    if num == -1:
        break
    total += num
    counter += 1

# conditional to check that the user has entered values to be totalled and average
if counter > 0:

    # defining a variable for calculating the average of the entered numbers
    average = total / counter
    # will print the average of the total to 2 decimal places
    print(f"The average of your total is: {average:.2f}")

# if the user enters -1 on the first entry it will tell them they didn't enter any numbers
else:
    print("You didn't enter any numbers!")    
>>>>>>> a2a808354ee9571f3dc6a535263b0b26bc315446
       