# Inches to Meters Converter with GUI
import FreeSimpleGUI as fsg

label1 = fsg.Text("Enter feet:")
input_box1 = fsg.InputText(key="feet")

label2 = fsg.Text("Enter inches:")
input_box2 = fsg.InputText(key="inches")

convert_button = fsg.Button("Convert")

output_label = fsg.Text(key="output")
exit_button = fsg.Button("Exit")

layout = [[label1, input_box1], [label2, input_box2], [convert_button, exit_button], [output_label]]

window = fsg.Window("Inches to Meters", layout=layout)

while True:
    event, values = window.read()
    if event == "Convert":
        feet = int(values["feet"])
        inches = int(values["inches"])

        feet_to_inches = feet * 12
        total_inches = feet_to_inches + inches
        meters = round((total_inches * 0.0254), 4)

        window["output"].update(f"{feet} feet and {inches} inches is equal to {meters} meters. (Precision: 4 decimal places)")

    elif event in [fsg.WIN_CLOSED, "Exit"]:
        break