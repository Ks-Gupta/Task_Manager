# Task_Manager
Simple Task Manager Using Python

# 📝 Task Manager (Command-Line Based)

A simple Python-based Command Line Interface (CLI) Task Manager that allows users to manage their tasks. Tasks are stored in a local `tasks.txt` file, enabling persistence across sessions.

---

## 🚀 Features

- 📌 Add a new task with a title
- ✅ Mark existing tasks as complete
- ❌ Delete tasks by ID
- 📄 View all current tasks with status
- 💾 Data persistence using a text file (`tasks.txt`)

---

## 🛠️ Technologies Used

- Python 3
- File Handling with built-in `open()`
- Dictionary-based task management

---

## 📂 Project Structure

```bash
task_manager.py    # Main Python script
tasks.txt          # File where tasks are saved (auto-created)
README.md          # Project documentation
````

---

## ▶️ How to Run

1. Clone or Download this repository.

2. Make sure you have **Python 3** installed.

3. Run the Python file:

```bash
python task_manager.py
```

4. Interact using the menu:

```
 Task Manager Menu:
 1. Add Task
 2. View Tasks
 3. Mark Task as Complete
 4. Delete Task
 5. Exit
```

---

## 🧠 Example Usage

```
Enter your choice: 1
Enter task title: Buy groceries
Task 'Buy groceries' added.

Enter your choice: 2
[1] Buy groceries - Incomplete

Enter your choice: 3
Enter task ID to mark as complete: 1
Task 'Buy groceries' marked as complete

Enter your choice: 5
GoodBye
```

---

## 📌 Notes

* Task IDs are assigned automatically and incrementally.
* Tasks are stored in the format: `task_id | title | status`
* The program handles basic error-checking for invalid task IDs and empty task lists.

---

