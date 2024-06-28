# Job Application Flask Project

## Overview
This project is a job application web application built with Flask. It allows users to submit job applications through a form, and it sends a confirmation email upon submission. The application includes a simple form for job applicants to fill out their details.

## Key Libraries
- **Flask**: The web framework used for building the application.
- **Flask_SQLAlchemy**: Used for database operations.
- **Flask_Mail**: Used for sending emails.
- **os**: Used for handling environment variables.
- **datetime**: Used for handling date operations.

## Project Structure
```
project_flask/
│
├── templates/
│   └── index.html         # HTML template for the job application form
├── app.py                 # Main application script
└── readme.md              # Readme file for the project
```

## Explanation of Key Functions and Methods

### `app.py`
- **Application Configuration**: Configures the Flask application, database URI, and email server settings using environment variables.
- **Database Model**: Defines the `Form` model to store job application data.
- **Routes**: 
  - `/`: Handles the display and submission of the job application form.
- **Email Sending**: Sends a confirmation email to the applicant upon successful form submission.

### `templates/index.html`
- HTML form for job applications, using Bootstrap for styling.

## How to Use

### Setup
1. **Install dependencies**:
   ```bash
   pip install Flask Flask_SQLAlchemy Flask_Mail
   ```

2. **Set up environment variables**:
   Add your database URI, secret key, and email credentials to your environment variables. You can add the following lines to your `.zshrc` file (or equivalent for your shell):
   ```sh
   export SECRET_KEY_DB="your_secret_key"
   export SQLALCHEMY_DATABASE_URI="your_database_uri"
   export MAIL_USERNAME="your_email_here"
   export MAIL_PASSWORD="your_email_password_here"
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

### Access the Application
- Open a web browser and go to `http://127.0.0.1:5000/` to view the job application form.

## Final Output
The final output is a fully functional job application web application that allows users to submit job applications and sends a confirmation email upon successful submission. The application includes a simple, styled form for applicants to fill out their details.

