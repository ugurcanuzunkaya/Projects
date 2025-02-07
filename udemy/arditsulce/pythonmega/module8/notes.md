# Days 50 - 56: Python Mega Course

##  Day 50

### Summary: Introduction to Building Web Applications with Flask and Django

In this video series, you'll learn to build web applications using two popular Python web frameworks: Flask and Django. Flask is ideal for smaller applications, while Django is better suited for larger projects. By the end of this series, you'll understand when to use each framework.

### Key Points - 1

- **Flask**: Best for relatively smaller web applications.
- **Django**: Preferred for larger, more complex web applications.
- **Learning Both**: Essential for web development to understand the strengths of each framework.

### Example App: Job Application Form with Flask

You'll build a simple web application using Flask that includes crucial aspects of web development:

1. **User Interaction**:
   - Users can fill out a job application form with their email, start date, and employment status.
   - Upon submission, users receive a success notification and an email confirmation.

2. **Email Notification**:
   - The server sends a confirmation email to the user from the server's email address.

3. **Database Storage**:
   - Employers can view submitted application data stored in the database.

### Steps Covered in the Series

1. **Structure the App**:
   - Create directories and files necessary for the Flask application.

2. **Add Code**:
   - Implement features incrementally while learning Flask in-depth.

### Practical Application

- Users will fill out the form on the web app.
- Example user email: `app8django@gmail.com`.
- Server email: `app8flask@gmail.com`.
- Users receive confirmation via email.
- Employers can access and review submitted data.

### Conclusion - 1

This series will guide you through the process of building a web application with Flask and understanding its core functionalities. Following this, you'll be better equipped to decide when to use Flask or Django for your web development projects.

----------------

### Summary: Starting a Flask Application

In this video, you'll learn how to create the structure of a Flask application and set up the basic components needed to handle HTTP requests and render HTML templates.

### Key Points - 2

1. **Project Setup**:
   - Create a new project in PyCharm.
   - Define the project directory (e.g., `App16_flask_form`).

2. **Flask App Structure**:
   - Create two important directories:
     - `static`: For static files like images, CSS, and JavaScript.
     - `templates`: For HTML templates.
   - Create a main Python file, typically named `app.py` or `main.py`.

3. **Creating HTML Template**:
   - Inside the `templates` directory, create an `index.html` file.
   - This file will contain the HTML code for the webpage.

4. **Writing Basic Flask Code**:
   - Import the Flask class:

     ```python
     from flask import Flask
     ```

   - Create a Flask app instance:

     ```python
     app = Flask(__name__)
     ```

   - Run the app with debug mode and a specified port:

     ```python
     if __name__ == '__main__':
         app.run(debug=True, port=5001)
     ```

   - Install Flask if not already installed by using PyCharm's package manager.

5. **Testing the App**:
   - Run the Flask app in PyCharm.
   - Check the output in the browser. Initially, you'll see a "Not Found" error, indicating the app is running but the routes are not yet defined.

6. **Handling HTTP Requests**:
   - Next steps involve writing Python code to handle HTTP requests and render HTML pages based on those requests.
   - For example, when a user visits the homepage (`/`), Flask will render `index.html`.

### Conclusion - 2

You have set up the basic structure of a Flask application and run the app to ensure it’s working. In the next video, you'll learn how to handle HTTP requests and render specific HTML pages based on those requests.

----------------

### Summary: Setting Up Routes and Rendering Templates in Flask

In this video, you'll learn how to handle HTTP requests in Flask and render HTML templates for the homepage. This involves setting up routes and ensuring the HTML content is properly displayed in the browser.

### Key Points - 3

1. **Handling HTTP Requests**:
   - Define routes using the `@app.route` decorator.
   - Example: Handle the homepage with `@app.route("/")`.

2. **Creating the Route**:
   - Define a function that will be called when the route is accessed.
   - Example:

     ```python
     @app.route("/")
     def index():
         return render_template("index.html")
     ```

3. **Importing Required Functions**:
   - Import the necessary functions from Flask:

     ```python
     from flask import Flask, render_template
     ```

4. **Running the App**:
   - Ensure the app is running by calling `app.run(debug=True, port=5001)`.
   - Check the browser to see the output.

5. **Writing HTML Content**:
   - Create a basic HTML structure in `index.html`:

     ```html
     <!DOCTYPE html>
     <html>
     <head>
         <meta charset="utf-8">
         <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
         <title>Job Application Form</title>
     </head>
     <body>
         <h1>Job Application Form</h1>
     </body>
     </html>
     ```

6. **Reloading the Page**:
   - Reload the browser to see the rendered HTML content.
   - Ensure the heading "Job Application Form" is displayed.

### Conclusion - 3

You have successfully set up a basic Flask application that handles HTTP requests and renders an HTML template for the homepage. In the next video, you'll add more content to the HTML frontend, specifically the input fields for the job application form.

----------------

### Summary: Building the Front End of a Flask Application Form

In this video, you will continue building the front end of your Flask application by adding input fields to the HTML form and making it more functional.

### Key Points - 4

1. **HTML Form Structure**:
   - The HTML form is created using form tags.
   - Inside the form, use label and input tags for user input fields.

2. **Adding Input Fields**:
   - Add fields for first name, last name, email, available start date, and current occupation.
   - Example for a text input field:

     ```html
     <div>
         <label for="first_name">First Name</label>
         <input type="text" id="first_name" name="first_name" required>
     </div>
     ```

   - Example for a date input field:

     ```html
     <div>
         <label for="date">Available Start Date</label>
         <input type="date" id="date" name="date" required>
     </div>
     ```

3. **Grouping Radio Buttons**:
   - Group radio buttons for current occupation so that only one can be selected at a time.
   - Example:

     ```html
     <div id="occupation">
         <label>Current Occupation</label><br>
         <input type="radio" id="employed" name="occupation" value="employed">
         <label for="employed">Employed</label><br>
         <input type="radio" id="unemployed" name="occupation" value="unemployed">
         <label for="unemployed">Unemployed</label><br>
         <input type="radio" id="self_employed" name="occupation" value="self_employed">
         <label for="self_employed">Self-Employed</label><br>
         <input type="radio" id="student" name="occupation" value="student">
         <label for="student">Student</label><br>
     </div>
     ```

4. **Adding a Submit Button**:
   - Add a button at the end of the form for submission.
   - Example:

     ```html
     <button type="submit">Submit</button>
     ```

5. **Testing the Form**:
   - Run the Flask app and ensure the form fields are displayed correctly.
   - Verify that only one radio button can be selected at a time.

6. **Next Steps**:
   - In the next video, you will add styles to the form using Bootstrap to improve its visual appeal.

### Conclusion - 4

You have successfully added various input fields to your HTML form, including text fields, email fields, date fields, and grouped radio buttons. In the next video, you will focus on styling the form using Bootstrap to enhance its visual presentation.

----------------

### Summary: Adding Bootstrap to Your Flask Application

In this video, you will learn how to enhance the visual appeal of your Flask application form using Bootstrap, a popular CSS framework.

### Key Points - 5

1. **Adding Bootstrap CSS**:
   - Include the Bootstrap CSS file by adding a link element inside the head tags of your HTML document.
   - Example:

     ```html
     <head>
         <meta charset="utf-8">
         <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
         <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">
     </head>
     ```

2. **Applying Bootstrap Classes**:
   - Use Bootstrap classes to style HTML elements.
   - Example for an h1 tag:

     ```html
     <h1 class="mt-4 mb-4">Job Application Form</h1>
     ```

3. **Creating a Container**:
   - Wrap your form content inside a div with the class "container".
   - Example:

     ```html
     <body>
         <div class="container">
             <!-- Form content goes here -->
         </div>
     </body>
     ```

4. **Styling Form Groups**:
   - Add the class "form-group mb-4" to each div containing an input field to create spacing.
   - Example:

     ```html
     <div class="form-group mb-4">
         <label for="first_name">First Name</label>
         <input type="text" id="first_name" name="first_name" class="form-control" required>
     </div>
     ```

5. **Styling Input Elements**:
   - Add the class "form-control" to input elements to style them using Bootstrap.
   - Example:

     ```html
     <input type="text" id="last_name" name="last_name" class="form-control" required>
     ```

