import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pathlib import Path
import json
from collections import Counter
from analyzer_dashboard import load_data, analyze_sender_performance

def extract_community_leader_data(df):
    """Extract data only for users with (Community Lead) or (Community Manager) suffix in their name."""
    leader_pattern = r'\((Community Lead|Community Manager)\)$'
    leaders = df[df['sender_full_name'].str.contains(leader_pattern, regex=True)]
    print(f"Found {len(leaders['sender_full_name'].unique())} community leaders in the dataset")
    return leaders

def create_leader_visualizations(df_leaders, sender_stats, hour_activity, top_streams_by_sender, output_dir):
    """Create individual visualizations for each community leader."""
    leaders_dir = os.path.join(output_dir, "leaders")
    os.makedirs(leaders_dir, exist_ok=True)
    
    leader_names = df_leaders['sender_full_name'].unique()
    visualization_paths = {}
    
    for leader in leader_names:
        # Create a sanitized folder name
        leader_dir = os.path.join(leaders_dir, leader.replace(" ", "_").replace("(", "").replace(")", ""))
        os.makedirs(leader_dir, exist_ok=True)
        
        # Create hour activity visualization for this leader
        if leader in hour_activity:
            plt.figure(figsize=(10, 6))
            hours = list(range(24))
            counts = [hour_activity[leader].get(hour, 0) for hour in hours]
            plt.bar(hours, counts, color='darkgreen')
            plt.title(f"{leader}'s Activity by Hour")
            plt.xlabel("Hour of Day")
            plt.ylabel("Message Count")
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            hour_viz_path = os.path.join(leader_dir, f"{leader.replace(' ', '_')}_hour_activity.png")
            plt.savefig(hour_viz_path)
            plt.close()
            
            # Add to paths dictionary
            if leader not in visualization_paths:
                visualization_paths[leader] = []
            visualization_paths[leader].append(hour_viz_path)
        
        # Create top streams visualization for this leader
        if leader in top_streams_by_sender and top_streams_by_sender[leader]:
            plt.figure(figsize=(12, 7))
            # Get top 10 streams or fewer if less exist
            streams = dict(sorted(top_streams_by_sender[leader].items(), 
                                  key=lambda x: x[1], reverse=True)[:10])
            
            # Handle longer stream names
            stream_names = list(streams.keys())
            if stream_names and max(len(name) for name in stream_names) > 15:
                plt.figure(figsize=(14, 7))  # Wider figure for longer names
            
            colors = plt.cm.viridis(np.linspace(0, 0.9, len(streams)))
            plt.bar(streams.keys(), streams.values(), color=colors)
            plt.title(f"{leader}'s Top Streams")
            plt.xticks(rotation=45, ha='right')
            plt.ylabel("Message Count")
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            stream_viz_path = os.path.join(leader_dir, f"{leader.replace(' ', '_')}_top_streams.png")
            plt.savefig(stream_viz_path)
            plt.close()
            
            # Add to paths dictionary
            if leader not in visualization_paths:
                visualization_paths[leader] = []
            visualization_paths[leader].append(stream_viz_path)
    
    return visualization_paths, leaders_dir

