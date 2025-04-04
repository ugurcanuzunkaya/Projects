from chat_downloader import ChatDownloader
import pandas as pd
import openpyxl

def download_chat(video_url, output_file):
    chat = ChatDownloader().get_chat(video_url)  # Create a generator for chat messages

    data = []
    for message in chat:
        timestamp = message.get('time_text', 'N/A')
        author = message['author']['name'] if 'author' in message else 'N/A'
        content = message.get('message', '')

        data.append({'Timestamp': timestamp, 'Author': author, 'Message': content})

    # Create a DataFrame and export to Excel
    df = pd.DataFrame(data)
    print(df.head())
    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    # Example usage
    # video_url = 'youtube_video_url_here'
    # output_file = 'chat_data.xlsx'
    # download_chat(video_url, output_file)

    # Dictionary of video URLs and their corresponding titles
    video_urls_dict = {}
    video_urls_dict["Açılış Yayını Chat"] = "https://www.youtube.com/live/XGNZuNsJpZc?si=lSoMDt9w6PKor419"
    video_urls_dict["Proje Yayını Chat"] = "https://www.youtube.com/live/aVJJsbH7Uec?si=FlXqo2DlvCEZyBZk"
    video_urls_dict["Eğitim 1 Yayını Chat"] = "https://www.youtube.com/live/KJHZfoN-AVg?si=XFDhwA-hEcyA3Kdu"
    video_urls_dict["Eğitim 2 Yayını Chat"] = "https://www.youtube.com/live/QAuakadzlWQ?si=em4mzZ94o_G3jM7A"
    
    # Iterate through the dictionary and download chat for each video
    for title, video_url in video_urls_dict.items():
        output_file = f"{title.replace(' ', '_')}_chat.xlsx"
        print(f"Downloading chat for {title}...")
        # Call the download_chat function with the video URL and output file name
        download_chat(video_url, output_file)

    
    print(f"Chat messages have been saved to {output_file}")