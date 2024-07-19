todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # python 3.10'dan sonrasında match case var
    if user_action == 'add':
        todo = input("Enter a todo: ")
        todos.append(todo)
    elif user_action == 'show':
        for ind, item in enumerate(todos):
            print(ind, item)
    elif user_action == 'edit':
        no = input("Give the id of the item to edit")
        if no.isdigit() and int(no) < len(todos):
            new_value = input(f"Provide the new value for {todos[int(no)]}\n Type -1 for canceling")
            if new_value != '-1':
                todos[int(no)] = new_value
        else:
            print("incorrect index")
    elif user_action == "complete":
        no = input("Provide the index of the item to complete")
        todos.pop(int(no))
    elif user_action == 'exit':
        break

