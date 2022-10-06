                  
print("L O G I N")
file = open("user.txt", "r+")
rfile = file.read()
user = input("Enter your username:\n")
password = input("Enter your password (case sensitive):\n")
# Prompts user for their username and password.
while user.lower() not in rfile:
    print("This username does not exist, please try again.")
    user = input("\n\nEnter your username:\n")
    break
# Requests user for their username and password until the correct information has been entered.

while password.lower() not in rfile:
    print("The password entered is incorrect,check and try again.")
    password = input("Enter your password (case sensitive):\n")
    break
    file.close()
# Requests user for their username and password until the correct information has been entered.

print("Welcome! \n")    
print("Please select one of the following options:\n "
      "r - register user\n "
      "a - add task\n "
      "va - view all tasks\n "
      "vm - view my tasks\n "
      "e - exit\n")
# Prints a list options for the user to choose from.

option = input(":\t")
# Prompts user to choose an option.

if option.lower() == "r":                                 # For option 'r'.
    file = open('user.txt', 'r+')
    rfile = file.read()
    new_user = input("Enter new username:\n")
    new_pass1 = input("Enter a password for this user:\n")
    new_pass2 = input("Confirm the above password:\n")
# Prompts user to enter a new user's name and password.

    while new_pass2 != new_pass1:
        print("\n\n Your passwords do not match, please check and try again. \n")
        new_pass2 = input("Confirm the above password:\n")
    # Ensures that "new_pass2" matches "new_pass2".
    
    file.write("\n" + new_user + ", " + new_pass1)
    file.close()
    # Writes new information to "user.txt" and closes the file.
    
elif option.lower() == "a":                            # For option 'a'.
    task_user = input("Enter the user that this task will be assigned to:\n")
    title = input("Enter the title of this task:\n")
    desc = input("Enter a task description:\n")
    from datetime import date                   # Importing 'date' from the 'datetime' module.
    today = str(date.today())                   # Casting 'date.today()' into a string enabling it to be written.
    due = input("Enter the tasks due date:\n")
    file = open('tasks.txt', 'r+')
    rfile = file.read()
# Prompts user for multiple inputs and opens 'tasks.txt' in read and write mode.

    file.write("Task:\t" + title+"\n"
             + "Assigned to:\t" + task_user+"\n"
             + "Description of task:\t" + desc + "\n"
             + "Date assigned:\t"+today + "\n"
             + "Due date:\t" + due + "\n"
             + "Completed?:\t" + "No")
    file.close()
# Writes new information to "tasks.txt" and closes the file.
                                        
elif option.lower() == "va":                            # For option 'va'.
    file = open("tasks.txt", "r+")
    rfile = file.read()
    print(rfile)
    file.close()
# Opens 'tasks.txt' in read and write mode then reads the entire file and prints it out.
    
elif option.lower() == "vm":                          # For option 'vm'.
    with open('tasks.txt') as file:                   # Opens 'task.txt' as 'fl'.
        for line in file:
            if user in line:
                for i in range(5):
                    after_line = next(file)           # Using the 'next()' method to return the next 5 lines after the line containing 'user'.
                    print("\n" + after_line)          # Prints the logged in users tasks.
    file.close()
# Closes file.
    
elif option.lower() == "e":                             # For option 'e'.
    exit(0)
# Exits program.
else:
    exit(0)
 # Exits program.