6. **Vertical Radio Buttons**:
   - Use the "btn-group-vertical" class to stack radio buttons vertically.
   - Example:

     ```html
     <div id="occupation" class="btn-group-vertical">
         <input type="radio" id="employed" name="occupation" value="employed" class="btn-check form-control">
         <label for="employed" class="btn btn-outline-secondary">Employed</label>
         <input type="radio" id="unemployed" name="occupation" value="unemployed" class="btn-check form-control">
         <label for="unemployed" class="btn btn-outline-secondary">Unemployed</label>
         <input type="radio" id="self_employed" name="occupation" value="self_employed" class="btn-check form-control">
         <label for="self_employed" class="btn btn-outline-secondary">Self-Employed</label>
         <input type="radio" id="student" name="occupation" value="student" class="btn-check form-control">
         <label for="student" class="btn btn-outline-secondary">Student</label>
     </div>
     ```

7. **Styling the Submit Button**:
   - Use Bootstrap classes to style the submit button.
   - Example:

     ```html
     <button type="submit" class="btn btn-secondary mb-4">Submit</button>
     ```

8. **Including JavaScript for Notifications**:
   - Add JavaScript links before the closing body tag to enable notification messages.
   - Example:

     ```html
     <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js"></script>
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js"></script>
     ```

### Conclusion - 5

You have successfully integrated Bootstrap into your Flask application to improve the visual presentation of your form. With these enhancements, your form now looks more professional and user-friendly. In the next steps, you will continue to build on this foundation to create a fully functional application.

----------------

## Day 51

### Summary: Implementing the Submit Button in Your Flask Application

In this video, you will learn how to handle form submissions in your Flask application. When a user fills out the form and presses the submit button, the data will be sent to your server using a POST request. Here's how to set it up:

### Key Points - 6

1. **Understanding HTTP Requests**:
   - **GET Request**: When the user loads a URL, they are performing a GET request to retrieve data.
   - **POST Request**: When the user submits a form, they are performing a POST request to send data to the server.

2. **Setting Up the Form**:
   - Ensure your form in `index.html` supports POST requests by adding the `method` attribute:

     ```html
     <form method="POST">
         <!-- form elements -->
     </form>
     ```

3. **Handling Requests in Flask**:
   - Update your route to handle both GET and POST requests by adding a `methods` attribute:

     ```python
     @app.route('/', methods=['GET', 'POST'])
     def index():
         if request.method == 'POST':
             first_name = request.form['first_name']
             last_name = request.form['last_name']
             email = request.form['email']
             date = request.form['date']
             occupation = request.form['occupation']
             # Process the data
         return render_template('index.html')
     ```

4. **Importing Required Libraries**:
   - Ensure you have imported `request` from `flask`:

     ```python
     from flask import Flask, render_template, request
     ```

5. **Debugging the Form Submission**:
   - Use print statements or debugging tools to verify that the form data is being correctly captured.
   - Example:

     ```python
     if request.method == 'POST':
         first_name = request.form['first_name']
         print(first_name)  # Debugging
     ```

6. **Fixing the Submit Button Type**:
   - Ensure your submit button in the form is correctly set to type "submit":

     ```html
     <button type="submit" class="btn btn-secondary mb-4">Submit</button>
     ```

7. **Adding Value Attributes to Radio Buttons**:
   - Make sure each radio button has a value attribute to correctly capture the selected option:

     ```html
     <input type="radio" id="employed" name="occupation" value="employed" class="btn-check form-control" required>
     <label for="employed" class="btn btn-outline-secondary">Employed</label>
     ```

### Steps to Implement

1. **Update HTML Form**:
   - Add `method="POST"` to the form tag.
   - Ensure the submit button has `type="submit"`.

2. **Modify Flask Route**:
   - Update your route to handle both GET and POST methods.
   - Extract form data using `request.form`.

3. **Test and Debug**:
   - Use print statements or PyCharm's debugging tool to verify that form data is correctly received.

4. **Add Value to Radio Buttons**:
   - Ensure each radio button has a `value` attribute to capture the user's selection correctly.

### Example Code Snippets

**HTML Form Update**:

```html
<form method="POST">
    <div class="form-group mb-4">
        <label for="first_name">First Name</label>
        <input type="text" id="first_name" name="first_name" class="form-control" required>
    </div>
    <!-- Additional form elements -->
    <button type="submit" class="btn btn-secondary mb-4">Submit</button>
</form>
```

