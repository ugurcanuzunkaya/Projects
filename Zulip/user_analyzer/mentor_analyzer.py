import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pathlib import Path
import json
from collections import Counter
from analyzer_dashboard import load_data, analyze_sender_performance

def extract_mentor_data(df):
    """Extract data only for users with (Mentor) suffix in their name."""
    mentor_pattern = r'\(Mentor\)$'
    mentors = df[df['sender_full_name'].str.contains(mentor_pattern, regex=True)]
    print(f"Found {len(mentors['sender_full_name'].unique())} mentors in the dataset")
    return mentors

def create_mentor_visualizations(df_mentors, sender_stats, hour_activity, top_streams_by_sender, output_dir):
    """Create individual visualizations for each mentor."""
    mentors_dir = os.path.join(output_dir, "mentors")
    os.makedirs(mentors_dir, exist_ok=True)
    
    mentor_names = df_mentors['sender_full_name'].unique()
    visualization_paths = {}
    
    for mentor in mentor_names:
        mentor_dir = os.path.join(mentors_dir, mentor.replace(" ", "_").replace("(", "").replace(")", ""))
        os.makedirs(mentor_dir, exist_ok=True)
        
        # Create hour activity visualization for this mentor
        if mentor in hour_activity:
            plt.figure(figsize=(10, 6))
            hours = list(range(24))
            counts = [hour_activity[mentor].get(hour, 0) for hour in hours]
            plt.bar(hours, counts, color='steelblue')
            plt.title(f"{mentor}'s Activity by Hour")
            plt.xlabel("Hour of Day")
            plt.ylabel("Message Count")
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            hour_viz_path = os.path.join(mentor_dir, f"{mentor.replace(' ', '_')}_hour_activity.png")
            plt.savefig(hour_viz_path)
            plt.close()
            
            # Add to paths dictionary
            if mentor not in visualization_paths:
                visualization_paths[mentor] = []
            visualization_paths[mentor].append(hour_viz_path)
        
        # Create top streams visualization for this mentor
        if mentor in top_streams_by_sender and top_streams_by_sender[mentor]:
            plt.figure(figsize=(12, 7))
            # Get top 10 streams or fewer if less exist
            streams = dict(sorted(top_streams_by_sender[mentor].items(), 
                                  key=lambda x: x[1], reverse=True)[:10])
            
            # Handle longer stream names
            stream_names = list(streams.keys())
            if stream_names and max(len(name) for name in stream_names) > 15:
                plt.figure(figsize=(14, 7))  # Wider figure for longer names
            
            colors = plt.cm.viridis(np.linspace(0, 0.9, len(streams)))
            plt.bar(streams.keys(), streams.values(), color=colors)
            plt.title(f"{mentor}'s Top Streams")
            plt.xticks(rotation=45, ha='right')
            plt.ylabel("Message Count")
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            stream_viz_path = os.path.join(mentor_dir, f"{mentor.replace(' ', '_')}_top_streams.png")
            plt.savefig(stream_viz_path)
            plt.close()
            
            # Add to paths dictionary
            if mentor not in visualization_paths:
                visualization_paths[mentor] = []
            visualization_paths[mentor].append(stream_viz_path)
    
    return visualization_paths, mentors_dir

