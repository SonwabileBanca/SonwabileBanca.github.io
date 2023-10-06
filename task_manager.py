# Capstone project
#Display
display = '''Good Day Sir/Madam, This is the \033[034mTask Manager\033[0m
Where we Assist you in managing your duties.'''
print(display + '\n')

#=====importing libraries===========

from datetime import datetime

current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print('Current date:', current_date)

#====Login Section====

with open('user.txt', 'r') as f:
  usernames = f.readlines()
  
  print(usernames)

usernames = [username.strip() for username in usernames]
print('Usernames', usernames)

# Correct usernames and password
correct_username = 'admin'
correct_password = 'adm1n'

# Validate and Inintaialise for user input
username = input('Enter usename:')
password = input('Enter password:')
#While loop to check that username and password is correct
while username != correct_username or password != correct_password:
  print('Error: Invalid username or password')
  username = input('Enter username\t')
  password = input('Enter password\t')
print('Login Completed!')

while True:
  # presenting the menu to the user and
  # making sure that the user input is coneverted to lower case.
  menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

  if menu == 'r':
    pass
    new_username = input('Enter a new username:')
    new_password = input('Enter new password:')
    confirm_password = input('Confirm the password:')
    if new_password == confirm_password:
      # Open the file on apppend mode and add a new udername & Password
      with open('user.txt', 'a') as f:
        f.write(f'{new_username}:{new_password}\n')
      print('The New user has been added succesfully')
    else:
      print('Password failed!, try again please.')

  elif menu == 'a':
    pass
    # Prompt details about task specifics.
    assigned_to = input('The person the task was assigned to:\n')
    title_task = input('Enter the title of the task:')
    task_description = input('Enter the description of task')
    due_date = input('Enter the due Date of task:')
    # Create a string to represent the task
    task_entry = f'Assigned to: {assigned_to}\nTitle: {title_task}\nDiscription: {task_description}\nDue Date: {due_date}\nDate Created: {current_date}\nCompleted No\n'
      
    with open('tasks.txt', 'a') as f:
      f.write(task_entry + '\n')
    print('Task was added scuccesfully!')
  elif menu == 'va':
    pass
    with open('tasks.txt', 'r') as f:
      # Read a line from user.txt
      line = f.readline()
      value = line.strip().split(', ')
      user_info = {'tasks': value[0],
                  'Assigned to': value[1],
                  'Date assigned': value[2],
                  'Due date': value[3],
                  'Tasks Complete?': value[4],
                  'Task description': value[5]
      }
      # The information of the user
      for key, value in user_info.items():
        print(f'{key}:{value}')

  elif menu == 'vm':
    pass
    with open('tasks.txt','r') as f:
      line = f.readline()
      value = line.strip().split(', ')
    log_in_username = input('Enter your username:')
    with open('user.txt', 'r') as f:
      line = f.readline()
      # Strip the newline charachters
      username, password = line.strip().split(',')
      if username == log_in_username:
        user_info = {'Tasks': value[0],
                  'Assigned to': value[1],
                  'Date assigned': value[2],
                  'Due date': value[3],
                  'Task Complete?': value[4],
                  'Task description': value[5]
                    }
        print('Login Succesful!')
      else:
        print('Username not found unfortunately')
        
  elif menu == 'e':
    print('Goodbye!!!')
    exit()

  else:
    print("You have made a wrong choice, Please Try again")