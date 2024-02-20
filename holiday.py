# calculate a user's total holiday cost which includes plane cost, hotel cost and car rental cost.
# get user input and save into variables for the chosen city, number of nights stay and number of days car rental
# create 4 functions, 1 to calculate and return hotel cost, 1 to return plane cost dependant on city chosen,
# 1 to calculate and return car rental cost and the last to calculate the holiday total
# by adding the values of the 3 previous functions together
# then print the output for the user to see the holiday total and the price breakdown



# variable containing the list of holiday destinations the user can choose from
cities = ["London", "Barcelona", "Lisbon", "Paris", "Istanbul"]

# variable containing a dictionary that links the city choice with the hotel rate
hotel_rates = {1: 199, 2: 229, 3: 169, 4: 299, 5: 139}

# using a while loop to continually ask the question until a correct input is entered
while True:
    try:
        city_flight = int(input(f"""Please type the number for your destination city from the following:\n
        1. {cities[0]}
        2. {cities[1]}
        3. {cities[2]}
        4. {cities[3]}
        5. {cities[4]}
        : """))

        # using an if-else as error handling for user input
        if city_flight <= 0:
            print("Error - you entered an invalid option\n")
        else:
            print(f"You have chosen: {cities[int(city_flight) - 1]}\n")
            break
    except ValueError:
        print("You didn't enter a number!\n")


# using a while loop to continually ask the question until a correct input is entered
while True:
    try:
        num_night = int(input("Please enter the number of nights you will be staying: \n"))

        if num_night <= 0:
            print("Error - you entered an invalid option\n")
        else:
            print(f"You have chosen to stay for {num_night} nights.\n")
            break
    except ValueError:
        print("Error - you did not enter a number\n")


# using a while loop to continually ask the question until a correct input is entered
while True:
    try:
        rental_days = int(input("Please enter the number of days you wish to hire a car for: \n"))
        if rental_days <= 0:
            print("Error - you entered an invalid option\n")
        else:    
            print('-' * 50 + f"\nYou have chosen to hire a car for {rental_days} days.\n" + '-' * 50)
            break
    except ValueError:
        print("Error - you did not enter a number\n")

hotel_price = hotel_rates.get(int(city_flight))


# function to calculate the hotel cost dependant on the number of nights stay entered by the user
def hotel_cost():
    total_cost = num_night * hotel_price
    return total_cost
    

# function to calculate the cost of car rental based on number of days entered by user
def car_rental():
    total_rental = int(rental_days) * 49
    return total_rental


# function to calculate the plane cost using an if-else dependant on city chosen by the user
def plane_cost():
    if city_flight == 1:
        return 289
    elif city_flight == 2:
        return 319
    elif city_flight == 3:
        return 309
    elif city_flight == 4:
        return 109
    elif city_flight == 5:
        return 349
    else:
        print("Error - no city chosen\n")


# function to calculate the total holiday cost
def holiday_cost():
    holiday_total = int(hotel_cost() + plane_cost() + car_rental())
    return holiday_total

# containing the functions into variables in order to print the values
holiday_total = holiday_cost()
hotel_total = hotel_cost() 
flight_cost = plane_cost()
rental_cost = car_rental()

# final printout of holiday total cost and breakdown
print('-' * 50 + f"\nYour total holiday cost is: £{holiday_total}\n" + '-' * 50)
print(f"""\nYour breakdown is as follows:\n
Hotel Cost: £{hotel_total}\n
Flight Cost: £{flight_cost}\n
Car Rental Cost: £{rental_cost}\n""")