import requests
import os
import pathlib
import streamlit as st

def change_dir_to_this_file():
    # getting the current working directory
    cwd = os.getcwd()
    path_of_this_file = pathlib.Path(__file__).parent
    if cwd != path_of_this_file:
        os.chdir(path_of_this_file)

change_dir_to_this_file()


# API key and URL setup
api_key = os.environ.get("NASA_API_KEY")
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# Fetch data from the API
response = requests.get(url)
data = response.json()

# # Extract data from JSON response
title = data['title']
image_url = data['url']
explanation = data['explanation']


# Check if the URL is a YouTube video link
if "youtube.com" in image_url:
    # Extract the YouTube video ID from the URL
    st.title(title)
    video_id = image_url.split('/')[-1]
    # Embed the YouTube video using an iframe
    st.markdown(f"""
        <iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        """, unsafe_allow_html=True)
else:
    # Download the image
    image_path = "image.png"
    image_response = requests.get(image_url)
    with open(image_path, "wb") as file:
        file.write(image_response.content)

    # Build the Streamlit web page for an image
    st.title(title)
    st.image(image_path)

st.write(explanation)