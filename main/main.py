class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if self.tasks:
            print("Your Tasks:")
            for i, task in enumerate(self.tasks):
                status = "✓" if task["completed"] else "✗"
                print(f"{i + 1}. [{status}] {task['description']}")
        else:
            print("You have no tasks.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task deleted successfully.")
        else:
            print("Invalid task index.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. View Tasks")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your Number choice:")

        if choice == "1":
            description = input("Enter task description: ")
            task_manager.add_task({"description": description, "completed": False})
        elif choice == "2":
            task_manager.view_tasks()
            task_index = int(input("Enter task index to mark as completed: ")) - 1
            task_manager.complete_task(task_index)
        elif choice == "3":
            task_manager.view_tasks()
        elif choice == "4":
            task_manager.view_tasks()
            task_index = int(input("Enter task index to delete: ")) - 1
            task_manager.delete_task(task_index)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
