# Compressor Project

## Overview
This project provides a set of tools for compressing and extracting files using ZIP archives. It includes both command-line and graphical user interfaces (GUI) for ease of use. The project utilizes PySimpleGUI for the GUI and Python's built-in zipfile module for handling ZIP files.

## Key Libraries
- **PySimpleGUI**: Used for creating the graphical user interface.
- **zipfile**: Used for creating and extracting ZIP archives.
- **os**: Used for handling file and directory operations.
- **pathlib**: Used for handling file paths.

## Project Structure
```
compressorproject/
│
├── gui_zipcreator.py      # Script for the ZIP creation GUI
├── gui_zipextractor.py    # Script for the ZIP extraction GUI
├── readme.md              # Readme file for the project
├── zipcreator.py          # Script containing functions for creating ZIP archives
└── zipextractor.py        # Script containing functions for extracting ZIP archives
```

## Explanation of Key Functions and Methods
- **change_dir_to_this_file (zipcreator.py and zipextractor.py)**: Ensures the working directory is set to the directory of the script to handle file operations correctly.
- **make_archive (zipcreator.py)**: Creates a ZIP archive from a list of file paths and saves it to the specified destination directory.
- **extract_archive (zipextractor.py)**: Extracts all contents of a ZIP archive to the specified destination directory.

### gui_zipcreator.py
This script provides a graphical user interface for creating ZIP archives. Users can select files to compress and a destination folder for the ZIP archive. The `make_archive` function from `zipcreator.py` is used to create the archive.

### gui_zipextractor.py
This script provides a graphical user interface for extracting ZIP archives. Users can select a ZIP archive and a destination folder for extracting the contents. The `extract_archive` function from `zipextractor.py` is used to extract the archive.

## Final Output
The final output is a set of tools for compressing and extracting files using ZIP archives. Users can use either the command-line interface or the graphical user interface to perform these operations.
