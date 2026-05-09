import os
import json

tasks = []
task = ''
priority = ''
status = ''

if os.path.exists('tasks.json'):
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
else:
    task_List = []

def mark_Task():
    task_name = input("Which task do you want to change? ")
    task = input("Do you want to change the task, priority or status? ")
    change_Task_To = input("What do you want to change the task to? ")

    for i in tasks:
        if i["task"] == task_name:
            if task == "task":
                i["task"] = change_Task_To
            elif task == "priority":
                i["priority"] = change_Task_To
            elif task == "status":
                i["status"] = change_Task_To

    with open('tasks.json', 'w' ) as file:
        json.dump(tasks, file)

def add_Task():
    tasks_dict = {}
    task = input("What is the task? ")
    tasks_dict["task"] = task

    priority = input("Is the priority High, Medium or Low? ")
    tasks_dict["priority"] = priority

    status = input("Is the task done or not done? ")
    tasks_dict['status'] = status

    tasks.append(tasks_dict)
    with open('tasks.json', 'w' ) as file:
        json.dump(tasks, file)

def delete_Task():
    task = input("What task do you want to delete?")
    for i in tasks:
        if i["task"] == task:
            tasks.remove(i)
    with open('tasks.json', 'w' ) as file:
        json.dump(tasks, file)


def view_Task():
    task = input("What task do you want to View? ")
    for i in tasks:
        if i["task"] == task:
            print(f'Task: {i["task"]}, Priority: {i["priority"]}, Status: {i["status"]}' )

option = input("Press 1 to add a task, 2 to view a taks, 3 to mark a task, 4 to Delete a task, 5 to view incomplete tasks, 6 to view priorities ")
option = int(option)

def view_incomplete():
    for i in tasks:
        if i["status"] == "not done":
            print(f"Not Done: {i["task"]}")

def view_priority():
    for i in tasks:
        if i["priority"] == "high":
            print(f"High: {i["task"]}")
        elif i["priority"] == "medium":
            print(f"Medium: {i["task"]}")
        elif i["priority"] == "low":
            print(f"Low: {i["task"]}")

if isinstance(option, int):
    if option == 1:
        add_Task()
    elif option == 2:
        view_Task()
    elif option == 3:
        mark_Task() 
    elif option == 4:
        delete_Task()
    elif option == 5:
        view_incomplete()
    elif option == 6:
        view_priority()
else:
    option = input("Press 1 to add a task, 2 to view a taks, 3 to edit a task, 4 to Delete a task, 5 to view incomplete tasks, 6 to view priorities ")


