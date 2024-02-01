# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # runtime error as animal vairable is undefined, Lion needs ""
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"
# logical error as number_of_teeth and animal_type have been put in the wrong place.
# logical error as full_spec has not been made a formatted string
print(full_spec)

