import pandas as pd
import random
import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.realpath(__file__))
current_dir = os.getcwd()

# Check if the script is being run from the correct directory
if script_dir != current_dir:
    print(f"Changing working directory from {current_dir} to {script_dir}")
    os.chdir(script_dir)

# List of mentor names
mentor_names = [
    "Mentor1",
]

# List of community lead names
community_lead_names = [
    "Community Lead1",
]


# Read the Excel file
df = pd.read_excel('users.xlsx')  # Replace with your Excel file name

# Remove mentors and community leads from the DataFrame
df_filtered = df[~df['full_name'].isin(mentor_names + community_lead_names)].copy()

# Shuffle the mentor list
random.shuffle(mentor_names)

# Assign each remaining row to a random mentor
df_filtered['mentor_assigned'] = [random.choice(mentor_names) for _ in range(len(df_filtered))]

# Save the result to a new Excel file
df_filtered.to_excel('assigned_users.xlsx', index=False)

# Group users by mentor
mentor_groups = df_filtered.groupby('mentor_assigned')

# Write mentor assignments to a text file
with open('mentor_assignments.txt', 'w') as f:
    for mentor, group in mentor_groups:
        f.write(f'{mentor}\n')
        emails = group['email'].tolist()
        emails_str = ', '.join(emails)
        f.write(f'{emails_str}\n\n')