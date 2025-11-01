tasks = []

def display_menu():
    print("\n---- To-Do List Menu ----")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Delete a task by name")
    print("4. Delete a task by number")
    print("5. Exit")

def add_new_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added!")

def view_all_tasks():
    if not tasks:
        print("No tasks in the list.")
        return  
    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']} - {'Done' if task['completed'] else 'Not done'}")

def delete_task_by_name():
    view_all_tasks()
    if not tasks:
        return
    name = input("Enter the name of the task to delete: ")
    for task in tasks:
        if task["task"] == name:
            tasks.remove(task)
            print(f"Task '{name}' deleted!")
            return
    print(f"Task '{name}' not found!")

def delete_task_by_number():
    view_all_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter the number of the task to delete: "))
        removed = tasks.pop(num - 1)
        print(f"Task '{removed['task']}' deleted!")
    except (ValueError, IndexError):
        print("Invalid number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1–5): ")

        if choice == "1":
            add_new_task()
        elif choice == "2":
            view_all_tasks()
        elif choice == "3":
            delete_task_by_name()
        elif choice == "4":
            delete_task_by_number()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
