# Zulip Message Sender Bot

This project is a Python bot designed to send a specific message to a specified channel (stream) in a Zulip organization. It can also include notifications such as `@everyone` to alert all members of a stream.

## Prerequisites

1. **Python**: Ensure Python 3.x is installed on your system.
2. **Zulip Python Library**: Install the Zulip Python bindings using pip:

   ```bash
   pip install zulip
   ```

3. **Zulip Bot Credentials**:
   - Log in to your Zulip organization.
   - Navigate to **Settings** > **Your bots**.
   - Create a new bot and download the `zuliprc` configuration file.

## Usage

1. Clone or download this repository.
2. Place your `zuliprc` file in the project directory.
3. Modify the `message_sender.py` script to include your desired message, stream, and topic.
4. Run the script:

   ```bash
   python message_sender.py
   ```

## Parameters

```python
# Define the message parameters
message = {
    "type": "stream",           # Indicates a channel message
    "to": "channel_name",       # Replace with the target channel name
    "topic": "message_topic",   # Replace with the desired topic
    "content": "@**everyone** Your message content here",  # Replace with your message
}
```

- **`path_to_zuliprc`**: Path to the `zuliprc` file downloaded from your Zulip organization.
- **`channel_name`**: The name of the stream (channel) where the message will be sent.
- **`message_topic`**: The topic under which the message will appear.

- Notifiers (if needed):
  - **`@**everyone**`**: Notifies all members of the specified stream.
  - **`@**username**`**: Notifies a specific user in the stream.
  - **`@**group**`**: Notifies a specific group in the stream.
  - **`@**all**`**: Notifies all members of the stream.

- **`Your message content here`**: The content of the message.

## Notes

- Ensure the Zulip organization or stream permissions allow the use of `@everyone`.
- Users must have permission to send messages to the specified stream.

## References

- [Zulip API Documentation](https://zulip.com/api/)
- [Python Zulip API GitHub Repository](https://github.com/zulip/python-zulip-api)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
