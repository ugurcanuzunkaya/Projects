import os
import zulip

def get_user_id(client, full_name):
    """
    Finds a user by their full name.
    :param client: Zulip client instance
    :param full_name: Full name of the user (name + surname)
    :return: User ID if found, None otherwise
    """
    response = client.get_members()
    if response['result'] == 'success':
        for member in response['members']:
            if member['full_name'] == full_name:
                return member['user_id']
    return None

def update_user_name(client, user_id, new_name):
    """
    Updates the user's name by their user ID.
    :param client: Zulip client instance
    :param user_id: The user ID of the user to update
    :param new_name: New name for the user
    """
    response = client.update_user_by_id(user_id, full_name=new_name)
    if response['result'] == 'success':
        print(f"Successfully updated the name to: {new_name}")
    else:
        print(f"Failed to update the name: {response.get('msg', 'Unknown error')}")

def subscribe_user_to_stream(client, user_email, stream_name):
    """
    Subscribes a user to a specific stream.
    :param client: Zulip client instance
    :param user_email: Email of the user to subscribe
    :param stream_name: Name of the stream to subscribe to
    """
    response = client.add_subscriptions(
        streams=[{"name": stream_name}],
        principals=[user_email]
    )
    if response['result'] == 'success':
        print(f"Successfully subscribed {user_email} to stream: {stream_name}")
    else:
        print(f"Failed to subscribe {user_email} to stream: {response.get('msg', 'Unknown error')}")

def process_users(client, user_list, stream_name):
    """
    Processes a list of users to update their names and subscribe them to a stream.
    :param client: Zulip client instance
    :param user_list: List of full names (name + surname)
    :param stream_name: Name of the stream to subscribe users to
    """
    for full_name in user_list:
        # Find user ID by full name
        user_id = get_user_id(client, full_name)
        if user_id:
            # Append "(Mentor)" to their name
            new_name = f"{full_name} (Mentor)"
            update_user_name(client, user_id, new_name)

            # Get user's email for subscription
            response = client.get_user_by_id(user_id)
            if response['result'] == 'success':
                user_email = response['user']['email']
                subscribe_user_to_stream(client, user_email, stream_name)
            else:
                print(f"Failed to fetch user email for {full_name}.")
        else:
            print(f"User with the name '{full_name}' not found.")

def main():
    # Read Zulip bot credentials from zuliprc file
    client = zulip.Client(config_file="zuliprc")

    # Input user list and stream name
    user_list = ["user1", "user2", "user3"]
    stream_name = "stream_name"

    # Process each user
    process_users(client, user_list, stream_name)

if __name__ == "__main__":
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    current_dir = os.getcwd()

    # Check if the script is being run from the correct directory
    if script_dir != current_dir:
        print(f"Changing working directory from {current_dir} to {script_dir}")
        os.chdir(script_dir)
    
    # Run the main function
    main()