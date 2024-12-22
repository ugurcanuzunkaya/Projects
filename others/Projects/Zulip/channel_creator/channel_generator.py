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
streams_to_create = [
    {"name": "channel1", "description": "description1"},
]

# Use the hardcoded group ID
group_id = 12345  # Replace with the actual group ID for 'Community Lead'

# Step 1: Retrieve members of the user group
user_groups = client.get_user_groups()
group = next((g for g in user_groups["user_groups"] if g["id"] == group_id), None)

if not group:
    print(f"Group with ID {group_id} not found.")
else:
    group_members = group["members"]
    if not group_members:
        print(f"No members found in the group '{group['name']}' (ID {group_id}).")
    else:
        print(f"Group '{group['name']}' found with {len(group_members)} members.")

        # Step 2: Ensure streams exist, add descriptions, and subscribe group members
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

            # Subscribe group members to the stream
            response = client.add_subscriptions(
                streams=[{"name": stream_name}],
                principals=group_members  # Subscribe all members by their email addresses
            )
            if response["result"] == "success":
                print(f"Subscribed group members to stream '{stream_name}'.")
            else:
                print(f"Failed to subscribe group members to stream '{stream_name}': {response['msg']}")