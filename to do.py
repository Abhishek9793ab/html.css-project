# To-Do List Program

tasks = []  # Yeh ek empty list hai jisme hum apne tasks store karenge

def show_menu():
    print("\n📋 To-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print(f"✅ Task '{task}' added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("📝 No tasks found!")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")

    elif choice == "3":
        if len(tasks) == 0:
            print("⚠ No tasks to remove!")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
            try:
                task_no = int(input("Enter task number to remove: "))
                removed = tasks.pop(task_no - 1)
                print(f"❌ Task '{removed}' removed successfully!")
            except (ValueError, IndexError):
                print("⚠ Invalid task number!")

    elif choice == "4":
        print("👋 Exiting... Goodbye!")
        break

    else:
        print("⚠ Invalid choice! Please enter 1-4.")