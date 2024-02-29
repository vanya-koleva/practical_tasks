def show_menu():
    print("\n💜💜💜 To-Do List Menu 💜💜💜")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View Tasks")
    print("4. Quit")


def add_task(to_do_list):
    task = input("Enter the task: ")
    to_do_list.append([task, False])
    print(f'Task "{task}" added successfully!')


def mark_completed(to_do_list):
    display_tasks(to_do_list)
    index = int(input("Enter the index of the task to mark as completed: ")) - 1
    if 0 <= index < len(to_do_list):
        to_do_list[index][1] = True
        print("Task marked as completed!")
    else:
        print("Invalid index. Please enter a valid index.")


def display_tasks(to_do_list):
    print("💜💜💜💜💜💜💜 Tasks 💜💜💜💜💜💜💜")
    for i, task in enumerate(to_do_list, start=1):
        task[1] = "[💜]" if task[1] == True else "[ ]"
        task = " ".join(task)
        print(f"Index {i}. {task}")


def to_do_list_program():
    to_do_list = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task(to_do_list)
        elif choice == "2":
            mark_completed(to_do_list)
        elif choice == "3":
            display_tasks(to_do_list)
        elif choice == "4":
            print("Exiting the program. Goodbye!!!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


to_do_list_program()
