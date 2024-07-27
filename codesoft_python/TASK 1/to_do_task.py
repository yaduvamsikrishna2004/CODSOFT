class TodoItem:
    def __init__(self, details):
        self.details = details
        self.is_done = False

    def __str__(self):
        status_symbol = "✓" if self.is_done else "✗"
        return f"[{status_symbol}] {self.details}"

# List to store all to-do items
todo_list = []

def add_todo_item(details):
    todo_list.append(TodoItem(details))
    print(f"Task '{details}' added.")

def modify_todo_item(index, details):
    if 0 <= index < len(todo_list):
        todo_list[index].details = details
        print(f"Task {index} updated to '{details}'.")
    else:
        print("Invalid index.")

def remove_todo_item(index):
    if 0 <= index < len(todo_list):
        removed_task = todo_list.pop(index)
        print(f"Task '{removed_task.details}' removed.")
    else:
        print("Invalid index.")

def mark_item_as_done(index):
    if 0 <= index < len(todo_list):
        todo_list[index].is_done = True
        print(f"Task {index} marked as done.")
    else:
        print("Invalid index.")

def view_tasks():
    if not todo_list:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(todo_list):
            print(f"{i}: {task}")

def main():
    while True:
        command = input("Enter the command: \n  ADD \n  UPDATE \n  DELETE \n  COMPLETE \n  VIEW \n  EXIT \n ").strip().lower()
        if command == "add":
            description = input("Enter task description: ").strip()
            add_todo_item(description)
        elif command == "update":
            index = int(input("Enter task index: "))
            description = input("Enter new description: ").strip()
            modify_todo_item(index, description)
        elif command == "delete":
            index = int(input("Enter task index: "))
            remove_todo_item(index)
        elif command == "complete":
            index = int(input("Enter task index: "))
            mark_item_as_done(index)
        elif command == "view":
            view_tasks()
        elif command == "exit":
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
