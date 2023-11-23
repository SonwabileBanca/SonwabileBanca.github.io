#Working with files===================
# Capstone project=================
#Display========
print('=============================================')

print('=====Welcome to the task Manager ==========')
print('=============================================')
print('\n\n\n')

import json

passUsername = None
tasks_filename = 'tasks.txt'

# Function to login
"""
    Perform user login.

    Prompts the user for a username and password, checks against stored information
    in the 'user.txt' file, and sets the global passUsername variable on successful login.

    Raises:
        FileNotFoundError: If 'user.txt' is not found.
    """


def login():
  # use global keyword to declare a global variable
  global passUsername

  try:
    # try to open the file
    with open('user.txt', 'r') as f:
      # separate the username and password by a comma and space.
      stored_info = [line.strip().split(', ') for line in f]
      # A while true loop to ask for username and password
      while True:
        passUsername = input('Enter your username: ')
        passPassword = input('Enter your password: ')
        if [passUsername, passPassword] in stored_info:
          print('Welcome back!')
          break
        else:
          print('Incorrect username or password.')
        # if the username and password is incorrect, the user will be asked to enter the username and password again
# Raise an error if the file is not found
  except FileNotFoundError:
    print('No user found.')


# A function that read a task
def read_tasks_file():
  """
    Read tasks from the 'tasks.txt' file and return a list of tasks.

    Returns:
        list: A list of dictionaries representing tasks.

    Raises:
        FileNotFoundError: If 'tasks.txt' is not found.
        Exception: If an error occurs while reading tasks.
    """
  #
  tasks = []
  try:
    with open('tasks.txt', 'r') as f:
      for line in f:
        task_data = line.strip().split(', ')
        if len(task_data) == 6:
          # use a dictionary to store the task data
          task = {
              'Assigned_to': task_data[0],
              'task_Title': task_data[1],
              'task_Description': task_data[2],
              'task_Due_Date': task_data[3],
              'date_created': task_data[4],
              'Complete': task_data[5]
          }
          tasks.append(task)
    return tasks
  except FileNotFoundError:
    print(f"Error: File '{tasks_filename}' not found.")
    return []
  except Exception as e:
    print(f"An error occurred while reading tasks: {e}")
    return []


# a function that displa the tasks
def display_task(tasks):
  """
    Display information about tasks.

    Args:
        tasks (list): A list of dictionaries representing tasks.

    Raises:
        Exception: If an error occurs while displaying tasks.
    """
  try:
    for task in tasks:
      print(f'Task Title: {task["task_Title"]}')
      print(f'Task Description: {task["task_Description"]}')
      print(f'Task Due Date: {task["task_Due_Date"]}')
      print(f'Date Created: {task["date_created"]}')
      print(f'Complete: {task["Complete"]}')
      print()
  except Exception as e:
    print(f"An error occurred: {e}")


def main():
  global passUsername, tasks_filename

  print('=====Welcome to the task Manager =====')

  login()
  print(f'Logged in as {passUsername}\n')
  # the Menu is a while true loop
  while True:
    print('Menu:')
    print('r. Register a user')
    print('a. Add a task')
    print('va. View all tasks')
    print('vm. View my tasks')
    print('e. Exit')

    choice = input('Enter your choice: ')

    if choice == 'r':
      try:
        usernames = []

        with open('user.txt', 'r') as f:
          for line in f:
            data = line.strip().split(', ')
            if len(data) == 2:
              usernames.append(data[0])
            else:
              print(f'Invalid data format in user.txt: {line}')

        username = input('Enter a new username: ')
        if username in usernames:
          print('Username already exists.')
          continue

        password = input('Enter a new password: ')
        with open('user.txt', 'a') as f:
          f.write(f'{username}, {password}\n')
          print('User registered successfully!')
      except Exception as e:
        print(f"An error occurred: {e}")

    elif choice == 'a':
      # Prompt user to enter task details
      try:
        tasks_detail = {
            'Assigned_to':
            passUsername,
            'task_Title':
            input('Enter the task title: '),
            'task_Description':
            input('Enter the task description: '),
            'task_Due_Date':
            input('Enter the task due date (YYYY-MM-DD): '),
            'date_created':
            input('Enter the date the task was created (YYYY-MM-DD): '),
            'Complete':
            input('Is the task complete? (y/n)').lower()
        }
        # Open the tasks file in append mode

        with open('tasks.txt', 'a') as f:
          # use the join method to join the tasks_detail dictionary with comma and space
          tasks_detail_str = ', '.join(
              str(value) for value in tasks_detail.values())
          f.write(tasks_detail_str + '\n')
          print('Task added successfully!')
      except Exception as e:
        print(f"An error occurred: {e}")

    elif choice == 'va':
      try:
        tasks = read_tasks_file()
        if not tasks:
          print('No tasks available.')
        else:
          print('=====All Tasks=====')
          print('\n')
          display_task(tasks)
          print('\n')
          print('===================')
      except Exception as e:
        print(f"An error occurred: {e}")


# if use choose view task then it will display the tasks of the user that is logged on at the time
# the first index in the txt file will show the name of the person resposible for task
    elif choice == 'vm':
      try:
        tasks = read_tasks_file()
        my_tasks = [
            task for task in tasks if task['Assigned_to'] == passUsername
        ]
        if not my_tasks:
          print(f'No tasks available for {passUsername}.')
        else:
          print(f'=====Tasks for {passUsername}=====')
          print('\n')
          display_task(my_tasks)
          print('\n')
          print('===================')
      except Exception as e:
        print(f"An error occurred: {e}")

    elif choice == 'e':
      print('Exiting the program. Goodbye!')
      print('===================')
      break

    else:
      print('Invalid choice. Please enter a valid option.')

if __name__ == "__main__":
  main()
