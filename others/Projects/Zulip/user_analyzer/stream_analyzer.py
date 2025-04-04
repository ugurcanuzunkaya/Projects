import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pathlib import Path
import json
from collections import Counter
from matplotlib.ticker import MaxNLocator
from analyzer_dashboard import load_data

def extract_mentor_streams(df, exclude_streams=None):
    """Extract data only for streams that start with 'mentor', excluding specified streams."""
    if exclude_streams is None:
        exclude_streams = []
        
    # Ensure exclude_streams is a list
    if isinstance(exclude_streams, str):
        exclude_streams = [exclude_streams]
    
    # Case insensitive match for streams starting with "mentor"
    mentor_pattern = '^[mM]entor'
    mentor_streams = df[df['stream_name'].str.contains(mentor_pattern, regex=True)]
    
    # Exclude specific streams
    if exclude_streams:
        print(f"Excluding specified streams: {', '.join(exclude_streams)}")
        for stream in exclude_streams:
            mentor_streams = mentor_streams[mentor_streams['stream_name'] != stream]
    
    mentor_stream_names = sorted(mentor_streams['stream_name'].unique())
    print(f"Found {len(mentor_stream_names)} mentor streams in the dataset (after exclusions):")
    for name in mentor_stream_names:
        print(f"  - {name}")
    
    return mentor_streams, mentor_stream_names

def analyze_mentor_stream_activity(df, mentor_streams, mentor_stream_names):
    """Analyze activity metrics for mentor streams."""
    print("Analyzing mentor stream activity metrics...")
    
    # Basic stream statistics
    mentor_stream_stats = mentor_streams.groupby('stream_name').agg(
        message_count=('message_id', 'count'),
        unique_senders=('sender_full_name', 'nunique'),
        topic_count=('topic', lambda x: len(set(x))),
        first_message=('datetime', 'min'),
        last_message=('datetime', 'max')
    ).reset_index()
    
    # Calculate active period in days
    mentor_stream_stats['active_days'] = (mentor_stream_stats['last_message'] - mentor_stream_stats['first_message']).dt.total_seconds() / (60 * 60 * 24)
    mentor_stream_stats['active_days'] = mentor_stream_stats['active_days'].apply(lambda x: max(1, x))  # Minimum 1 day
    
    # Calculate messages per day
    mentor_stream_stats['messages_per_day'] = mentor_stream_stats['message_count'] / mentor_stream_stats['active_days']
    
    # Get participants with mentor role
    mentor_participants = df[df['sender_full_name'].str.contains(r'\(Mentor\)$', regex=True)]['sender_full_name'].unique()
    
    # Analyze top contributors for each mentor stream
    top_contributors = {}
    mentor_participation = {}
    
    for stream in mentor_stream_names:
        stream_df = mentor_streams[mentor_streams['stream_name'] == stream]
        total_messages = stream_df.shape[0]
        
        # Get contributor counts
        contributors = stream_df['sender_full_name'].value_counts().to_dict()
        
        # Calculate percentage contribution for top contributors
        formatted_contributors = {}
        for contributor, count in contributors.items():
            is_mentor = "(Mentor)" in contributor
            formatted_contributors[contributor] = {
                'count': count,
                'percentage': round(count / total_messages * 100, 2),
                'is_mentor': is_mentor
            }
        
        # Store top 10 contributors for this stream
        top_contributors[stream] = dict(sorted(formatted_contributors.items(), 
                                             key=lambda x: x[1]['count'], 
                                             reverse=True)[:10])
        
        # Calculate mentor vs non-mentor participation
        mentor_msgs = stream_df[stream_df['sender_full_name'].str.contains(r'\(Mentor\)$', regex=True)].shape[0]
        mentor_participation[stream] = {
            'mentor_messages': mentor_msgs,
            'total_messages': total_messages,
            'mentor_percentage': round(mentor_msgs / total_messages * 100 if total_messages > 0 else 0, 2),
            'non_mentor_messages': total_messages - mentor_msgs,
            'non_mentor_percentage': round((total_messages - mentor_msgs) / total_messages * 100 if total_messages > 0 else 0, 2)
        }
    
    return mentor_stream_stats, top_contributors, mentor_participation

