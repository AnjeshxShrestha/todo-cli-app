import os
import json

TODO_FILE = "todos.json"

def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)

def save_todos(todos):
    with open(TODO_FILE, "w") as file:
        json.dump(todos, file, indent=4)

def list_todos(todos):
    if not todos:
        print(" No tasks! You're all caught up.")
    for i, task in enumerate(todos, 1):
        status = " right " if task['done'] else "Wrong"
        print(f"{i}. {status} {task['task']}")

def add_todo(task):
    todos = load_todos()
    todos.append({"task": task, "done": False})
    save_todos(todos)
    print("Task added.")

def mark_done(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        todos[index]["done"] = True
        save_todos(todos)
        print("Task marked as done.")
    else:
        print("Invalid task number.")

def delete_todo(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        removed = todos.pop(index)
        save_todos(todos)
        print(f"Deleted task: {removed['task']}")
    else:
        print(" Invalid task number.")

def main():
    while True:
        print("\n--- To-Do List ---")
        todos = load_todos()
        list_todos(todos)

        print("\nOptions:")
        print("1. Add task")
        print("2. Mark task as done")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            add_todo(task)
        elif choice == "2":
            index = int(input("Enter task number to mark done: ")) - 1
            mark_done(index)
        elif choice == "3":
            index = int(input("Enter task number to delete: ")) - 1
            delete_todo(index)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