**Flask Route Update**:

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        date = request.form['date']
        occupation = request.form['occupation']
        print(first_name, last_name, email, date, occupation)  # Debugging
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
```

By following these steps, you will be able to capture and process form data in your Flask application, preparing you for further tasks such as storing data in a database and sending emails.

----------------

### Summary: Storing Form Data in an SQL Database with Flask

In this video, you will learn how to store user-entered data in an SQL database using Flask and SQLAlchemy. The steps include setting up the database, creating a model for the database, and storing form data.

### Key Points - 7

1. **Install Flask-SQLAlchemy**:
   - Open your terminal and install Flask-SQLAlchemy using pip:

     ```bash
     pip install flask-sqlalchemy
     ```

2. **Import Necessary Libraries**:
   - Import SQLAlchemy from the Flask-SQLAlchemy package:

     ```python
     from flask_sqlalchemy import SQLAlchemy
     ```

3. **Configure the Flask App**:
   - Set up the configuration for the SQLAlchemy database:

     ```python
     app = Flask(__name__)
     app.config['SECRET_KEY'] = 'myapplication123'
     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
     db = SQLAlchemy(app)
     ```

4. **Create a Database Model**:
   - Define a model class that represents the database table:

     ```python
     class Form(db.Model):
         id = db.Column(db.Integer, primary_key=True)
         first_name = db.Column(db.String(80))
         last_name = db.Column(db.String(80))
         email = db.Column(db.String(120))
         date = db.Column(db.Date)
         occupation = db.Column(db.String(80))
     ```

5. **Create the Database**:
   - Add the code to create the database:

     ```python
     with app.app_context():
         db.create_all()
     ```

6. **Run the App to Create the Database**:
   - Execute the app to create the `data.db` database file:

     ```python
     if __name__ == '__main__':
         app.run(debug=True, port=5001)
     ```

7. **Verify the Database**:
   - Use DB Browser for SQLite to open and inspect the database file (`data.db`) to ensure the table and columns have been created correctly.

### Example Code

**app.py**:

```python
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myapplication123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        date = request.form['date']
        occupation = request.form['occupation']
        # You will add code here to store data in the database
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
```

**index.html**:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">
    <title>Job Application Form</title>
</head>
<body class="container mt-5">
    <h1 class="mt-4 mb-4">Job Application Form</h1>
    <form method="POST">
        <div class="form-group mb-4">
            <label for="first_name">First Name</label>
            <input type="text" id="first_name" name="first_name" class="form-control" required>
        </div>
        <div class="form-group mb-4">
            <label for="last_name">Last Name</label>
            <input type="text" id="last_name" name="last_name" class="form-control" required>
        </div>
        <div class="form-group mb-4">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" class="form-control" required>
        </div>
        <div class="form-group mb-4">
            <label for="date">Available Start Date</label>
            <input type="date" id="date" name="date" class="form-control" required>
        </div>
        <div class="form-group mb-4">
            <label>Current Occupation</label><br>
            <input type="radio" id="employed" name="occupation" value="employed" class="btn-check form-control" required>
            <label for="employed" class="btn btn-outline-secondary">Employed</label><br>
            <input type="radio" id="unemployed" name="occupation" value="unemployed" class="btn-check form-control" required>
            <label for="unemployed" class="btn btn-outline-secondary">Unemployed</label><br>
            <input type="radio" id="self-employed" name="occupation" value="self-employed" class="btn-check form-control" required>
            <label for="self-employed" class="btn btn-outline-secondary">Self-Employed</label><br>
            <input type="radio" id="student" name="occupation" value="student" class="btn-check form-control" required>
            <label for="student" class="btn btn-outline-secondary">Student</label><br>
        </div>
        <button type="submit" class="btn btn-secondary mb-4">Submit</button>
    </form>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

By following these steps, you will be able to store user data in an SQLite database using Flask and SQLAlchemy. In the next video, you'll learn how to insert the form data into the database and send confirmation emails.

----------------

### Summary: Storing Form Data in an SQL Database with Flask - 2

In this video, you will learn how to store user-entered data in an SQL database using Flask and SQLAlchemy. The steps include setting up the database, creating a model for the database, and storing form data.

### Key Points - 7

1. **Install Flask-SQLAlchemy**:
   - Open your terminal and install Flask-SQLAlchemy using pip:

     ```bash
     pip install flask-sqlalchemy
     ```

2. **Import Necessary Libraries**:
   - Import SQLAlchemy from the Flask-SQLAlchemy package:

     ```python
     from flask_sqlalchemy import SQLAlchemy
     ```

3. **Configure the Flask App**:
   - Set up the configuration for the SQLAlchemy database:

     ```python
     app = Flask(__name__)
     app.config['SECRET_KEY'] = 'myapplication123'
     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
     db = SQLAlchemy(app)
     ```

4. **Create a Database Model**:
   - Define a model class that represents the database table:

     ```python
     class Form(db.Model):
         id = db.Column(db.Integer, primary_key=True)
         first_name = db.Column(db.String(80))
         last_name = db.Column(db.String(80))
         email = db.Column(db.String(120))
         date = db.Column(db.Date)
         occupation = db.Column(db.String(80))
     ```

5. **Create the Database**:
   - Add the code to create the database:

     ```python
     with app.app_context():
         db.create_all()
     ```

6. **Run the App to Create the Database**:
   - Execute the app to create the `data.db` database file:

     ```python
     if __name__ == '__main__':
         app.run(debug=True, port=5001)
     ```

7. **Verify the Database**:
   - Use DB Browser for SQLite to open and inspect the database file (`data.db`) to ensure the table and columns have been created correctly.

8. **Storing Form Data**:
   - Access the form data and store it in the database:

     ```python
     @app.route('/', methods=['GET', 'POST'])
     def index():
         if request.method == 'POST':
             first_name = request.form['first_name']
             last_name = request.form['last_name']
             email = request.form['email']
             date = request.form['date']
             occupation = request.form['occupation']
             
             # Convert string date to datetime object
             dateobj = datetime.strptime(date, '%Y-%m-%d')
             
             # Create a new Form instance
             form = Form(
                 first_name=first_name,
                 last_name=last_name,
                 email=email,
                 date=dateobj,
                 occupation=occupation
             )
             
             # Add to the session and commit to the database
             db.session.add(form)
             db.session.commit()
             
         return render_template('index.html')
     ```

### Example Code - 2

**app.py**:

```python
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myapplication123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        date = request.form['date']
        occupation = request.form['occupation']
        
        # Convert string date to datetime object
        dateobj = datetime.strptime(date, '%Y-%m-%d')
        
        # Create a new Form instance
        form = Form(
            first_name=first_name,
            last_name=last_name,
            email=email,
            date=dateobj,
            occupation=occupation
        )
        
        # Add to the session and commit to the database
        db.session.add(form)
        db.session.commit()
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
```

**index.html**:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">
    <title>Job Application Form</title>
</head>
<body class="container mt-5">
    <h1 class="mt-4 mb-4">Job Application Form</h1>
    <form method="POST">
        <div class="form-group mb-4">
            <label for="first_name">First Name</label>
            <input type="text" id="first_name" name="first_name" class="form-control" required>
        </div>
        <div class="form-group mb-4">
            <label for="last_name">Last Name</label>
            <input type="text" id="last_name" name="last_name" class="form-control" required>
        </div>
        <div class="form-group mb-4">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" class="form-control" required>
        </div>
        <div class="form-group mb-4">
            <label for="date">Available Start Date</label>
            <input type="date" id="date" name="date" class="form-control" required>
        </div>
        <div class="form-group mb-4">
            <label>Current Occupation</label><br>
            <input type="radio" id="employed" name="occupation" value="employed" class="btn-check form-control" required>
            <label for="employed" class="btn btn-outline-secondary">Employed</label><br>
            <input type="radio" id="unemployed" name="occupation" value="unemployed" class="btn-check form-control" required>
            <label for="unemployed" class="btn btn-outline-secondary">Unemployed</label><br>
            <input type="radio" id="self-employed" name="occupation" value="self-employed" class="btn-check form-control" required>
            <label for="self-employed" class="btn btn-outline-secondary">Self-Employed</label><br>
            <input type="radio" id="student" name="occupation" value="student" class="btn-check form-control" required>
            <label for="student" class="btn btn-outline-secondary">Student</label><br>
        </div>
        <button type="submit" class="btn btn-secondary mb-4">Submit</button>
    </form>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

By following these steps, you will be able to store user data in an SQLite database using Flask and SQLAlchemy. In the next video, you'll learn how to insert the form data into the database and send confirmation emails.

----------------

### Summary: Adding a Success Message to a Flask Form

In this video, we will enhance user experience by displaying a success message below the submit button when the form is submitted successfully. This helps in providing feedback to the users, making the web application more user-friendly.

### Key Points - 8

1. **Static Success Message**:
   - Initially, we add a static message below the submit button in `index.html`:

     ```html
     <div>
         Form was submitted successfully.
     </div>
     ```

2. **Dynamic Success Message**:
   - To make the message dynamic, we use Jinja2 syntax to conditionally display the message only after form submission:

     ```html
     {% with messages = get_flashed_messages() %}
         {% if messages %}
             <div>
                 {% for message in messages %}
                     {{ message }}
                 {% endfor %}
             </div>
         {% endif %}
     {% endwith %}
     ```

3. **Flash Messages in Flask**:
   - In `app.py`, import the `flash` function from Flask:

     ```python
     from flask import flash
     ```

   - Use the `flash` function to set a success message after the form data is saved to the database:

     ```python
     flash(f"{first_name}, your form was submitted successfully!", "success")
     ```

4. **Displaying Flash Messages in HTML**:
   - Enhance the HTML to display flash messages:

     ```html
     <form method="POST">
         <!-- form fields here -->
         <button type="submit" class="btn btn-secondary mb-4">Submit</button>
     </form>

     {% with messages = get_flashed_messages() %}
         {% if messages %}
             <div class="alert alert-success">
                 {% for message in messages %}
                     {{ message }}
                 {% endfor %}
             </div>
         {% endif %}
     {% endwith %}
     ```

### Example Code - 3

**app.py**:

```python
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myapplication123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        date = request.form['date']
        occupation = request.form['occupation']
        
        dateobj = datetime.strptime(date, '%Y-%m-%d')
        
        form = Form(
            first_name=first_name,
            last_name=last_name,
            email=email,
            date=dateobj,
            occupation=occupation
        )
        
        db.session.add(form)
        db.session.commit()
        
        flash(f"{first_name}, your form was submitted successfully!", "success")
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
```

**index.html**:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">
    <title>Job Application Form</title>
</head>
<body class="container mt-5">
    <h1 class="mt-4 mb-4">Job Application Form</h1>
    <form method="POST">
        <div class="form-group mb-4">
            <label for="first_name">First Name</label>
            <input type="text" id="first_name" name="first_name" class="form-control" required>
        </div>
        <div class="form-group mb-4">
            <label for="last_name">Last Name</label>
            <input type="text" id="last_name" name="last_name" class="form-control" required>
        </div>
        <div class="form-group mb-4">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" class="form-control" required>
        </div>
        <div class="form-group mb-4">
            <label for="date">Available Start Date</label>
            <input type="date" id="date" name="date" class="form-control" required>
        </div>
        <div class="form-group mb-4">
            <label>Current Occupation</label><br>
            <input type="radio" id="employed" name="occupation" value="employed" class="btn-check form-control" required>
            <label for="employed" class="btn btn-outline-secondary">Employed</label><br>
            <input type="radio" id="unemployed" name="occupation" value="unemployed" class="btn-check form-control" required>
            <label for="unemployed" class="btn btn-outline-secondary">Unemployed</label><br>
            <input type="radio" id="self-employed" name="occupation" value="self-employed" class="btn-check form-control" required>
            <label for="self-employed" class="btn btn-outline-secondary">Self-Employed</label><br>
            <input type="radio" id="student" name="occupation" value="student" class="btn-check form-control" required>
            <label for="student" class="btn btn-outline-secondary">Student</label><br>
        </div>
        <button type="submit" class="btn btn-secondary mb-4">Submit</button>
    </form>

    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <div class="alert alert-success">
                {% for message in messages %}
                    {{ message }}
                {% endfor %}
            </div>
        {% endif %}
    {% endwith %}
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

By following these steps, you will be able to display a success message to the user after form submission, enhancing the user experience. In the next video, we will learn how to send a confirmation email to the user.

----------------

### Summary: Sending Confirmation Emails in Flask Application

In this video, we will implement functionality to send a confirmation email to users once they submit the form. We will use the `Flask-Mail` extension to handle email sending.

### Steps

1. **Create a Gmail Account for the Application**:
   - Use a separate Gmail account for sending emails from your Flask application.
   - Enable two-step verification for this account and generate an app-specific password.

2. **Install Flask-Mail**:
   - Install the `Flask-Mail` extension using pip:

     ```sh
     pip install Flask-Mail
     ```

3. **Configure Flask-Mail**:
   - In `app.py`, configure the necessary email settings:

     ```python
     from flask_mail import Mail, Message

     app.config['MAIL_SERVER'] = 'smtp.gmail.com'
     app.config['MAIL_PORT'] = 465
     app.config['MAIL_USE_SSL'] = True
     app.config['MAIL_USERNAME'] = 'your_gmail@gmail.com'
     app.config['MAIL_PASSWORD'] = 'your_app_password'

     mail = Mail(app)
     ```

4. **Send Email in the Index Function**:
   - Modify the `index` function to send a confirmation email upon form submission:

     ```python
     @app.route('/', methods=['GET', 'POST'])
     def index():
         if request.method == 'POST':
             first_name = request.form['first_name']
             last_name = request.form['last_name']
             email = request.form['email']
             date = request.form['date']
             occupation = request.form['occupation']
             
             dateobj = datetime.strptime(date, '%Y-%m-%d')
             
             form = Form(
                 first_name=first_name,
                 last_name=last_name,
                 email=email,
                 date=dateobj,
                 occupation=occupation
             )
             
             db.session.add(form)
             db.session.commit()
             
             # Sending confirmation email
             message_body = (
                 f"Thank you for your submission, {first_name}.\n\n"
                 "Here are your data:\n"
                 f"First Name: {first_name}\n"
                 f"Last Name: {last_name}\n"
                 f"Email: {email}\n"
                 f"Available Start Date: {date}\n"
                 f"Occupation: {occupation}\n\n"
                 "Thank you!"
             )
             
             msg = Message("New Form Submission",
                           sender=app.config['MAIL_USERNAME'],
                           recipients=[email])
             msg.body = message_body
             mail.send(msg)
             
             flash(f"{first_name}, your form was submitted successfully!", "success")
             
         return render_template('index.html')
     ```

### Example Code - 4

**app.py**:

```python
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myapplication123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'your_gmail@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_app_password'

