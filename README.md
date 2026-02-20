# to-do-manager
Terminal To-Do Manager (Python CLI)

Project Overview

A simple command-line based task manager built using Python.
This program allows a user to manage daily tasks directly from the terminal without any graphical interface.

The goal of this project is to practice core programming fundamentals such as data structures, functions, file handling, error handling, and program flow control.

All tasks are saved permanently using a JSON file so they remain available even after closing the program.

---

Features

- Add a new task
- View all tasks
- Mark a task as completed
- Delete a task
- Automatic task ID assignment
- Persistent storage using JSON file
- Handles invalid user input safely
- Menu-driven interface that runs continuously until exit

---

Technologies Used

- Python 3
- JSON file storage
- Command Line Interface (CLI)

---

How the Program Works

1. The program starts and loads tasks from a file (if it exists)
2. A menu is displayed repeatedly
3. User selects an option
4. The corresponding function runs
5. Changes are saved immediately to file
6. Program exits only when user selects Exit

---

Menu Options

1. Add Task
2. View Tasks
3. Mark Task Complete
4. Delete Task
5. Exit

---

Data Structure

Tasks are stored as a list of dictionaries:

Example:
[
{"id": 1, "title": "Buy milk", "status": "Pending"},
{"id": 2, "title": "Study Python", "status": "Done"}
]

---

How to Run

Open terminal inside project folder and run:

python app.py

---

Learning Objectives

This project helps understand:

- Python program structure
- Loops and conditions
- Functions and modular coding
- Lists and dictionaries
- File handling
- JSON data storage
- Input validation
- Debugging logic

---

Author

Built as a foundational programming project while learning Python and software development fundamentals.
