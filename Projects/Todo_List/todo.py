# This list will store all tasks
# It is outside the function so data is not lost
tasks = []
# Source: Python lists
# https://docs.python.org/3/tutorial/datastructures.html


def todo():
    while True:
        # Display menu
        print("\n-------- TODO LIST --------")
        print("1 : CREATE")
        print("2 : DELETE")
        print("3 : UPDATE")
        print("4 : READ")
        print("5 : EXIT")

        # Take user choice
        choice = int(input("Enter the operation number: "))
        # Source: input() and int()
        # https://docs.python.org/3/library/functions.html#input

        # ---------------- CREATE ----------------
        if choice == 1:
            task = input("Enter your task: ")
            tasks.append(task)
            # append() adds item to the list
            # Source:
            # https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
            print("Task added successfully.")

        # ---------------- READ ----------------
        elif choice == 4:
            if len(tasks) == 0:
                print("No tasks available.")
            else:
                for i in range(len(tasks)):
                    print(f"{i + 1}. {tasks[i]}")
                # i+1 is shown to user because humans count from 1
                # Python internally uses index starting from 0
                # Source:
                # https://docs.python.org/3/tutorial/introduction.html#lists

        # ---------------- DELETE ----------------
        elif choice == 2:
            if len(tasks) == 0:
                print("No tasks to delete.")
            else:
                for i in range(len(tasks)):
                    print(f"{i + 1}. {tasks[i]}")

                num = int(input("Enter task number to delete: "))
                index = num - 1
                # Convert user input to zero-based index

                if 0 <= index < len(tasks):
                    tasks.pop(index)
                    # pop() removes item at given index
                    # Source:
                    # https://docs.python.org/3/tutorial/datastructures.html
                    print("Task deleted.")
                else:
                    print("Invalid task number.")

        # ---------------- UPDATE ----------------
        elif choice == 3:
            if len(tasks) == 0:
                print("No tasks to update.")
            else:
                for i in range(len(tasks)):
                    print(f"{i + 1}. {tasks[i]}")

                num = int(input("Enter task number to update: "))
                index = num - 1

                if 0 <= index < len(tasks):
                    new_task = input("Enter new task: ")
                    tasks[index] = new_task
                    # List items can be updated using index
                    # Source:
                    # https://docs.python.org/3/tutorial/introduction.html#lists
                    print("Task updated.")
                else:
                    print("Invalid task number.")

        # ---------------- EXIT ----------------
        elif choice == 5:
            print("Exiting TODO list. Goodbye!")
            break
            # break stops the loop
            # Source:
            # https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements

        # ---------------- INVALID OPTION ----------------
        else:
            print("Invalid option. Please try again.")


# Function call (VERY IMPORTANT)
todo()
# Source:
# https://docs.python.org/3/tutorial/controlflow.html#defining-functions
