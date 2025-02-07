# Day 27 - 28: Python Mega Course

## Day 27 and 28

### Short Summary - 1

In this video, we discussed APIs (Application Programming Interfaces), focusing on RESTful APIs, which are commonly used for web and application development. We explored the differences between a web app and an API, highlighting that while web apps are designed for human interaction, APIs are meant for computer programs to exchange data. By the end of the video, you'll understand how to use APIs in your applications to fetch and manipulate data programmatically.

#### Key Points - 1

- **Definition and Purpose**:
  - **API**: Stands for Application Programming Interface.
  - APIs are used by applications to communicate and exchange data.
  
- **Comparison**:
  - **Web App**: Designed for human interaction, visually appealing.
  - **API**: Designed for programmatic interaction, data is usually in JSON format, readable by computers.

- **Example**:
  - News website vs. News API: The website shows news for human readers, while the API provides structured news data for apps.

- **Usage**:
  - APIs are used by various types of apps (web, email, desktop, mobile) to fetch and display data.
  - For instance, a web app can fetch news data from a news API to display on its site.

By understanding APIs, you can enhance your applications with external data and functionalities, leading to more dynamic and robust software solutions.

---

### Short Summary - 2

In this video, we discussed how to build a Python application that automatically sends news updates about a specific topic (like Tesla) to your email every morning. This involves using APIs to fetch data and the `requests` library in Python to access and handle the data.

#### Key Points - 2

- **Introduction to APIs**:
  - APIs (Application Programming Interfaces) allow applications to communicate and exchange data.
  - APIs are commonly used to fetch data from external sources, like news websites.

- **Setting Up the Project**:
  - Create a new Python project and a `main.py` file.
  - Use the `requests` library to fetch data from a URL.

- **Fetching Data from a URL**:
  - Use `requests.get(URL).text` to get the content of a webpage.
  - This method is useful for fetching data from APIs rather than regular web pages, as APIs provide structured data (like JSON) that is easier for programs to use.

- **Using the News API**:
  - Sign up for an account on `newsapi.org` and obtain an API key.
  - Construct a URL with the API key to fetch news about a specific topic.
  - Store the API key and URL in your Python script.

- **Parsing the Data**:
  - Use the `requests` library to fetch data from the News API.
  - The data fetched can be used programmatically within your application, such as sending it via email.

This video provides a foundational understanding of how to fetch and use data from APIs, setting the stage for building an automated news email application in Python.

---

### Short Summary - 3

In this video, we continue building our Python app that sends daily news updates via email. We fetch news data from the News API, parse it, and prepare to send it via email using the SMTP library. This involves converting the fetched JSON data into a dictionary, extracting specific information, and using a debugging tool to understand the data structure.

#### Key Points - 3

- **Fetching Data from the News API**:
  - Use the `requests` library to fetch data from the News API.
  - Convert the fetched JSON data into a dictionary using `.json()` method.

- **Extracting Relevant Information**:
  - The data is structured in a dictionary containing lists of articles.
  - Extract specific fields like the title and description of each article.

- **Debugging and Understanding Data**:
  - Use PyCharm’s debugging tool to explore and understand complex data structures.
  - Utilize breakpoints and the debugger console to interact with and inspect the data.

- **Example Code**:

  ```python
  import requests

  api_key = "YOUR_API_KEY"
  url = "https://newsapi.org/v2/everything?q=tesla&from=2023-06-12&sortBy=publishedAt&apiKey=" + api_key
  response = requests.get(url)
  content = response.json()

  articles = content['articles']
  for article in articles:
      print(article['title'])
      print(article['description'])
  ```

- **Next Steps**:
  - Use the SMTP library to send the extracted news articles via email.
  - Commit the progress to version control using Git.

By the end of the video, we have successfully fetched and printed news articles' titles and descriptions, setting the stage for sending this information via email.

---

### Short Summary - 4

In this exercise, you are tasked with extending the functionality of the news fetching app. The goal is to send the fetched news articles' titles and descriptions via email. This involves using Python's SMTP library to automate sending emails.

