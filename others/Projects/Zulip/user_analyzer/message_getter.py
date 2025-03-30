import zulip
import os
import pandas as pd
from datetime import datetime, timezone, timedelta
from typing import List, Dict, Any, Optional

class ZulipMessageGetter:
    def __init__(self, zuliprc_path: str = "zuliprc"):
        """Initialize the Zulip client using credentials from zuliprc file."""
        if os.path.exists(zuliprc_path):
            self.client = zulip.Client(config_file=zuliprc_path)
        else:
            raise FileNotFoundError(f"Zuliprc file {zuliprc_path} not found. Please create it with your Zulip credentials.")
    
    def get_user_id_by_full_name(self, full_name: str) -> Optional[int]:
        """Get a user's ID by their full name."""
        result = self.client.get_users()
        if result['result'] == 'success':
            for user in result['members']:
                if user['full_name'] == full_name:
                    print(f"User ID for '{full_name}' is {user['user_id']}")
                    return user['user_id']
        return None
    
    def get_messages_by_user(self, full_name: str, limit: int = 1000) -> List[Dict[str, Any]]:
        """Get messages sent by a user identified by their full name."""
        user_id = self.get_user_id_by_full_name(full_name)
        if not user_id:
            print(f"User '{full_name}' not found.")
            return []
        
        request = {
            "anchor": "newest",
            "num_before": limit,
            "num_after": 0,
            "narrow": [
                {"operator": "sender", "operand": user_id}
            ]
        }
        
        result = self.client.get_messages(request)
        if result['result'] == 'success':
            print(f"Retrieved {len(result['messages'])} messages for user '{full_name}'.")
            return result['messages']
        else:
            print(f"Error retrieving messages: {result['msg']}")
            return []
    
    def get_all_streams(self) -> List[Dict[str, Any]]:
        """Get all streams the user has access to."""
        result = self.client.get_streams()
        if result['result'] == 'success':
            print(f"Retrieved {len(result['streams'])} streams.")
            return result['streams']
        else:
            print(f"Error retrieving streams: {result['msg']}")
            return []
    
    def search_all_channels(self, query: str = None, limit: int = 5000) -> List[Dict[str, Any]]:
        """Search through all channels/streams for messages.
        
        If query is provided, it will search for that content.
        Otherwise, it will return recent messages from all channels.
        """
        request = {
            "anchor": "newest",
            "num_before": limit,
            "num_after": 0,
            "narrow": []
        }
        
        # Add query to narrow if provided
        if query:
            request["narrow"].append({"operator": "search", "operand": query})
            
        result = self.client.get_messages(request)
        if result['result'] == 'success':
            print(f"Retrieved {len(result['messages'])} messages from all channels.")
            return result['messages']
        else:
            print(f"Error retrieving messages: {result['msg']}")
            return []
    
    def _convert_zulip_timestamp(self, timestamp_value):
        """
        Convert Zulip timestamp to datetime, handling the specific format used by Zulip.
        March 11, 2025, 22:46:25 (UTC+2) corresponds to 1741725985 in Zulip's format.
        """
        # Create a reference point - what we know is correct
        reference_ts = 1741725985
        reference_dt = datetime(2025, 3, 11, 22, 46, 25)  # Timezone naive datetime
        
        if timestamp_value == reference_ts:
            return reference_dt
        
        # Calculate seconds difference from reference point
        seconds_diff = timestamp_value - reference_ts
        
        # Apply difference to reference datetime
        result_dt = reference_dt + timedelta(seconds=seconds_diff)
        return result_dt

    def export_messages_to_excel(self, messages: List[Dict[str, Any]], filename: str) -> None:
        """Export messages to an Excel file."""
        if not messages:
            print("No messages to export.")
            return
        
        # Extract relevant data from messages
        data = []
        for msg in messages:
            # Convert timestamp using custom function
            timestamp = self._convert_zulip_timestamp(msg['timestamp'])
            
            # Remove timezone information for Excel compatibility
            if timestamp.tzinfo is not None:
                timestamp = timestamp.replace(tzinfo=None)
            
            # Create a single record for each message with all available fields
            message_data = {
                'message_id': msg.get('id', ''),
                'sender_id': msg.get('sender_id', ''),
                'sender_full_name': msg.get('sender_full_name', ''),
                'sender_email': msg.get('sender_email', ''),
                'sender_realm_str': msg.get('sender_realm_str', ''),
                'timestamp': timestamp,
                'date': timestamp.strftime("%Y-%m-%d"),
                'time': timestamp.strftime("%H:%M:%S"),
                'content': msg.get('content', ''),
                'content_type': msg.get('content_type', ''),
                'recipient_id': msg.get('recipient_id', ''),
                'recipient_type': msg.get('type', ''),  # 'stream' or 'private'
                'stream_id': msg.get('stream_id', ''),
                'stream_name': msg.get('display_recipient', ''),
                'subject': msg.get('subject', ''),
                'topic': msg.get('subject', ''),  # Duplicate of subject for clarity
                'client': msg.get('client', ''),
                'is_me_message': msg.get('is_me_message', False),
                'has_topic_links': len(msg.get('topic_links', [])) > 0,
                'has_submessages': len(msg.get('submessages', [])) > 0,
                'flags': ', '.join(msg.get('flags', [])),
                'avatar_url': msg.get('avatar_url', '')
            }
            
            # Add reactions if present
            if 'reactions' in msg and msg['reactions']:
                message_data['reactions'] = ', '.join([f"{r['emoji_name']}({r['user_id']})" for r in msg['reactions']])
            else:
                message_data['reactions'] = ''
                
            data.append(message_data)
        
        # Create DataFrame and export to Excel
        df = pd.DataFrame(data)
        
        # Save to the same directory as the script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(script_dir, filename)
        
        df.to_excel(output_path, index=False)
        print(f"Messages exported to {output_path}")

def main():
    # Example usage
    try:
        # Use zuliprc file in the same directory
        zuliprc_path = os.path.join(os.path.dirname(__file__), "zuliprc")
        getter = ZulipMessageGetter(zuliprc_path)
        
        # Ask user what they want to do
        print("\nZulip Message Analyzer")
        print("=====================")
        print("1. Get messages from a specific user")
        print("2. Search all channels for messages")
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == "1":
            # Get messages from a specific user
            full_name = input("Enter user's full name: ")
            messages = getter.get_messages_by_user(full_name)
            safe_name = full_name.replace(" ", "_")
            filename_prefix = safe_name
        elif choice == "2":
            # Search all channels
            query = input("Enter search query (leave empty to get all recent messages): ").strip()
            messages = getter.search_all_channels(query if query else None)
            filename_prefix = "all_channels" if not query else f"search_{query.replace(' ', '_')}"
        else:
            print("Invalid choice. Exiting.")
            return
        
        # Generate unique filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{filename_prefix}_messages_{timestamp}.xlsx"
        
        # Export to Excel (the path is now handled inside the export function)
        getter.export_messages_to_excel(messages, filename)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
