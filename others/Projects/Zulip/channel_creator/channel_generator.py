import os
import zulip

# Get the directory of the script
script_dir = os.path.dirname(os.path.realpath(__file__))
current_dir = os.getcwd()

# Check if the script is being run from the correct directory
if script_dir != current_dir:
    print(f"Changing working directory from {current_dir} to {script_dir}")
    os.chdir(script_dir)

# Initialize the Zulip client
client = zulip.Client(config_file="zuliprc")

# Define the streams and their descriptions
streams_to_create = []

# Define the stream creation options
single = True  # Set to True to create a single stream
multiple = False  # Set to True to create multiple streams

if single:
    # Add a single stream to create with its description
    stream_name = "channel_name"
    stream_description = "stream_description"
    streams_to_create.append({"name": stream_name, "description": stream_description})
    print(f"Stream '{stream_name}' added to the list.")

if multiple:
    # Define the range of streams to create
    start_point = 1 # Replace with the desired starting number of streams
    end_point = 21 # Replace with the desired number of streams

    # Add multiple streams to create with their descriptions
    for i in range(start_point, end_point):
        stream_name = f"channel_name-{i:02}"
        stream_description = f"stream_description"
        streams_to_create.append({"name": stream_name, "description": stream_description})
        print(f"Stream '{stream_name}' added to the list.")

print(f"Creating {len(streams_to_create)} streams...")

# Find user by full name
user_full_name = "John Doe"  # Replace with the full name of the user
users_response = client.get_users()
user_email = None

if users_response["result"] == "success":
    for user in users_response["members"]:
        if user["full_name"] == user_full_name:
            user_email = user["email"]
            print(f"Found user: {user_full_name} with email: {user_email}")
            break
    
    if user_email is None:
        print(f"User with name '{user_full_name}' not found.")
else:
    print(f"Failed to retrieve users: {users_response['msg']}")

# Create streams and subscribe the specific user
for stream in streams_to_create:
    stream_name = stream["name"]
    stream_description = stream["description"]

    # Check if the stream exists
    existing_streams = client.get_streams()["streams"]
    existing_stream = next((s for s in existing_streams if s["name"] == stream_name), None)

    if not existing_stream:
        # Create the stream if it doesn't exist
        print(f"Creating stream '{stream_name}'...")
        response = client.add_subscriptions(streams=[{"name": stream_name}])

        if response["result"] != "success":
            print(f"Failed to create stream '{stream_name}': {response['msg']}")
            continue

        # Refresh the stream list to get the newly created stream's ID
        existing_streams = client.get_streams()["streams"]

    # Update the stream's description
    stream_id = next((s["stream_id"] for s in existing_streams if s["name"] == stream_name), None)
    if stream_id:
        update_response = client.update_stream({
            "stream_id": stream_id,
            "description": stream_description
        })
        if update_response["result"] == "success":
            print(f"Description for stream '{stream_name}' updated successfully.")
        else:
            print(f"Failed to update description for stream '{stream_name}': {update_response['msg']}")

    # Subscribe the specific user to the stream
    if user_email:
        response = client.add_subscriptions(
            streams=[{"name": stream_name}],
            principals=[user_email]  # Subscribe the specific user by their email
        )
        if response["result"] == "success":
            print(f"Subscribed {user_full_name} to stream '{stream_name}'.")
        else:
            print(f"Failed to subscribe {user_full_name} to stream '{stream_name}': {response['msg']}")
    else:
        print(f"Cannot subscribe user to stream '{stream_name}' as user was not found.")
