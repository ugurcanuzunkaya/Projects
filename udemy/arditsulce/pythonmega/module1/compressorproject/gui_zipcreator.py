import PySimpleGUI as psg
from zipcreator import make_archive, change_dir_to_this_file

label1 = psg.Text("Select files to compress:")
input_box1 = psg.Input()
choose_button1 = psg.FilesBrowse("Choose", key="files")

label2 = psg.Text("Select destination folder:")
input_box2 = psg.Input()
choose_button2 = psg.FolderBrowse("Choose", key="folder")

compress_button = psg.Button("Compress")
output_label = psg.Text(key="output")

window = psg.Window(
    "Compressor",
    layout=[
        [label1, input_box1, choose_button1],
        [label2, input_box2, choose_button2],
        [compress_button, output_label],
    ],
)

while True:
    event, values = window.read()
    if event == "Compress":
        filepaths = values["files"].split(";")
        folder = values["folder"]

        change_dir_to_this_file()
        make_archive(filepaths=filepaths, dest_dir=folder)

        window["output"].update("Compression completed!")

    elif event == psg.WIN_CLOSED:
        window.close()
        break
