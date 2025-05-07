#!/bin/bash
# filepath: /Users/ugurcanuzunkaya/Documents/GitHub/Projects/others/Projects/Global AI Hub/youtube_chat_analyzer/run.sh

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Navigate to script directory
cd "$SCRIPT_DIR" || exit 1

# Check if .venv exists
if [ ! -d ".venv" ]; then
    echo "Error: Virtual environment not found."
    echo "Please create a virtual environment first with: uv venv"
    exit 1
fi

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate || source .venv/Scripts/activate

# Check if activation was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to activate virtual environment."
    exit 1
fi

# Run the chat exporter script
echo "Running chat_exporter.py..."
python chat_exporter.py

echo "Process completed!"
