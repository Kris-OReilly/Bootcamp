num_str = input("Enter a number, or enter 'NO' to stop the program: ") 
if num_str == "2":
    num_int = int(num_str)
    #string input was cast to int
    print ("The string '2' was successfully cast to an integer")
elif num_str == "3":
     num_int = int(num_str)
     #string input was cast to int 
     print ("The string '3' was successfully cast to an integer")
elif num_str > "3":
    print ("I don't know what to do with this number for any number higher than 3?")      
else:
    print ("The word 'NO' can't be cast to an int.")