#### Key Points - 4

- **Exercise Objective**:
  - Send news articles' titles and descriptions fetched from the News API to your email address.

- **Instructions**:
  - Use the provided email sending script from the portfolio app.
  - Ensure the email script includes the correct Gmail address and app password.

- **Preparation**:
  - If you don't have the email sending script, it is available in the lecture resources.
  - Modify the email sending script with your Gmail address and app password.
  - Set the sender and receiver email addresses.

- **Hint**:
  - Fetch and print the news articles' titles and descriptions as done in the previous exercise.
  - Integrate the email sending functionality to send this information.

- **Expected Outcome**:
  - Receive an email containing the titles and descriptions of approximately 100 news articles.

### Example Email Script Integration

Here is an example of how you might integrate the email sending functionality:

```python
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Fetching news articles
api_key = "YOUR_API_KEY"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-06-12&sortBy=publishedAt&apiKey=" + api_key
response = requests.get(url)
content = response.json()

# Extracting articles
articles = content['articles']
news_content = ""
for article in articles:
    news_content += f"Title: {article['title']}\nDescription: {article['description']}\n\n"

# Email setup
email_user = 'your_email@gmail.com'
email_password = 'your_app_password'
email_send = 'your_email@gmail.com'

subject = 'Daily News Update'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

msg.attach(MIMEText(news_content, 'plain'))

# Sending the email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)
    text = msg.as_string()
    server.sendmail(email_user, email_send, text)
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {str(e)}")
```

### Steps

1. **Fetch News Articles**:
   - Use the News API to get articles about Tesla.
   - Extract titles and descriptions from the fetched data.

2. **Prepare Email Content**:
   - Format the extracted titles and descriptions into a readable string.

3. **Set Up Email**:
   - Configure SMTP settings with your Gmail address and app password.
   - Prepare the email with the extracted news content.

4. **Send Email**:
   - Use the SMTP library to send the prepared email to your address.

By attempting this exercise, you will enhance your problem-solving skills and deepen your understanding of integrating multiple functionalities in Python.

---

### Summary and Improvements to News Email Automation Program

In this video, we made five significant improvements to our program that sends news articles by email. These enhancements aim to provide a better user experience by making the emails more informative and the program more flexible.

### Improvements Made

1. **Add Links to News Articles**:
   - Each news article now includes a clickable link that directs the user to the full article.
   - Code snippet:

     ```python
     for article in content['articles'][:20]:
         news_content += f"Title: {article['title']}\nDescription: {article['description']}\nURL: {article['url']}\n\n"
     ```

2. **Limit Number of News Articles**:
   - Reduced the number of news articles sent in the email to 20 instead of 100.
   - Code snippet:

     ```python
     for article in content['articles'][:20]:
         ...
     ```

3. **Filter News by Language**:
   - Added a parameter to fetch only English news articles.
   - Code snippet:

     ```python
     url = ("https://newsapi.org/v2/everything?q=tesla&"
            "sortBy=publishedAt&apiKey=" + api_key + "&language=en")
     ```

4. **Add Subject to Email**:
   - Included a subject line in the email to provide context for the recipient.
   - Code snippet:

     ```python
     subject = 'Subject: Today\'s News\n\n'
     msg.attach(MIMEText(subject + news_content, 'plain'))
     ```

5. **Dynamic Topic Selection**:
   - Made the news topic dynamic by using a variable instead of hardcoding "Tesla".
   - Code snippet:

     ```python
     topic = "Tesla"
     url = f"https://newsapi.org/v2/everything?q={

topic}&sortBy=publishedAt&apiKey={api_key}&language=en"
     ```

### Full Updated Code Example

```python
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Fetching news articles
api_key = "YOUR_API_KEY"
topic = "Tesla"
url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey={api_key}&language=en"
response = requests.get(url)
content = response.json()

# Extracting articles and creating email content
articles = content['articles'][:20]
news_content = ""
for article in articles:
    news_content += f"Title: {article['title']}\nDescription: {article['description']}\nURL: {article['url']}\n\n"

# Email setup
email_user = 'your_email@gmail.com'
email_password = 'your_app_password'
email_send = 'your_email@gmail.com'

subject = 'Subject: Today\'s News\n\n'
msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = 'Today\'s News'

msg.attach(MIMEText(subject + news_content, 'plain'))

# Sending the email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)
    text = msg.as_string()
    server.sendmail(email_user, email_send, text)
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {str(e)}")
```

