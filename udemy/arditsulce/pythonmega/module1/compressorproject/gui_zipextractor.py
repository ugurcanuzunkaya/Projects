import PySimpleGUI as psg
from zipextractor import extract_archive, change_dir_to_this_file

label1 = psg.Text("Select archive")
input_box1 = psg.Input()
choose_button1 = psg.FilesBrowse("Choose", key="archive")

label2 = psg.Text("Select destination folder:")
input_box2 = psg.Input()
choose_button2 = psg.FolderBrowse("Choose", key="folder")

compress_button = psg.Button("Extract")
output_label = psg.Text(key="output")

window = psg.Window(
    "Archive Extractor",
    layout=[
        [label1, input_box1, choose_button1],
        [label2, input_box2, choose_button2],
        [compress_button, output_label],
    ],
)

while True:
    event, values = window.read()
    match event:
        case "Extract":
            archivepath = values["archive"]
            folder = values["folder"]

            change_dir_to_this_file()
            extract_archive(archive_path=archivepath, dest_dir=folder)

            window["output"].update("Extraction completed!")

        case psg.WIN_CLOSED:
            window.close()
            break
