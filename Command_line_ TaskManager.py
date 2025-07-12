import os

#File to Store Task
FILE_NAME = "tasks.txt"

# load task from files
def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task_id, title, status = line.strip().split(" | ")
                tasks[int(task_id)] = {"title": title, "status": status}
                
    return tasks        


# save tasks to file

def save_tasks(tasks):
    with open(FILE_NAME , "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']}\n")
            
            
# Add new Task
def add_task(tasks):
    title = input("Enter task title:")
    task_id = max(tasks.keys(), default=0) + 1 
    tasks[task_id] = {"title" : title, "status" : "Incomplete"} # just created so incomplete
    print(f"Task '{title}' added.")
    
    
# View all the tasks

def view_task(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for task_id, task in tasks.items():
            print(f"[{task_id}] {task['title']} - {task['status']}")
            
#marks task as complete from incomplete status
def mark_task_complete(tasks):
    task_id = int(input("Enter task ID to mark as complete:"))
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print(f"Task '{tasks[task_id]['title']}' marked as complete")
    else:
        print("Task ID not found.")
        
    
# Delete a task
def delete_tasks(tasks):
    task_id = int(input("Enter task ID to Delete:"))
    if task_id in tasks:
        delete_task = tasks.pop(task_id)
        print(f"Task '{delete_task['title']}' deleted")
    else:
        print("Task ID not found.")
        
 
 #Main Menu
def main():
     tasks = load_tasks()
     while True:
         print("\n Task Manager Menu:")
         print("1. Add Task")
         print("2. view Tasks")
         print("3. Mark Task as complete")
         print("4. Delete Task")
         print("5. Exit")
         choice = input("Enter your choice:")
         
         if choice == "1":
            add_task(tasks)
         elif choice == "2":
             view_task(tasks)
         elif choice == "3":
             mark_task_complete(tasks)
         elif choice == "4":
             delete_tasks(tasks)
         elif choice == "5":
             save_tasks(tasks)
             print("GoodBye")
             break
         else:
             print("Invalid Choice. Please try again")
             
if __name__ == "__main__":
    main() 
             
             
         