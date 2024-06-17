import FreeSimpleGUI as fsg
import functions

label = fsg.Text("Type in a to-do item")
input_box = fsg.InputText(tooltip="Enter todo")
add_button = fsg.Button("Add")

window = fsg.Window("To-Do List", layout=[[label], [input_box], [add_button]])
window.read()
window.close()