db = SQLAlchemy(app)
mail = Mail(app)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        date = request.form['date']
        occupation = request.form['occupation']
        
        dateobj = datetime.strptime(date, '%Y-%m-%d')
        
        form = Form(
            first_name=first_name,
            last_name=last_name,
            email=email,
            date=dateobj,
            occupation=occupation
        )
        
        db.session.add(form)
        db.session.commit()
        
        # Sending confirmation email
        message_body = (
            f"Thank you for your submission, {first_name}.\n\n"
            "Here are your data:\n"
            f"First Name: {first_name}\n"
            f"Last Name: {last_name}\n"
            f"Email: {email}\n"
            f"Available Start Date: {date}\n"
            f"Occupation: {occupation}\n\n"
            "Thank you!"
        )
        
        msg = Message("New Form Submission",
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[email])
        msg.body = message_body
        mail.send(msg)
        
        flash(f"{first_name}, your form was submitted successfully!", "success")
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
```

### Next Steps

- Move on to creating the same application using Django.
- Explore adding an admin interface to manage form submissions more efficiently.

By following these steps, you can now send confirmation emails to users upon form submission, enhancing the user experience of your web application.

## Day 52

### Setting Up a Django Project and Application

In this video, we will set up a Django project and application. We will go through installing Django, creating a new project, setting up an app, and running the Django server to see the default view in the browser.

#### Steps to Set Up a Django Project

1. **Create a New PyCharm Project**:
   - Create a new project in PyCharm and make sure you have a virtual environment set up.

2. **Install Django**:
   - Open the terminal in PyCharm and run the following command to install Django:

     ```sh
     pip install django
     ```

3. **Set Up a Django Project**:
   - In the terminal, navigate to your project directory and run the following command to create a new Django project:

     ```sh
     django-admin startproject mysite .
     ```

   - This will create a new directory named `mysite` with several Python files inside it.

4. **Create a Django App**:
   - In the terminal, run the following command to create a new Django app:

     ```sh
     python manage.py startapp job_application
     ```

   - This will create a new directory named `job_application` with several configuration files inside it.

5. **Register the App with the Project**:
   - Open the `settings.py` file located in the `mysite` directory.
   - Find the `INSTALLED_APPS` list and add `'job_application',` to it:

     ```python
     INSTALLED_APPS = [
         ...
         'job_application',
     ]
     ```

6. **Run the Django Server**:
   - In the terminal, run the following command to start the Django development server:

     ```sh
     python manage.py runserver
     ```

   - You should see output indicating the server is running and the URL to access your project (e.g., `http://127.0.0.1:8000/`).

7. **View the Default Django Page**:
   - Open a web browser and navigate to the URL provided in the terminal (e.g., `http://127.0.0.1:8000/`).
   - You should see the default Django welcome page.

### Example Commands and Configuration

**Terminal Commands**:

```sh
pip install django
django-admin startproject mysite .
python manage.py startapp job_application
python manage.py runserver
```

**settings.py**:

```python
INSTALLED_APPS = [
    ...
    'job_application',
]
```

### Next Steps - 2

- In the next videos, we will add content to our Django app, including setting up templates, models, and views, to build the job application form.

By following these steps, you have successfully set up a Django project and created an application within it. This sets the foundation for building a more complex web application with Django.

----------------

### Developing the Django App: Creating a Database Model

In this video, we will develop our Django app by creating a database model. We will use a bottom-up approach, starting with the database, then coding the backend, and finally coding the frontend.

#### Steps to Create a Database Model

1. **Stop the Django Server**:
   - In the terminal where the Django app is running, press `CTRL+C` to stop the server.

2. **Create a Database Model**:
   - Open the `models.py` file located in the `job_application` directory.
   - Delete the existing comments and create a new class named `Form`. This class should inherit from `models.Model`.
   - Define the fields of the database table (e.g., `first_name`, `last_name`, `email`, `date`, and `occupation`).

    ```python
    from django.db import models

    class Form(models.Model):
        first_name = models.CharField(max_length=80)
        last_name = models.CharField(max_length=80)
        email = models.EmailField()
        date = models.DateField()
        occupation = models.CharField(max_length=80)

        def __str__(self):
            return f"{self.first_name} {self.last_name}"
    ```

3. **Apply the Database Model to the Database**:
   - To apply the model to the database, we need to create and apply migrations.
   - Open the terminal and run the following command to create migrations:

     ```sh
     python manage.py makemigrations
     ```

   - This command generates a Python file inside the `migrations` directory under `job_application`.

4. **Migrate the Database**:
   - Run the following command to apply the migrations to the database:

     ```sh
     python manage.py migrate
     ```

   - This command will update the `db.sqlite3` database file with the new table schema.

5. **Verify the Database**:
   - Use the DB Browser for SQLite program to open the `db.sqlite3` file and verify that the `job_application_form` table has been created with the specified columns.

### Example Commands

**Terminal Commands**:

```sh
python manage.py makemigrations
python manage.py migrate
```

### DB Browser for SQLite

- Download and install the DB Browser for SQLite if you haven't already.
- Open the `db.sqlite3` file to verify the database schema.

### Next Steps - 3

- In the next videos, we will create the frontend by adding HTML templates, and then we will connect the frontend to the backend to complete the job application form.

By following these steps, we have successfully created and applied a database model to our Django project. This sets the foundation for building the rest of the application, where we will handle user inputs and store them in the database.

----------------

### Developing the Django App: Creating a Custom Homepage

#### Steps to Create a Custom Homepage

1. **Start the Django Server**:
   - In the terminal, run the following command to start the Django server:

     ```sh
     python manage.py runserver
     ```

2. **Create a View Function**:
   - Locate the `views.py` file in the `job_application` directory.
   - Define a view function named `index` with a `request` parameter. This function will return the rendered HTML template.

    ```python
    from django.shortcuts import render

    def index(request):
        return render(request, 'index.html')
    ```

3. **Create the HTML Template**:
   - Create a `templates` directory inside the `job_application` directory.
   - Inside the `templates` directory, create an HTML file named `index.html`.

    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Job Application Form</title>
    </head>
    <body>
        <h1>Hello</h1>
    </body>
    </html>
    ```

4. **Connect the View Function to a URL**:
   - Create a `urls.py` file in the `job_application` directory.
   - Import the necessary modules and connect the view function to the homepage URL.

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
    ]
    ```