def create_mentor_comparison(mentors_df, mentor_stats, hour_activity, output_dir):
    """Create comparative visualizations for all mentors."""
    comparison_dir = os.path.join(output_dir, "mentor_comparisons")
    os.makedirs(comparison_dir, exist_ok=True)
    
    # Plot message count comparison
    plt.figure(figsize=(12, 8))
    mentor_message_counts = mentor_stats.sort_values('message_count', ascending=False)
    sns.barplot(x='message_count', y='sender_full_name', data=mentor_message_counts, 
                palette='viridis')
    plt.title('Message Count by Mentor')
    plt.xlabel('Number of Messages')
    plt.tight_layout()
    plt.savefig(os.path.join(comparison_dir, 'mentor_message_count.png'))
    plt.close()
    
    # Plot messages per day comparison
    plt.figure(figsize=(12, 8))
    mentor_activity = mentor_stats.sort_values('messages_per_day', ascending=False)
    sns.barplot(x='messages_per_day', y='sender_full_name', data=mentor_activity,
                palette='mako')
    plt.title('Messages per Day by Mentor')
    plt.xlabel('Average Messages per Day')
    plt.tight_layout()
    plt.savefig(os.path.join(comparison_dir, 'mentor_daily_activity.png'))
    plt.close()
    
    # Combined hour activity heatmap
    mentor_names = mentors_df['sender_full_name'].unique()
    
    if len(mentor_names) > 0:
        plt.figure(figsize=(14, 10))
        hour_data = []
        
        for mentor in mentor_names:
            if mentor in hour_activity:
                hours = list(range(24))
                counts = [hour_activity[mentor].get(hour, 0) for hour in hours]
                for hour, count in zip(hours, counts):
                    hour_data.append({
                        'Mentor': mentor,
                        'Hour': hour,
                        'Count': count
                    })
        
        if hour_data:
            hour_df = pd.DataFrame(hour_data)
            hour_pivot = hour_df.pivot(index='Mentor', columns='Hour', values='Count')
            hour_pivot = hour_pivot.fillna(0)
            
            plt.figure(figsize=(16, 10))
            sns.heatmap(hour_pivot, cmap="YlGnBu", annot=True, fmt=".0f", linewidths=.5)
            plt.title('Hourly Activity Comparison Among Mentors')
            plt.xlabel('Hour of Day')
            plt.ylabel('Mentor')
            plt.tight_layout()
            plt.savefig(os.path.join(comparison_dir, 'mentor_hour_activity_comparison.png'))
            plt.close()
    
    # Stream participation comparison - find common streams across mentors
    common_streams = {}
    for mentor in mentor_names:
        mentor_df = mentors_df[mentors_df['sender_full_name'] == mentor]
        streams = mentor_df['stream_name'].value_counts().to_dict()
        for stream, count in streams.items():
            if stream not in common_streams:
                common_streams[stream] = {}
            common_streams[stream][mentor] = count
    
    # Focus on streams that multiple mentors participate in
    multi_mentor_streams = {s: mentors for s, mentors in common_streams.items() 
                          if len(mentors) > 1}
    
    # Create visualization for top shared streams
    if multi_mentor_streams:
        top_shared_streams = sorted(multi_mentor_streams.items(), 
                                   key=lambda x: len(x[1]), reverse=True)[:10]
        
        # Prepare data for grouped bar chart
        stream_data = []
        for stream, mentors in top_shared_streams:
            for mentor, count in mentors.items():
                stream_data.append({
                    'Stream': stream,
                    'Mentor': mentor,
                    'Messages': count
                })
        
        if stream_data:
            stream_df = pd.DataFrame(stream_data)
            
            plt.figure(figsize=(16, 10))
            chart = sns.barplot(x='Stream', y='Messages', hue='Mentor', data=stream_df,
                              palette='tab10')
            plt.title('Mentor Participation in Shared Streams')
            plt.xticks(rotation=45, ha='right')
            plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.savefig(os.path.join(comparison_dir, 'mentor_stream_comparison.png'))
            plt.close()
    
    return comparison_dir

