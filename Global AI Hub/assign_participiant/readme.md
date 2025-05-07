# Participant Assignment Tool

A Python script designed to assign participants to mentors in a round-robin manner, shuffle the data, and generate a new Excel file with the assignments. This tool is ideal for streamlining mentor-participant assignment tasks.

## File Structure

```bash
assign_participiant/
├── assign_participants.py         # Main Python script for assigning participants to mentors
├── participiant.xlsx              # Input file containing participant details
├── assigned.xlsx          # Output file with assigned mentors
└── README.md                      # Project documentation
```

## Features

- Reads participant data from an Excel file.
- Randomly shuffles participant entries to ensure fair assignments.
- Assigns mentors to participants in a round-robin manner.
- Adds a column to indicate the number of participants assigned to each mentor.
- Generates a new Excel file with the updated data.

## Prerequisites

To use this script, ensure you have the following:

- Python 3 installed on your machine.
- The `openpyxl` and `pandas` libraries installed for handling Excel files and data manipulation.

## Installation

1. Clone this repository or download the script files:

   ```bash
   git clone https://github.com/yourusername/participant-mentor-assigner.git
   cd participant-mentor-assigner
   ```

2. Install the required dependencies:

   ```bash
   pip install pandas openpyxl
   ```

3. Place the input Excel file (`Katılımcılar.xlsx`) in the project directory.

## Usage

1. Open `assign_participants.py` and configure the list of mentors:

   ```python
   mentors = ["Mentor 1", "Mentor 2", "Mentor 3"]
   ```

   Add or modify the mentor names as needed.

2. Run the script:

   ```bash
   python assign_participants.py
   ```

3. The script will:
   - Shuffle the participant data.
   - Assign mentors to participants in a round-robin manner.
   - Generate a new Excel file named `assigned.xlsx` with the assignments.

## Example Output

The script provides console output during execution:

```
Changing working directory from /current/dir to /script/dir
New Excel file 'assigned.xlsx' has been created.
```

## Input File Format

The input Excel file (`participiant.xlsx`) should have a structured format, with participant details organized into rows. The script will add a new column, `Mentor Adı`, to indicate the assigned mentor.

## Troubleshooting

- **File Not Found**: Ensure that `participiant.xlsx` is placed in the script's directory and named correctly.
- **Missing Libraries**: Run `pip install pandas openpyxl` to install the required dependencies.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues or pull requests if you'd like to improve this tool!
