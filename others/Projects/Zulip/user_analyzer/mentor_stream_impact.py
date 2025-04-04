import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pathlib import Path
import json
from collections import Counter
from analyzer_dashboard import load_data

def extract_mentor_data(df):
    """Extract data only for users with (Mentor) suffix in their name."""
    mentor_pattern = r'\(Mentor\)$'
    mentors = df[df['sender_full_name'].str.contains(mentor_pattern, regex=True)]
    mentor_names = mentors['sender_full_name'].unique()
    print(f"Found {len(mentor_names)} mentors in the dataset:")
    for name in mentor_names:
        print(f"  - {name}")
    return mentors, mentor_names

def analyze_mentor_stream_impact(df, mentors_df, mentor_names):
    """Analyze each mentor's impact on their top 5 streams."""
    
    # Calculate total message count for each stream
    stream_totals = df.groupby('stream_name').size().to_dict()
    
    # Store results for each mentor
    mentor_stream_impact = {}
    
    for mentor in mentor_names:
        # Get this mentor's messages
        mentor_msgs = mentors_df[mentors_df['sender_full_name'] == mentor]
        
        # Get their stream participation
        mentor_streams = mentor_msgs.groupby('stream_name').size().to_dict()
        
        # Calculate impact percentage
        stream_impact = {}
        for stream, count in mentor_streams.items():
            if stream in stream_totals and stream_totals[stream] > 0:
                percentage = (count / stream_totals[stream]) * 100
                stream_impact[stream] = {
                    'mentor_messages': count,
                    'total_messages': stream_totals[stream],
                    'percentage': percentage
                }
        
        # Sort by mentor's message count in each stream
        sorted_impact = {k: v for k, v in sorted(
            stream_impact.items(), 
            key=lambda item: item[1]['mentor_messages'], 
            reverse=True
        )}
        
        # Store top 5 streams for this mentor
        mentor_stream_impact[mentor] = {
            'top_streams': dict(list(sorted_impact.items())[:5]),
            'total_messages': len(mentor_msgs),
            'stream_count': len(mentor_streams)
        }
    
    return mentor_stream_impact, stream_totals

