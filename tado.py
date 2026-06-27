import json
from datetime import datetime

FILENAME = "tasks.json"

def load_tasks():
    try:
        with open(FILENAME, "r") as f:
           return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f)

def add_tasks(tasks):
    name = input("Task name: ")
    due = input("Due date (dd/mm/yyyy) or press Enter to skip: ")
    priority = input("Priority (high/medium/low): ").lower()
    if priority not in ["high", "medium", "low"]:
        priority = "medium"
    task = {
        "name": name,
        "due": due,
        "priority": priority,
        "done": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added: {name}")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return
    for i, task in enumerate(tasks, 1):
        status = "DONE" if task["done"] else "x"
        print(f"{i}. [{status}] {task['name']} | {task['priority'].upper()} | Due: {task['due']}")

def mark_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Mark which task as done? ")) - 1
        tasks[num]["done"] = True
        save_tasks(tasks)
        print("Marked as done!")
    except (ValueError, IndexError):
        print("Invalid number, try again!")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Delete which number? ")) - 1
        removed = tasks.pop(num)
        save_tasks(tasks)
        print(f"Deleted: {removed['name']}")
    except(ValueError, IndexError):
        print("Invalid number, try again!")

tasks = load_tasks()

while True:
    print("\n1. Add 2. View 3. Mark Done 4. Delete 5. Quit")
    choice = input("Choose: ")
    if choice == "1":
        add_tasks(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        mark_done(tasks)
    elif choice =="4":
        delete_task(tasks)
    elif choice == "5":
        break
