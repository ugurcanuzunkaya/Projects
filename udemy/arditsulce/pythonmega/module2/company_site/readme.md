# Best Company Website

## Overview
This company website showcases the mission, vision, and team of Best Company. It also includes a contact form for inquiries and collaborations. The website is built using Streamlit, and it features sections for a company introduction, team member profiles, and a contact form.

## Key Libraries
- **Streamlit**: Used for creating the interactive web application.
- **Pandas**: Used for handling data from CSV files.
- **smtplib**: Used for sending emails from the contact form.

## Project Structure
```
company_site/
│
├── images/               # Folder containing images for team members
│   ├── 1.png
│   ├── 2.png
│   ├── ...
│   └── 12.png
│
├── pages/                # Folder containing the contact page script
│   └── Contact.py
│
├── .zshrc                # Zsh configuration file
├── data.csv              # CSV file containing team member details
├── Home.py               # The main script to display the homepage
├── readme.md             # Readme file for the project
├── send_email.py         # The script to handle sending emails
└── topics.csv            # CSV file containing contact form topics
```

## External File Structure
- **data.csv**: This CSV file contains details about the team members, including first names, last names, roles, and image filenames. Example:
  ```
  first name,last name,role,image
  john,smith,Marketing Manager,1.png
  alberto ,lock,Junior Data Scientist,2.png
  ...
  ```
- **topics.csv**: This CSV file contains topics for the contact form. Example:
  ```
  topic
  Job Inquiries
  Project Proposals
  Other
  ```

## Explanation of Key Functions and Methods
- **Streamlit configuration**: Sets the page title, icon, layout, and initial sidebar state.
- **Displaying content**: Uses Streamlit to display the company introduction, team member profiles, and contact form.
- **Email sending**: Utilizes `smtplib` to send emails from the contact form.

### Home.py
This script is responsible for displaying the homepage of the company website. It reads team member details from `data.csv` and displays them in a three-column layout. It also includes sections for the company's mission and vision.

### Contact.py
This script contains the contact form. It allows visitors to send messages via email using the `send_email` function from `send_email.py`. It also reads topics for the contact form from `topics.csv`.

### send_email.py
This script handles the email sending functionality. It uses environment variables for the email credentials and receiver address to securely send emails.

## Final Output
The final output is a fully functional company website with a homepage showcasing the company's mission, vision, and team members, as well as a contact page for inquiries and collaborations.
