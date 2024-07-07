# daily_reminder.py

def main():
    # Prompt for a single task
    task = input("Enter the task description: ")
    priority = input("Enter the task's priority (high, medium, low): ").strip().lower()
    time_bound = input("Is the task time-bound? (yes or no): ").strip().lower()

    # Process the task based on priority and time sensitivity
    reminder = f"Task: {task}\nPriority: {priority.capitalize()}"

    match priority:
        case 'high':
            reminder += "\nThis is a high-priority task."
        case 'medium':
            reminder += "\nThis is a medium-priority task."
        case 'low':
            reminder += "\nThis is a low-priority task."
        case _:
            reminder += "\nInvalid priority entered. Assuming low priority."

    if time_bound == 'yes':
        reminder += " This task requires immediate attention today!"

    # Provide a customized reminder
    print("\nReminder:")
    print(reminder)

if __name__ == "__main__":
    main()
