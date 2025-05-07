import zulip
import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.realpath(__file__))
current_dir = os.getcwd()

# Check if the script is being run from the correct directory
if script_dir != current_dir:
    print(f"Changing working directory from {current_dir} to {script_dir}")
    os.chdir(script_dir)


# Initialize the Zulip client
client = zulip.Client(config_file="zuliprc")

# Define message content (used for all channels)
message_content = "message_content"  # Replace with the desired message content
message_topic = "topic"  # Replace with the desired message topic


# Define the channels to send the message to (single or multiple)
single = False  # Set to True to send the message to a single channel
multiple = True  # Set to True to send the message to multiple channels

if single:
    # Add a single channel to send the message to
    channel_name = "channel_name"  # Replace with the desired channel name
    channels = [channel_name]
    print(f"Sending message to '{channel_name}'.")

if multiple:
    # Define the range of channels to send the message to
    start_point = 1  # Replace with the desired starting number of channels
    end_point = 21  # Replace with the desired ending number of channels
    channels = [f"channel_name-{i:02}" for i in range(start_point, end_point)] # Replace with the desired channel names
    print(f"Sending message to {len(channels)} channels...")
    print(channels)

# Send the message to each channel
for channel in channels:
    message = {
        "type": "stream",
        "to": channel,
        "topic": message_topic,
        "content": message_content,
    }
    
    # Send the message
    result = client.send_message(message)
    
    # Check the result
    if result["result"] == "success":
        print(f"Message sent successfully to '{channel}', ID: {result['id']}")
    else:
        print(f"Failed to send message to '{channel}': {result['msg']}")