### Conclusion

By following these improvements, the program now provides a more user-friendly email with fewer, relevant news articles, proper language filtering, clickable links, and a dynamic topic selection.

---

### Summary: Downloading Binary Data with the Requests Library

In this video, we learned how to use the requests library to download binary data, such as images or zip files, from the web. Previously, we worked with text data using the text and json methods of the requests library. Now, we focus on handling non-text data.

### Steps to Download Binary Data

1. **Identify the URL of the Binary File**:
   - For example, to download an image from a Wikipedia page, right-click the image and select "Open image in new tab." Copy the URL from the address bar.

2. **Set Up the URL and Import the Requests Library**:
   - Example URL for an image:

     ```python
     url = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Golden_Gate_Bridge%2C_SF_%28cropped%29.jpg/800px-Golden_Gate_Bridge%2C_SF_%28cropped%29.jpg"
     ```

   - Import the requests library:

     ```python
     import requests
     ```

3. **Make a Request to Get the Binary Data**:
   - Use the `requests.get` method to fetch the data:

     ```python
     response = requests.get(url)
     ```

4. **Check the Response**:
   - Ensure the request was successful (HTTP status code 200):

     ```python
     if response.status_code == 200:
         # Proceed to save the binary data
     ```

5. **Write the Binary Data to a File**:
   - Open a file in write binary mode (`wb`) and write the response content:

     ```python
     with open("downloaded_image.jpg", "wb") as file:
         file.write(response.content)
     ```

6. **Verify the Downloaded File**:
   - Refresh your project directory to see the downloaded file.

### Full Code Example

```python
import requests

# URL of the image to be downloaded
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Golden_Gate_Bridge%2C_SF_%28cropped%29.jpg/800px-Golden_Gate_Bridge%2C_SF_%28cropped%29.jpg"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Open a file in write binary mode and save the content
    with open("downloaded_image.jpg", "wb") as file:
        file.write(response.content)

print("Image downloaded successfully.")
```

### Notes

- **Binary Mode (`wb`)**: When working with binary files, such as images, ensure you open the file in write binary mode (`wb`).
- **Response Content**: Use `response.content` to access the raw binary data from the response.
- **File Extension**: Ensure the file extension matches the type of file you are downloading (e.g., `.jpg` for images, `.zip` for zip files).

By following these steps, you can download and save any binary file from the web using Python and the requests library.

---

### Summary: Constructing a Website with Streamlit and Requests

In this video, the instructor demonstrates how to construct a simple website using Streamlit and the requests library to fetch and display an astronomy picture along with its title and explanation from an API. The entire process is done in about 27 lines of code. Below are the steps and the code explained:

### Steps to Construct the Website

1. **Import Libraries**:
   - Import the required libraries: `requests` for fetching data and `streamlit` for building the web interface.

2. **Set Up API Key and URL**:
   - Prepare the API key and the URL to the astronomy picture of the day API. Use an f-string to embed the API key within the URL.

3. **Fetch Data from API**:
   - Use the `requests.get` method to send a GET request to the API URL and gather the data in JSON format.

4. **Extract Data from JSON**:
   - Extract the title, URL of the image, and explanation from the JSON response.

5. **Download the Image**:
   - Create a file path for the downloaded image.
   - Send a GET request to the image URL to fetch the image data.
   - Open a new file in write-binary mode (`wb`) and write the image data to the file.

6. **Build the Streamlit Web Page**:
   - Use Streamlit's `st.title` to display the title.
   - Use `st.image` to display the downloaded image.
   - Use `st.write` to display the explanation.

### Full Code Example for the Website

