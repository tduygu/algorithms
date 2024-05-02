todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # python 3.10'dan sonrasında match case var
    if user_action.startswith("add"):
        todo = user_action[4:] +"\n"

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
        for ind, item in enumerate(todos):
            item = item.strip('\n')
            print(ind+1, item)

    elif user_action.startswith("edit"):
        try:
            num = user_action[5:]
            if num.isdigit():
                no = int(num) -1
            else:
                continue

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_value = input(f"Provide the new value for {todos[no]}")
            todos[no] = new_value + '\n'

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Invalid command")
            continue
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('complete'):
        try:
            num = user_action[9:]
            if num.isdigit():
                index = int(num) - 1
            else:
                continue

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todo_to_remove  = todos[index].strip('\n')
            todos.pop(index)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            print(f"{todo_to_remove} is removed.")
        except ValueError:
            print("Invalid command")
            continue
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