5. **Include the App URLs in the Project URLs**:
   - Open the `urls.py` file in the `mysite` directory.
   - Include the URLs of the `job_application` app.

    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('job_application.urls')),
    ]
    ```

6. **Check for Errors**:
   - Ensure that all the necessary modules are imported, and the syntax is correct.
   - If you encounter an error related to the `render` function, ensure that you pass `request` as the first argument and the template name as the second argument.

#### Example Command to Run the Server

```sh
python manage.py runserver
```

#### Troubleshooting

- **Error: Missing Template Name**:
  - Ensure that the `render` function call in the view function includes `request` and `'index.html'` as arguments:

    ```python
    return render(request, 'index.html')
    ```

#### Expected Output

- After reloading the page, you should see the heading "Hello" displayed on the homepage.

By following these steps, you have successfully created a custom homepage for your Django app. Next, we will add a form to the homepage, accept user data, store it in the database, send a confirmation email, and create an admin interface to view the submitted data. Stay tuned for the next videos!

----------------

## Day 53

### Handling Form Submission in Django

#### Step 1: Setting Up Views for Form Handling

1. **Open the `views.py` file**:
   - Navigate to `job_application/views.py`.

2. **Modify the `index` view function**:
   - We need to handle both GET and POST requests in this function.
   - Add logic to capture form data on a POST request and save it to the database.

```python
from django.shortcuts import render, redirect
from .models import Form

