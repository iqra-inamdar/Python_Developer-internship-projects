import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks():
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)

def add_task(): 
        task_name = input("Enter task: ")
        task = {
            "task": task_name,
            "completed": False
        }      

        tasks.append(task)
        save_tasks()

        print("Task added successfully!")

def view_tasks():
     if not tasks:
          print("No rasks available.")
          return
     print("\n========== YOU TASKS ==========")
     for i, task in enumerate(tasks, start=1):
          status = "Completed" if task["completed"] else "Pending"
          print(f"{i}. {task['task']} - {status}")
def complete_task():
     view_tasks()

     if not tasks:
          return
     try:
          task_number = int(input("\nEnter task number to mark as completed: "))

          if 1 <= task_number <= len(tasks):
               tasks[task_number -1] ["completed"] = True
               save_tasks()

               print("Task marked as completed!")
          else:
               print("Invalid task number.") 
     except ValueError:
          print("Please enter a valid number.")
def delete_task():
     view_tasks()

     if not tasks:
          return
     try:
          task_number = int(input("\nEnter task number to delete: "))
          if 1 <= task_number <= len(tasks):
               deleted_task = tasks.pop(task_number - 1)

               save_tasks()

               print(f"Task '{deleted_task[ 'task']}' deleted successfully!") 
          else:
               print("Invalid task number.")
     except ValueError:
          print("Please enter a valid number.")

tasks = load_tasks() 
while True:

     print("\n================================")
     print("       TO-DO LIST")
     print("==================================")
     print("1. Add Task")
     print("2. View Tasks")
     print("3. Mark Task as Completed")
     print("4. Delete Task")
     print("5. Exit")

     choice = input("\nEnter your choice: ")

     if choice == "1":
          add_task()
     elif choice == "2":
          view_tasks()
     elif choice == "3":
          complete_task()
     elif choice == "4":
          delete_task()
     elif choice == "5":
          print("Thank You for using To-Do List!")
          break

     else:
          print("Invalid choice. Please try agaun.")             



                                   
             

