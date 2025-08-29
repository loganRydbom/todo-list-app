# todo.py
import os
# Step 1: Start with an empty list to hold tasks
tasks = []
# Step 2: Add a task
def add_task(task):
    tasks.append(task)

# Step 3: View tasks
def view_tasks():
    global tasks
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
# Step 4: Delete a task
def delete_task(taskPlacement):
    global tasks
    tasks.pop(taskPlacement)
# Step 5: Mark task complete
def mark_complete(task):
    global tasks
    tasks[task - 1]= tasks[task - 1] + " [Finished]"
# Step 6: Save/load (extra stretch for today)
def save_tasks():
    global tasks
    user = os.getlogin()
    try:
        theFile = open(f"C:/Users/{user}/Documents/taskSave.txt", "x")
    except FileExistsError:
        theFile = open(f"C:/Users/{user}/Documents/taskSave.txt", "w")
    
    for task in tasks:
        theFile.write(task + "\n")

# Load Tasks
# Demo flow (you can run this file directly: python todo.py)
if __name__ == "__main__":
    add_task("Finish Cyber 201 assignment")
    add_task("Push code to GitHub")
    #delete_task(1)
    view_tasks()
    mark_complete(1)
    view_tasks()
    save_tasks()