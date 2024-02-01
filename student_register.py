# write a program that allows a user to register students for an exam venue
# ask the user how many students are registering
# create a for loop that runs for that number of students
# each loop should ask the user to enter the next student ID number
# write each of the ID numbers to a text file called reg_form.txt
# include a dotted line after each student ID 


student_num = input("Enter number of students registering: \n")

if student_num.isnumeric():
    student_num = int(student_num)
    with open("reg_form.txt", 'w') as f:
        for students in range(0, (student_num)):
            ID_number = input("Enter student ID number: \n")
            f.write(ID_number+'\n' + ("-" * 80) +'\n')
    
else:    
    print("Error - You did not enter a number. Check and try again.\n")