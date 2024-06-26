# Inches to Meters Converter with GUI
import PySimpleGUI as psg

label1 = psg.Text("Enter feet:")
input_box1 = psg.InputText(key="feet")

label2 = psg.Text("Enter inches:")
input_box2 = psg.InputText(key="inches")

convert_button = psg.Button("Convert")

output_label = psg.Text(key="output")
exit_button = psg.Button("Exit")

layout = [[label1, input_box1], [label2, input_box2], [convert_button, exit_button], [output_label]]

window = psg.Window("Inches to Meters", layout=layout)

while True:
    event, values = window.read()
    if event == "Convert":
        feet = int(values["feet"])
        inches = int(values["inches"])

        feet_to_inches = feet * 12
        total_inches = feet_to_inches + inches
        meters = round((total_inches * 0.0254), 4)

        window["output"].update(f"{feet} feet and {inches} inches is equal to {meters} meters. (Precision: 4 decimal places)")

    elif event in [psg.WIN_CLOSED, "Exit"]:
        break