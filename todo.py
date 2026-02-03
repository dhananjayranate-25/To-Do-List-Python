tasks = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print(" No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print(" No tasks to update.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            index = int(input("Enter task number to update: ")) - 1
            if 0 <= index < len(tasks):
                new_task = input("Enter updated task: ")
                tasks[index] = new_task
                print("Task updated!")
            else:
                print(" Invalid task number.")

    elif choice == "4":
        if not tasks:
            print(" No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f" Task removed: {removed}")
            else:
                print(" Invalid task number.")

    elif choice == "5":
        print(" Exiting To-Do List. Goodbye!")
        break

    else:
        print(" Please choose a valid option (1-5)")
