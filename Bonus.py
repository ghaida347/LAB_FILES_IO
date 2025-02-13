import json
file1=open("To_do","r",encoding="utf-8")
contant1=file1.read()
json_data=json.dumps(contant1, indent=4)
print("The json data is ",json_data)
file1.close()

#import json
from datetime import datetime

def load_tasks():
    try:
        with open("to_do.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    return tasks

def save_tasks(tasks):
    with open("to_do.json", "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    title = input("Enter your new To-Do item: ")
    task = {
        "title": title,
        "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "done": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully.")


def list_tasks(tasks):
    if not tasks:
        print("No tasks found!")
        return
    for idx, task in enumerate(tasks, 1):
        done_status = "DONE" if task["done"] else "NOT DONE"
        print(f"{idx}- {task['title']} - {task['date_time']} - {done_status}")

def mark_done(tasks):
    list_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as done: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["done"] = True
            save_tasks(tasks)
            print(f"Task '{tasks[task_number - 1]['title']}' marked as DONE.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def search_task(tasks):
    search_term = input("Enter the title or keyword to search for: ").lower()
    found_tasks = [task for task in tasks if search_term in task["title"].lower()]
    if found_tasks:
        for idx, task in enumerate(found_tasks, 1):
            done_status = "DONE" if task["done"] else "NOT DONE"
            print(f"{idx}- {task['title']} - {task['date_time']} - {done_status}")
    else:
        print("No tasks found matching your search.")

def main():
    tasks = load_tasks()

    while True:
        print("\nWhat would you like to do?")
        action = input("1- Add a new task (y/n)\n2- List tasks (y/n)\n3- Mark task as done (y/n)\n4- Search tasks (y/n)\nType 'exit' to exit\n")
        
        if action.lower() == "exit":
            print("Thank you for using the To-Do program, come back again soon!")
            break
        elif action.lower() == "y":
            sub_action = input("What would you like to do? (add/list/mark/search): ").lower()
            if sub_action == "add":
                add_task(tasks)
            elif sub_action == "list":
                list_tasks(tasks)
            elif sub_action == "mark":
                mark_done(tasks)
            elif sub_action == "search":
                search_task(tasks)
            else:
                print("Invalid action.")
        elif action.lower() == "n":
            print("Okay, let's go back to the main menu.")
        else:
            print("Invalid option, please try again.")


main()