def create_leader_comparison(leaders_df, leader_stats, hour_activity, output_dir):
    """Create comparative visualizations for all community leaders."""
    comparison_dir = os.path.join(output_dir, "leader_comparisons")
    os.makedirs(comparison_dir, exist_ok=True)
    
    # Plot message count comparison
    plt.figure(figsize=(12, 8))
    leader_message_counts = leader_stats.sort_values('message_count', ascending=False)
    sns.barplot(x='message_count', y='sender_full_name', data=leader_message_counts, 
                palette='viridis')
    plt.title('Message Count by Community Leader')
    plt.xlabel('Number of Messages')
    plt.tight_layout()
    plt.savefig(os.path.join(comparison_dir, 'leader_message_count.png'))
    plt.close()
    
    # Plot messages per day comparison
    plt.figure(figsize=(12, 8))
    leader_activity = leader_stats.sort_values('messages_per_day', ascending=False)
    sns.barplot(x='messages_per_day', y='sender_full_name', data=leader_activity,
                palette='mako')
    plt.title('Messages per Day by Community Leader')
    plt.xlabel('Average Messages per Day')
    plt.tight_layout()
    plt.savefig(os.path.join(comparison_dir, 'leader_daily_activity.png'))
    plt.close()
    
    # Add role column to differentiate Community Leads from Community Managers
    leader_stats['role'] = leader_stats['sender_full_name'].apply(
        lambda x: 'Community Manager' if '(Community Manager)' in x else 'Community Lead'
    )
    
    # Plot message count by role
    plt.figure(figsize=(10, 6))
    role_counts = leader_stats.groupby('role')['message_count'].sum().reset_index()
    sns.barplot(x='role', y='message_count', data=role_counts, palette='Set2')
    plt.title('Total Messages by Community Role')
    plt.ylabel('Total Message Count')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(os.path.join(comparison_dir, 'role_message_count.png'))
    plt.close()
    
    # Combined hour activity heatmap
    leader_names = leaders_df['sender_full_name'].unique()
    
    if len(leader_names) > 0:
        plt.figure(figsize=(14, 10))
        hour_data = []
        
        for leader in leader_names:
            if leader in hour_activity:
                hours = list(range(24))
                counts = [hour_activity[leader].get(hour, 0) for hour in hours]
                for hour, count in zip(hours, counts):
                    hour_data.append({
                        'Leader': leader,
                        'Hour': hour,
                        'Count': count
                    })
        
        if hour_data:
            hour_df = pd.DataFrame(hour_data)
            hour_pivot = hour_df.pivot(index='Leader', columns='Hour', values='Count')
            hour_pivot = hour_pivot.fillna(0)
            
            plt.figure(figsize=(16, 10))
            sns.heatmap(hour_pivot, cmap="YlGnBu", annot=True, fmt=".0f", linewidths=.5)
            plt.title('Hourly Activity Comparison Among Community Leaders')
            plt.xlabel('Hour of Day')
            plt.ylabel('Community Leader')
            plt.tight_layout()
            plt.savefig(os.path.join(comparison_dir, 'leader_hour_activity_comparison.png'))
            plt.close()
    
    # Stream participation comparison - find common streams across leaders
    common_streams = {}
    for leader in leader_names:
        leader_df = leaders_df[leaders_df['sender_full_name'] == leader]
        streams = leader_df['stream_name'].value_counts().to_dict()
        for stream, count in streams.items():
            if stream not in common_streams:
                common_streams[stream] = {}
            common_streams[stream][leader] = count
    
    # Focus on streams that multiple leaders participate in
    multi_leader_streams = {s: leaders for s, leaders in common_streams.items() 
                          if len(leaders) > 1}
    
    # Create visualization for top shared streams
    if multi_leader_streams:
        top_shared_streams = sorted(multi_leader_streams.items(), 
                                   key=lambda x: len(x[1]), reverse=True)[:10]
        
        # Prepare data for grouped bar chart
        stream_data = []
        for stream, leaders in top_shared_streams:
            for leader, count in leaders.items():
                stream_data.append({
                    'Stream': stream,
                    'Leader': leader,
                    'Messages': count
                })
        
        if stream_data:
            stream_df = pd.DataFrame(stream_data)
            
            plt.figure(figsize=(16, 10))
            chart = sns.barplot(x='Stream', y='Messages', hue='Leader', data=stream_df,
                              palette='tab10')
            plt.title('Community Leader Participation in Shared Streams')
            plt.xticks(rotation=45, ha='right')
            plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.savefig(os.path.join(comparison_dir, 'leader_stream_comparison.png'))
            plt.close()
    
    return comparison_dir

