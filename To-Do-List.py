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


def view_Task():
    task = input("What task do you want to View? ")
    for i in tasks:
        if i["task"] == task:
            print(f'Task: {i["task"]}, Priority: {i["priority"]}, Status: {i["status"]}' )

option = input("Press 1 to add a task, Press 2 to view a taks, Press 3 to delete a task ")
option = int(option)

if isinstance(option, int):
    if option == 1:
        add_Task()
    elif option == 2:
        view_Task() 
else:
    option = input("Press 1 to add a task, Press 2 to view a taks, Press 3 to delete a task ")


