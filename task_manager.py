"""Create a program designed for a small business to help it manage 
tasks assigned to each member of a team.
"""
#pseudocode

#1. start
#2. declare global variables
#3. prompt user for username and password. 
#4. If login sucessfully then display menu option for different task
#5. For each menu item write a seperate function
#6. Menu options are registering user, adding tasks, view task, view my task,
#edit task, generating report, display statistics,display report 
#7.In register user- add new user to the user.txt file, if not exist 
#8.add task - add new task to the user
#9.edit task - edit existing task in the file or assign a task to other user and update in file.
#10.generate report -create file task_overview and user_overview file
#11.display report- print the report using task_overview and user_overview files to the console
#12. stop


# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====Importing Libraries===========

import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

#====Functions Defination Section====

def get_user_accounts():
    # If no user.txt file, write one with a default account
    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as default_file:
            default_file.write("admin;password")

    # Reading  user data
    with open("user.txt", 'r') as user_file:
        user_data = user_file.read().split("\n")

    # Convert to a dictionary
    username_password = {}
    for user in user_data:
        username, password = user.split(';')
        username_password[username] = password
    
    return username_password


def get_tasks():
    # Create tasks.txt if it doesn't exist
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w") as default_file:
            pass

    # Reading from the file tasks.txt
    with open("tasks.txt", 'r') as task_file:
        task_data = task_file.read().split("\n")
        task_data = [task_str for task_str in task_data if task_str != ""]


    task_list = []
    for task_str in task_data:
        curr_task = {}

    # Split by semicolon and manually add each component
        task_components = task_str.split(";")
        curr_task['username'] = task_components[0]
        curr_task['title'] = task_components[1]
        curr_task['description'] = task_components[2]
        curr_task['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
        curr_task['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        curr_task['completed'] = True if task_components[5] == "Yes" else False

        task_list.append(curr_task)

    return task_list


def login():
    '''This code reads usernames and password from the user.txt file to 
    allow a user to login. Display an appropriate error message if the 
    user enters a username and password that is not in the listed file and it stores in
    following format:
    -a username followed by comma and then password
    -one username and corresponding password per line    
    '''
    logged_in = False
    while not logged_in:

        print("\n\n=============TASK MANAGER LOGIN=============\n\n")
        curr_user = input("Username: ")
        #curr_pass = input("Password: ")
        if curr_user not in user_accounts.keys():
            print("User does not exist")
        elif user_accounts[curr_user] != input("Password: "):
            print("Wrong password")
            continue
        else:
            print("Login Successful!")
            logged_in = True
    return curr_user


def display_menu():
    '''Menu should be displayed once user successfully logged in.
    '''
    input("Press enter to Retun to Main Menu: ")
    #clear the screen 
    os.system("cls")
    if current_user == "admin":
            #menu options for admin
            menu = input('''Select one of the following Options below:
            r -  Registering A User
            a -  Adding A Task
            va - View All Tasks
            vm - View My Tasks
            gr - Generate Report
            dr - Display Report
            ds - Display Statistics
            e -  Exit
======================================================
            \n> ''').lower()
    else:
            #menu options for other users
            menu = input('''Select one of the following Options below:
            r -  Registering a user
            a -  Adding a task
            va - View all tasks
            vm - View my task
            e -  Exit
======================================================

            \n> ''').lower()
            
    return menu

    
def main_menu():
    '''Process the user selected options.
    '''
    while True:
        # presenting the menu to the user and 
        # making sure that the user input is converted to lower case.
        print("="*55)
        menu = display_menu()
    
        if menu == 'r':
            register_new_user()
       
        elif menu == 'a':
            task_username = input("Name of a person to assigned task: ")
            if task_username not in user_accounts.keys():
                print("User does not exist. Please enter a valid username.")
                continue
            add_task(task_username)
        
        elif menu == 'va':
            display_all_tasks()
           
        elif menu == 'vm':
            my_tasks(current_user)
             
        elif menu == 'gr'and current_user == 'admin':
            generate_report()    
        
        elif menu == 'dr'and current_user == 'admin':
            display_report()
        
        #Display statistics only for admin user
        elif menu == 'ds' and current_user == 'admin': 
            display_statistics()
        
        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")
    

def does_user_exist(user_name):
    '''check whether the user exists or not by extrating keys from dictionary
    '''
    user_exist = False
    user_names = user_accounts.keys()
    for name in user_names:
        if name == user_name:
            user_exist = True
            break
            
    return user_exist


def register_new_user():
    '''Add a new user to the user.txt file'''
    # - Request input of a new username
    new_username = input("New Username: ")
    while does_user_exist(new_username):
        new_username = input("New Username: ")
    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")
    new_username_password = {}

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        new_username_password[new_username] = new_password
            
        with open("user.txt", "a+") as out_file:
            user_data = []
            for k in new_username_password:
                user_data.append(f"\n{k};{new_username_password[k]}")
                out_file.write("\n".join(user_data))

        #Now update the user_accounts global variable
        user_accounts.update(new_username_password)
    # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")


def display_all_tasks():
    '''Reads the task from task.txt file and prints to the console in the 
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling). If the user chooses 'va' then it will display all 
    the tasks. 
    '''
    
    for task in task_list:
        disp_str = f"Task: \t\t {task['title']}\n"
        disp_str += f"Assigned to: \t {task['username']}\n"
        disp_str += f"Date Assigned: \t {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: {task['description']}\n"
        task_status = "Yes" if task['completed'] == True else "No"
        disp_str += f"Task Status: \t {task_status}\n" 
        print(disp_str)
        print("="*55)


def my_tasks(user_name):
    '''Reads the task from task.txt file and prints to the console in the 
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling). If the user chooses 'vm'to view the task that are  assigned
    the user is currently logged in.
    '''
    print(f"Task list for :{current_user}")
    print("-"*55)
    
    #Filter out user's tasks
    user_tasks = [task for task in task_list if task['username'] == user_name]
    
    enum_task_list = enumerate(user_tasks,1)
    for t in enum_task_list:
        # Now the dictionary is the 2nd item (index=1) in the enumerated tuple
            disp_str = f"Task No: \t {t[0]}\n"
            disp_str += f"Task: \t\t {t[1]['title']}\n"
            disp_str += f"Assigned to: \t {t[1]['username']}\n"
            disp_str += f"Date Assigned: \t {t[1]['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t[1]['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: {t[1]['description']}\n"
            task_status = "Yes" if t[1]['completed'] == True else "No"
            disp_str += f"Task Status: \t {task_status}\n" 
            print(disp_str)
            print("="*55)
    
    #allow user to edit task
    
    if len(user_tasks) !=0:
        selected_task_no = int(input('''Please select the task number to edit 
Or -1 return to main menu > '''))
        if selected_task_no != -1:
            user_option = input('''What would you like to do:
            c - Complete
            e - Edit Task
            >\n ''').lower()  
        #Enumerating the tasks to find the matching user selected task
            enum_task_list = enumerate(user_tasks,1)
            selected_task = {}
            for enumated_task in enum_task_list:
                if enumated_task[0] == selected_task_no:
                    selected_task = enumated_task[1]
                    break
                       
            if user_option == "c" and selected_task != {} :                
                complete_task(selected_task)
            
            elif user_option == "e" and selected_task != {}:
                edit_task(selected_task)
            else:
                print("Invalid Option")
    
        else:
            print("You selected -1. Returing to main menu ...")
    else:
        print("You have no task")     
    

def edit_task(task_to_edit):
    '''Editing the task to mark as complete or assign to other user .
    '''
    if task_to_edit['completed'] is False:   
        print(f"You have selected to edit Task: {task_to_edit} ")
        edit_option = input('''What would you like to change:
            u - Username to Assign someone
            d - Due Date
            : ''').lower()
        
        list_updated = False
        if edit_option == "u":
            assign_to = input("Please enter a username to assign this task: ")
            if does_user_exist(assign_to) is True:
                for task in task_list:
                    if task == task_to_edit:
                        task['username'] = assign_to
                list_updated = True
            else:
                print("User does not exist.")            
        elif edit_option == "d":
            new_due_date = input(f"Please enter a new due date {DATETIME_STRING_FORMAT} for this task: ")
            for task in task_list:
                if task == task_to_edit:
                    # converting the date string into a python date
                    task['due_date'] = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
            list_updated = True
        
        if list_updated is True:
            update_task_file()         
    else:
        print("completed task cannot be edited")


def complete_task(task_to_complete):
    
    print(f"Complete the task :{task_to_complete}" )
    for task in task_list:
        if task == task_to_complete:
            task['completed'] =True
    update_task_file()


def display_statistics():
    '''Display statistics about number of users
    and tasks.'''
    num_users = len(user_accounts.keys())
    num_tasks = len(task_list)

    print("-----------------------------------")
    print(f"Number of users: \t\t {num_users}")
    print(f"Number of tasks: \t\t {num_tasks}")
    print("-----------------------------------") 
    print("\n")   


def display_report():
    '''
    Display report about user and tasks statistics by using the file user_overview.txt
    and  task_overview.txt first check whether the file exist or not if not then
    first it will shows message to generate report-gr then it will shows report.
    .'''
     
    if not (os.path.exists("task_overview.txt") and os.path.exists("user_overview.txt")):
        print("First generate the report using -gr- option")
        return

    with open("task_overview.txt", 'r') as task_file:
        task_data = task_file.read().split("\n")
        for data in task_data:
            print(data)
        
    with open("user_overview.txt", 'r') as task_file:
        user_data = task_file.read().split("\n")
        for data in user_data:
            print(data)
            

def add_task(task_username):
    '''Allow a user to add a new task to task.txt file
    Prompt a user for the following: 
    - A username of the person whom the task is assigned to,
    - A title of a task,
    - A description of the task and 
    - the due date of the task.'''
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
    print(f"the date is: {curr_date} ")
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
    print("adding a new task")

    task_list.append(new_task)
    update_task_file()
    print("Task successfully added.")


def update_task_file():
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

                 
def generate_report():
    '''Generating report by creating task_overview and user_overview file.
    '''
    print("Report Generated: ")
    create_task_overview()
    create_user_overview()


def create_task_overview():
    '''
    creates task oeverview records calculating statics of tasks.
    '''
    total_tasks =len(task_list)
    completed_tasks = len([task for task in task_list if task['completed'] is True])
    uncompleted_tasks = len([task for task in task_list if task['completed'] is False])
    overdue_tasks = len([task for task in task_list if task['completed'] is False\
          and task['due_date'].date() < datetime.now().date()])
    
    #calculate percentage, rounding to 2 decimal places
    pc_incomplete = round(uncompleted_tasks*100/len(task_list), 2)
    pc_overdue = round(overdue_tasks*100/len(task_list),2)
    
    task_overview_list = []
    task_overview_list.append(f"========= TASK OVERVIEW - PREPARED DATE :{datetime.now().date()} ==========\n\n")
    task_overview_list.append(f"The total number of tasks : {total_tasks} \n")
    task_overview_list.append(f"The total number of completed tasks : {completed_tasks} \n")    
    task_overview_list.append(f"The total number of uncompleted tasks :{uncompleted_tasks} \n")
    task_overview_list.append(f"The total number of overdue task :{overdue_tasks} \n")
    task_overview_list.append(f"The percentage of tasks that are incomplete :{pc_incomplete} %\n")
    task_overview_list.append(f"The percentage of tasks that are overdue :{pc_overdue} %\n")
    task_overview_list.append("\n==================================================================")
    
    write_report_data("task_overview.txt", task_overview_list)
    
    
def create_user_overview():
    '''
    creates user overview records, calculating statistics for each user tasks.
    '''
    num_users = len(user_accounts.keys())
    total_tasks = len(task_list)
    
    user_overview_list = []
    user_overview_list.append(f"========= USER OVERVIEW - PREPARED DATE :{datetime.now().date()} ==========\n\n")
    user_overview_list.append(f"The total number of users :{num_users} \n")
    user_overview_list.append(f"The total number of tasks :{total_tasks} \n\n")
    for username in user_accounts.keys():
        
        #total task count for this user
        user_task_count = len([task for task in task_list if task['username'] == username])
        
        #completed task for this user
        user_completedtask_count = len([task for task in task_list \
            if task['username'] == username and task['completed'] is True])
        
        #incompleted task for this user
        user_incompletedtask_count = len([task for task in task_list \
            if task['completed'] is False \
                and task['username'] == username])
        
        #percentage task for this user
        pc_user_total_task = user_task_count*100/total_tasks\
        if total_tasks != 0 else 0
    
        #percentage completed by this user
        pc_user_completed_task = user_completedtask_count*100/user_task_count\
        if user_task_count != 0 else 0  
        
        #percentage incomplete by this user
        pc_user_incompleted_task = user_incompletedtask_count*100/user_task_count\
        if user_task_count != 0 else 0
        
        user_overdue_task_count = len([task for task in task_list \
            if task['due_date'].date() < datetime.now().date()\
                and (task['completed'] is False \
                and task['username'] == username)])
        
        pc_user_overdue_task =user_overdue_task_count*100/user_task_count \
        if user_task_count != 0 else 0
        
        user_overview_list.append(f"\n=========OVERVIEW FOR USER {username}========\n\n") 
        user_overview_list.append(f"The total number of tasks assigned : {user_task_count} \n")
        user_overview_list.append(f"The percentage of total number of tasks : {round(pc_user_total_task,2)}\n")
        user_overview_list.append(f"The percentage of total number of tasks completed :{round(pc_user_completed_task,2)}% \n")
        user_overview_list.append(f"The percentage of total number of tasks incomplete:{round(pc_user_incompleted_task,2)}% \n")
        user_overview_list.append(f"The percentage of total number of tasks overdue: {round(pc_user_overdue_task,2)}% \n")  
    user_overview_list.append("\n============================================\n")        
    
    write_report_data("user_overview.txt", user_overview_list)


def write_report_data(file_name, report_data_list):
    '''
    Writes records provided as a list of lines to a given file.
    '''
    with open(file_name, "w") as report_file:
        for item in report_data_list:
            report_file.write(item)


#===End Of Functions Definations===

#===Main Program===

#Global variables for efficiency

task_list = get_tasks()
user_accounts = get_user_accounts()
current_user = login()        
main_menu()
    