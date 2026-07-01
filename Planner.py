tasks = []

def add_task():
    subject = input("Subject: ")

    #1: You forgot to ask for the task.
    task = input("Task: ")

    priority = input("Priority (high/medium/low): ")

    #2: This must be inside add_task()
    tasks.append({
        "subject": subject,
        "task": task,
        "priority": priority
    })

    #3: This should also be inside add_task()
    print("Task added successfully!\n")


def show_tasks():
    if not tasks:
        print("No tasks yet!\n")
        return

    #4: This must be after the if statement,
    # not after return.
    print("\nYour Study Tasks:")

    #5: The loop belongs inside show_tasks()
    for i, t in enumerate(tasks):
        print(f"{i+1}. {t['subject']} - {t['task']} (Priority: {t['priority']})")

    print()


while True:
    print("=== Smart Study Planner ===")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Exit")

    choice = input("Choose: ")

    #6: These if statements must be inside the while loop.
    if choice == "1":
        add_task()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        break

    else:
        print("Invalid choice. Please try again.\n")
