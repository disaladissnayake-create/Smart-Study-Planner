tasks = []

def add_task():
    subject = input("Subject: ")

    task = input("Task: ")

    priority = input("Priority (high/medium/low): ")

    tasks.append({
        "subject": subject,
        "task": task,
        "priority": priority
    })

    print("Task added successfully!\n")


def show_tasks():
    if not tasks:
        print("No tasks yet!\n")
        return

    print("\nYour Study Tasks:")

    for i, t in enumerate(tasks):
        print(f"{i+1}. {t['subject']} - {t['task']} (Priority: {t['priority']})")

    print()


while True:
    print("=== Smart Study Planner ===")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        break

    else:
        print("Invalid choice. Please try again.\n")
