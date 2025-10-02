# Simple To-Do List

tasks = []

def show_tasks():
    if tasks:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
    else:
        print("Your To-Do List is empty.")

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"'{task}' has been added to your to-do list.")

def remove_task():
    show_tasks()
    try:
        task_number = int(input("Enter the number of the task to remove: "))
        removed_task = tasks.pop(task_number - 1)
        print(f"'{removed_task}' has been removed from your to-do list.")
    except (IndexError, ValueError):
        print("Invalid task number.")

while True:
    print("\nTo-Do List Menu:")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
