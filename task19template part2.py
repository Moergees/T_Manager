
print("L O G I N")
file = open("user.txt", "r+")
rfile = file.read()
user = input("Enter your username:\n")
password = input("Enter your password (case sensitive):\n")

while user.lower() not in rfile:
    print("This username does not exist, please try again.")
    user = input("\n\nEnter your username:\n")
    break

while password.lower() not in rfile:
    print("The password entered is incorrect,check and try again.")
    password = input("Enter your password (case sensitive):\n")
    break

file.close()
print("Welcome! \n\n")
# Provides only 'admin' with the stats option in the menu
if user == "admin":                       
    print("Please select one of the following options:\n "
          "r - register user\n "
          "a - add task\n "
          "va - view all tasks\n "
          "vm - view my tasks\n "
          "s - view statistics\n "
          "e - exit\n")
else:
    print("Please select one of the following options:\n "
          "r - register user\n "
          "a - add task\n "
          "va - view all tasks\n "
          "vm - view my tasks\n "
          "e - exit\n")

option = input(":\t")

# Ensures that only 'admin' can access this option.
if option.lower() == "r":
    if user == 'admin':                   
        file = open('user.txt', 'r+')
        rfile = file.read()
        new_user = input("Enter new username:\n")
        new_pass1 = input("Enter a password for this user:\n")
        new_pass2 = input("Confirm the above password:\n")

        while new_pass2 != new_pass1:
            print("\n\n Your passwords do not match, please check and try again. \n")
            new_pass2 = input("Confirm the above password:\n")
    
        file.write("\n" + new_user + ", " + new_pass1)
        user_count = 0
        for line in file:
            user_count += line
        file.close()
        
    else:
        print("Only Admin users can use this feature.")
    
elif option.lower() == "a":
    task_user = input("Enter the user that this task will be assigned to:\n")
    title = input("Enter the title of this task:\n")
    desc = input("Enter a task description:\n")
    from datetime import date                           
    today = str(date.today())                           
    due = input("Enter the tasks due date:\n")
    file = open('tasks.txt', 'r+')
    rfile = file.read()
    file.write("Task:\t" + title+"\n"
             + "Assigned to:\t" + task_user+"\n"
             + "Description of task:\t" + desc + "\n"
             + "Date assigned:\t"+today + "\n"
             + "Due date:\t" + due + "\n"
             + "Completed?:\t" + "No")
    file.close()
    
                                        
elif option.lower() == "va":                            
    file = open("tasks.txt", "r+")
    rfile = file.read()
    print(rfile)
    file.close()
    
    
elif option.lower() == "vm":                            
    with open('tasks.txt') as file:                       
        for line in file:
            if user in line:
                for i in range(5):
                    after_line = next(file)               
                    print("\n" + after_line)
    file.close()
# For 's'.    
elif option.lower() == "s":         
    if user == 'admin':
        with open('user.txt') as file:
            line_count = 0
            for i in file:
                line_count += 1
                users = line_count - 1
        print("Total number of registered users:\t", users)
        file.close()
# Since each user in "user.txt" is on a new line the for loop counts each line then
# subtracts 1 (to exclude empty lines), ultimately counting the amount of users.

        with open('tasks.txt', 'r+') as file:
            task_count = 0
            for line in file:
                if "Task:" in line:
                    task_count += 1
        print("Total number of tasks:\t", task_count)
        file.close()                
# Since each task contains the string "Task:"  the for loop counts every line
# that contains the specified string,ultimately counting each task.
        

elif option.lower() == "e":                             
    exit(0)
    
else:
    exit(0)
