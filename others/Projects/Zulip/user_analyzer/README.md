# Zulip User Analyzer

A toolkit for downloading, analyzing, and visualizing user activity data from Zulip chat platforms.

## Overview

This project consists of two main components:

1. **Message Getter** (`message_getter.py`): Downloads messages from Zulip servers.
2. **Analyzer Dashboard** (`analyzer_dashboard.py`): Analyzes and visualizes user activity based on the downloaded messages.

## Setup Instructions

### Prerequisites

- Python 3.7+
- Required packages: `zulip`, `pandas`, `matplotlib`, `seaborn`, `numpy`
- A Zulip account with API access

### Installation

1. Clone this repository or download the files
2. Install required packages:

   ```bash
   pip install zulip pandas matplotlib seaborn numpy openpyxl
   ```

3. Create a `zuliprc` file in the same directory as the scripts:

   This file should contain your Zulip API credentials. You can download it from your Zulip account:
   - Go to Zulip web interface
   - Click on Settings (gear icon)
   - Select "Personal settings"
   - Navigate to the "API key" section
   - Click "Show/change API key"
   - Click "Download zuliprc"

   Place the downloaded file in the `user_analyzer` directory.

## Usage

### Step 1: Download Messages

Run the message getter script to download messages from your Zulip instance:

```bash
python message_getter.py
```

You'll be prompted to:

1. Choose between getting messages from a specific user or searching all channels
2. Enter a user's full name or a search query
3. The script will create an Excel file (`<name>_messages_<timestamp>.xlsx`) containing the downloaded messages

### Step 2: Analyze User Activity

After downloading messages, run the analyzer dashboard:

```bash
python analyzer_dashboard.py
```

The script expects a file named `zulip_messages.xlsx` in the same directory.
If your file has a different name, rename it or modify the script to use your filename.

## Analysis Output

The analyzer produces several outputs in the `analysis_output` directory:

### Excel Report

A comprehensive Excel file (`user_performance_analysis.xlsx`) with multiple sheets:

- **User Performance**: Overall user activity metrics
- **Top Streams by User**: What streams each user is most active in
- **Daily Activity**: Message counts by day and user
- **Hour Summary**: Message distribution by hour of day

### Visualizations

- **Message Count**: Bar chart of message counts by top users
- **Messages per Day**: Daily activity rate by top users
- **Hour Activity**: Hourly distribution of messages for top users
- **Day of Week Activity**: Message distribution across weekdays
- **Top Streams**: Most active streams for top users

## File Descriptions

- `message_getter.py`: Tool for downloading messages from Zulip
- `analyzer_dashboard.py`: Tool for analyzing user activity
- `zuliprc`: Configuration file with API credentials (you need to create this)
- `analysis_output/`: Directory containing analysis results

## Notes

- The time analysis is based on message timestamps in the Zulip database
- Performance metrics include message count, activity rate, and engagement patterns
- Visualizations help identify user activity patterns and peak usage times
