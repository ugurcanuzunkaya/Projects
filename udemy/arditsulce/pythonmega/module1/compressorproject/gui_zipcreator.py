import PySimpleGUI as fsg
from zipcreator import make_archive, change_dir_to_this_file

label1 = fsg.Text("Select files to compress:")
input_box1 = fsg.Input()
choose_button1 = fsg.FilesBrowse("Choose", key="files")

label2 = fsg.Text("Select destination folder:")
input_box2 = fsg.Input()
choose_button2 = fsg.FolderBrowse("Choose", key="folder")

compress_button = fsg.Button("Compress")
output_label = fsg.Text(key="output")

window = fsg.Window("Compressor", layout=[[label1, input_box1, choose_button1], 
                                        [label2, input_box2, choose_button2], 
                                        [compress_button, output_label]])

while True:
    event, values = window.read()
    if event == "Compress":
        filepaths = values["files"].split(";")
        folder = values["folder"]
        
        change_dir_to_this_file()
        make_archive(filepaths=filepaths, dest_dir=folder)
        
        window["output"].update("Compression completed!")

    elif event == fsg.WIN_CLOSED:
        window.close()
        break