def export_mentor_excel(mentor_stats, top_streams_by_mentors, hour_activity, mentors_df, output_dir):
    """Export mentor data to a dedicated Excel file."""
    excel_path = os.path.join(output_dir, "mentor_analysis.xlsx")
    
    try:
        with pd.ExcelWriter(excel_path) as writer:
            # Format dates for better readability
            if 'first_message' in mentor_stats.columns and 'last_message' in mentor_stats.columns:
                mentor_stats['first_message'] = mentor_stats['first_message'].dt.strftime('%Y-%m-%d %H:%M')
                mentor_stats['last_message'] = mentor_stats['last_message'].dt.strftime('%Y-%m-%d %H:%M')
            
            # Round numeric columns
            for col in ['avg_message_length', 'active_days', 'messages_per_day']:
                if col in mentor_stats.columns:
                    mentor_stats[col] = mentor_stats[col].round(2)
            
            # Main stats sheet
            mentor_stats.to_excel(writer, index=False, sheet_name='Mentor Performance')
            
            # Stream activity sheet
            stream_data = []
            for mentor, streams in top_streams_by_mentors.items():
                for stream, count in streams.items():
                    stream_data.append({
                        'Mentor': mentor,
                        'Stream': stream,
                        'Message Count': count
                    })
            
            if stream_data:
                stream_df = pd.DataFrame(stream_data)
                stream_df.to_excel(writer, index=False, sheet_name='Stream Activity')
            
            # Hourly activity sheet
            hour_data = []
            for mentor, hours in hour_activity.items():
                if mentor in mentor_stats['sender_full_name'].values:  # Only include mentors
                    for hour, count in hours.items():
                        hour_data.append({
                            'Mentor': mentor,
                            'Hour': hour,
                            'Message Count': count
                        })
            
            if hour_data:
                hour_df = pd.DataFrame(hour_data)
                hour_df.to_excel(writer, index=False, sheet_name='Hourly Activity')
            
            # Daily activity sheet
            if 'parsed_date' in mentors_df.columns:
                daily = mentors_df.groupby([mentors_df['parsed_date'].dt.date, 'sender_full_name']).size().reset_index()
                daily.columns = ['Date', 'Mentor', 'Message Count']
                daily.to_excel(writer, index=False, sheet_name='Daily Activity')
        
        print(f"Mentor analysis exported to Excel: {excel_path}")
        return excel_path
    except Exception as e:
        print(f"Error exporting mentor data to Excel: {e}")
        return None

def analyze_mentors():
    """Main function for mentor analysis."""
    # Define paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "zulip_messages.xlsx")
    # Update output directory to match README structure (analysis_output/mentor_analysis)
    output_dir = os.path.join(script_dir, "analysis_output", "mentor_analysis")
    os.makedirs(output_dir, exist_ok=True)
    
    # Load data
    df = load_data(data_path)
    if df is None:
        print("Please ensure 'zulip_messages.xlsx' is in the same directory as this script.")
        return
    
    # Filter mentor data
    mentors_df = extract_mentor_data(df)
    if len(mentors_df) == 0:
        print("No mentors found in the dataset. Ensure mentor names end with '(Mentor)'.")
        return
    
    # Analyze mentor performance
    print("Analyzing mentor performance metrics...")
    mentor_stats, hour_activity, top_streams_by_sender = analyze_sender_performance(mentors_df)
    
    # Filter the analysis results to include only mentors
    mentor_names = mentors_df['sender_full_name'].unique()
    mentor_stats = mentor_stats[mentor_stats['sender_full_name'].isin(mentor_names)]
    
    # Filter hour_activity and top_streams_by_sender to include only mentors
    mentor_hour_activity = {k: v for k, v in hour_activity.items() if k in mentor_names}
    mentor_streams = {k: v for k, v in top_streams_by_sender.items() if k in mentor_names}
    
    # Create visualizations for each mentor
    print("Creating individual mentor visualizations...")
    viz_paths, mentors_dir = create_mentor_visualizations(
        mentors_df, mentor_stats, mentor_hour_activity, mentor_streams, output_dir
    )
    
    # Create comparative visualizations across all mentors
    print("Creating mentor comparison visualizations...")
    comparison_dir = create_mentor_comparison(mentors_df, mentor_stats, mentor_hour_activity, output_dir)
    
    # Export mentor data to Excel
    excel_path = export_mentor_excel(mentor_stats, mentor_streams, mentor_hour_activity, mentors_df, output_dir)
    
    print(f"\nMentor analysis complete!")
    print(f"Individual mentor visualizations: {mentors_dir}")
    print(f"Comparative visualizations: {comparison_dir}")
    print(f"Excel report: {excel_path}")

if __name__ == "__main__":
    analyze_mentors()