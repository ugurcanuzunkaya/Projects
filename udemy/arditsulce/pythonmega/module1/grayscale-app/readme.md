# Grayscale Image Converter

## Overview
This project is a web application that converts images to grayscale. Users can either upload an image or take a photo using their camera. The application uses Streamlit for the web interface and Pillow for image processing.

## Key Libraries
- **Streamlit**: Used for creating the web interface.
- **Pillow (PIL)**: Used for image processing.

## Project Structure
```
grayscale-app/
│
├── readme.md            # Readme file for the project
└── web.py               # Script for the web interface
```

## Explanation of Key Functions and Methods
- **Streamlit components**: Provides the web interface elements for starting the camera, uploading an image, and displaying the grayscale image.
- **Pillow's Image module**: Used to open and convert images to grayscale.

### web.py
This script provides the web interface for the application. It includes functionalities to start the camera, upload an image, convert the image to grayscale, and display the grayscale image.


## Final Output
The final output is a web application that allows users to convert images to grayscale by either uploading an image or taking a photo with their camera. The grayscale image is displayed on the web page.
