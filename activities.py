# To-Do List App
import json
import datetime
import streamlit as st

# Load tasks from file
try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

def display_tasks():
    print("To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['name']} - {status}")

def convert_to_24hour(time_str):
    hour, minute, am_pm = time_str.split(":")[0], time_str.split(":")[1].split(" ")[0], time_str.split(" ")[1]
    hour = int(hour)
    if am_pm == "PM" and hour != 12:
        hour += 12
    elif am_pm == "AM" and hour == 12:
        hour = 0
    return f"{hour:02d}:{minute}"

def add_task():
    """Add a new task"""
    task_name = input("Enter task name: ")
    task_due_date = input("Enter task due date (YYYY-MM-DD): ")
    task_due_time = input("Enter task due time (HH:MM AM/PM): ")
    task_due_time_24hour = convert_to_24hour(task_due_time)
    tasks.append({
        "name": task_name,
        "completed": False,
        "due_date": task_due_date,
        "due_time": task_due_time_24hour
    })
    print(f"Task '{task_name}' added!")

def remove_task():
    task_number = int(input("Enter task number to remove: ")) - 1
    if task_number < len(tasks):
        del tasks[task_number]
        print("Task removed!")
    else:
        print("Invalid task number!")

def mark_completed():
    task_number = int(input("Enter task number to mark as completed: ")) - 1
    if task_number < len(tasks):
        tasks[task_number]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number!")

def edit_task():
    """Edit a task"""
    task_number = int(input("Enter task number to edit: ")) - 1
    if task_number < len(tasks):
        task_name = input("Enter new task name: ")
        task_due_date = input("Enter new task due date (YYYY-MM-DD): ")
        tasks[task_number]["name"] = task_name
        tasks[task_number]["due_date"] = task_due_date
        print("Task edited!")
    else:
        print("Invalid task number!")

def search_tasks():
    """Search for tasks"""
    search_query = input("Enter search query: ")
    search_results = [task for task in tasks if search_query.lower() in task["name"].lower()]
    if search_results:
        print("Search results:")
        for i, task in enumerate(search_results, 1):
            status = "Completed" if task["completed"] else "Pending"
            due_date = task.get("due_date", "No due date")
            due_time_24hour = task.get("due_time", "No due time")
            hour, minute = due_time_24hour.split(":")
            hour = int(hour)
            if hour > 12:
                am_pm = "PM"
                hour -= 12
            elif hour == 12:
                am_pm = "PM"
            else:
                am_pm = "AM"
            due_time = f"{hour}:{minute} {am_pm}"
            print(f"{i}. {task['name']} - {status} - Due: {due_date} {due_time}")
    else:
        print("No search results found.")

def main():
    while True:
        print("\nTo-Do List App")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as completed")
        print("5. Edit task")
        print("6. Search tasks")
        print("7. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_completed()
        elif choice == "5":
            edit_task()
        elif choice == "6":
            search_tasks()
        elif choice == "7":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
