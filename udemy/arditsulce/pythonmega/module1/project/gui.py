import FreeSimpleGUI as fsg
import functions
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        file.write("")


fsg.theme("DarkAmber")

clock = fsg.Text("", key="clock")

label = fsg.Text("Type in a to-do item")
input_box = fsg.InputText(tooltip="Enter todo", key="todo")
add_button = fsg.Button("Add")

list_box = fsg.Listbox(values=functions.file_operations(filename="todos", listname=[], operation="r"),
                        key="todos", enable_events=True, size=(40, 10))

edit_button = fsg.Button("Edit")
complete_button = fsg.Button("Complete")
exit_button = fsg.Button("Exit")

layout = [[clock],
        [label], 
        [input_box, add_button], 
        [list_box, edit_button, complete_button],
        [exit_button]
        ]

window = fsg.Window("To-Do List", 
                    layout=layout,
                    font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=100)
    window["clock"].update(value=time.strftime("%b %d %Y | %H:%M:%S"))
    match event:
        case "Add":
            todo = values["todo"]
            todos = functions.file_operations(filename="todos", listname=[], operation="r")
            
            todos.append(todo)
            functions.file_operations(filename="todos", listname=todos, operation="w")
            
            todos = functions.file_operations(filename="todos", listname=[], operation="r")
            window["todos"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                
                todos = functions.file_operations(filename="todos", listname=[], operation="r")
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                
                functions.file_operations(filename="todos", listname=todos, operation="w")
                window["todos"].update(values=todos)
            
            except IndexError:
                fsg.popup("Select a to-do item to edit")

        case "Complete":
            todo_to_complete = values["todos"][0]

            todos = functions.file_operations(filename="todos", listname=[], operation="r")
            todos.remove(todo_to_complete)
            functions.file_operations(filename="todos", listname=todos, operation="w")
            
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        
        case "todos":
            window["todo"].update(value=values["todos"][0])
            
        case "Exit", fsg.WIN_CLOSED:
            break