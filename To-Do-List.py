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

add_Task()