def index(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        occupation = request.POST.get('occupation')
        
        form_entry = Form(
            first_name=first_name,
            last_name=last_name,
            email=email,
            date=date,
            occupation=occupation
        )
        form_entry.save()
        
        # Flash message
        request.session['message'] = 'Form was submitted successfully.'
        return redirect('index')
    
    # Check for flash message
    message = request.session.pop('message', None)
    
    return render(request, 'index.html', {'message': message})
```

#### Explanation

- **Import Statements**:
  - We import `redirect` from `django.shortcuts` to handle redirects.
  - We import our `Form` model to save data to the database.

- **Handling POST Request**:
  - We check if the request method is `POST`.
  - We extract data from the form using `request.POST.get`.
  - We create a new instance of the `Form` model with the extracted data and save it to the database.
  - We set a flash message in the session and redirect to the index page.

- **Handling GET Request**:
  - For a GET request, we render the `index.html` template.
  - We pass a flash message (if any) to the template.

#### Step 2: Updating HTML Template to Display Flash Messages

1. **Update the `index.html` file**:
   - Navigate to `job_application/templates/index.html`.
   - Add logic to display flash messages.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Job Application Form</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>
<div class="container">
    <h1>Job Application Form</h1>
    <form method="POST">
        {% csrf_token %}
        <div class="form-group">
            <label for="first_name">First Name</label>
            <input type="text" class="form-control" id="first_name" name="first_name" required>
        </div>
        <div class="form-group">
            <label for="last_name">Last Name</label>
            <input type="text" class="form-control" id="last_name" name="last_name" required>
        </div>
        <div class="form-group">
            <label for="email">Email</label>
            <input type="email" class="form-control" id="email" name="email" required>
        </div>
        <div class="form-group">
            <label for="date">Available Start Date</label>
            <input type="date" class="form-control" id="date" name="date" required>
        </div>
        <div class="form-group">
            <label>Current Occupation</label>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="occupation" id="employed" value="employed" required>
                <label class="form-check-label" for="employed">
                    Employed
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="occupation" id="unemployed" value="unemployed" required>
                <label class="form-check-label" for="unemployed">
                    Unemployed
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="occupation" id="self_employed" value="self_employed" required>
                <label class="form-check-label" for="self_employed">
                    Self-Employed
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="occupation" id="student" value="student" required>
                <label class="form-check-label" for="student">
                    Student
                </label>
            </div>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
    {% if message %}
    <div class="alert alert-success" role="alert">
        {{ message }}
    </div>
    {% endif %}
</div>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
</body>
</html>
```

#### Explanation - 2

- **Flash Message Display**:
  - We add a conditional block `{% if message %}` to check if there is a flash message.
  - If there is a message, we display it inside a Bootstrap alert component.

#### Step 3: Testing the Form Submission

1. **Run the Server**:
   - Start the server using the command `python manage.py runserver`.

2. **Visit the Webpage**:
   - Go to your browser and navigate to `http://127.0.0.1:8000/`.

3. **Fill Out the Form and Submit**:
   - Enter test data into the form fields and submit.

4. **Check the Flash Message**:
   - Ensure that the flash message "Form was submitted successfully." is displayed below the submit button.

5. **Verify Data in Database**:
   - Open the `db.sqlite3` database using DB Browser for SQLite.
   - Verify that the submitted form data is stored in the `job_application_form` table.

In the next video, we will implement functionality to send a confirmation email to the user upon form submission. Stay tuned!

----------------

### Storing Form Data in the Database

#### Step 1: Update `views.py` to Save Data to the Database

1. **Open the `views.py` file**:
   - Navigate to `job_application/views.py`.

2. **Modify the `index` view function**:
   - After capturing the form data, save it to the database using the `Form` model.

```python
from django.shortcuts import render, redirect
from .models import Form
from .forms import ApplicationForm

def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']
            
            form_entry = Form(
                first_name=first_name,
                last_name=last_name,
                email=email,
                date=date,
                occupation=occupation
            )
            form_entry.save()
            
            # Flash message
            request.session['message'] = 'Form was submitted successfully.'
            return redirect('index')
    
    # Check for flash message
    message = request.session.pop('message', None)
    
    return render(request, 'index.html', {'message': message})
```

#### Explanation - 3

- **Import Statements**:
  - We import our `Form` model to save data to the database.
  - We import our `ApplicationForm` to handle form validation and data extraction.

- **Saving Data to the Database**:
  - After extracting the form data, we create an instance of the `Form` model with the extracted data.
  - We call `save()` on the model instance to store the data in the database.

#### Step 2: Updating HTML Template to Display Flash Messages and Form Fields

1. **Update the `index.html` file**:
   - Navigate to `job_application/templates/index.html`.
   - Add logic to display flash messages.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Job Application Form</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>
<div class="container">
    <h1>Job Application Form</h1>
    <form method="POST">
        {% csrf_token %}
        <div class="form-group">
            <label for="first_name">First Name</label>
            <input type="text" class="form-control" id="first_name" name="first_name" required>
        </div>
        <div class="form-group">
            <label for="last_name">Last Name</label>
            <input type="text" class="form-control" id="last_name" name="last_name" required>
        </div>
        <div class="form-group">
            <label for="email">Email</label>
            <input type="email" class="form-control" id="email" name="email" required>
        </div>
        <div class="form-group">
            <label for="date">Available Start Date</label>
            <input type="date" class="form-control" id="date" name="date" required>
        </div>
        <div class="form-group">
            <label>Current Occupation</label>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="occupation" id="employed" value="employed" required>
                <label class="form-check-label" for="employed">
                    Employed
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="occupation" id="unemployed" value="unemployed" required>
                <label class="form-check-label" for="unemployed">
                    Unemployed
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="occupation" id="self_employed" value="self_employed" required>
                <label class="form-check-label" for="self_employed">
                    Self-Employed
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="occupation" id="student" value="student" required>
                <label class="form-check-label" for="student">
                    Student
                </label>
            </div>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
    {% if message %}
    <div class="alert alert-success" role="alert">
        {{ message }}
    </div>
    {% endif %}
</div>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
</body>
</html>
```

#### Explanation - 4

- **Flash Message Display**:
  - We add a conditional block `{% if message %}` to check if there is a flash message.
  - If there is a message, we display it inside a Bootstrap alert component.

#### Step 3: Testing the Form Submission and Database Storage

1. **Run the Server**:
   - Start the server using the command `python manage.py runserver`.

2. **Visit the Webpage**:
   - Go to your browser and navigate to `http://127.0.0.1:8000/`.

3. **Fill Out the Form and Submit**:
   - Enter test data into the form fields and submit.

4. **Check the Flash Message**:
   - Ensure that the flash message "Form was submitted successfully." is displayed below the submit button.

5. **Verify Data in Database**:
   - Open the `db.sqlite3` database using DB Browser for SQLite.
   - Verify that the submitted form data is stored in the `job_application_form` table.

In the next video, we will implement functionality to send a confirmation email to the user upon form submission. Stay tuned!

----------------

### Sending Confirmation Emails with Django

In this video, we will add functionality to send a confirmation email to the user upon form submission. Let's dive in.

#### Step 1: Install and Configure Django Email Backend

1. **Install Django Mailer**:
   - Ensure you have the Django mailer installed. If not, install it using the command:

     ```bash
     pip install django
     ```

2. **Update Settings**:
   - Open `mysite/settings.py` and configure the email backend settings. We'll use Gmail's SMTP server for this example.

```python
# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_gmail_account@gmail.com'
EMAIL_HOST_PASSWORD = 'your_gmail_app_password'
```

**Note**: Replace `'your_gmail_account@gmail.com'` with your Gmail account and `'your_gmail_app_password'` with the app password you generated from Gmail's security settings.

#### Step 2: Create the Email Sending Functionality

1. **Update `views.py`**:
   - After storing the form data in the database, send a confirmation email to the user.

```python
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Form
from .forms import ApplicationForm

def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']
            
            # Save form data to the database
            Form.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                date=date,
                occupation=occupation
            )
            
            # Send confirmation email
            send_mail(
                'Job Application Received',
                f'Thank you for your submission, {first_name}.\n\n'
                f'Here are the details you provided:\n'
                f'First Name: {first_name}\n'
                f'Last Name: {last_name}\n'
                f'Email: {email}\n'
                f'Available Start Date: {date}\n'
                f'Occupation: {occupation}\n\n'
                f'Thank you!',
                'your_gmail_account@gmail.com',
                [email],
                fail_silently=False,
            )
            
            messages.success(request, 'Form submitted successfully.')
            return redirect('index')
    
    message = request.session.pop('message', None)
    return render(request, 'index.html', {'message': message})
```

#### Explanation - 5

- **Import Statements**:
  - We import `send_mail` from `django.core.mail` to send the email.
  - We configure the email message content, including the recipient's email.

- **Sending the Email**:
  - We use `send_mail` to send the confirmation email with the relevant details provided by the user.

#### Step 3: Testing the Email Functionality

1. **Run the Server**:
   - Start the server using the command:

     ```bash
     python manage.py runserver
     ```

2. **Visit the Webpage**:
   - Go to your browser and navigate to `http://127.0.0.1:8000/`.

3. **Fill Out the Form and Submit**:
   - Enter test data into the form fields and submit.

4. **Check the Email**:
   - Check the recipient's email to ensure the confirmation email was received with the correct details.

### Conclusion

You have successfully added functionality to send a confirmation email to the user upon form submission. In the next video, we will implement the admin interface to view and manage submitted data more conveniently. Stay tuned!

----------------

Instructor: Hey, welcome back.

In this video, you will learn how to send a confirmation email through a Django form. When a user fills out the form and submits it, Django will send an email to the user's provided email address. This email will contain the data that the user submitted as a confirmation.

Let's start by configuring Django to send emails.

### Step 1: Configure Email Settings in Django

1. **Open `settings.py`**:
   - Located in your `mysite` directory.
   - Add the following configuration for the email backend using Gmail:

```python
# settings.py

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_gmail_account@gmail.com'
EMAIL_HOST_PASSWORD = 'your_gmail_app_password'
```

Replace `'your_gmail_account@gmail.com'` with your Gmail account and `'your_gmail_app_password'` with the app password generated from Gmail's security settings.

### Step 2: Generate an App Password in Gmail

1. **Go to your Google Account Settings**:
   - Navigate to the Security section.
   - Ensure that 2-Step Verification is turned on.
   - Under "Signing in to Google," select "App passwords."

2. **Generate an App Password**:
   - Select "Other" (Custom name).
   - Enter a name like "Django Application Form" and click "Generate."
   - Copy the generated password and use it as `EMAIL_HOST_PASSWORD` in `settings.py`.

### Step 3: Update Views to Send Email

1. **Import EmailMessage in `views.py`**:

```python
# views.py
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Form
from .forms import ApplicationForm

def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']
            
            # Save form data to the database
            Form.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                date=date,
                occupation=occupation
            )
            
            # Prepare email content
            message_body = (
                f"Thank you for your submission, {first_name}.\n\n"
                f"Here are the details you provided:\n"
                f"First Name: {first_name}\n"
                f"Last Name: {last_name}\n"
                f"Email: {email}\n"
                f"Available Start Date: {date}\n"
                f"Occupation: {occupation}\n\n"
                f"Thank you!"
            )
            
            # Create and send email
            email_message = EmailMessage(
                'Job Application Received',
                message_body,
                'your_gmail_account@gmail.com',
                [email],
            )
            email_message.send()
            
            # Show success message to the user
            messages.success(request, 'Form submitted successfully.')
            return redirect('index')
    
    return render(request, 'index.html')
```

#### Explanation - 6

- **Import Statements**:
  - We import `EmailMessage` from `django.core.mail` to handle sending emails.
- **Email Content**:
  - We create the email body using an f-string with user-submitted data.
- **Send Email**:
  - We create an instance of `EmailMessage` and call `send()` to dispatch the email.

### Step 4: Testing the Email Functionality

1. **Run the Server**:
   - Start the server using the command:

     ```bash
     python manage.py runserver
     ```

2. **Visit the Webpage**:
   - Go to your browser and navigate to `http://127.0.0.1:8000/`.

3. **Fill Out the Form and Submit**:
   - Enter test data into the form fields and submit.

4. **Check the Email**:
   - Check the recipient's email to ensure the confirmation email was received with the correct details.

### Conclusion - 7

You have successfully added functionality to send a confirmation email to the user upon form submission. This ensures that users receive a notification that their job application has been received along with the details they submitted. In the next videos, we will continue to enhance our Django application with more features. Stay tuned!

----------------

## Day 54

Ardit: Hey, welcome back.

In this video, you'll learn how to create and customize admin interfaces for your Django apps. So far, our Django app allows users to submit data through a form, but as admins, we don't have an easy way to access this data without using a third-party tool like DB Browser for SQLite. Django provides a built-in admin interface to make this process easier.

### Step 1: Setting Up the Admin Interface

1. **Navigate to `admin.py`**:
   - Located in the `job_application` folder.

2. **Register the Model**:
   - Import the `Form` model and register it with the admin site.

```python
# admin.py
from django.contrib import admin
from .models import Form

admin.site.register(Form)
```

### Step 2: Create a Superuser

1. **Open Terminal**:
   - Stop the server with `Ctrl + C` if it's running.

2. **Create Superuser**:
   - Run the following command:

     ```bash
     python manage.py createsuperuser
     ```

   - Enter a username, email, and password as prompted.

3. **Run the Server**:
   - Start the server again:

     ```bash
     python manage.py runserver
     ```

### Step 3: Access the Admin Interface

1. **Visit the Admin URL**:
   - Navigate to `http://127.0.0.1:8000/admin`.
   - Log in with the superuser credentials.

2. **View and Manage Data**:
   - You should see the `Form` model listed in the admin interface.
   - Click on `Forms` to see the submitted data.

### Step 4: Customizing the Admin Interface

To enhance the admin interface, you can customize it by modifying the `admin.py` file.

1. **Customize the List Display**:
   - To display more fields in the list view, use `FormAdmin` class.

    ```python
    # admin.py
    from django.contrib import admin
    from .models import Form

    class FormAdmin(admin.ModelAdmin):
        list_display = ('first_name', 'last_name', 'email', 'date', 'occupation')

    admin.site.register(Form, FormAdmin)
    ```

2. **Make Fields Read-Only**:
   - To make certain fields read-only, modify the `FormAdmin` class.

    ```python
    # admin.py
    from django.contrib import admin
    from .models import Form

    class FormAdmin(admin.ModelAdmin):
        list_display = ('first_name', 'last_name', 'email', 'date', 'occupation')
        readonly_fields = ('first_name', 'last_name', 'email', 'date', 'occupation')

    admin.site.register(Form, FormAdmin)
    ```

### Step 5: Testing the Custom Admin Interface

1. **Refresh the Admin Interface**:
   - Navigate to `http://127.0.0.1:8000/admin` and log in if prompted.

2. **View the Changes**:
   - You should see the list view displaying all specified fields.
   - When you click on a record, the specified fields should be read-only.

### Conclusion - 8

You've successfully set up and customized the Django admin interface for your application. This interface allows you to easily manage the data submitted by users without needing to use a third-party tool. In the next video, we will explore more advanced customizations and features for the admin interface.

Thanks for following along, and I'll see you in the next video.

----------------

Ardit: Hey, welcome back.

In this video, you'll learn how to create and customize admin interfaces for your Django apps. So far, our Django app allows users to submit data through a form, but as admins, we don't have an easy way to access this data without using a third-party tool like DB Browser for SQLite. Django provides a built-in admin interface to make this process easier.

### Step 1: Setting Up the Admin Interface - 2

1. **Navigate to `admin.py`**:
   - Located in the `job_application` folder.

2. **Register the Model**:
   - Import the `Form` model and register it with the admin site.

```python
# admin.py
from django.contrib import admin
from .models import Form

admin.site.register(Form)
```

### Step 2: Create a Superuser - 2

1. **Open Terminal**:
   - Stop the server with `Ctrl + C` if it's running.

2. **Create Superuser**:
   - Run the following command:

     ```bash
     python manage.py createsuperuser
     ```

   - Enter a username, email, and password as prompted.

3. **Run the Server**:
   - Start the server again:

     ```bash
     python manage.py runserver
     ```

### Step 3: Access the Admin Interface - 2

1. **Visit the Admin URL**:
   - Navigate to `http://127.0.0.1:8000/admin`.
   - Log in with the superuser credentials.

2. **View and Manage Data**:
   - You should see the `Form` model listed in the admin interface.
   - Click on `Forms` to see the submitted data.

### Step 4: Customizing the Admin Interface - 2

To enhance the admin interface, you can customize it by modifying the `admin.py` file.

1. **Customize the List Display**:
   - To display more fields in the list view, use `FormAdmin` class.

    ```python
    # admin.py
    from django.contrib import admin
    from .models import Form

    class FormAdmin(admin.ModelAdmin):
        list_display = ('first_name', 'last_name', 'email', 'date', 'occupation')

    admin.site.register(Form, FormAdmin)
    ```

2. **Make Fields Read-Only**:
   - To make certain fields read-only, modify the `FormAdmin` class.

    ```python
    # admin.py
    from django.contrib import admin
    from .models import Form

    class FormAdmin(admin.ModelAdmin):
        list_display = ('first_name', 'last_name', 'email', 'date', 'occupation')
        readonly_fields = ('first_name', 'last_name', 'email', 'date', 'occupation')

    admin.site.register(Form, FormAdmin)
    ```

### Step 5: Testing the Custom Admin Interface - 2

1. **Refresh the Admin Interface**:
   - Navigate to `http://127.0.0.1:8000/admin` and log in if prompted.

2. **View the Changes**:
   - You should see the list view displaying all specified fields.
   - When you click on a record, the specified fields should be read-only.

### Conclusion - 8

You've successfully set up and customized the Django admin interface for your application. This interface allows you to easily manage the data submitted by users without needing to use a third-party tool. In the next video, we will explore more advanced customizations and features for the admin interface.

Thanks for following along, and I'll see you in the next video.

----------------

Ardit: Hey, welcome back.

In this video, you'll learn how to add a navigation bar to your Django website. The navigation bar will be responsive, meaning it will adapt to different screen sizes, and will provide a consistent way to navigate between pages on your site.

### Step 1: Create a Base Template

1. **Duplicate `index.html`**:
   - Copy `index.html` and rename the copy to `base.html`.

2. **Create Additional Pages**:
   - Create a new file named `about.html`.

```html
<!-- about.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>About</title>
</head>
<body>
    <h1>About Us</h1>
</body>
</html>
```

### Step 2: Modify `base.html`

1. **Remove Specific Content**:
   - Remove the content specific to `index.html` from `base.html`. Keep the structure and metadata.

```html
<!-- base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        {% block content %}
        {% endblock %}
    </div>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
</body>
</html>
```

### Step 3: Extend `base.html` in Other Templates

1. **Modify `index.html`**:
   - Remove redundant code and extend `base.html`.

    ```html
    <!-- index.html -->
    {% extends "base.html" %}
    {% block title %}Job Application{% endblock %}
    {% block content %}
    <h1>Job Application Form</h1>
    <form method="post">
        {% csrf_token %}
        <!-- form fields here -->
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
    {% endblock %}
    ```

2. **Modify `about.html`**:
   - Extend `base.html`.

```html
<!-- about.html -->
{% extends "base.html" %}
{% block title %}About{% endblock %}
{% block content %}
<h1 class="mt-4 mb-4">About Us</h1>
<p>This is the about page.</p>
{% endblock %}
```

### Step 4: Add URLs for the About Page

1. **Create a View for the About Page**:
   - Add a function in `views.py` for the about page.

    ```python
    # views.py
    from django.shortcuts import render

    def about(request):
        return render(request, 'about.html')
    ```

2. **Update `urls.py`**:
   - Add a URL pattern for the about page.

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
```

### Step 5: Add a Navigation Bar

1. **Add Navigation Bar to `base.html`**:
   - Include a Bootstrap navigation bar in the `base.html` file.

```html
<!-- base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">Django App</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item active">
                    <a class="nav-link" href="{% url 'index' %}">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'about' %}">About</a>
                </li>
            </ul>
        </div>
    </nav>
    <div class="container">
        {% block content %}
        {% endblock %}
    </div>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
