todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # python 3.10'dan sonrasında match case var
    if user_action == 'add':
        todo = input("Enter a todo: ") +"\n"

        # file=open('files/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        file = open('files/todos.txt', 'w')
        #absolute path for Linux
        #use r"c:\Users\.." for Windows
        #file = open("/home/duygu/Documents/todos.txt")
        file.writelines(todos)
        file.close()
    elif user_action == 'show':
        # file = open('files/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
        for ind, item in enumerate(todos):
            item = item.strip('\n')
            print(ind+1, item)
    elif user_action == 'edit':
        no = int(input("Give the id of the item to edit"))
        no = no -1

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        new_value = input(f"Provide the new value for {todos[no]}")
        todos[no] = new_value + '\n'

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

        # if no.isdigit() and int(no) <= len(todos) and int(no)>0:
        #     new_value = input(f"Provide the new value for {todos[int(no)]}\n Type -1 for canceling")
        #     if new_value != '-1':
        #         todos[int(no)-1] = new_value
        # else:
        #     print("incorrect index")
    elif user_action == "complete":
        no = int(input("Provide the index of the item to complete"))

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        index = no -1
        todo_to_remove  = todos[index].strip('\n')
        todos.pop(no-1)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

        print(f"{todo_to_remove} is removed.")


        # if no.isdigit() and int(no) <= len(todos) and int(no)>0:
        #     todos.pop(int(no)-1)
    elif user_action == 'exit':
        break
    else:
        print("Command is not valid.")

