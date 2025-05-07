import pandas as pd
import os
import argparse
import sys
from analyzer_dashboard import load_data
from stream_analyzer import analyze_mentor_stream_activity, create_mentor_stream_visualizations, export_mentor_stream_excel

# ======= HARDCODED CONFIGURATION =======
# Modify these variables to change the Excel file and stream name
EXCEL_FILE = "zulip_messages.xlsx"  # File name in the script directory
TARGET_STREAM = "06. Yararlı Kaynaklar"  # Stream name to analyze
DISPLAY_MESSAGES = True  # Set to True to display individual messages
OUTPUT_EXCEL = True  # Set to True to export messages to Excel
# =======================================

def filter_by_stream(stream_name, excel_file, display_messages=False, output_excel=False):
    """Filter messages by a specific stream name and perform analysis on just that stream."""
    # Define paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, excel_file)
    output_dir = os.path.join(script_dir, "analysis_output", "stream_specific", stream_name.replace("/", "_").replace(" ", "_"))
    os.makedirs(output_dir, exist_ok=True)
    
    # Load data
    print(f"Loading data from {data_path}...")
    df = load_data(data_path)
    if df is None:
        print(f"Please ensure '{excel_file}' is in the same directory as this script.")
        return
    
    # Process datetime if not already done
    if 'datetime' not in df.columns and 'date' in df.columns and 'time' in df.columns:
        print("Processing date and time columns to create datetime...")
        try:
            df['parsed_date'] = pd.to_datetime(df['date'], errors='coerce')
            df['parsed_time'] = pd.to_datetime(df['time'], format='%H:%M:%S', errors='coerce').dt.time
            
            # Create datetime column
            df['datetime'] = pd.NaT
            for i in df.index[df['parsed_date'].notna()]:
                if df.loc[i, 'parsed_time'] is not None:
                    try:
                        df.loc[i, 'datetime'] = pd.Timestamp.combine(
                            df.loc[i, 'parsed_date'].date(),
                            df.loc[i, 'parsed_time']
                        )
                    except:
                        continue
                        
            # Use timestamp as fallback
            if 'timestamp' in df.columns:
                missing_dt = df['datetime'].isna()
                df.loc[missing_dt, 'datetime'] = pd.to_datetime(df.loc[missing_dt, 'timestamp'], errors='coerce')
        except Exception as e:
            print(f"Error processing datetime: {e}")
    
    # Filter messages by the specified stream name
    print(f"Filtering messages for stream: {stream_name}")
    filtered_df = df[df['stream_name'] == stream_name]
    
    if filtered_df.empty:
        print(f"No messages found for stream '{stream_name}'.")
        print("Available stream names:")
        for name in sorted(df['stream_name'].unique()):
            print(f"  - {name}")
        return
    
    # Show basic stats about the filtered data
    print(f"\nStream: {stream_name}")
    print(f"Total messages: {filtered_df.shape[0]}")
    print(f"Date range: {filtered_df['datetime'].min().strftime('%Y-%m-%d')} to {filtered_df['datetime'].max().strftime('%Y-%m-%d')}")
    print(f"Unique participants: {filtered_df['sender_full_name'].nunique()}")
    print(f"Unique topics: {filtered_df['topic'].nunique()}")
    
    # Display individual messages if requested
    if display_messages:
        print("\n--- Individual Messages ---")
        # Sort by datetime to show messages in chronological order
        message_df = filtered_df.sort_values('datetime')
        # Select only relevant columns for display
        message_display = message_df[['datetime', 'sender_full_name', 'topic', 'content']]
        
        # Format the output for better readability
        for _, row in message_display.iterrows():
            date_str = row['datetime'].strftime('%Y-%m-%d %H:%M:%S') if pd.notna(row['datetime']) else "Unknown date"
            print(f"\nTime: {date_str}")
            print(f"Sender: {row['sender_full_name']}")
            print(f"Topic: {row['topic']}")
            print(f"Message: {row['content'][:200]}..." if len(row['content']) > 200 else f"Message: {row['content']}")
            print("-" * 50)
    
    # Export messages to Excel if requested
    if output_excel:
        excel_messages_path = os.path.join(output_dir, f"{stream_name.replace('/', '_').replace(' ', '_')}_messages.xlsx")
        # Sort by datetime to show messages in chronological order
        message_export = filtered_df.sort_values('datetime')
        
        try:
            with pd.ExcelWriter(excel_messages_path) as writer:
                # Create primary messages sheet with key information
                message_export[['datetime', 'sender_full_name', 'topic', 'content']].to_excel(
                    writer, sheet_name='Messages', index=False
                )
                
                # Add sheet with participant statistics
                participant_stats = message_export['sender_full_name'].value_counts().reset_index()
                participant_stats.columns = ['Participant', 'Message Count']
                participant_stats['Percentage'] = (participant_stats['Message Count'] / participant_stats['Message Count'].sum() * 100).round(2)
                participant_stats.to_excel(writer, sheet_name='Participant Stats', index=False)
                
                # Add sheet with topic statistics
                topic_stats = message_export['topic'].value_counts().reset_index()
                topic_stats.columns = ['Topic', 'Message Count']
                topic_stats['Percentage'] = (topic_stats['Message Count'] / topic_stats['Message Count'].sum() * 100).round(2)
                topic_stats.to_excel(writer, sheet_name='Topic Stats', index=False)
                
                # Add sheet with daily activity
                if 'datetime' in message_export.columns:
                    message_export['date'] = message_export['datetime'].dt.date
                    daily_activity = message_export.groupby('date').size().reset_index(name='message_count')
                    daily_activity.columns = ['Date', 'Message Count']
                    daily_activity.to_excel(writer, sheet_name='Daily Activity', index=False)
            
            print(f"\nMessages exported to Excel: {excel_messages_path}")
        except Exception as e:
            print(f"Error exporting messages to Excel: {e}")
    
    # Create a "fake" mentor_streams variable to reuse the analysis functions
    mentor_streams = filtered_df
    mentor_stream_names = [stream_name]
    
    # Analyze stream activity
    print("\nAnalyzing stream activity...")
    stream_stats, top_contributors, participation = analyze_mentor_stream_activity(
        df, mentor_streams, mentor_stream_names
    )
    
    # Create visualizations
    print("Creating stream visualizations...")
    vis_dir = create_mentor_stream_visualizations(
        stream_stats, top_contributors, participation, output_dir
    )
    
    # Export to Excel
    excel_path = export_mentor_stream_excel(
        stream_stats, top_contributors, participation, mentor_streams, output_dir
    )
    
    print(f"\nStream analysis complete for '{stream_name}'!")
    print(f"Visualizations directory: {vis_dir}")
    print(f"Stream messages Excel: {excel_messages_path if output_excel else 'Not exported'}")
    print(f"Analysis Excel report: {excel_path}")
    
    return filtered_df

