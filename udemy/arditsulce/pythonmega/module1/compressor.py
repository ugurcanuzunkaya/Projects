import FreeSimpleGUI as fsg

label1 = fsg.Text("Select files to compress:")
input_box1 = fsg.Input()
choose_button1 = fsg.FilesBrowse("Choose files")

label2 = fsg.Text("Select destination folder:")
input_box2 = fsg.Input()
choose_button2 = fsg.FolderBrowse("Choose folder")

compress_button = fsg.Button("Compress")

window = fsg.Window("Compressor", layout=[[label1, input_box1, choose_button1], [label2, input_box2, choose_button2], [compress_button]])
window.read()
window.close()