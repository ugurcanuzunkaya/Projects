import pandas as pd
import os
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
from collections import Counter
import seaborn as sns
from pathlib import Path
import json

def load_data(file_path):
    """Load the Excel data file."""
    try:
        df = pd.read_excel(file_path)
        print(f"Successfully loaded data with {len(df)} records")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def analyze_sender_performance(df):
    """Analyze sender performance metrics."""
    # Process date column (expected format: YYYY-MM-DD)
    if 'date' in df.columns:
        print("Processing date column...")
        try:
            df['parsed_date'] = pd.to_datetime(df['date'], format='%Y-%m-%d', errors='coerce')
            print(f"Processed {df['parsed_date'].notna().sum()} valid dates")
        except Exception as e:
            print(f"Error parsing dates: {e}")
            df['parsed_date'] = pd.NaT
    else:
        print("Warning: No 'date' column found in the data")
        df['parsed_date'] = pd.NaT
    
    # Process time column (expected format: HH:MM:SS)
    if 'time' in df.columns:
        print("Processing time column...")
        try:
            df['parsed_time'] = pd.to_datetime(df['time'], format='%H:%M:%S', errors='coerce').dt.time
            print(f"Processed {df['parsed_time'].notna().sum()} valid times")
        except Exception as e:
            print(f"Error parsing times: {e}")
            df['parsed_time'] = None
    else:
        print("Warning: No 'time' column found in the data")
        df['parsed_time'] = None
    
    # Create complete datetime from parsed date and time
    valid_dates = df['parsed_date'].notna()
    df['datetime'] = pd.NaT  # Initialize with NaT
    
    # Only combine for rows with valid dates
    if 'parsed_time' in df.columns and 'parsed_date' in df.columns:
        for i in df.index[valid_dates]:
            if pd.notna(df.loc[i, 'parsed_date']) and df.loc[i, 'parsed_time'] is not None:
                try:
                    date_part = df.loc[i, 'parsed_date']
                    time_part = df.loc[i, 'parsed_time']
                    df.loc[i, 'datetime'] = pd.Timestamp.combine(
                        date_part.date(), time_part
                    )
                except Exception:
                    continue
    
    # Count valid datetime entries
    valid_dt_count = df['datetime'].notna().sum()
    print(f"Created {valid_dt_count} valid datetime entries ({valid_dt_count/len(df)*100:.1f}% of data)")
    
    # For analysis purposes, fill any missing datetimes with timestamp if available
    if 'timestamp' in df.columns and df['datetime'].isna().any():
        missing_dt = df['datetime'].isna()
        df.loc[missing_dt, 'datetime'] = pd.to_datetime(df.loc[missing_dt, 'timestamp'], errors='coerce')
        print(f"Used timestamp as fallback for {missing_dt.sum()} entries")
    
    # Basic message count per sender
    sender_stats = df.groupby('sender_full_name').agg(
        message_count=('message_id', 'count'),
        first_message=('datetime', 'min'),
        last_message=('datetime', 'max'),
        avg_message_length=('content', lambda x: np.mean([len(str(msg)) for msg in x])),
        topic_count=('topic', lambda x: len(set(x))),
        stream_count=('stream_name', lambda x: len(set(x))),
        reaction_count=('reactions', lambda x: sum(1 for r in x if r and r == r))
    ).reset_index()
    
    # Get top 10 streams for each sender
    top_streams_by_sender = {}
    for sender in df['sender_full_name'].unique():
        sender_df = df[df['sender_full_name'] == sender]
        stream_counts = sender_df['stream_name'].value_counts().head(10).to_dict()
        top_streams_by_sender[sender] = stream_counts
    
    # Add top streams as a JSON column to sender_stats
    sender_stats['top_streams'] = sender_stats['sender_full_name'].map(
        lambda sender: json.dumps(top_streams_by_sender.get(sender, {}))
    )
    
    # Calculate active period in days using datetime
    sender_stats['active_days'] = (sender_stats['last_message'] - sender_stats['first_message']).dt.total_seconds() / (60 * 60 * 24)
    sender_stats['active_days'] = sender_stats['active_days'].apply(lambda x: max(1, x))  # Minimum 1 day
    
    # Calculate messages per day
    sender_stats['messages_per_day'] = sender_stats['message_count'] / sender_stats['active_days']
    
    # Calculate hour of day from parsed_time for hourly activity analysis
    hour_activity = {}
    for sender in df['sender_full_name'].unique():
        sender_df = df[df['sender_full_name'] == sender]
        
        # Extract hours directly from the parsed_time column
        hours = []
        for t in sender_df['parsed_time'].dropna():
            if t is not None and hasattr(t, 'hour'):
                hours.append(t.hour)
        
        # Use datetime as fallback if needed
        if not hours and 'datetime' in sender_df.columns:
            datetime_hours = sender_df['datetime'].dt.hour.dropna()
            hours = list(datetime_hours)
            
        hour_activity[sender] = dict(Counter(hours))
    
    # Determine peak activity hours
    peak_hours = {}
    for sender, hours in hour_activity.items():
        if hours:  # Make sure there's data
            peak_hour = max(hours.items(), key=lambda x: x[1])[0]
            peak_hours[sender] = peak_hour
    
    sender_stats['peak_hour'] = sender_stats['sender_full_name'].map(peak_hours)
    
    # Calculate day of week from parsed_date
    day_activity = {}
    for sender in df['sender_full_name'].unique():
        sender_df = df[df['sender_full_name'] == sender]
        if 'parsed_date' in sender_df.columns:
            days = sender_df['parsed_date'].dt.day_name().dropna()
            day_activity[sender] = dict(Counter(days))
    
    # Find most active day for each sender
    peak_days = {}
    for sender, days in day_activity.items():
        if days:
            peak_day = max(days.items(), key=lambda x: x[1])[0]
            peak_days[sender] = peak_day
    
    sender_stats['peak_day'] = sender_stats['sender_full_name'].map(peak_days)
    
    return sender_stats, hour_activity, top_streams_by_sender

