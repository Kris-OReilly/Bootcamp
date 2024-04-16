# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%d-%m-%Y"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")
    

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


def reg_user():
    while True:

        '''Add a new user to the user.txt file'''
        # - Request input of a new username
        new_username = input("New Username: ")
            
        # - Open the user file and check the input against existing usernames
        with open('user.txt', 'r') as users:
            lines = users.readlines()
        for line in lines:
            existing_user, _ = line.strip().split(';')
            if new_username == existing_user:
                print("Username already exists, please try again")
                break
        else:
            # - Request input of a new password
            new_password = input("New Password: ")

            # - Request input of password confirmation.
            confirm_password = input("Confirm Password: ")

            # - Check if the new password and confirmed password are the same.
            if new_password == confirm_password:
                # - If they are the same, add them to the user.txt file,
                print("New user added")
                username_password[new_username] = new_password
                
                with open("user.txt", "w") as out_file:
                    user_data = []
                    for k in username_password:
                        user_data.append(f"{k};{username_password[k]}")
                    out_file.write("\n".join(user_data))
                    break

                # - Otherwise you present a relevant message.
            else:
                print("Passwords do not match")
            

def add_task():
    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
            - A username of the person whom the task is assigned to,
            - A title of a task,
            - A description of the task and 
            - the due date of the task.'''
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
    else:
        pass
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")


    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")


def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling) 
    '''

    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)


def update_tasks_file(tasks):
    # Update the tasks.txt file with the given list of tasks. The function converts the list
    # of tasks into a formatted string and writes it to the file.


    # If tasks is a string, convert it to a list of dictionaries
    if isinstance(tasks, str):
        tasks = [dict(zip(['username', 'title', 'description', 'due_date', 'assigned_date', 'completed'], task.split(';')))
                 for task in tasks.strip().split('\n')]

    with open("tasks.txt", "w") as file:
        for task in tasks:
            # Convert completed status to "Yes" or "No"
            completed_status = "Yes" if task.get('completed', False) else "No"
            
            # Write formatted task details to the file
            file.write(f"{task['username']},{task['title']},{task['description']},"
                       f"{task['assigned_date'].strftime('%d-%m-%Y')},{task['due_date'].strftime('%d-%m-%Y')},"
                       f"{completed_status}\n")


def edit_task(chosen_task, task_list):
    # open tasks.txt, locate relevant task number, check the task is not complete.
    # If not complete, allow user to edit the username of task assigned or the due date of task.

    if chosen_task['completed']:
        print("\nCannot edit a completed task.\n")
        return
    
    while True:
        new_username = input("Enter the new user:\t\t ").lower()
        # Check if the new_username exists in the user file
        if new_username in username_password:
            break
        else:
            print("\nUser not found. Please enter a valid username.\n")

    while True:
        try:
            new_due_date = input("New Due Date (DD-MM-YYYY):\t ")
            due_date_time = datetime.strptime(new_due_date, "%d-%m-%Y")
            break  # Break the loop if the input is a valid date
        except ValueError:
            print("Invalid date format. Please enter the date in the format DD-MM-YYYY.")


    new_task = input("New Title:\t\t\t ")
    new_description = input("New Description:\t\t ")
    

    try:
        due_date_time = datetime.strptime(new_due_date, "%d-%m-%Y")
        # Update task attributes with new values
        chosen_task['username'] = new_username
        chosen_task['due_date'] = due_date_time
        chosen_task['title'] = new_task
        chosen_task['description'] = new_description
        chosen_task['completed'] = False  # Reset completed status
        update_tasks_file(task_list)
        print("\nTask has been edited successfully.\n")
        print("*" * 80 + "\n")
    except ValueError:
        print("Invalid datetime format. Task not edited.")


def mark_complete(tasks):
    # If tasks is a string, convert it to a list of dictionaries
    if isinstance(tasks, str):
        tasks = [dict(zip(['username', 'title', 'description', 'due_date', 'assigned_date', 'completed'], task.split(';')))
                 for task in tasks.strip().split('\n')]

    with open("tasks.txt", "w") as file:
        for task in tasks:
            # Convert completed status to "Yes" or "No"
            completed_status = "Yes" if task.get('completed', False) else "No"
            
            # Write formatted task details to the file
            file.write(f"{task['username']},{task['title']},{task['description']},"
                       f"{task['assigned_date'].strftime('%d-%m-%Y')},{task['due_date'].strftime('%d-%m-%Y')},"
                       f"{completed_status}\n")
            

