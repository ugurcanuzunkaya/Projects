# Zulip User Updater

This project is a Python script designed to perform the following tasks on a Zulip server:

1. Find users by their full name (name + surname).
2. Update the user's name by appending a title (e.g., "(Mentor)").
3. Subscribe users to a specific Zulip stream.

## Prerequisites

To use this script, ensure the following are in place:

1. **Zulip Bot Credentials**: A Zulip bot is required to interact with the Zulip server. You need a `zuliprc` file with the bot's credentials.
   - Create a bot in the Zulip settings and download the configuration file.
2. **Python Environment**: Install Python 3.x.
3. **Zulip Python API**: Install the Zulip Python API library using pip:

   ```bash
   pip install zulip
   ```

## Features

- **Get User ID**: Searches for a user by their full name.
- **Update User Name**: Modifies a user's full name by appending a specified title.
- **Subscribe to Stream**: Adds a user to a specific Zulip stream by their email address.

## How to Use

1. **Clone the Repository**

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Place the `zuliprc` File**
   Ensure the `zuliprc` file is in the same directory as the script.

3. **Edit the Script**
   Update the `user_list` and `stream_name` variables in the `main()` function:

   ```python
   user_list = ["user1", "user2", "user3"]
   stream_name = "stream_name"
   ```

4. **Run the Script**
   Execute the script with Python:

   ```bash
   python user_update.py
   ```

5. **Output**
   The script will:
   - Update the names of the users in the `user_list` by appending the title "(Mentor)".
   - Subscribe the users to the specified `stream_name`.

## Error Handling

- If a user cannot be found, the script will print an error message: `User with the name '<name>' not found.`
- If updating a user or subscribing them to a stream fails, an appropriate error message will be displayed.

## Example Output

```bash
Successfully updated the name to: user1 (Mentor)
Successfully subscribed user1@example.com to stream: stream_name
Successfully updated the name to: user2 (Mentor)
Successfully subscribed user2@example.com to stream: stream_name
User with the name 'user3' not found.
```

## Notes

- Ensure the bot used has administrative privileges to update user information.
- The `zuliprc` file must be securely stored to avoid exposing sensitive credentials.

## License

This project is licensed under the MIT License.
