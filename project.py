tasks = []

print("📝 TO-DO LIST")
print("Type 'add' to add a task")
print("Type 'show' to see your tasks")
print("Type 'remove' to remove a task")
print("Type 'exit' to quit")

while True:
    command = input("\nWhat do you want to do? ").lower()

    if command == "add":
        task = input("Enter a task: ")
        tasks.append(task)
        print("✅ Task added!")

    elif command == "show":
        if len(tasks) == 0:
            print("📭 Your list is empty.")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif command == "remove":
        if len(tasks) == 0:
            print("📭 There are no tasks to remove.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

            number = int(input("Enter the task number to remove: "))

            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(f"🗑️ Removed: {removed}")
            else:
                print("❌ Invalid task number.")

    elif command == "exit":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Unknown command.")
