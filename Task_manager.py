print("========PERSONAL TASK MANAGER")
print("========")
tasks = []
def save_tasks():
    with open("tasks.txt","w") as file:
        for task in tasks:
            file.write(f'{task["name"]}|{task["completed"]}\n')
try:
    with open("tasks.txt","r") as file:
        for line in file:
           task_name, status= line.strip().split("|")
           tasks.append({"name":task_name,
                   "completed":status.strip()=="True" })
except FileNotFoundError:
    print("No such file exists")
print("1.ADD Task \n 2.View Tasks \n" \
"3.Mark Task completed \n" \
"4. Delete Task \n 5. Exit")

while True:
   try:
        choose = int(input("choose an option from above :"))
        if choose == 5:
            print("===============")
            print("EXIT!!!")
            print("Have a Great day")
            break
        elif choose ==1:
            task = input("Enter your task :")
            if task.isdigit() or task =="":
                print("Enter a valid task!!")
            else:
                tasks.append({"name":task,"completed":False})
                print("Task added successfully")
                save_tasks()
                with open("tasks.txt","a") as file:
                    file.write(task + "\n")
        elif choose ==2:
            if len(tasks) == 0:
                print("No tasks")
            else:
                for task in tasks:
                    if task["completed"]:
                        print(task["name"], "- completed")
                    else:
                        print(task["name"],"- pending")
        elif choose == 4:
            task_name = input("Enter task to delete :")
            found = False
            for task in tasks:
                if task["name"] == task_name:
                    tasks.remove(task)
                    save_tasks()
                    found = True
                    print("Task deleted successfully!!")
                    break
            else:
                print("Task not found !!")
    
        elif choose == 3:
            task_name = input("Enter the completed task name :")
            for task in tasks:
                if task["name"] == task_name:
                    task["completed"] = True
                    save_tasks()
                    print("Task marked completed!!")
                    break
            else:
                print("The task doesnt found")

   except ValueError :
        print("Please choose a correct option")

