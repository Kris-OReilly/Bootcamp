# Create a list called menu with items being sold, create 2 dictionaries, one called stock and
# other named price. Stock contains the amount of stock for each item, price contains the price for
# each item. By naming each key in both dictionaries to match the menu items, this ensures clarity and visibility of the data.  
# An empty list is created called stock totals which will be used to append the calculated totals for each stock item.


menu = ["Scone", "Toast", "Porridge", "Tea", "Coffee"]

stock = {"Scone": 37, "Toast": 50, "Porridge": 87, "Tea": 107, "Coffee": 61}

price = {"Scone": 2.29, "Toast": 1.09, "Porridge": 1.09, "Tea": 1.49, "Coffee": 2.19}

stock_totals =[] # create an empty list to store the calculated totals for each stock item to make them iterable later for totalling all items.

for item in menu: # loops through each item in the menu list
    if item in stock and price: # this condition checks if the item in the menu list is in both the stock dictionary and the price dictionary
        stock_value = stock[item] * price[item] # if this returns True then the individual stock value is calculated and saved inside the stock_value variable
        stock_totals.append(stock_value) # each stock value is then appended to the stock_totals list.
    else:
        print("Item not found") # error handling in case a named key in either stock or price does not match a menu item
        break

# error handling to make sure there is no issues with missing items.
if len(stock_totals) != len(menu):  # this checks that the number of items match between the menu and stock_totals
    print("Check all menu items match")
else:
    total = sum(stock_totals) # the total variable is used to add all values in the stock_totals list together to get a final total
    print(f"The total value of the stock on hand is: £{total}")