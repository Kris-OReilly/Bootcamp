# read in the data from the DOB.txt file by using readlines to return all lines one by one
 
with open('DOB.txt', 'r') as dob:
    dob_read = dob.readlines()
     
info = []  # initialises the info list

for line in dob_read:
    info.append(line.strip('\n'))


names = []     # initialises the names list
birthdate = [] # initialises the birthdate list

# loop through each string in the info list
for data in info:
    words = data.split(' ')   # Splitting the strings in the list into individual words
    names.extend(words[:2])   # This saves words at index 0 and 1 into the names list
    birthdate.extend(words[2:]) # This saves words at index 2, 3 and 4 into the birthdate list

full_names = []  # initialises the full_names list

# loop through every 2 strings and concatenating them with spaces between to create the full names
for i in range(0, len(names)-1, 2):
    full_names.append(names[i] + " " + names[i+1])

births = []  # initialises the births list

# loop through every 3 strings and concatenating them with spaces between to create the birthdates
for j in range(0, len(birthdate)-1, 3):
    births.append(birthdate[j] + " " + birthdate[j+1] + " " + birthdate[j+2])


# defining function for name, this prints each concatenated full name
def name():
    for n in full_names:
        print(n)

# defining function for birth_date, this prints each concatenated birth date
def birth_date():
    for b in births:
        print(b)

# defining function for printing the title Name in bold
def bold_name():

    print('\033[1m' + "Name")
    print('\033[0m')

# defining function for printing the title Birthdate in bold
def bold_birthdate():

    print('\033[1m' + "Birthdate")
    print('\033[0m')

bold_name()
name()
print()
bold_birthdate()
birth_date()