def create_mentor_stream_visualizations(mentor_stream_stats, top_contributors, mentor_participation, output_dir):
    """Create visualizations for mentor stream analysis, sorted in descending order."""
    vis_dir = os.path.join(output_dir, "mentor_stream_visualizations")
    os.makedirs(vis_dir, exist_ok=True)
    
    # 1. Plot mentor streams by message count (descending order)
    plt.figure(figsize=(14, 10))
    sorted_streams = mentor_stream_stats.sort_values('message_count', ascending=False)
    ax = sns.barplot(x='message_count', y='stream_name', data=sorted_streams, palette='viridis')
    plt.title('Mentor Streams by Message Count', fontsize=16)
    plt.xlabel('Number of Messages', fontsize=12)
    plt.ylabel('Stream Name', fontsize=12)
    
    # Add value labels to the bars
    for i, v in enumerate(sorted_streams['message_count']):
        ax.text(v + 0.1, i, str(v), va='center')
    
    plt.tight_layout()
    msg_count_path = os.path.join(vis_dir, 'mentor_streams_by_message_count.png')
    plt.savefig(msg_count_path)
    plt.close()
    
    # 2. Plot mentor streams by unique participants (descending order)
    plt.figure(figsize=(14, 10))
    participant_streams = mentor_stream_stats.sort_values('unique_senders', ascending=False)
    ax = sns.barplot(x='unique_senders', y='stream_name', data=participant_streams, palette='mako')
    plt.title('Mentor Streams by Number of Unique Participants', fontsize=16)
    plt.xlabel('Number of Unique Participants', fontsize=12)
    plt.ylabel('Stream Name', fontsize=12)
    
    # Add value labels to the bars
    for i, v in enumerate(participant_streams['unique_senders']):
        ax.text(v + 0.1, i, str(v), va='center')
    
    plt.tight_layout()
    participants_path = os.path.join(vis_dir, 'mentor_streams_by_participant_count.png')
    plt.savefig(participants_path)
    plt.close()
    
    # 3. Create mentor participation percentage visualization (descending order)
    plt.figure(figsize=(14, 10))
    
    # Sort data by mentor percentage in descending order
    sorted_participation = dict(sorted(mentor_participation.items(), 
                                      key=lambda x: x[1]['mentor_percentage'], 
                                      reverse=True))
    
    streams = []
    percentages = []
    
    for stream, data in sorted_participation.items():
        streams.append(stream)
        percentages.append(data['mentor_percentage'])
    
    # Create bar chart with percentage mentors vs non-mentors
    bars = plt.barh(streams, percentages, color='darkgreen', alpha=0.7)
    plt.title('Mentor Participation Percentage in Mentor Streams', fontsize=16)
    plt.xlabel('Percentage of Messages from Mentors (%)', fontsize=12)
    plt.xlim(0, 100)
    
    # Add percentage labels on bars
    for i, bar in enumerate(bars):
        width = bar.get_width()
        plt.text(width + 1, i, f'{percentages[i]:.1f}%', va='center')
    
    plt.tight_layout()
    mentor_pct_path = os.path.join(vis_dir, 'mentor_participation_percentage.png')
    plt.savefig(mentor_pct_path)
    plt.close()
    
    # 4. Create stacked bar chart showing mentor vs non-mentor message counts (descending by total)
    plt.figure(figsize=(14, 10))
    
    # Sort by total messages in descending order
    sorted_by_total = dict(sorted(mentor_participation.items(), 
                                 key=lambda x: x[1]['total_messages'], 
                                 reverse=True))
    
    stream_names = []
    mentor_counts = []
    non_mentor_counts = []
    
    for stream, data in sorted_by_total.items():
        stream_names.append(stream)
        mentor_counts.append(data['mentor_messages'])
        non_mentor_counts.append(data['non_mentor_messages'])
    
    # Create stacked bars
    plt.barh(stream_names, non_mentor_counts, color='skyblue', alpha=0.8, label='Non-Mentor Messages')
    plt.barh(stream_names, mentor_counts, left=non_mentor_counts, color='darkgreen', alpha=0.8, label='Mentor Messages')
    
    plt.title('Message Distribution in Mentor Streams', fontsize=16)
    plt.xlabel('Number of Messages', fontsize=12)
    plt.legend(loc='lower right')
    
    # Add total message count labels
    for i, stream in enumerate(stream_names):
        total = mentor_participation[stream]['total_messages']
        plt.text(total + 5, i, str(total), va='center')
    
    plt.tight_layout()
    distribution_path = os.path.join(vis_dir, 'mentor_message_distribution.png')
    plt.savefig(distribution_path)
    plt.close()
    
    # 5. Create individual visualizations for each mentor stream
    for stream, contributors in top_contributors.items():
        # Create a directory for each stream
        stream_dir = os.path.join(vis_dir, stream.replace(' ', '_').replace('/', '_'))
        os.makedirs(stream_dir, exist_ok=True)
        
        # Extract names, counts and mentor status
        names = list(contributors.keys())
        counts = [contributor['count'] for contributor in contributors.values()]
        is_mentor = [contributor['is_mentor'] for contributor in contributors.values()]
        
        # Sort by count in descending order
        sorted_data = sorted(zip(names, counts, is_mentor), key=lambda x: x[1], reverse=True)
        sorted_names, sorted_counts, sorted_is_mentor = zip(*sorted_data)
        
        # Define colors based on mentor status
        colors = ['darkgreen' if mentor else 'steelblue' for mentor in sorted_is_mentor]
        
        # Create contributor visualization
        plt.figure(figsize=(14, 8))
        bars = plt.bar(sorted_names, sorted_counts, color=colors)
        plt.title(f'Top Contributors in {stream}', fontsize=14)
        plt.ylabel('Message Count', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        
        # Add legend
        mentor_patch = plt.Rectangle((0, 0), 1, 1, color='darkgreen')
        non_mentor_patch = plt.Rectangle((0, 0), 1, 1, color='steelblue')
        plt.legend([mentor_patch, non_mentor_patch], ['Mentor', 'Non-Mentor'], loc='upper right')
        
        # Add count labels on top of bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{int(height)}', ha='center', va='bottom')
        
        plt.tight_layout()
        contrib_path = os.path.join(stream_dir, f'{stream.replace(" ", "_")}_contributors.png')
        plt.savefig(contrib_path)
        plt.close()
        
        # Create percentage contribution visualization (already sorted in descending order above)
        plt.figure(figsize=(14, 8))
        percentages = [contributor['percentage'] for contributor in contributors.values()]
        
        # Use the same sorting as for the counts (already in descending order)
        
        bars = plt.bar(sorted_names, percentages, color=colors)
        plt.title(f'Contribution Percentage in {stream}', fontsize=14)
        plt.ylabel('Percentage of Messages (%)', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        
        # Add legend
        plt.legend([mentor_patch, non_mentor_patch], ['Mentor', 'Non-Mentor'], loc='upper right')
        
        # Add percentage labels on bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{height:.1f}%', ha='center', va='bottom')
        
        plt.tight_layout()
        pct_path = os.path.join(stream_dir, f'{stream.replace(" ", "_")}_percentages.png')
        plt.savefig(pct_path)
        plt.close()
    
    return vis_dir


def export_mentor_stream_excel(mentor_stream_stats, top_contributors, mentor_participation, mentor_streams, output_dir):
    """Export mentor stream analysis to Excel format with sorted data."""
    excel_path = os.path.join(output_dir, "mentor_stream_analysis.xlsx")
    
    try:
        with pd.ExcelWriter(excel_path) as writer:
            # Format dates for better readability
            if 'first_message' in mentor_stream_stats.columns and 'last_message' in mentor_stream_stats.columns:
                mentor_stream_stats['first_message'] = mentor_stream_stats['first_message'].dt.strftime('%Y-%m-%d %H:%M')
                mentor_stream_stats['last_message'] = mentor_stream_stats['last_message'].dt.strftime('%Y-%m-%d %H:%M')
            
            # Round numeric columns for better readability
            for col in ['active_days', 'messages_per_day']:
                if col in mentor_stream_stats.columns:
                    mentor_stream_stats[col] = mentor_stream_stats[col].round(2)
            
            # Sort by message count for main sheet (descending)
            stream_stats_sorted = mentor_stream_stats.sort_values('message_count', ascending=False)
            stream_stats_sorted.to_excel(writer, index=False, sheet_name='Stream Overview')
            
            # Mentor participation sheet (sorted by mentor percentage descending)
            participation_data = []
            for stream, data in mentor_participation.items():
                participation_data.append({
                    'Stream': stream,
                    'Total Messages': data['total_messages'],
                    'Mentor Messages': data['mentor_messages'],
                    'Mentor Percentage': data['mentor_percentage'],
                    'Non-Mentor Messages': data['non_mentor_messages'],
                    'Non-Mentor Percentage': data['non_mentor_percentage']
                })
            
            if participation_data:
                participation_df = pd.DataFrame(participation_data)
                participation_df_sorted = participation_df.sort_values('Mentor Percentage', ascending=False)
                participation_df_sorted.to_excel(writer, index=False, sheet_name='Mentor Participation')
            
            # Top contributors sheet (sorted by message count descending within each stream)
            contributors_data = []
            for stream, contributors in top_contributors.items():
                for contributor, data in contributors.items():
                    contributors_data.append({
                        'Stream': stream,
                        'Contributor': contributor,
                        'Is Mentor': data['is_mentor'],
                        'Message Count': data['count'],
                        'Percentage': data['percentage']
                    })
            
            if contributors_data:
                contributors_df = pd.DataFrame(contributors_data)
                contributors_df_sorted = contributors_df.sort_values(['Stream', 'Message Count'], ascending=[True, False])
                contributors_df_sorted.to_excel(writer, index=False, sheet_name='Top Contributors')
            
            # Topics by stream sheet (sorted by message count descending within each stream)
            topics_data = []
            for stream in mentor_stream_stats['stream_name']:
                stream_df = mentor_streams[mentor_streams['stream_name'] == stream]
                topic_counts = stream_df['topic'].value_counts()
                
                for topic, count in topic_counts.items():
                    topics_data.append({
                        'Stream': stream,
                        'Topic': topic,
                        'Message Count': count
                    })
            
            if topics_data:
                topics_df = pd.DataFrame(topics_data)
                topics_df_sorted = topics_df.sort_values(['Stream', 'Message Count'], ascending=[True, False])
                topics_df_sorted.to_excel(writer, index=False, sheet_name='Stream Topics')
            
            # Activity timeline (sorted by date within each stream)
            if 'datetime' in mentor_streams.columns:
                mentor_streams['date'] = mentor_streams['datetime'].dt.date
                
                # Daily activity by stream
                daily_activity = mentor_streams.groupby(['stream_name', 'date']).size().reset_index(name='message_count')
                daily_activity_sorted = daily_activity.sort_values(['stream_name', 'date'])
                daily_activity_sorted.to_excel(writer, index=False, sheet_name='Daily Activity')
                
                # Mentor vs non-mentor daily activity
                mentor_daily = mentor_streams[mentor_streams['sender_full_name'].str.contains(r'\(Mentor\)$', regex=True)] \
                    .groupby(['stream_name', 'date']).size().reset_index(name='mentor_messages')
                
                # Merge with overall daily activity
                merged_daily = daily_activity.merge(mentor_daily, on=['stream_name', 'date'], how='left')
                merged_daily['mentor_messages'] = merged_daily['mentor_messages'].fillna(0).astype(int)
                merged_daily['non_mentor_messages'] = merged_daily['message_count'] - merged_daily['mentor_messages']
                merged_daily['mentor_percentage'] = (merged_daily['mentor_messages'] / merged_daily['message_count'] * 100).round(2)
                
                merged_daily_sorted = merged_daily.sort_values(['stream_name', 'date'])
                merged_daily_sorted.to_excel(writer, index=False, sheet_name='Daily Mentor Activity')
        
        print(f"Mentor stream analysis exported to Excel: {excel_path}")
        return excel_path
    except Exception as e:
        print(f"Error exporting mentor stream data to Excel: {e}")
        return None

def analyze_mentor_streams():
    """Main function for mentor stream analysis with exclusion."""
    # Define paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "zulip_messages.xlsx")
    output_dir = os.path.join(script_dir, "mentor_stream_analysis")
    os.makedirs(output_dir, exist_ok=True)
    
    # Define streams to exclude
    exclude_streams = ["mentor-21-222222"]
    
    # Load data
    df = load_data(data_path)
    if df is None:
        print("Please ensure 'zulip_messages.xlsx' is in the same directory as this script.")
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
    
    # Extract and filter mentor streams, excluding specified streams
    print("Extracting mentor streams...")
    mentor_streams, mentor_stream_names = extract_mentor_streams(df, exclude_streams)
    
    if len(mentor_streams) == 0:
        print("No suitable mentor streams found in the dataset after applying exclusions.")
        return
    
    # Analyze mentor stream activity
    print("Analyzing mentor stream activity...")
    mentor_stream_stats, top_contributors, mentor_participation = analyze_mentor_stream_activity(
        df, mentor_streams, mentor_stream_names
    )
    
    # Create visualizations
    print("Creating mentor stream visualizations...")
    vis_dir = create_mentor_stream_visualizations(
        mentor_stream_stats, top_contributors, mentor_participation, output_dir
    )
    
    # Export to Excel
    excel_path = export_mentor_stream_excel(
        mentor_stream_stats, top_contributors, mentor_participation, mentor_streams, output_dir
    )
    
    print(f"\nMentor stream analysis complete!")
    print(f"Excluded streams: {', '.join(exclude_streams)}")
    print(f"Visualizations directory: {vis_dir}")
    print(f"Excel report: {excel_path}")

if __name__ == "__main__":
    analyze_mentor_streams()