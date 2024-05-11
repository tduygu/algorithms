import functions

import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box =sg.InputText("Enter todo", key="txt_todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="lst_todos", enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

# window = sg.Window("My To-Do App", layout=[[label, input_box]])
window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button],[list_box, edit_button]],
                   font=('Helvetica', 20))
# event = window.read()
# print(event)
######################################
# event, values =window.read()
# print(event)
# print(values)
######################################
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['txt_todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['lst_todos'].update(values=todos)
        case sg.WIN_CLOSED:
            break
        case 'lst_todos':
            window['txt_todo'].update(value=values['lst_todos'][0])
        case "Edit":
            todo_to_edit = values['lst_todos'][0]
            new_todo = values['txt_todo'] + '\n'
            todos = functions.get_todos()
            n = todos.index(todo_to_edit)
            todos[n] = new_todo
            functions.write_todos(todos)
            window['lst_todos'].update(values=todos)
window.close()