def create_mentor_impact_visualizations(mentor_stream_impact, output_dir):
    """Create visualizations showing mentor impact on streams."""
    vis_dir = os.path.join(output_dir, "mentor_stream_impact")
    os.makedirs(vis_dir, exist_ok=True)
    
    # Individual mentor visualizations
    for mentor, data in mentor_stream_impact.items():
        if not data['top_streams']:
            continue
            
        # Create sanitized mentor name for files
        mentor_file = mentor.replace(' ', '_').replace('(', '').replace(')', '')
        
        # Extract top 5 streams and their metrics
        streams = list(data['top_streams'].keys())
        message_counts = [d['mentor_messages'] for d in data['top_streams'].values()]
        percentages = [d['percentage'] for d in data['top_streams'].values()]
        
        # Create a figure with two subplots side by side
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))
        
        # Plot 1: Message counts in top streams
        colors1 = plt.cm.viridis(np.linspace(0, 0.9, len(streams)))
        bars1 = ax1.bar(streams, message_counts, color=colors1)
        ax1.set_title(f"{mentor}'s Top 5 Streams by Message Count", fontsize=14)
        ax1.set_ylabel("Number of Messages", fontsize=12)
        ax1.set_xticklabels(streams, rotation=45, ha='right')
        
        # Add value labels on the bars
        for bar in bars1:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{int(height)}', ha='center', va='bottom')
        
        # Plot 2: Impact percentage in those streams
        colors2 = plt.cm.plasma(np.linspace(0, 0.9, len(streams)))
        bars2 = ax2.bar(streams, percentages, color=colors2)
        ax2.set_title(f"{mentor}'s Impact Percentage in Top Streams", fontsize=14)
        ax2.set_ylabel("Percentage of Stream Messages (%)", fontsize=12)
        ax2.set_xticklabels(streams, rotation=45, ha='right')
        
        # Add percentage labels on the bars
        for bar in bars2:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{height:.2f}%', ha='center', va='bottom')
        
        plt.tight_layout()
        plt.savefig(os.path.join(vis_dir, f"{mentor_file}_stream_impact.png"))
        plt.close()
    
    # Create comparative visualization across all mentors
    # Find streams that have multiple mentors participating
    stream_to_mentors = {}
    for mentor, data in mentor_stream_impact.items():
        for stream in data['top_streams'].keys():
            if stream not in stream_to_mentors:
                stream_to_mentors[stream] = []
            stream_to_mentors[stream].append(mentor)
    
    # Filter to streams with multiple mentors
    shared_streams = {stream: mentors for stream, mentors in stream_to_mentors.items() 
                     if len(mentors) > 1}
    
    if shared_streams:
        # Prepare data for visualization
        top_shared_streams = sorted(shared_streams.items(), 
                                    key=lambda x: len(x[1]), 
                                    reverse=True)[:7]  # Top 7 shared streams
        
        # Create visualization for each shared stream
        for stream, stream_mentors in top_shared_streams:
            plt.figure(figsize=(12, 7))
            
            # Get data for each mentor in this stream
            mentor_percentages = []
            mentor_messages = []
            
            for mentor in stream_mentors:
                if stream in mentor_stream_impact[mentor]['top_streams']:
                    data = mentor_stream_impact[mentor]['top_streams'][stream]
                    mentor_percentages.append(data['percentage'])
                    mentor_messages.append(data['mentor_messages'])
                else:
                    mentor_percentages.append(0)
                    mentor_messages.append(0)
            
            # Sort both lists based on message count
            sorted_data = sorted(zip(stream_mentors, mentor_messages, mentor_percentages),
                               key=lambda x: x[1], reverse=True)
            sorted_mentors, sorted_messages, sorted_percentages = zip(*sorted_data)
            
            # Plot the data
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
            
            # Message count plot
            bars1 = ax1.bar(sorted_mentors, sorted_messages, color='steelblue')
            ax1.set_title(f"Mentor Message Count in '{stream}'", fontsize=14)
            ax1.set_ylabel("Number of Messages", fontsize=12)
            ax1.set_xticklabels(sorted_mentors, rotation=45, ha='right')
            
            # Add value labels
            for bar in bars1:
                height = bar.get_height()
                ax1.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                        f'{int(height)}', ha='center', va='bottom')
            
            # Percentage impact plot
            bars2 = ax2.bar(sorted_mentors, sorted_percentages, color='darkgreen')
            ax2.set_title(f"Mentor Impact Percentage in '{stream}'", fontsize=14)
            ax2.set_ylabel("Percentage of Stream Messages (%)", fontsize=12)
            ax2.set_xticklabels(sorted_mentors, rotation=45, ha='right')
            
            # Add percentage labels
            for bar in bars2:
                height = bar.get_height()
                ax2.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                        f'{height:.2f}%', ha='center', va='bottom')
            
            plt.tight_layout()
            stream_file = stream.replace(' ', '_').replace('/', '_')
            plt.savefig(os.path.join(vis_dir, f"shared_stream_{stream_file}.png"))
            plt.close()
    
    return vis_dir

