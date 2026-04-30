
import json

################ JSON saving now ########################

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except:
        return[]

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


#############      Hello PC! let's WARM-UP ########################

to_do = ["breakfast", "code", "Vermouth"]
numbering = 0
for task in to_do:
    numbering += 1
    print(f"{numbering}. {task}")

for index, task in enumerate(to_do):
    print(f"{index+1}. {task}")

################### MAIN EXERCIZE #############################

tasks = []

def add_task(list_of_tasks):

    try:
        name_task = str(input("Please input a new task name: "))
        status_task = bool(input("Please input the status of the task (Completed/leave Empty): "))
        new_task = {
            "name": name_task,
            "status": status_task
        }
    except ValueError:
        print("Invalid input. Please enter a valid task name and status.")
        return
    list_of_tasks.append(new_task)


def show_tasks(list_of_tasks):
    if not list_of_tasks:
        print("No tasks yet in the list!")
    else:
        for index, task in enumerate(list_of_tasks):
            print(f"Task {index+1}: {task['name']} - Status: {task['status']}")

def remove_task(list_of_tasks,task_index):
    try:
        task_index = int(input("Which task would you like to remove? "))
        if not list_of_tasks:
            print("No tasks yet in the list!")
        else:
            list_of_tasks.pop(task_index - 1)
            print(f"Task number {task_index} removed.")
            for index, task in enumerate(list_of_tasks):
                print(f"Task {index+1}: {task['name']}")
    except ValueError:
        print("Invalid input. Please enter a number.")

def remove_task2(list_of_tasks):
    if not list_of_tasks:
        print("No tasks yet in the list!")
        return
    try:
        task_index = int(input("Which task would you like to remove? "))
        
        if task_index < 1 or task_index > len(list_of_tasks):
            print("Invalid task number.")
            return
        else:
            list_of_tasks.pop(task_index - 1)
            print(f"Task number {task_index} removed.")
            for index, task in enumerate(list_of_tasks):
                print(f"Task {index+1}: {task['name']}")
    except ValueError:
        print("Invalid input. Please enter a number.")


def mark_done(lists_of_tasks):
    if not lists_of_tasks:
        print("No tasks yet in the list!")
        return
    try:
        task_index = int(input("Which task would you like to mark as done? "))
        print (f"You chose {task_index}")        
        if task_index < 1 or task_index > len(lists_of_tasks):
            print("Invalid task number.")
            return
        lists_of_tasks[task_index-1]["status"] = True
        print(f"Task number {task_index} - {lists_of_tasks[task_index-1]['name']} marked as done")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except:
        print("An error occurred while marking the task as done.")

def menu():
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Quit")

tasks = load_tasks()
while True:
    menu()
    try:
        choice = int(input("What would you like to do: "))
        if choice == 1:
            add_task(tasks)
            save_tasks(tasks)
        elif choice == 2:
            show_tasks(tasks)
        elif choice == 3:
            remove_task2(tasks)
            save_tasks(tasks)
        elif choice ==4:
            mark_done(tasks)
            save_tasks(tasks)
        elif choice == 5:
            print("Ok, See you tomorrow!")
            save_tasks(tasks)
            for index,task in enumerate(tasks):
                print(f"Task {index+1}: {task['name']}")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except KeyboardInterrupt:
        print("\nGoodbye!")
        break