def create_visualizations(sender_stats, hour_activity, output_dir):
    """Create visualizations for the analysis."""
    os.makedirs(output_dir, exist_ok=True)
    
    # Plot message count per user (top 15)
    plt.figure(figsize=(12, 8))
    top_senders = sender_stats.sort_values('message_count', ascending=False).head(15)
    sns.barplot(x='message_count', y='sender_full_name', data=top_senders)
    plt.title('Message Count by User (Top 15)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'message_count.png'))
    
    # Plot messages per day
    plt.figure(figsize=(12, 8))
    top_active = sender_stats.sort_values('messages_per_day', ascending=False).head(15)
    sns.barplot(x='messages_per_day', y='sender_full_name', data=top_active)
    plt.title('Messages per Day by User (Top 15)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'messages_per_day.png'))
    
    # Plot time distribution for top 5 users
    plt.figure(figsize=(15, 10))
    top_5_users = sender_stats.sort_values('message_count', ascending=False).head(5)['sender_full_name'].tolist()
    
    for i, user in enumerate(top_5_users):
        if user in hour_activity:
            hours = list(range(24))
            counts = [hour_activity[user].get(hour, 0) for hour in hours]
            plt.subplot(2, 3, i+1)
            plt.bar(hours, counts)
            plt.title(f"{user}'s Activity by Hour")
            plt.xlabel("Hour of Day")
            plt.ylabel("Message Count")
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'hour_activity.png'))
    
    return [
        os.path.join(output_dir, 'message_count.png'),
        os.path.join(output_dir, 'messages_per_day.png'),
        os.path.join(output_dir, 'hour_activity.png')
    ]

def export_to_excel(sender_stats, file_path, top_streams_by_sender, df):
    """Export results to Excel format."""
    try:
        # Format dates for better readability
        sender_stats['first_message'] = sender_stats['first_message'].dt.strftime('%Y-%m-%d %H:%M')
        sender_stats['last_message'] = sender_stats['last_message'].dt.strftime('%Y-%m-%d %H:%M')
        
        # Round numeric columns for better readability
        for col in ['avg_message_length', 'active_days', 'messages_per_day']:
            sender_stats[col] = sender_stats[col].round(2)
        
        # Add rank columns
        sender_stats['message_count_rank'] = sender_stats['message_count'].rank(ascending=False).astype(int)
        sender_stats['activity_rank'] = sender_stats['messages_per_day'].rank(ascending=False).astype(int)
        
        # Reorder columns for better presentation
        columns_order = [
            'sender_full_name', 'message_count', 'message_count_rank',
            'messages_per_day', 'activity_rank', 'avg_message_length',
            'topic_count', 'stream_count', 'reaction_count',
            'peak_hour', 'peak_day', 'active_days', 'first_message', 'last_message', 'top_streams'
        ]
        
        columns_order = [col for col in columns_order if col in sender_stats.columns]
        sender_stats = sender_stats[columns_order]
        
        # Create a writer to output multiple sheets
        with pd.ExcelWriter(file_path) as writer:
            # Export main stats to the first sheet
            sender_stats.to_excel(writer, index=False, sheet_name='User Performance')
            
            # Create a new sheet for detailed stream analysis
            stream_data = []
            for sender, streams in top_streams_by_sender.items():
                for stream, count in streams.items():
                    stream_data.append({
                        'sender_full_name': sender,
                        'stream_name': stream,
                        'message_count': count
                    })
            
            if stream_data:
                stream_df = pd.DataFrame(stream_data)
                stream_df.to_excel(writer, index=False, sheet_name='Top Streams by User')
            
            # Add daily activity sheet (aggregated by parsed_date)
            if 'parsed_date' in df.columns:
                daily_activity = df.groupby([df['parsed_date'].dt.date, 'sender_full_name']).size().reset_index()
                daily_activity.columns = ['date', 'sender_full_name', 'message_count']
                daily_activity.to_excel(writer, index=False, sheet_name='Daily Activity')
            
            # Add time analysis sheet showing activity by hour
            hourly_summary = pd.DataFrame(columns=['hour', 'message_count'])
            if 'parsed_time' in df.columns:
                hour_counts = df['parsed_time'].dropna().apply(lambda x: x.hour if hasattr(x, 'hour') else None).value_counts().sort_index()
                hourly_summary = pd.DataFrame({
                    'hour': hour_counts.index,
                    'message_count': hour_counts.values
                })
                hourly_summary.to_excel(writer, index=False, sheet_name='Hour Summary')
        
        print(f"Results exported to Excel: {file_path}")
        return True
    except Exception as e:
        print(f"Error exporting to Excel: {e}")
        return False

