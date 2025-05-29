def add_task():
    task=input("Enter Task: ")
    with open ('tasks.txt','a') as f:
        f.write(f"{task}\n")
    print("Task added!\n")

def view_tasks():
    try:
        with open ('tasks.txt','r') as f:
            tasks=f.read().splitlines()

        if not tasks:
            print("No tasks found\n")

        else:
            for index,value in enumerate(tasks):
                print(f"{index+1}. {value}")

    except FileNotFoundError:
        print("No file.\n")

def delete_tasks():
    while True:
        confirm=input("Are you sure you want to delete all tasks? (yes/no):")
        if(confirm.lower()=="yes"):
            with open ('tasks.txt','w') as f:
                pass
            print("All tasks deleted.")
            break
        elif confirm.lower()=="no":
            print("Deletion cancelled.\n")
            break
        else:
            print("Please enter 'yes' or 'no'.")

while(1):
    print("\nTo-Do List Menu\n")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete all tasks")
    print("4. Exit")

    try:
        option=int(input("Choose an option:"))
    except ValueError:
        print("Enter Valid Number\n")
        continue

    match option:
        case 1:
            add_task()
        case 2:
            view_tasks()
        case 3:
            delete_tasks()
        case 4:
            print("Goodbye!")
            break
        case _:
            print("Invalid option!")
            