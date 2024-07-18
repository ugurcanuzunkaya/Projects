# Image Downloader

## Overview
This project is a simple script that downloads an image from a given URL. The user can either input the URL of the image or use a hardcoded default URL. The downloaded image is saved in the same directory as the script.

## Key Libraries
- **requests**: Used for sending HTTP requests to download the image.
- **os**: Used for handling file and directory operations.
- **pathlib**: Used for handling file paths.

## Project Structure
```
image_downloader/
│
└── image_downloader.py    # Script for downloading an image from a URL
```

## Explanation of Key Functions and Methods
- **change_dir_to_this_file**: Ensures the working directory is set to the directory of the script to handle file operations correctly.
- **Downloading an image**: The script allows the user to input the URL of the image or use a default URL. It then sends an HTTP GET request to the URL and saves the image in the current directory.

## How to Use
1. Run the `image_downloader.py` script.
2. When prompted, decide if you want to enter the URL of the image to be downloaded or use the default URL.
   - If you choose to enter the URL, type the URL of the image when prompted.
   - If you choose not to enter the URL, the script will use the default URL: `https://upload.wikimedia.org/wikipedia/commons/4/40/Image_test.png`.
3. The script will download the image and save it in the same directory as the script with the appropriate file extension.

## Final Output
The final output is the downloaded image saved in the same directory as the script. The image will be named `downloaded_image` followed by the appropriate file extension based on the URL.
