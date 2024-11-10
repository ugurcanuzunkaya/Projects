# Zulip Users Exporter

A Python script to export all users' names and email addresses from a Zulip organization and save them to an Excel file. This tool can be helpful for Zulip admins or team members looking to keep track of their organization's user information.

## File Structure

```bash
zulip-users-exporter/
├── export_zulip_users.py         # Main Python script for exporting users
├── README.md                     # Project documentation
├── requirements.txt              # List of required packages
├── zuliprc                       # Zulip API credentials file (not included, see instructions)
└── zulip_users.xlsx              # Output file (generated after running the script)
```

## Features

- Fetch all users' full names and email addresses from your Zulip organization.
- Export the data into an Excel file for easy access and management.
  
## Prerequisites

To use this script, ensure you have the following:

- A Zulip account with the necessary permissions to access user data.
- A Zulip bot's API key (for authentication).
- Python 3 installed on your machine.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/zulip-users-exporter.git
   cd zulip-users-exporter
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Zulip API credentials:
   - Log in to your Zulip account.
   - Go to **Personal settings** and navigate to the **Your bots** section.
   - Download the `zuliprc` file for the bot you wish to use.
   - Place the `zuliprc` file in the project directory or specify the file path in the script.

## Usage

1. Open `export_zulip_users.py` and confirm that the path to the Zulip API credentials is correct:
   ```python
   client = zulip.Client(config_file="path_to_your_zuliprc_file")
   ```

2. Run the script:
   ```bash
   python export_zulip_users.py
   ```

3. After successful execution, you will find a file named `zulip_users.xlsx` in your directory, containing the names and email addresses of all users in your Zulip organization.

## Example Output

The generated Excel file (`zulip_users.xlsx`) will have the following structure:

| full_name         | email                |
|-------------------|----------------------|
| User One          | userone@example.com  |
| User Two          | usertwo@example.com  |
| ...               | ...                  |

## Troubleshooting

- **Authentication Errors**: Ensure your `zuliprc` file is properly configured and has the necessary permissions to access user data.
- **Library Not Found**: If you encounter missing library errors, make sure to run `pip install zulip pandas openpyxl` to install dependencies.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues or pull requests if you'd like to improve this tool!
