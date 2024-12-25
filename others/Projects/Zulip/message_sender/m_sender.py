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

# Define the message parameters
message = {
    "type": "stream",           # Indicates a channel message
    "to": "channel_name",       # Replace with the target channel name
    "topic": "message_topic",   # Replace with the desired topic
    "content": "your messaage content",  # Replace with your message
}

# Send the message
result = client.send_message(message)

# Check the result
if result["result"] == "success":
    print(f"Message sent successfully, ID: {result['id']}")
else:
    print(f"Failed to send message: {result['msg']}")
