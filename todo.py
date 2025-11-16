FILE_NAME = "todo.txt"

def load_tasks():
    tasks = []
    try:
        with open(FILE_NAME, 'r') as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        for task in tasks:
            file.write(task + "\n")

def add_tasks(tasks):
    task = input("Enter the new task:")
    tasks.append(task)
    print("Task added successfully!")
    
def view_tasks(tasks):   
    if not tasks:
        print("no tassk found.")
    else:
        print("\n your  To-Do lists or tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
            
def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_no = int(input("Enter task number to remove:"))
            if 1<= task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(f"Removed task:{removed}")
            
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")
            
            
            
def main():
    tasks = load_tasks()
    
    while True:
        print("\n======To-Do List Menu======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter your choice (1-4):")
        
        if choice == '1':
            add_tasks(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        
        elif choice == '4':
            save_tasks(tasks)
            print(" Tasks saved. Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")
main()