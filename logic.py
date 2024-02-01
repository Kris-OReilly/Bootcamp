# this code asks the user to enter what times table they would like to see and then prints it

num_table = input("Enter which times table you want to see:") # asks the user to input a times table they wish to see
num_table = int(num_table)

for i in range(num_table, num_table+1):  # runs the loop just for the inputted number
    for j in range(1, 13):  # runs through from 1 to 12 in the times table
        times_table = i*j  # calculates the answer for each multiplication
        print("{i} x {j} = {times_table}")  # prints each line of the times table
        