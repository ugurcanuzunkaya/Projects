# Job Application Django Project

## Overview
This project is a job application web application built with Django. It allows users to submit job applications through a form, and it sends a notification email upon submission. The application includes multiple pages and templates for different sections of the website.

## Key Libraries
- **Django**: The web framework used for building the application.
- **os**: Used for handling environment variables.
- **pathlib**: Used for handling file paths.
- **smtplib**: Used for sending emails.
- **ssl**: Used for creating a secure SSL context for email sending.

## Project Structure
```
project_django/
│
├── job_application/
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   ├── templates/
│   │   ├── about.html
│   │   ├── base.html
│   │   ├── homepage.html
│   │   └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── mysite/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── readme.md
```

## Explanation of Key Functions and Methods

### `manage.py`
- The command-line utility for administrative tasks.

### `mysite/settings.py`
- Configuration settings for the Django project, including installed apps, middleware, database settings, and email settings.

### `mysite/urls.py`
- URL configuration for the project, routing URLs to views.

### `mysite/wsgi.py`
- WSGI configuration for deploying the project.

### `job_application/views.py`
- `index`: Handles the job application form submission and sends a notification email.
- `about`: Renders the About Us page.
- `homepage`: Renders the homepage.

### `job_application/models.py`
- `Form`: Defines the model for storing job application data.

### `job_application/forms.py`
- `ApplicationForm`: Defines the form for job applications.

### `job_application/urls.py`
- URL configuration for the `job_application` app, routing URLs to views.

### `job_application/templates`
- Contains HTML templates for different sections of the website, including the base template, job application form, homepage, and about page.

## How to Use
1. **Set up the environment**:
   - Add your email credentials to your environment variables. You can add the following lines to your `.zshrc` file (or equivalent for your shell):
     ```
     export EMAIL_HOST_USER="your_email_here"
     export EMAIL_HOST_PASSWORD="your_email_password_here"
     ```

2. **Run the project**:
   - Apply migrations:
     ```
     python manage.py migrate
     ```
   - Create a superuser:
     ```
     python manage.py createsuperuser
     ```
   - Run the development server:
     ```
     python manage.py runserver
     ```

3. **Access the application**:
   - Open a web browser and go to `http://127.0.0.1:8000/` to view the job application form.

## Final Output
The final output is a fully functional job application web application that allows users to submit job applications, and sends a notification email upon successful submission. The application includes multiple pages, such as the homepage and about page, with a consistent layout and navigation.
