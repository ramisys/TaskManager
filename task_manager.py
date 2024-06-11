import os
import json

TASKS_FILE = 'tasks.json'

# Making sure that the files are always exist
def initialize_files():
    for filename in [TASKS_FILE]:
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                json.dump(f)

# Read task from the tasks.json
def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)
    
# Write task in the tasks.json
def save_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Making sure that the interface is clean
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Adding task
def add_task(task):
    tasks = load_json(TASKS_FILE)
    for t in tasks:
        if t == task:
            print("That task is already added.")
            return
    tasks.append(task)
    save_json(tasks, TASKS_FILE)
    print(f"Task '{task}' has added!")

# Deleting task
def delete_task(task_no):
    tasks = load_json(TASKS_FILE)
    if task_no >= 0 and task_no < len(tasks):
        tasks.pop(task_no)
        save_json(tasks, TASKS_FILE)
        print(f"Task #{task_no + 1} has been removed.")
    else:
        print(f"Task #{task_no + 1} was not found.")

# Displays all the tasks saved
def list_task():
    tasks = load_json(TASKS_FILE)
    if not tasks:
        print("There are no currently tasks.")
        return
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

# Main menu
def main():
    while True:
        initialize_files()
        
        print("\nSelect one of the following options:")
        print("------------------------------------------")
        print("[1] Add a task")
        print("[2] Delete a task")
        print("[3] List task")
        print("[4] Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            clear_screen()
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            clear_screen()
            list_task()
            try:
                task_no = int(input("Input the task no. you want to delete: "))
                delete_task(task_no - 1)
            except:
                print("Invalid Input.")
        elif choice == '3':
            clear_screen()
            list_task()
        elif choice == '4':
            clear_screen()
            print("Goodbye!")
            break
        else:
            print("Invalid input!")    

if __name__ == "__main__":
    main()