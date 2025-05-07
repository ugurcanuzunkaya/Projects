# Zulip User Analyzer

A comprehensive toolkit for downloading, analyzing, and visualizing user activity data from Zulip chat platforms.

## Overview

This project provides a set of Python scripts to analyze user activity in a Zulip workspace, with specialized analyses for different user roles (mentors, community leaders) and communication channels (streams).

### Key Components

1. **Message Getter** (`message_getter.py`): Downloads messages from Zulip servers to a local Excel file
2. **Core Analysis** (`analyzer_dashboard.py`): Base functionality for analyzing user activity patterns
3. **Role-specific Analysis**:
   - **Mentor Analyzer** (`mentor_analyzer.py`): Analyzes activity of users with "(Mentor)" suffix
   - **Lead Analyzer** (`lead_analyzer.py`): Analyzes activity of users with "(Community Lead)" or "(Community Manager)" suffix
4. **Stream Analysis**:
   - **Stream Analyzer** (`stream_analyzer.py`): Analyzes activity in different Zulip streams
   - **Mentor Stream Impact** (`mentor_stream_impact.py`): Measures the impact of mentors in different streams

## Setup Instructions

### Prerequisites

- Python 3.7+
- Required packages: `zulip`, `pandas`, `matplotlib`, `seaborn`, `numpy`, `openpyxl`
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

Run the message getter script to download messages from your Zulip workspace:

```bash
python message_getter.py
```

This will create a file named `zulip_messages.xlsx` in the current directory.

### Step 2: Run Analysis

Run any of the analyzer scripts based on your needs:

```bash
# For general user analysis
python analyzer_dashboard.py

# For mentor-specific analysis
python mentor_analyzer.py

# For community leader analysis
python lead_analyzer.py

# For stream analysis
python stream_analyzer.py

# For mentor impact analysis
python mentor_stream_impact.py
```

## Analysis Output

The analyzer produces several outputs in separate directories:

### Core Analysis (`analysis_output/`)

- **Excel Report**: `user_performance_analysis.xlsx` with multiple sheets
- **Visualizations**:
  - Message counts by top users
  - Daily activity rates
  - Hourly distribution of messages
  - Day of week activity patterns
  - Top active streams

### Mentor Analysis (`mentor_analysis/`)

- Individual visualizations for each mentor
- Comparative visualizations across mentors
- Excel report with mentor-specific metrics

### Community Leader Analysis (`community_leader_analysis/`)

- Individual visualizations for each community leader
- Comparative visualizations across leaders
- Excel report with leader-specific metrics

### Stream Analysis (`mentor_stream_analysis/`)

- Activity metrics for mentor-focused streams
- Top contributors to each stream
- Mentor participation rates

### Mentor Impact Analysis (`mentor_impact_analysis/`)

- Influence measurements of mentors in various streams
- Visualization of mentor impact percentages
- Excel report with impact metrics

## File Structure

```bash
user_analyzer/
├── message_getter.py              # Downloads messages from Zulip
├── analyzer_dashboard.py          # Core analysis functionality
├── mentor_analyzer.py             # Analysis for mentors
├── lead_analyzer.py               # Analysis for community leaders
├── stream_analyzer.py             # Analysis for streams
├── mentor_stream_impact.py        # Analysis of mentor impact in streams
├── README.md                      # This documentation file
├── zuliprc                        # Zulip API credentials (you need to create this)
├── zulip_messages.xlsx            # Downloaded message data
└── analysis_output/               # Output directory for analysis results
      ├── user_performance_analysis.xlsx
      ├── visualizations/
      │   ├── message_counts_by_user.png
      │   ├── daily_activity_rate.png
      │   ├── hourly_distribution.png
      │   ├── day_of_week_activity.png
      │   └── top_active_streams.png
      ├── mentor_analysis/
         ├── mentor1_analysis.xlsx
         ├── mentor2_analysis.xlsx
         └── ...
      ├── community_leader_analysis/
         ├── leader1_analysis.xlsx
         ├── leader2_analysis.xlsx
         └── ...
      ├── mentor_stream_analysis/
         ├── stream1_analysis.xlsx
         ├── stream2_analysis.xlsx
         └── ...
      └── mentor_impact_analysis/
         ├── impact_analysis.xlsx
         └── ...
```

## Notes

- The time analysis is based on message timestamps in the Zulip database
- Performance metrics include message count, activity rate, and engagement patterns
- Visualizations help identify user activity patterns and peak usage times
- The analysis recognizes user roles based on name suffixes:
  - Mentors are identified by "(Mentor)" suffix
  - Community leaders are identified by "(Community Lead)" or "(Community Manager)" suffixes
- Certain streams can be excluded from analysis by editing the `exclude_streams` list in `stream_analyzer.py`

## License

This project is licensed under the MIT License.