</body>
</html>
```

### Step 6: Test the Navigation

1. **Run the Server**:
   - Ensure your server is running:

     ```bash
     python manage.py runserver
     ```

2. **Test Navigation**:
   - Visit the homepage and about page using the navigation bar.

### Conclusion - 9

You've successfully added a responsive navigation bar to your Django website. This navigation bar allows users to easily navigate between different pages, enhancing the usability and user experience of your site. In the next video, we'll explore more advanced features and customizations for your Django application.

Thanks for following along, and I'll see you in the next video.

----------------

## Day 55

### Summary of Video on Building a Restaurant Menu Web App with Django

In this video, the instructor introduces a new project: building a restaurant menu web app using Django. The app will have functionalities for both restaurant customers and staff, offering a comprehensive learning experience in web development with Django.

### Key Takeaways - 1

- **Project Overview**
  - The app is designed for restaurant owners and customers.
  - Customers can view the menu and see the availability of dishes.
  - The backend admin interface allows restaurant staff to manage the menu.

- **Customer Interface**
  - Customers can view all dishes on the menu.
  - Availability of dishes is indicated (e.g., unavailable dishes are shown in strikethrough).
  - Customers can access the website via a QR code.

- **Admin Interface**
  - Restaurant staff can add new dishes with details such as name, description, price, category, author (cook), and availability status.
  - Staff can update the status of dishes to available or unavailable.
  - Changes in the admin interface are reflected on the customer interface in real-time.

- **Additional Features**
  - The app includes the functionality to generate a QR code that directs customers to the website.
  - Clicking on a dish in the menu takes the customer to a detailed page for that dish.
  - The structure of the app can be adapted to other uses, such as a blog.

- **Learning Outcomes**
  - Gain a deep understanding of Django and its capabilities.
  - Learn to create both front-end and back-end components of a web app.
  - Understand how to implement real-time updates and generate QR codes with Python.

This project offers a comprehensive learning opportunity in Django web development, focusing on building a practical application with real-world utility.

----------------

### Summary of Video on Generating a QR Code with Python

In this video, the instructor demonstrates how to generate a QR code using Python. The QR code will be used to direct users to the web app created with Django. This process involves using the `qrcode` library and the `pillow` library for image processing.

### Key Takeaways - 2

- **Project Setup**
  - Create a new Python project and a file named `qr.py`.
  - Ensure the correct Python interpreter is selected (e.g., Python 3.11).

- **Library Installation**
  - Install the `qrcode` library using `pip install qrcode`.
  - Install the `pillow` library using `pip install pillow`.

- **Generating the QR Code**
  - Import the `qrcode` library.
  - Use the `qrcode.make` function to generate a QR code that directs to the URL `127.0.0.1:8000`, which is the local address where the Django app will run.
  - Save the generated QR code as an image file using `image.save('qr.png')`.

- **Future Steps**
  - When deploying the app, update the URL in the `qr.py` file to the actual public domain of the deployed app and regenerate the QR code.

### Example Code for `qr.py`

```python
import qrcode

# URL to be encoded in the QR code
url = "http://127.0.0.1:8000"

# Generate QR code
qr_image = qrcode.make(url)

