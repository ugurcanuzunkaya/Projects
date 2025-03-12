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

# Read the Excel file
df = pd.read_excel('users.xlsx')  # Replace with your Excel file name

# Extract mentor names and community lead names from the Excel file
mentor_names = []
community_lead_names = []

for _, row in df.iterrows():
    full_name = row['full_name']
    if full_name.endswith("(Mentor)"):
        # Remove the "(Mentor)" suffix and add to mentor_names
        mentor_names.append(full_name)
    elif any(full_name.endswith(suffix) for suffix in ["(Community Lead)", "(Community Manager)", "(Bot)"]):
        # Add to community_lead_names
        community_lead_names.append(full_name)

# Print the extracted mentor and community lead names for verification
print(f"Mentors: {mentor_names}, Total: {len(mentor_names)}")
print(f"Community Leads: {community_lead_names}, Total: {len(community_lead_names)}")


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
    # Sort mentor groups by mentor name and enumerate them
    for i, (mentor, group) in enumerate(sorted(mentor_groups), 1):
        # Write mentor name with number (zero-padded to 2 digits) and count of users
        f.write(f'{mentor} - {i:02d} - {len(group)}\n')
        emails = group['email'].tolist()
        emails_str = ', '.join(emails)
        f.write(f'{emails_str}\n\n')