```python
import requests
import streamlit as st

# API key and URL setup
api_key = "YOUR_API_KEY"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# Fetch data from the API
response = requests.get(url)
data = response.json()

# Extract data from JSON response
title = data['title']
image_url = data['url']
explanation = data['explanation']

# Download the image
image_path = "image.png"
image_response = requests.get(image_url)
with open(image_path, "wb") as file:
    file.write(image_response.content)

# Build the Streamlit web page
st.title(title)
st.image(image_path)
st.write(explanation)
```

### Detailed Explanation

1. **Importing Libraries**:
   - `requests`: To handle HTTP requests.
   - `streamlit`: To create and display the web application.

2. **API Key and URL**:
   - The API key is stored in a variable `api_key`.
   - The URL to the NASA API is created using an f-string for embedding the API key.

3. **Fetching Data**:
   - A GET request is sent to the API URL using `requests.get(url)`.
   - The response is converted to JSON format using `response.json()`.

4. **Extracting Data**:
   - The `title`, `url` (for the image), and `explanation` fields are extracted from the JSON response and stored in separate variables.

5. **Downloading the Image**:
   - The image URL is used to send another GET request to fetch the image data.
   - The image data is written to a file named `image.png` in binary mode.

6. **Building the Web Page**:
   - `st.title(title)` displays the title of the image.
   - `st.image(image_path)` displays the downloaded image.
   - `st.write(explanation)` displays the explanation of the image.

This process effectively uses the requests library to fetch and process data from an API and Streamlit to build and display a web page with the fetched data.

---

### Summary: Scheduling Tasks with Python Anywhere

In this video, the instructor introduces Python Anywhere, a service that provides a server running 24/7, allowing users to host web apps and schedule Python scripts for execution at specific times daily. The key points covered include setting up Python Anywhere, uploading files, scheduling tasks, and checking logs for errors.

### Steps to Schedule Tasks with Python Anywhere

1. **Sign Up and Log In**:
   - Create a free beginner account on Python Anywhere.
   - Log in to access the dashboard.

2. **Check Python Version**:
   - Go to the Consoles menu to see the latest Python version supported (e.g., Python 3.10).

3. **Upload Your Python Files**:
   - Navigate to the Files menu.
   - Upload your script files (e.g., `main.py` and `send_email.py`).

4. **Schedule the Task**:
   - Go to the Tasks menu.
   - Copy the path to your script file and specify the Python interpreter version.
   - Example command: `python3

    .10 /path/to/your/main.py`.

    - Set the time for the task to run daily.

5. **Check Logs for Errors**:
   - After the task runs, check the logs for any errors or confirmation of task completion.

### Detailed Steps and Code Example

1. **Sign Up and Log In**:
   - Go to [pythonanywhere.com](https://www.pythonanywhere.com) and sign up for a free account.
   - Log in and navigate to the dashboard.

2. **Check Python Version**:
   - In the Consoles menu, note the latest Python version (e.g., Python 3.10).

3. **Upload Files**:
   - Go to the Files menu.
   - Upload your `main.py` and `send_email.py` scripts by clicking "Upload a file".

4. **Schedule a Task**:
   - Go to the Tasks menu and paste the path to your script:

     ```plaintext
     python3.10 /home/yourusername/path/to/main.py
     ```

   - Set the time for the task to run (e.g., two minutes from now for testing).

5. **Check Logs**:
   - If the task runs successfully, you will receive the scheduled email.
   - If there are issues, check the logs for error messages and troubleshoot accordingly.

### Example Command for Scheduling

```plaintext
python3.10 /home/yourusername/path/to/main.py
```

- Ensure to replace `/home/yourusername/path/to/main.py` with the actual path to your script.

### Additional Features

- **Consoles**: Open an interactive Python shell for coding directly in the browser.
- **Web Apps**: Python Anywhere supports hosting web apps built with frameworks like Django and Flask but not Streamlit.

### Conclusion - Python Anywhere

Python Anywhere is a powerful tool for scheduling Python tasks and hosting web apps, providing a continuous running server to execute scripts at specified times, ensuring automated processes like sending emails or scraping data run smoothly.