def main():
    # Use the hardcoded configuration by default
    stream_name = TARGET_STREAM
    display_messages = DISPLAY_MESSAGES
    output_excel = OUTPUT_EXCEL
    excel_file = EXCEL_FILE
    
    # # Also provide command-line options to override hardcoded values if needed
    # parser = argparse.ArgumentParser(description='Filter Zulip messages by stream name and analyze.')
    # parser.add_argument('--stream', help='Override the hardcoded stream name')
    # parser.add_argument('--file', help='Override the hardcoded Excel file name')
    # parser.add_argument('--list', action='store_true', help='List all available stream names')
    # parser.add_argument('--messages', action='store_true', help='Display individual messages in the stream')
    # parser.add_argument('--no-messages', action='store_true', help='Do not display individual messages')
    # parser.add_argument('--excel', action='store_true', help='Export messages to Excel file')
    # parser.add_argument('--no-excel', action='store_true', help='Do not export messages to Excel')
    
    # args = parser.parse_args()
    
    # # Override hardcoded values if command-line arguments are provided
    # if args.stream:
    #     stream_name = args.stream
    # if args.file:
    #     excel_file = args.file
    # if args.messages:
    #     display_messages = True
    # if args.no_messages:
    #     display_messages = False
    # if args.excel:
    #     output_excel = True
    # if args.no-excel:
    #     output_excel = False
    
    # if args.list:
    #     # Load data and show available streams
    #     script_dir = os.path.dirname(os.path.abspath(__file__))
    #     data_path = os.path.join(script_dir, excel_file)
    #     df = load_data(data_path)
    #     if df is None:
    #         print(f"Please ensure '{excel_file}' is in the same directory as this script.")
    #         return
        
    #     print("Available stream names:")
    #     for name in sorted(df['stream_name'].unique()):
    #         print(f"  - {name}")
    #     return
    
    # Proceed with analysis using either hardcoded values or command-line overrides
    print(f"Analyzing stream: {stream_name}")
    print(f"Using Excel file: {excel_file}")
    print(f"Display messages: {display_messages}")
    print(f"Export to Excel: {output_excel}")
    
    filter_by_stream(stream_name, excel_file, display_messages, output_excel)

if __name__ == "__main__":
    main()