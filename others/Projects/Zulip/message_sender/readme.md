# Mentor Assignment Tool

This project is a Python script designed to assign users to mentors in a systematic way, using data from an Excel file.

## Prerequisites

1. **Python**: Ensure Python 3.x is installed on your system.
2. **Required Libraries**: Install the required Python libraries using pip:

   ```bash
   pip install pandas openpyxl
   ```

3. **Excel File**: Prepare an Excel file named `users.xlsx` with at least the following columns:
   - `full_name`: Contains the full names of users, mentors, and community leads
   - `email`: Contains the email addresses of users

## Usage

1. Ensure your `users.xlsx` file is in the same directory as the script.
2. Run the script:

   ```bash
   python channel_assigner.py
   ```

3. The script will generate:
   - `assigned_users.xlsx`: Excel file with all users assigned to mentors
   - `mentor_assignments.txt`: Text file with mentor assignments and associated user emails

## How It Works

The script performs the following operations:

1. **Identification**: Identifies mentors and community leads from the Excel file based on name suffixes:
   - Identifies mentors by the suffix "(Mentor)"
   - Identifies community leads by suffixes like "(Community Lead)", "(Community Manager)", or "(Bot)"

2. **Filtering**: Filters out the mentors and community leads from the list of users to be assigned.

3. **Assignment**:
   - Randomly shuffles the list of mentors
   - Assigns each user to a random mentor

4. **Output Generation**:
   - Saves all users with their assigned mentors to an Excel file
   - Creates a text file with mentor assignments organized by mentor, including user emails

## Configuration Options

The script identifies different user roles based on name suffixes:

- Mentors are identified by the suffix "(Mentor)"
- Community leads are identified by suffixes like "(Community Lead)", "(Community Manager)", or "(Bot)"

To modify these identifiers or add new ones, update the condition checks in the script.

## Notes

- The script automatically detects and changes to the directory where it's located.
- Ensure the Excel file format is consistent, with proper column names.
- The random assignment ensures a fair distribution of users to mentors.

## References

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Python Random Module Documentation](https://docs.python.org/3/library/random.html)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