def view_mine(curr_user, task_list):
    '''Display the tasks assigned to the current user.

    Using the current username and the task_list, filters each task and displays the task information
    for each task. The user can select a task to view the details, mark the task complete or edit
    the task. 
    '''

    # filter tasks assigned to current user
    user_assigned_tasks = [t for t in task_list if t['username'] == curr_user]

    if not user_assigned_tasks:
        print("You have no assigned tasks.")
    else:
        for index, t in enumerate(user_assigned_tasks, start=1):
            disp_str = f"Task {index}: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t\t {t['username']}\n"
            disp_str += f"Date Assigned: \t\t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t\t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \t {t['description']}\n"
            print(disp_str)


        # present a menu for user to select a specific task
        while True:
            print()
            task_menu = int(input('''Type a task number to select it or enter -1 to return to the main menu:'''))

            if task_menu == '-1':
                return None

            try:
                task_index = int(task_menu) - 1
                if 0 <= task_index < len(user_assigned_tasks):
                    chosen_task = user_assigned_tasks[task_index]
                    print("\nSelected Task Details\n")
                    print(f"Title: \t\t\t {chosen_task['title']}")
                    print(f"Assigned to: \t\t {chosen_task['username']}")
                    print(f"Date Assigned: \t\t {chosen_task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
                    print(f"Due Date: \t\t {chosen_task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
                    print(f"Task Description: \t {chosen_task['description']}\n")
                    print(f"Status: \t\t {'Completed' if chosen_task['completed'] else 'Not Completed'}\n")
                    print("_ " * 40 + "\n")


                    # variable to store the user option of marking a task complete or editing it
                    task_edit = input("Type 'm' to mark task complete, 'e' to edit task or '-1' to exit to main menu:").lower()

                    # loop to keep asking for correct input
                    while task_edit not in ['m', 'e', '-1']:
                        task_edit = input("Please enter 'm' to mark as complete, 'e' to edit, or '-1' to return to menu: ").lower()

                    if task_edit == 'm':
                        chosen_task['completed'] = True
                        mark_complete(task_list)
                        print("\nTask marked as complete\n")

                    elif task_edit == 'e':
                        edit_task(chosen_task, task_list)
                    
                    elif task_edit == '-1':
                        break

                    else:
                        print("You didn't choose 'm' or 'e'")
                
            except ValueError:
                print("\nInvalid task number, try again\n")
                

def load_tasks():
    # Function to load the tasks from the tasks.txt file and return a list of dictionaries
    # representing the tasks for the user

    try:
        with open("tasks.txt", "r") as file:
            lines = file.readlines()

        # Convert lines to a list of dictionaries
        tasks = [dict(zip(['username', 'title', 'description', 'due_date', 'assigned_date', 'completed'], line.strip().split(';')))
                 for line in lines]

        return tasks

    except FileNotFoundError:
        print("File not found. Returning an empty list.")
        return []
   
        
def read_task_file():
    # read the task details from the tasks.txt file and returns a list of dictionaries

    with open("tasks.txt", "r") as file:
        tasks = []
        for line in file:
            # Splitting the line into different attributes based on the comma separator
            line_split = line.strip().split(";")
            
            # Check if the line has the expected number of elements
            if len(line_split) == 6:
                user_dict = {
                    "username": line_split[0],
                    "title": line_split[1],
                    "description": line_split[2],
                    "due_date": datetime.strptime(line_split[3], "%d-%m-%Y"),
                    "assigned_date": datetime.strptime(line_split[4], "%d-%m-%Y"),
                    "completed": line_split[5] == "Yes"
                }
                tasks.append(user_dict)
            else:
                # Print a warning and skip the line if the format is unexpected
                print(f"Warning: Skipping line due to unexpected format: {line}")

        return tasks


def generate_task_overview(task_list):
    # Function to generate a summary of task completion as a status and write to a text file.

    # Initiate task count variables
    completed_tasks = 0
    incomplete_tasks = 0
    overdue_tasks = 0

    # For each task, update variables accordingly
    for task in task_list:
        completed_status = task.get("completed", False)
        if completed_status:
            completed_tasks += 1
        elif "due_date" in task:
            due_date = task["due_date"]
            if isinstance(due_date, str):
                due_date = datetime.strptime(due_date, "%d-%m-%Y")

            if datetime.today() > due_date:
                incomplete_tasks += 1
                overdue_tasks += 1
            else:
                incomplete_tasks += 1
        else:
            incomplete_tasks += 1

    total_tasks = len(task_list)

    # Calculate percentages for each variable
    try:
        pc_complete = (completed_tasks / total_tasks) * 100
        pc_incomplete = (incomplete_tasks / total_tasks) * 100
        pc_overdue = (overdue_tasks / total_tasks) * 100

    # If there are no tasks at all, set all percentages to 0
    except ZeroDivisionError:
        pc_complete = pc_incomplete = pc_overdue = 0

    with open("task_overview.txt", "w", encoding="utf-8") as report_file:
        report_file.write("\tTask Overview Report\n\n")
        report_file.write(f"Total Tasks: \t\t\t {total_tasks}\n")
        report_file.write(f"Completed Tasks: \t\t {completed_tasks}\n")
        report_file.write(f"Incomplete Tasks: \t\t {incomplete_tasks}\n")
        report_file.write(f"Overdue Tasks: \t\t\t {overdue_tasks}\n")
        report_file.write(f"Percentage of completed Tasks: \t {pc_complete:.0f}%\n")
        report_file.write(f"Percentage of Incomplete Tasks:  {pc_incomplete:.0f}%\n")
        report_file.write(f"Percentage of Overdue Tasks: \t {pc_overdue:.0f}%\n")


def generate_user_overview(username_password, task_list):
    # Function to generate a detailed overview of the tasks assigned to each user
    # This then writes the information to a text file.

    # Initiate variables for number of users and number of tasks
    total_users = len(username_password)

    with open("user_overview.txt", "w") as report_file:
        report_file.write("----------------------------------------\n")
        report_file.write("\tUser Overview Report\n\n")
        report_file.write(f"Total number of users: \t\t {total_users}\n")
        report_file.write("-----------------------------------------\n")

        print("Inside generate_user_overview")  # Debug statement

        for current_user in sorted(username_password):
            print(f"Processing user: {current_user}")  # Debug statement

            user_tasks_list = [task for task in task_list if task['username'] == current_user]

            print(f"Tasks for user {current_user}: {user_tasks_list}")  # Debug statement

            user_total_tasks = len(user_tasks_list)
            print(f"Total tasks for user {current_user}: {user_total_tasks}")

            # Set variables to 0
            completed_tasks = 0
            incomplete_tasks = 0
            overdue_tasks = 0

            # For each task, update variables accordingly
            for user_task in user_tasks_list:
                if user_task["completed"]:
                    completed_tasks += 1
                elif datetime.today() > user_task["due_date"]:
                    incomplete_tasks += 1
                    overdue_tasks += 1
                else:
                    incomplete_tasks += 1
            
            # Calculate percentages for each variable
            try:
                pc_assigned = (user_total_tasks / len(task_list)) * 100
                pc_completed = (completed_tasks / user_total_tasks) * 100
                pc_incomplete = (incomplete_tasks / user_total_tasks) * 100
                pc_overdue = (overdue_tasks / user_total_tasks) * 100

            # If user has no tasks assigned, set all percentages to 0
            except ZeroDivisionError:
                pc_assigned = pc_completed = pc_incomplete = pc_overdue = 0

            report_file.write(f"\nUser: \t\t\t\t {current_user}\n")
            report_file.write(f"Total Tasks Assigned: \t\t {user_total_tasks}\n")
            report_file.write(f"Percentage of Total Tasks: \t {pc_assigned:.0f}%\n")
            report_file.write(f"Percentage of Completed Tasks: \t {pc_completed:.0f}%\n")
            report_file.write(f"Percentage of Incomplete Tasks:  {pc_incomplete:.0f}%\n")
            report_file.write(f"Percentage of Overdue Tasks: \t {pc_overdue:.0f}%\n")



# Load the tasks information from the tasks.txt file
task_list = load_tasks()


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print("\n---MAIN MENU---\n")
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        #Register a new user
        reg_user()

    elif menu == 'a':
        #Add a new task
        add_task()

    elif menu == 'va':
        #View all tasks
        task_list = read_task_file()
        view_all()

    elif menu == 'vm':
        #View tasks assigned to current user
        view_mine(curr_user, task_list)
    
    elif menu == 'gr' and curr_user == 'admin':
        # Generate reports (admin-only)
        generate_task_overview(task_list)
        generate_user_overview(username_password, task_list)
        print("*" * 80 + "\n")
        print("\nReports generated successfully.\n")
        print("*" * 80 + "\n")

    elif menu == 'ds' and curr_user == 'admin': 
        # Display statistics if admin or generate the reports if the don't yet exist

        print("Generating statistics...")
        print(f"Current user: {curr_user}")

        if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
            # Generate reports if not exist         
            generate_task_overview(task_list)
            generate_user_overview(username_password, task_list)
            print("Reports generated successfully.")
            
        else:
            # Read and display statistics from the existing reports
            with open("task_overview.txt", "r") as task_report_file:
                task_report_data = task_report_file.read()
                print(task_report_data)

            with open("user_overview.txt", "r") as user_report_file:
                user_report_data = user_report_file.read()
                print(user_report_data)

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")