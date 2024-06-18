from calendar import c
import FreeSimpleGUI as fsg
from zipextractor import extract_archive, change_dir_to_this_file

label1 = fsg.Text("Select archive")
input_box1 = fsg.Input()
choose_button1 = fsg.FilesBrowse("Choose", key="archive")

label2 = fsg.Text("Select destination folder:")
input_box2 = fsg.Input()
choose_button2 = fsg.FolderBrowse("Choose", key="folder")

compress_button = fsg.Button("Extract")
output_label = fsg.Text(key="output")

window = fsg.Window("Archive Extractor", 
                    layout=[[label1, input_box1, choose_button1],
                            [label2, input_box2, choose_button2], 
                            [compress_button, output_label],
                            ])

while True:
    event, values = window.read()
    match event:
        case "Extract":
            archivepath = values["archive"]
            folder = values["folder"]
            
            change_dir_to_this_file()
            extract_archive(archive_path=archivepath, dest_dir=folder)
            
            window["output"].update("Extraction completed!")

        case fsg.WIN_CLOSED:
            window.close()
            break
