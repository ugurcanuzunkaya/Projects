# Portfolio Website

## Overview
This portfolio website showcases my projects and provides a platform for potential collaborators to contact me. The website is built using Streamlit, and it includes sections for a personal introduction, a list of projects, and a contact form.

## Key Libraries
- **Streamlit**: Used for creating the interactive web application.
- **Pandas**: Used for handling data from a CSV file.
- **smtplib**: Used for sending emails from the contact form.

## Project Structure
```
portfolio_project/
│
├── images/               # Folder containing images for the projects and personal photo
│   ├── 1.png
│   ├── 2.png
│   ├── ...
│   └── photo.png
│
├── pages/                # Folder containing the contact page script
│   └── Contact.py
│
├── .zshrc                # Zsh configuration file
├── data.csv              # CSV file containing project details
├── Home.py               # The main script to display the homepage
├── readme.md             # Readme file for the project
└── send_email.py         # The script to handle sending emails
```

## External File Structure
- **data.csv**: This CSV file contains details about the projects, including titles, descriptions, URLs, and image filenames. Example:
  ```
  title;description;url;image
  Todo App;A distraction-free web app to help you focus on creating and completing tasks.;https://pythonhow.com;1.png
  Portfolio Website;A website built entirely in Python to showcase coding projects and apps.;https://pythonhow.com;2.png
  ...
  ```

## Explanation of Key Functions and Methods
- **Streamlit configuration**: Sets the page title, icon, layout, and initial sidebar state.
- **Displaying content**: Uses Streamlit to display the personal introduction, project details, and images.
- **Email sending**: Utilizes `smtplib` to send emails from the contact form.

### Home.py
This script is responsible for displaying the homepage of the portfolio. It reads project details from `data.csv` and displays them in a two-column layout. It also includes a personal introduction and an image.

### Contact.py
This script contains the contact form. It allows visitors to send messages via email using the `send_email` function from `send_email.py`. 

### send_email.py
This script handles the email sending functionality. It uses environment variables for the email credentials and receiver address to securely send emails.

## Final Output
The final output is a fully functional portfolio website with a homepage showcasing various projects and a contact page for reaching out. The homepage includes a personal introduction and displays project details in a visually appealing manner.
