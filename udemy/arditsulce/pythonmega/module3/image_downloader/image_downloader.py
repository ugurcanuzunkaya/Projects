import requests
import os
import pathlib

def change_dir_to_this_file():
    # getting the current working directory
    cwd = os.getcwd()
    path_of_this_file = pathlib.Path(__file__).parent
    if cwd != path_of_this_file:
        os.chdir(path_of_this_file)

change_dir_to_this_file()

# URL of the image to be downloaded
hardcoded_or_not = input("Do you want to enter the URL of the image to be downloaded? (y/n): ")
if hardcoded_or_not == "y":
    url = input("Enter the URL of the image to be downloaded: ")
elif hardcoded_or_not == "n":
    url = "https://upload.wikimedia.org/wikipedia/commons/4/40/Image_test.png"
file_format = url.split(".")[-1]

# Send a GET request to the URL
response = requests.get(url)


# Check if the request was successful
if response.status_code == 200:
    # Open a file in write binary mode and save the content
    with open(f"downloaded_image.{file_format}", "wb") as file:
        file.write(response.content)

    print("Image downloaded successfully.")