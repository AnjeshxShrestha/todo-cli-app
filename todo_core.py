def list_todos(todos):
    return [
        f"{i + 1}. {'✔️' if task['done'] else '❌'} {task['task']}"
        for i, task in enumerate(todos)
    ]

def add_todo(todos, task):
    todos.append({"task": task, "done": False})
    return todos

def mark_done(todos, index):
    if 0 <= index < len(todos):
        todos[index]["done"] = True
    return todos

def delete_todo(todos, index):
    if 0 <= index < len(todos):
        todos.pop(index)
    return todos
