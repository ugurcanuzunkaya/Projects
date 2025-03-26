#!/bin/bash

# Check if we're in a git repository
if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
    echo "Error: Not in a git repository."
    exit 1
fi

# Check git status
echo "Checking git status..."
git status

# Show changes in files
echo -e "\nShowing file differences..."
git diff --stat

# Ask if user wants to see detailed changes
read -p "Do you want to see detailed changes? (y/n): " see_diff
if [[ $see_diff == "y" || $see_diff == "Y" ]]; then
    git diff
fi

# Get list of changed files
changed_files=$(git diff --name-only)

if [ -z "$changed_files" ]; then
    echo "No changed files detected. Did you stage your changes?"
    read -p "Do you want to see staged changes? (y/n): " see_staged
    if [[ $see_staged == "y" || $see_staged == "Y" ]]; then
        git diff --staged
        changed_files=$(git diff --staged --name-only)
    fi
fi

# Generate a suggested commit message based on the changes
commit_subject=""
if [ ! -z "$changed_files" ]; then
    # Get the most common file extension or directory to infer the type of changes
    common_ext=$(echo "$changed_files" | awk -F. '{print $NF}' | sort | uniq -c | sort -nr | head -1 | awk '{print $2}')
    common_dir=$(echo "$changed_files" | grep "/" | cut -d/ -f1 | sort | uniq -c | sort -nr | head -1 | awk '{print $2}')
    
    # Try to make a relevant commit message
    if [ ! -z "$common_dir" ]; then
        commit_subject="Update $common_dir components"
    elif [ ! -z "$common_ext" ]; then
        commit_subject="Update $common_ext files"
    else
        commit_subject="Make various changes"
    fi
    
    echo -e "\nSuggested commit message: $commit_subject"
else
    echo "No changes detected for commit"
    exit 0
fi

# Ask for commit message
echo -e "\nEnter commit message (press Enter to use the suggested message):"
read user_message

if [ -z "$user_message" ]; then
    user_message=$commit_subject
fi

# Confirm and commit
echo -e "\nCommit message will be: \"$user_message\""
read -p "Proceed with commit? (y/n): " do_commit

if [[ $do_commit == "y" || $do_commit == "Y" ]]; then
    git commit -m "$user_message"
    echo "Commit successful!"
else
    echo "Commit cancelled."
fi
