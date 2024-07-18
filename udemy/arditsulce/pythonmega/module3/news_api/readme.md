# News API Project

## Overview
This project fetches the latest news articles based on a user-specified topic using the NewsAPI and sends an email with the article titles and descriptions. The application is built using Python and includes functionality to change the working directory, make API requests, process JSON responses, and send emails.

## Key Libraries
- **requests**: Used for sending HTTP requests to the NewsAPI.
- **os**: Used for handling environment variables.
- **pathlib**: Used for handling file paths.
- **json**: Used for processing JSON data.
- **smtplib**: Used for sending emails.
- **ssl**: Used for creating a secure SSL context for email sending.

## Project Structure
```
news_api/
│
├── .zshrc                 # Zsh configuration file for environment variables
├── news_api.py            # Script for fetching news articles and sending emails
└── send_email.py          # Script for sending emails
```

## Explanation of Key Functions and Methods
- **change_dir_to_this_file**: Ensures the working directory is set to the directory of the script to handle file operations correctly.
- **Fetching news articles**: The script uses the NewsAPI key stored in an environment variable to fetch news articles based on the user-specified topic. The articles are saved in both JSON and text formats.
- **Sending emails**: The `send_email` function sends an email with the news articles' titles and descriptions to the specified receiver.

## How to Use
1. Set up your environment by adding your NewsAPI key and email credentials to your environment variables. You can add the following lines to your `.zshrc` file (or equivalent for your shell):
   ```
   export NEWSAPI_KEY="your_newsapi_key_here"
   export USER_MAIL="your_email_here"
   export USER_MAIL_PASSWORD="your_email_password_here"
   export RECEIVER_MAIL="receiver_email_here"
   ```
2. Run the `news_api.py` script:
   ```
   python news_api.py
   ```
3. When prompted, enter the topic you want to fetch news articles about.
4. The script will fetch the latest news articles, save them in JSON and text formats, and send an email with the article titles and descriptions to the specified receiver.

## Final Output
The final output is an email sent to the specified receiver containing the latest news articles' titles and descriptions based on the user-specified topic.
