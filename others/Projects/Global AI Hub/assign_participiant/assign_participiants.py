import pandas as pd
import random
import os
import openpyxl

# Get the directory of the script
script_dir = os.path.dirname(os.path.realpath(__file__))
current_dir = os.getcwd()

# Check if the script is being run from the correct directory
if script_dir != current_dir:
    print(f"Changing working directory from {current_dir} to {script_dir}")
    os.chdir(script_dir)

# List of mentors
mentors = ["Mentor 1", "Mentor 2", "Mentor 3"]

# Read the existing Excel file
df = pd.read_excel('participiants.xlsx')

# Shuffle the DataFrame
df = df.sample(frac=1).reset_index(drop=True)

# Assign mentors in a round-robin fashion
mentor_count = len(mentors)
df['Mentor Adı'] = [mentors[i % mentor_count] for i in range(len(df))]

# Group by "Mentor Adı" and add the count of rows for each mentor
grouped_df = df.groupby('Mentor Adı').apply(lambda x: x.assign(Mentor_Count=len(x)))

# Write the new Excel file
grouped_df.to_excel('assigned.xlsx', index=False)

print("New Excel file 'assigned.xlsx' has been created.")