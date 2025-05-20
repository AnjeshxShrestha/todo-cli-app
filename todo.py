from todo_storage import load_todos, save_todos
from todo_core import list_todos, add_todo, mark_done, delete_todo

def main():
    while True:
        print("\n--- To-Do List ---")
        todos = load_todos()
        for line in list_todos(todos):
            print(line)
        
        print("\nOptions:")
        print("1. Add task")
        print("2. Mark task as done")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            todos = add_todo(todos, task)
            save_todos(todos)
        elif choice == "2":
            index = int(input("Enter task number to mark done: ")) - 1
            todos = mark_done(todos, index)
            save_todos(todos)
        elif choice == "3":
            index = int(input("Enter task number to delete: ")) - 1
            todos = delete_todo(todos, index)
            save_todos(todos)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice.")

if __name__ == "__main__":
    main()
