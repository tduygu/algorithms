import functions

import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box =sg.InputText("Enter todo")
add_button = sg.Button("Add")

# window = sg.Window("My To-Do App", layout=[[label, input_box]])
window = sg.Window("My To-Do App", layout=[[label], [input_box, add_button]])
window.read()
print("paused here")
window.close()



