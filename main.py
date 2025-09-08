import classes
import atexit

database = classes.database
entry = classes.entry
find_task = classes.find_task

import os

def main():

    print("======To-Do-List======")
    classes.load_databases()
    user, entries = classes.select_user()
    while True:
        # Select An Action
        print(f"What would you like to do {user.name}?")
        print("[1] Add a task")
        print("[2] Remove a task")
        print("[3] Change task completion status")
        print("[4] View all tasks")
        print("[5] Change user")
        print("[6] Quit")
        try:
            match (int(input("Your Choice: "))):
                case 1:
                    print()
                    name=input("What is the name of the new task? ")
                    task = find_task(entries,name)
                    if task:
                        print("\nError: Task already exist\n")
                        continue
                    des = input("What is it about? ")
                    print(f"Added task: {name}")
                    new_entry = entry(name,description=des)
                    user.add(new_entry)
                case 2:
                    print()
                    name=input("What is the task you would like to remove? ")
                    task = find_task(entries,name)
                    if task:
                        print(f"Deleted task: {task.name}")
                        user.remove(task)
                    else:
                        print("\nERROR: Task does not exist\n")
                        continue
                case 3:
                    print()
                    name=input("What is the task you would like to change status? ")
                    task = find_task(entries,name)
                    change = "Incomplete"
                    if task:
                        if task.completed == False:
                            change ="Complete"
                        print(f"Would you like to change the status of the task \"{task.name}\" to {change}?")
                        print("[1] Yes")
                        print("[2] No")
                        try:
                            if int(input("Your Choice: ")) == 1:
                                user.change_status(task)
                                print(f"\nChanged status to {change}")
                            else:
                                print("\nDid not change status")
                        except:
                            print("\nERROR: Invalid input")
                    else:
                        print("\nERROR: Task does not exist\n")
                        continue
                case 4:
                    print()
                    print("Your tasks:")
                    iter = 1
                    for v in entries.values():
                        complete = "Incomplete"
                        if v.completed == True:
                            complete = "Completed"
                        print(f"[{iter}] {v.name} - {complete} \n\t{v.description}")
                        iter+=1
                case 5:
                    print()
                    user, entries = classes.select_user()
                case 6:
                    print("\nQuit To-Do-List\n")
                    break
                case _:
                    print("\nERROR: Invalid Input\n")
                    continue
        except:
            print("\nERROR: Invalid Input")
        print()

def exit_handler():
    classes.save_databses()

if __name__=="__main__":
    main()
atexit.register(exit_handler)
