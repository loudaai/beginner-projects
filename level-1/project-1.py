tasks = []

while True:
    print("\n === TO DO LIST ===")
    print("1. View Tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")

    elif choice == "2":
        task = input("Enter a task: ")
        tasks.append(task)
        print("task added.")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete")
        else:
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")

            task_number = int(input("Enter task number to delete:"))
            tasks.pop(task_number - 1)
            print("Task deleted.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