def main():
    # Define paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "zulip_messages.xlsx")  # Assuming Excel file name
    output_dir = os.path.join(script_dir, "analysis_output")
    os.makedirs(output_dir, exist_ok=True)
    
    # Load data
    df = load_data(data_path)
    if df is None:
        print("Please ensure 'zulip_messages.xlsx' is in the same directory as this script.")
        return
    
    # Add additional analysis by day of week using parsed_date
    if 'date' in df.columns:
        print("Adding day of week analysis...")
        parsed_dates = pd.to_datetime(df['date'], errors='coerce')
        day_of_week = parsed_dates.dt.day_name()
        
        # Create day of week visualization
        plt.figure(figsize=(10, 6))
        day_counts = day_of_week.value_counts().reindex([
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
        ])
        sns.barplot(x=day_counts.index, y=day_counts.values)
        plt.title('Message Activity by Day of Week')
        plt.tight_layout()
        day_viz_path = os.path.join(output_dir, 'day_of_week_activity.png')
        plt.savefig(day_viz_path)
    
    # Analyze data
    print("Analyzing sender performance metrics...")
    sender_stats, hour_activity, top_streams_by_sender = analyze_sender_performance(df)
    
    # Create visualizations
    print("Creating visualizations...")
    # Create visualizations directory if it doesn't exist
    viz_dir = os.path.join(output_dir, 'visualizations')
    os.makedirs(viz_dir, exist_ok=True)
    
    # Update visualization paths to use the 'visualizations' subdirectory
    image_paths = create_visualizations(sender_stats, hour_activity, viz_dir)
    
    # Add additional visualization for top streams
    print("Creating stream activity visualizations...")
    plt.figure(figsize=(14, 10))
    
    # Get top 5 users by message count
    top_5_users = sender_stats.sort_values('message_count', ascending=False).head(5)['sender_full_name'].tolist()
    
    for i, user in enumerate(top_5_users):
        if user in top_streams_by_sender and top_streams_by_sender[user]:
            plt.subplot(2, 3, i+1)
            
            # Get top 5 streams for visualization clarity
            streams = dict(sorted(top_streams_by_sender[user].items(), key=lambda x: x[1], reverse=True)[:5])
            
            plt.bar(streams.keys(), streams.values())
            plt.title(f"{user}'s Top Streams")
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
    
    stream_viz_path = os.path.join(viz_dir, 'top_active_streams.png')
    plt.savefig(stream_viz_path)
    image_paths.append(stream_viz_path)
    
    # Create subdirectories for other analyses mentioned in the README
    os.makedirs(os.path.join(output_dir, 'mentor_analysis'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'community_leader_analysis'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'mentor_stream_analysis'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'mentor_impact_analysis'), exist_ok=True)
    
    # Export results to Excel only (no markdown)
    excel_path = os.path.join(output_dir, "user_performance_analysis.xlsx")
    export_to_excel(sender_stats, excel_path, top_streams_by_sender, df)
    
    print(f"\nAnalysis complete! Results saved to '{output_dir}'")
    print(f"Excel report: {excel_path}")
    print(f"Visualizations saved to '{viz_dir}'")
    print("\nTo perform additional analyses, you can run:")
    print(" - mentor_analyzer.py for mentor-specific analysis")
    print(" - lead_analyzer.py for community leader analysis")
    print(" - stream_analyzer.py for stream-specific analysis")
    print(" - mentor_stream_impact.py for mentor impact analysis")

if __name__ == "__main__":
    main()
