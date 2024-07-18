# NASA API Project

## Overview
This project retrieves and displays the Astronomy Picture of the Day (APOD) from NASA's API. The application uses Streamlit for the web interface, allowing users to view the image or video of the day along with its title and explanation.

## Key Libraries
- **requests**: Used for sending HTTP requests to the NASA API.
- **os**: Used for handling environment variables.
- **pathlib**: Used for handling file paths.
- **Streamlit**: Used for creating the web interface.

## Project Structure
```
nasa_api/
│
├── .zshrc                 # Zsh configuration file for environment variables
├── readme.md              # Project overview and instructions
└── nasa_api.py            # Script for fetching and displaying the NASA APOD
```

## Explanation of Key Functions and Methods
- **change_dir_to_this_file**: Ensures the working directory is set to the directory of the script to handle file operations correctly.
- **Fetching data from NASA API**: The script uses the API key stored in an environment variable to fetch data from NASA's APOD API.
- **Displaying data with Streamlit**: Depending on the type of content (image or YouTube video), the script displays the content along with its title and explanation using Streamlit.

## How to Use
1. Set up your environment by adding your NASA API key to your environment variables. You can add the following line to your `.zshrc` file (or equivalent for your shell):
   ```
   export NASA_API_KEY="your_api_key_here"
   ```
2. Run the `nasa_api.py` script using Streamlit:
   ```
   streamlit run nasa_api.py
   ```
3. The application will fetch the APOD from NASA's API and display it in the web interface. If the content is a YouTube video, it will be embedded in the page. If it is an image, it will be downloaded and displayed along with its title and explanation.

## Final Output
The final output is a Streamlit web application that displays NASA's Astronomy Picture of the Day, including the title and explanation. The content can be either an image or a YouTube video.