# Save the QR code as an image file
qr_image.save("qr.png")
```

### Instructions for Running the Code

1. **Ensure Virtual Environment is Activated**: Make sure the virtual environment (venv) is activated in your terminal.
2. **Run the Code**: Execute the `qr.py` script to generate the `qr.png` file.
3. **Scan the QR Code**: Use a mobile device to scan the generated QR code, which will direct you to the specified URL.

This setup prepares you to integrate the QR code with the Django web app, facilitating easy access for users.

----------------

### Summary of Video on Setting Up the Django App

In this video, the instructor walks through the steps to set up a new Django project and app. The process includes installing Django, creating a project and an app, connecting the app to the project, and running the project to view the default Django webpage.

### Key Takeaways - 3

- **Install Django**
  - Install Django using the command: `pip install django`.

- **Create a Django Project**
  - Create a new project using the command: `django-admin startproject mysite .`.
  - This command creates a directory named `mysite` with default Django project files.

- **Create a Django App**
  - Inside the project directory, create a new app using the command: `python manage.py startapp restaurant_menu`.
  - This creates a new directory named `restaurant_menu` with the app files.

- **Connect the App to the Project**
  - Open `mysite/settings.py`.
  - Add the app name `'restaurant_menu'` to the `INSTALLED_APPS` list.
  - Ensure it is correctly added as a string in the list with a trailing comma.

- **Run the Project**
  - Use the command: `python manage.py runserver` to start the Django development server.
  - Access the default Django webpage by clicking the provided URL (usually `http://127.0.0.1:8000/`).

### Example Commands and Code

1. **Install Django**

   ```sh
   pip install django
   ```

2. **Create a Django Project**

   ```sh
   django-admin startproject mysite .
   ```

3. **Create a Django App**

   ```sh
   python manage.py startapp restaurant_menu
   ```

4. **Modify `settings.py`**

   ```python
   # mysite/settings.py
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'restaurant_menu',  # Add your app here
   ]
   ```

5. **Run the Django Server**

   ```sh
   python manage.py runserver
   ```

By following these steps, you set up the foundation for the Django project and app, preparing it for further development where specific functionalities and URL mappings will be added.

----------------

### Summary of Video on Creating Database Models in Django

In this video, the instructor demonstrates how to set up the database models for the restaurant menu web app using Django. The models define the structure and relationships of the data that will be used in the application.

### Key Takeaways - 4

- **Database Model Setup**
  - Models define the structure of the database tables.
  - Use a bottom-up approach: start by defining the database models.

- **Creating the Model**
  - Define a class `Item` that inherits from `models.Model`.
  - Add fields to the model representing different attributes of the menu items.

### Example Code for `models.py`

```python
from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    MEAL_TYPE = (
        ('starters', 'Starters'),
        ('salads', 'Salads'),
        ('main_dishes', 'Main Dishes'),
        ('desserts', 'Desserts'),
    )
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    
    STATUS = (
        (0, 'Unavailable'),
        (1, 'Available'),
    )
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.meal
```

### Steps to Create and Migrate the Model

1. **Stop the Django Server**

   ```sh
   CTRL + C
   ```

2. **Navigate to the App Directory**

   ```sh
   cd restaurant_menu
   ```

3. **Edit `models.py`**
   - Define the `Item` class with fields for `meal`, `description`, `price`, `meal_type`, `author`, `status`, `date_created`, and `date_updated`.
   - Define choices for `meal_type` and `status`.
   - Use a `ForeignKey` to associate `Item` with the `User` model.

4. **Create and Apply Migrations**
   - Create migration files:

     ```sh
     python manage.py makemigrations
     ```

   - Apply migrations to create the database table:

     ```sh
     python manage.py migrate
     ```

5. **Verify the Database**
   - Use a database browser like `DB Browser for SQLite` to view the `db.sqlite3` file and ensure the `restaurant_menu_item` table has been created with the correct fields.

### Next Steps - 5

- After defining and migrating the database models, the next step is to create views for the models to display the data on the front end.

By following these steps, you set up the database structure for the restaurant menu app, allowing you to store and manage menu items efficiently.

----------------

## Day 56

### Summary of Video on Creating Views in Django

In this video, the instructor explains how to create views in Django using both class-based and function-based approaches. The focus is on setting up views that fetch data from the models and render it to the front end through HTML templates.

### Key Takeaways - 5

- **Class-Based Views**
  - **MenuList View**: A class-based view to display a list of menu items.
  - **MenuItemDetail View**: A class-based view to display details of a specific menu item.

- **Steps to Create Views**
  1. **Define Views in `views.py`**
     - Use class-based views for a cleaner and more organized codebase.
  2. **Connect Views to Templates**
     - Specify the template name for each view.
  3. **Setup URLs**
     - Map URLs to the corresponding views in `urls.py`.
  4. **Create HTML Templates**
     - Create HTML files to render the data fetched by the views.

### Example Code for `views.py`

```python
from django.shortcuts import render
from django.views import generic
from .models import Item

class MenuList(generic.ListView):
    queryset = Item.objects.order_by('-date_created')
    template_name = 'index.html'

class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = 'menu_item_detail.html'
```

### Example Code for `urls.py`

```python
# restaurant_menu/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),
    path('<int:pk>/', views.MenuItemDetail.as_view(), name='menu_item_detail'),
]
```

### Example Code for Main `urls.py`

```python
# mysite/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant_menu.urls')),
]
```

### Creating HTML Templates

1. **Index Template**

   ```html
   <!-- restaurant_menu/templates/index.html -->
   <!DOCTYPE html>
   <html>
   <head>
       <title>Restaurant Menu</title>
   </head>
   <body>
       <h1>Restaurant Menu</h1>
       <ul>
           {% for item in object_list %}
               <li><a href="{% url 'menu_item_detail' item.pk %}">{{ item.meal }}</a> - {{ item.price }}</li>
           {% endfor %}
       </ul>
   </body>
   </html>
   ```

2. **Detail Template**

   ```html
   <!-- restaurant_menu/templates/menu_item_detail.html -->
   <!DOCTYPE html>
   <html>
   <head>
       <title>Menu Item Detail</title>
   </head>
   <body>
       <h1>{{ object.meal }}</h1>
       <p>{{ object.description }}</p>
       <p>Price: {{ object.price }}</p>
   </body>
   </html>
   ```

### Steps to Ensure Templates are Located Correctly

1. **Create `templates` Directory**
   - Create a `templates` directory inside the `restaurant_menu` app directory.
2. **Move Templates Inside `templates` Directory**
   - Place `index.html` and `menu_item_detail.html` inside the `templates` directory.

### Troubleshooting Tips

- **Template Not Found Error**
  - Ensure that the `templates` directory is correctly located inside the `restaurant_menu` app directory.
  - Alternatively, specify the path in the `DIRS` key in `settings.py` if using a global `templates` directory.

By following these steps, you set up class-based views in Django, link them to the appropriate templates, and ensure that the data is correctly fetched from the database and displayed on the front end.

----------------

### Summary of Video on Context in Django

In this video, the instructor introduces the concept of context in Django, explaining how to pass data from the backend (views.py) to the frontend (index.html). Context in Django allows you to send data from your Python code to your HTML templates, enabling dynamic content rendering.

### Key Takeaways

- **Context Concept**
  - Context is a dictionary containing keys and values.
  - Keys in the context dictionary can be accessed as variables in the HTML template.

- **Passing Data from Python to HTML**
  - Use the `get_context_data` method in class-based views to define the context.
  - The context dictionary can contain any data you want to pass to the template.

### Example Code for Context Implementation

#### views.py

```python
from django.shortcuts import render
from django.views import generic
from .models import Item

class MenuList(generic.ListView):
    queryset = Item.objects.order_by('-date_created')
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meals'] = ['Pizza', 'Pasta']  # Static example data
        context['ingredients'] = ['Tomato', 'Cheese']  # Static example data
        return context
```

#### index.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Restaurant Menu</title>
</head>
<body>
    <h1>Restaurant Menu</h1>
    <h3>Meals:</h3>
    <ul>
        {% for meal in meals %}
            <li>{{ meal }}</li>
        {% endfor %}
    </ul>
    <h3>Ingredients:</h3>
    <ul>
        {% for ingredient in ingredients %}
            <li>{{ ingredient }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Steps to Implement Context

1. **Define the Context in Views**
   - Override the `get_context_data` method in the class-based view.
   - Create a context dictionary and add keys and values.

2. **Access Context in Templates**
   - Use Django template tags to access the context variables in the HTML template.
   - Iterate over lists or display individual variables as needed.

### Practical Example

- **Static Data Example**
  - Define static data in the context for demonstration purposes.
  - Pass a list of meals and ingredients to the template.

- **Accessing Data in Templates**
  - Use the Jinja2 syntax (`{{ variable }}`) to display context variables.
  - Use `{% for variable in list %}` to iterate over lists.

### Next Steps - 6

- **Admin Interface**
  - Create an admin interface to add records to the database.
  - Fetch real data from the database and pass it to the template using context.

By understanding and utilizing context in Django, you can dynamically render data from your database or backend logic to the frontend, enhancing the interactivity and usability of your web application.

----------------