def export_mentor_impact_excel(mentor_stream_impact, stream_totals, output_dir):
    """Export mentor stream impact data to Excel."""
    excel_path = os.path.join(output_dir, "mentor_stream_impact.xlsx")
    
    try:
        with pd.ExcelWriter(excel_path) as writer:
            # Create main impact sheet
            impact_data = []
            
            for mentor, data in mentor_stream_impact.items():
                mentor_total = data['total_messages']
                
                for stream, metrics in data['top_streams'].items():
                    impact_data.append({
                        'Mentor': mentor,
                        'Stream': stream,
                        'Mentor Messages': metrics['mentor_messages'],
                        'Stream Total Messages': metrics['total_messages'],
                        'Impact Percentage': round(metrics['percentage'], 2),
                        'Mentor Total Messages': mentor_total,
                        'Stream Contribution %': round((metrics['mentor_messages'] / mentor_total) * 100, 2)
                    })
            
            if impact_data:
                impact_df = pd.DataFrame(impact_data)
                
                # Sort by mentor name and then by their message count in each stream
                sorted_impact = impact_df.sort_values(['Mentor', 'Mentor Messages'], 
                                                     ascending=[True, False])
                sorted_impact.to_excel(writer, index=False, sheet_name='Mentor Stream Impact')
            
            # Create mentor summary sheet
            summary_data = []
            
            for mentor, data in mentor_stream_impact.items():
                # Calculate metrics for this mentor
                stream_count = data['stream_count']
                total_messages = data['total_messages']
                
                # Top stream and its percentage of this mentor's messages
                top_stream = None
                top_stream_count = 0
                top_stream_pct = 0
                
                if data['top_streams']:
                    # Get top stream by mentor message count
                    top_stream = list(data['top_streams'].keys())[0]
                    top_stream_count = data['top_streams'][top_stream]['mentor_messages']
                    top_stream_pct = (top_stream_count / total_messages) * 100
                
                summary_data.append({
                    'Mentor': mentor,
                    'Total Messages': total_messages,
                    'Streams Participated': stream_count,
                    'Top Stream': top_stream,
                    'Messages in Top Stream': top_stream_count,
                    'Top Stream % of Mentor Messages': round(top_stream_pct, 2)
                })
            
            if summary_data:
                summary_df = pd.DataFrame(summary_data)
                
                # Sort by total message count
                sorted_summary = summary_df.sort_values('Total Messages', ascending=False)
                sorted_summary.to_excel(writer, index=False, sheet_name='Mentor Summary')
            
            # Stream summary sheet showing all mentors' impact by stream
            stream_data = []
            
            for stream, total in stream_totals.items():
                # Find all mentors who participated in this stream
                mentor_count = 0
                mentor_message_count = 0
                
                for mentor, data in mentor_stream_impact.items():
                    if stream in data['top_streams']:
                        mentor_count += 1
                        mentor_message_count += data['top_streams'][stream]['mentor_messages']
                
                # Only include streams with mentor participation
                if mentor_count > 0:
                    stream_data.append({
                        'Stream': stream,
                        'Total Messages': total,
                        'Mentor Messages': mentor_message_count,
                        'Mentor Message %': round((mentor_message_count / total) * 100, 2),
                        'Number of Mentors': mentor_count
                    })
            
            if stream_data:
                stream_df = pd.DataFrame(stream_data)
                
                # Sort by percentage of mentor messages
                sorted_streams = stream_df.sort_values('Mentor Message %', ascending=False)
                sorted_streams.to_excel(writer, index=False, sheet_name='Stream Summary')
        
        print(f"Mentor stream impact analysis exported to Excel: {excel_path}")
        return excel_path
    except Exception as e:
        print(f"Error exporting mentor impact data to Excel: {e}")
        return None

def analyze_mentor_impact():
    """Main function for mentor stream impact analysis."""
    # Define paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "zulip_messages.xlsx")
    output_dir = os.path.join(script_dir, "mentor_impact_analysis")
    os.makedirs(output_dir, exist_ok=True)
    
    # Load data
    df = load_data(data_path)
    if df is None:
        print("Please ensure 'zulip_messages.xlsx' is in the same directory as this script.")
        return
    
    # Filter mentor data
    mentors_df, mentor_names = extract_mentor_data(df)
    if len(mentors_df) == 0:
        print("No mentors found in the dataset. Ensure mentor names end with '(Mentor)'.")
        return
    
    # Analyze mentor stream impact
    print("Analyzing mentor impact on streams...")
    mentor_stream_impact, stream_totals = analyze_mentor_stream_impact(df, mentors_df, mentor_names)
    
    # Create visualizations
    print("Creating mentor impact visualizations...")
    vis_dir = create_mentor_impact_visualizations(mentor_stream_impact, output_dir)
    
    # Export to Excel
    excel_path = export_mentor_impact_excel(mentor_stream_impact, stream_totals, output_dir)
    
    print("\nMentor stream impact analysis complete!")
    print(f"Visualizations directory: {vis_dir}")
    print(f"Excel report: {excel_path}")
    
    # Print a sample of results for each mentor
    print("\nSample of top stream impact for each mentor:")
    for mentor, data in mentor_stream_impact.items():
        if data['top_streams']:
            top_stream = list(data['top_streams'].keys())[0]
            impact = data['top_streams'][top_stream]
            print(f"- {mentor}: {impact['percentage']:.2f}% of messages in '{top_stream}' ({impact['mentor_messages']} of {impact['total_messages']} messages)")

if __name__ == "__main__":
    analyze_mentor_impact()