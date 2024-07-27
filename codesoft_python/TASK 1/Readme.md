To-Do List Application

A simple command-line To-Do List application written in Python. This script provides functionality to manage your tasks efficiently by allowing you to add, update, delete, complete, and view tasks.
Features

    Add Task: Add a new task with a description.
    Update Task: Modify the details of an existing task.
    Delete Task: Remove a task from the list.
    Complete Task: Mark a task as completed.
    View Tasks: Display all tasks with their status.

Getting Started
Prerequisites

    Python 3.x installed on your machine.
    
Run the script:

bash

    python todo_list.py

Usage

When you run the script, you will be prompted to enter a command. The available commands are:

    ADD: Adds a new task. You will be asked to provide a description for the task.
    UPDATE: Updates an existing task. Enter the task index and the new description.
    DELETE: Removes a task. Provide the index of the task to be deleted.
    COMPLETE: Marks a task as completed. Specify the index of the task.
    VIEW: Lists all tasks along with their current status.
    EXIT: Exits the application.

Example

text

Enter the command: 
  ADD 
  UPDATE 
  DELETE 
  COMPLETE 
  VIEW 
  EXIT 
add
Enter task description: Buy groceries
Task 'Buy groceries' added.

Enter the command: 
  ADD 
  UPDATE 
  DELETE 
  COMPLETE 
  VIEW 
  EXIT 
view
0: [✗] Buy groceries

