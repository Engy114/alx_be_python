# Prompt user for the task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task based on its priority and time sensitivity using match case
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task.")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task. Complete it when possible.")
    case "low":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level.")
