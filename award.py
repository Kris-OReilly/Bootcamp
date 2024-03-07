
# create a variable input for swimming time, 
# a variable input for cycling time,
# a variable input for running time.
# create a variable for total_time which calculates the total of all 3 inputted times.
# print the total time for completion
# print the award the participant will receive using an if-else condition
# if total_time <= 100, the award will be 'Provincial colours'
# elif 101 <= total_time <= 105; the award will be 'Provincial half colours'
# elif 106 <= total_time <= 110; the award will be 'Provincial scroll'
# else no award given

while True:
    try:
        swimming_time = int(input("Enter swim time in whole minutes:"))
        cycling_time = int(input("Enter cycling time in whole minutes:"))
        running_time = int(input("Enter running time in whole minutes:"))
        break
        # our 3 event completion times need to be inputted to calculate the total time 
    except ValueError:
        print("You did not enter a valid number, try again")
           
    
total_time = swimming_time + cycling_time + running_time # variable to add the three inputted times together
print(f"Your triathlon completion time is: {total_time} minutes") # using an f string to display triathlon completion time


if total_time <= 100: # checks if the value of total_time is less than 100 minutes to return True
    print("You won Provincial Colours!")
elif total_time >= 101 and total_time <= 105: # checks if the value of total_time is between 101-105 minutes to return True
    print("You won Provincial Half Colours!")
elif total_time >= 106 and total_time <= 110: # checks if the value of total_time is between 106-110 minutes to return True
    print("You won a Provincial Scroll!")
else:    # if the value of total_time is any value 111 and above this will return True
    print("Sorry, your time did not qualify for an award, better luck next time")
