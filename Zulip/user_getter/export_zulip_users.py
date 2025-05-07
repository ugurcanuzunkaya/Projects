import os
import zulip
import pandas as pd

# Get the directory of the script
script_dir = os.path.dirname(os.path.realpath(__file__))
current_dir = os.getcwd()

# Check if the script is being run from the correct directory
if script_dir != current_dir:
    print(f"Changing working directory from {current_dir} to {script_dir}")
    os.chdir(script_dir)

# Initialize the Zulip client
client = zulip.Client(config_file=r"zuliprc")

# Fetch all users
response = client.get_users()

if response['result'] == 'success':
    print("Successfully fetched")
    # Extract user data
    users = response['members']
    # Create a DataFrame with selected user information
    df = pd.DataFrame(users, columns=['full_name', 'email'])
    # Write the DataFrame to an Excel file
    df.to_excel('users.xlsx', index=False)
    print("User data has been written to 'users.xlsx'.")
else:
    print(f"Failed to fetch users: {response['msg']}")