def export_leader_excel(leader_stats, top_streams_by_leaders, hour_activity, leaders_df, output_dir):
    """Export community leader data to a dedicated Excel file."""
    excel_path = os.path.join(output_dir, "community_leader_analysis.xlsx")
    
    try:
        with pd.ExcelWriter(excel_path) as writer:
            # Add role column to differentiate Community Leads from Community Managers
            if 'role' not in leader_stats.columns:
                leader_stats['role'] = leader_stats['sender_full_name'].apply(
                    lambda x: 'Community Manager' if '(Community Manager)' in x else 'Community Lead'
                )
            
            # Format dates for better readability
            if 'first_message' in leader_stats.columns and 'last_message' in leader_stats.columns:
                leader_stats['first_message'] = leader_stats['first_message'].dt.strftime('%Y-%m-%d %H:%M')
                leader_stats['last_message'] = leader_stats['last_message'].dt.strftime('%Y-%m-%d %H:%M')
            
            # Round numeric columns
            for col in ['avg_message_length', 'active_days', 'messages_per_day']:
                if col in leader_stats.columns:
                    leader_stats[col] = leader_stats[col].round(2)
            
            # Main stats sheet
            leader_stats.to_excel(writer, index=False, sheet_name='Leader Performance')
            
            # Role summary sheet
            role_summary = leader_stats.groupby('role').agg(
                total_leaders=('sender_full_name', 'nunique'),
                total_messages=('message_count', 'sum'),
                avg_messages_per_day=('messages_per_day', 'mean'),
                avg_msg_length=('avg_message_length', 'mean')
            ).reset_index()
            role_summary.to_excel(writer, index=False, sheet_name='Role Summary')
            
            # Stream activity sheet
            stream_data = []
            for leader, streams in top_streams_by_leaders.items():
                # Add role for easier filtering
                role = 'Community Manager' if '(Community Manager)' in leader else 'Community Lead'
                for stream, count in streams.items():
                    stream_data.append({
                        'Leader': leader,
                        'Role': role,
                        'Stream': stream,
                        'Message Count': count
                    })
            
            if stream_data:
                stream_df = pd.DataFrame(stream_data)
                stream_df.to_excel(writer, index=False, sheet_name='Stream Activity')
            
            # Hourly activity sheet
            hour_data = []
            for leader, hours in hour_activity.items():
                if leader in leader_stats['sender_full_name'].values:
                    role = 'Community Manager' if '(Community Manager)' in leader else 'Community Lead'
                    for hour, count in hours.items():
                        hour_data.append({
                            'Leader': leader,
                            'Role': role,
                            'Hour': hour,
                            'Message Count': count
                        })
            
            if hour_data:
                hour_df = pd.DataFrame(hour_data)
                hour_df.to_excel(writer, index=False, sheet_name='Hourly Activity')
            
            # Daily activity sheet
            if 'parsed_date' in leaders_df.columns:
                # Add a role column to the leaders_df for grouping
                leaders_df['role'] = leaders_df['sender_full_name'].apply(
                    lambda x: 'Community Manager' if '(Community Manager)' in x else 'Community Lead'
                )
                
                daily = leaders_df.groupby([leaders_df['parsed_date'].dt.date, 'sender_full_name', 'role']).size().reset_index()
                daily.columns = ['Date', 'Leader', 'Role', 'Message Count']
                daily.to_excel(writer, index=False, sheet_name='Daily Activity')
                
                # Also add a summary by role and date
                role_daily = leaders_df.groupby([leaders_df['parsed_date'].dt.date, 'role']).size().reset_index()
                role_daily.columns = ['Date', 'Role', 'Message Count']
                role_daily.to_excel(writer, index=False, sheet_name='Role Daily Activity')
        
        print(f"Community leader analysis exported to Excel: {excel_path}")
        return excel_path
    except Exception as e:
        print(f"Error exporting community leader data to Excel: {e}")
        return None

def analyze_community_leaders():
    """Main function for community leader analysis."""
    # Define paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "zulip_messages.xlsx")
    output_dir = os.path.join(script_dir, "community_leader_analysis")
    os.makedirs(output_dir, exist_ok=True)
    
    # Load data
    df = load_data(data_path)
    if df is None:
        print("Please ensure 'zulip_messages.xlsx' is in the same directory as this script.")
        return
    
    # Filter community leader data
    leaders_df = extract_community_leader_data(df)
    if len(leaders_df) == 0:
        print("No community leaders found in the dataset. Ensure names end with '(Community Lead)' or '(Community Manager)'.")
        return
    
    # Analyze leader performance
    print("Analyzing community leader performance metrics...")
    leader_stats, hour_activity, top_streams_by_sender = analyze_sender_performance(leaders_df)
    
    # Filter the analysis results to include only community leaders
    leader_names = leaders_df['sender_full_name'].unique()
    leader_stats = leader_stats[leader_stats['sender_full_name'].isin(leader_names)]
    
    # Filter hour_activity and top_streams_by_sender to include only community leaders
    leader_hour_activity = {k: v for k, v in hour_activity.items() if k in leader_names}
    leader_streams = {k: v for k, v in top_streams_by_sender.items() if k in leader_names}
    
    # Create visualizations for each community leader
    print("Creating individual community leader visualizations...")
    viz_paths, leaders_dir = create_leader_visualizations(
        leaders_df, leader_stats, leader_hour_activity, leader_streams, output_dir
    )
    
    # Create comparative visualizations across all community leaders
    print("Creating community leader comparison visualizations...")
    comparison_dir = create_leader_comparison(leaders_df, leader_stats, leader_hour_activity, output_dir)
    
    # Export community leader data to Excel
    excel_path = export_leader_excel(leader_stats, leader_streams, leader_hour_activity, leaders_df, output_dir)
    
    print(f"\nCommunity leader analysis complete!")
    print(f"Individual community leader visualizations: {leaders_dir}")
    print(f"Comparative visualizations: {comparison_dir}")
    print(f"Excel report: {excel_path}")

if __name__ == "__main__":
    analyze_community_leaders()