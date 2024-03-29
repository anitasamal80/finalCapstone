# The Capstone Project - Task Manager
A program designed for a small business that can help it to manage task assigned to each member.
### Using this application you can:
* Register a new user
* Add a new task
* View all tasks
* View user own task
* Generate Report (admin only)
* Display Report (admin only)    
* Display Statistics (admin only)

Note:-
Once user is successfully logged in, it creates a user.txt file, adds an admin user and displays menu items.

#### Register a new user
* Adds a new user (to user.txt)
* user must provide password twice and the password must match
#### Add a new task
Allow a user to add a new task to task.txt file
Prompt a user for the following: 
 - A username of the person whom the task is assigned to,
 - A title of a task,
 - A description of the task and 
 - the due date of the task
#### View all tasks
Reads the task from task.txt file and prints to the console. If the user chooses 'va' then it will display all the tasks.
#### View user own task
Reads the task from task.txt file and prints to the console. If the user chooses 'vm'to view the task that are  assigned the user is currently logged in. User select the task number to edit.
#### Generate Report
Generating report by creating task_overview and user_overview file
#### Display Report
Display report about user and tasks statistics by using the file user_overview.txt
and  task_overview.txt first check whether the file exist or not if not then
first it will shows message to generate report-gr then it will shows report.
#### Display Statistics
Display statistics about number of users and tasks

#### How to Run this code
1. clone the repository
2. cd finalCapstone
3. python task_manager.py

Note:-
Use the following username and password to access the admin rights 
username: admin
password: password
