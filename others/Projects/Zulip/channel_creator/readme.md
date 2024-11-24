# Zulip Channel Creator and Group Subscription Tool

A Python script to create streams (channels) in Zulip, set their descriptions, and subscribe all members of a specific user group to these streams. This tool simplifies stream management and group coordination for Zulip administrators.

## File Structure

```bash
channel_creator/
├── channel_generator.py          # Main Python script for creating streams and subscribing group members
├── README.md                     # Project documentation
├── requirements.txt              # List of required packages
└── zuliprc                       # Zulip API credentials file (not included, see instructions)
```

## Features

- Create streams (channels) in Zulip if they do not already exist.
- Automatically update stream descriptions.
- Subscribe all members of a specified user group to the streams.

## Prerequisites

To use this script, ensure you have the following:

- A Zulip account with the necessary permissions to create streams and manage subscriptions.
- A Zulip bot or human user's API key (for authentication).
- Python 3 installed on your machine.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/zulip-channel-creator.git
   cd zulip-channel-creator
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Zulip API credentials:
   - Log in to your Zulip account.
   - Go to **Personal settings** and navigate to the **Your bots** section.
   - Download the `zuliprc` file for the bot or user account you wish to use.
   - Place the `zuliprc` file in the project directory or specify the file path in the script.

## Usage

1. Open `channel_generator.py` and configure the following:
   - Define the streams and their descriptions:

     ```python
     streams_to_create = [
         {"name": "Channel Name 1", "description": "Channel description 1"},
         {"name": "Channel Name 2", "description": "Channel description 2"},
         # Add more streams as needed
     ]
     ```

   - Set the group ID for the user group to subscribe:

     ```python
     group_id = 12345  # Replace with the actual group ID of the management group (Ex: Community Lead)
     ```

2. Run the script:

   ```bash
   python channel_generator.py
   ```

3. The script will:
   - Create the streams if they do not exist.
   - Update their descriptions.
   - Subscribe all members of the specified group to the streams.

## Example Output

The script provides console output during execution, indicating the progress and any errors encountered:

```
Creating stream 'Channel Name 1'...
Description for stream 'Channel Name 1' updated successfully.
Subscribed group members to stream 'Channel Name 1'.
Creating stream 'Channel Name 2'...
Description for stream 'Channel Name 2' updated successfully.
Subscribed group members to stream 'Channel Name 2'.
```

## Troubleshooting

- **Authentication Errors**: Ensure your `zuliprc` file is correctly configured and has the necessary permissions to create streams and manage subscriptions.
- **Group Not Found**: Verify that the group ID is correct and that the group exists in your Zulip organization.
- **Missing Libraries**: Run `pip install zulip` to ensure all dependencies are installed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues or pull requests if you'd like to improve this tool!
