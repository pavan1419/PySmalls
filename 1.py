# Python pseudocode for a To-Do List application

# Step 1: Define a class for tasks
class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

# Step 2: Create a list to store tasks
tasks = []

# Step 3: Function to add a task
def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    new_task = Task(title, description)
    tasks.append(new_task)
    print("Task added successfully!")

# Step 4: Function to view tasks
def view_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. Title: {task.title}, Description: {task.description}, Completed: {task.completed}")

# Step 5: Function to mark a task as completed
def complete_task():
    view_tasks()
    choice = int(input("Enter the number of the task to mark as completed: "))
    if 1 <= choice <= len(tasks):
        tasks[choice - 1].completed = True
        print("Task marked as completed!")
    else:
        print("Invalid choice.")

# Step 6: Main function
def main():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Completed\n4. Exit")
        option = int(input("Enter your choice: "))
        
        if option == 1:
            add_task()
        elif option == 2:
            view_tasks()
        elif option == 3:
            complete_task()
        elif option == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Step 7: Call the main function
if __name__ == "__main__":
    main()
