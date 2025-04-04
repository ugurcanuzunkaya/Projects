#!/bin/bash
# filepath: /Users/ugurcanuzunkaya/Documents/GitHub/Projects/others/Projects/Global AI Hub/youtube_chat_analyzer/setup_and_run.sh

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check if current directory is the same as script directory
if [ "$SCRIPT_DIR" != "$PWD" ]; then
    echo "Changing directory to $SCRIPT_DIR"
    cd "$SCRIPT_DIR" || exit 1
fi

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "Error: uv not found. Installing uv..."
    pip install uv
    if [ $? -ne 0 ]; then
        echo "Error: Failed to install uv. Please install it manually."
        exit 1
    fi
fi

# Create virtual environment using uv
echo "Creating virtual environment using uv..."
uv venv
if [ $? -ne 0 ]; then
    echo "Error: Failed to create virtual environment using uv."
    exit 1
fi

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Error: Failed to activate virtual environment."
    exit 1
fi

# Install requirements using uv
echo "Installing requirements using uv..."
uv pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Error: Failed to install requirements using uv."
    exit 1
fi

# Run the chat exporter script
echo "Running chat_exporter.py..."
python chat_exporter.py
if [ $? -ne 0 ]; then
    echo "Error: chat_exporter.py failed to run."
    exit 1
fi

echo "Process completed successfully!"