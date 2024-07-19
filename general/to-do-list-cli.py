#from functions import get_todos, write_todos
import functions
import time

# text = """
# Principles of productivity:
# Managing your inflow.
# Systemizing everything that repeats.
# """
#
# print(text)

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is",now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # python 3.10'dan sonrasında match case var
    if user_action.startswith("add"):
        todo = user_action[4:] +"\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(filepath='files/todos.txt', todos_list=todos)


    elif user_action.startswith("show"):
        todos = functions.get_todos()
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

            todos = functions.get_todos()

            new_value = input(f"Provide the new value for {todos[no]}")
            todos[no] = new_value + '\n'

            functions.write_todos(todos)

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

            todos = functions.get_todos()

            todo_to_remove  = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

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

