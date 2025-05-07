# Channel Assigner

## Overview

The channel_assigner.py script assigns users to mentors randomly and generates an Excel file and a text file with the assignments. It reads user data from an Excel file, filters out mentors and community leads, and assigns each remaining user to a random mentor.

## Key Libraries

- **pandas**: Used for reading and manipulating data from the Excel file.
- **random**: Used for shuffling the mentor list and assigning mentors randomly.
- **os**: Used for handling file paths and changing the working directory.

## Project Structure

```text
channel_assigner/
│
├── channel_assigner.py      # The main script for assigning users to mentors
├── users.xlsx               # The input Excel file containing user data
├── assigned_users.xlsx      # The output Excel file with assigned mentors
├── mentor_assignments.txt   # The output text file with mentor assignments
└── README.md                # Readme file for the project
```

## Explanation of Key Functions and Methods

- **Reading the Excel file**: The script reads user data from `users.xlsx` using pandas.
- **Filtering users**: Mentors and community leads are removed from the DataFrame.
- **Shuffling mentors**: The mentor list is shuffled to ensure random assignment.
- **Assigning mentors**: Each remaining user is assigned to a random mentor.
- **Saving results**: The assignments are saved to `assigned_users.xlsx` and `mentor_assignments.txt`.

## How to Use

1. Ensure you have the required libraries installed:

   ```sh
   pip install pandas
   ```

2. Place your user data in an Excel file named `users.xlsx` in the same directory as the script. The Excel file should have at least two columns: `full_name` and `email`.

3. Run the script:

   ```sh
   python channel_assigner.py
   ```

4. After running the script, you will find two output files in the same directory:
   - `assigned_users.xlsx`: An Excel file with the assigned mentors.
   - `mentor_assignments.txt`: A text file with the mentor assignments and user emails.

## Example Output

### assigned_users.xlsx

| full_name | email              | mentor_assigned |
|-----------|--------------------|-----------------|
| User One  | <userone@example.com>| Mentor1         |
| User Two  | <usertwo@example.com>| Mentor1         |

### mentor_assignments.txt

```text
Mentor1
userone@example.com, usertwo@example.com
```

## License

This project is licensed under the MIT License. See the

LICENSE

 file for details.

## Contributing

Contributions are welcome! If you have any improvements or new features to add, please follow these steps:

1. Fork the repository.
2. Create a new branch:

   ```sh
   git checkout -b feature/your-feature-name
   ```

3. Make your changes and commit them:

   ```sh
   git commit -m 'Add some feature'
   ```

4. Push to the branch:

   ```sh
   git push origin feature/your-feature-name
   ```

5. Create a new Pull Request.
