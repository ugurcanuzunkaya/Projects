# To-Do Web App

## Overview
This project is a simple to-do list application that provides a command-line interface, a graphical user interface (GUI), and a web interface for managing tasks. It allows users to add, edit, complete, and delete to-do items. The application uses text files for storing the to-do items.

## Key Libraries
- **PySimpleGUI**: Used for creating the graphical user interface.
- **Streamlit**: Used for creating the web interface.
- **OS**: Used for handling file and directory operations.
- **Pathlib**: Used for handling file paths.
- **Time**: Used for displaying the current time in the GUI.

## Project Structure
```
to-do-webapp/
│
├── functions.py         # Script containing the file operations function
├── gui.py               # Script for the graphical user interface
├── main.py              # Script for the command-line interface
├── readme.md            # Readme file for the project
├── requirements.txt     # Requirements file listing the project's dependencies
├── todos.txt            # Text file for storing the to-do items
└── web.py               # Script for the web interface
```

## Explanation of Key Functions and Methods
- **file_operations (functions.py)**: Handles reading from and writing to the text file containing the to-do items. It takes the filename, a list, and an operation ('r' for read, 'w' for write) as parameters.
- **add_todo (web.py)**: Adds a new to-do item to the list and updates the text file.
- **clear_all_todos (web.py)**: Clears all to-do items from the list and updates the text file.
- **change_dir_to_this_file (web.py)**: Changes the working directory to the directory of the current script to ensure correct file operations.

## GUI (gui.py)
This script provides a graphical user interface using PySimpleGUI. It includes functionalities to add, edit, complete, and delete to-do items. The to-do items are displayed in a listbox, and the current time is shown at the top of the window.

## Command-Line Interface (main.py)
This script provides a command-line interface for managing the to-do list. It supports operations such as adding, showing, editing, completing, deleting, and clearing to-do items. The to-do items are stored in a text file.

## Web Interface (web.py)
This script provides a web interface using Streamlit. It includes functionalities to add new to-do items, clear all to-do items, and display the current list of to-do items. Users can also mark items as completed by checking a checkbox.

## External Files
- **todos.txt**: This text file stores the to-do items. Each line in the file represents a to-do item.

## Final Output
The final output is a fully functional to-do list application with three interfaces:
1. **Command-Line Interface**: Run `main.py` to interact with the application through the terminal.
2. **Graphical User Interface**: Run `gui.py` to interact with the application through a windowed interface.
3. **Web Interface**: Run `web.py` to interact with the application through a web browser using Streamlit.
