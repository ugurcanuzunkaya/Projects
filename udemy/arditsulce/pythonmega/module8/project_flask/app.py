from mailbox import Message
from re import sub
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import os
import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY_DB')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_SSL'] = True

db = SQLAlchemy(app)

mail = Mail(app)


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    available_date = db.Column(db.Date, nullable=False)
    occupation = db.Column(db.String(50), nullable=False)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        available_date = request.form['available_date']
        available_date = datetime.datetime.strptime(available_date, '%Y-%m-%d').date()
        occupation = request.form['occupation']

        form = Form(first_name=first_name, last_name=last_name, email=email, available_date=available_date, occupation=occupation)
        db.session.add(form)
        db.session.commit()

        message_body = f'Thank you {first_name} {last_name} for submitting your form! We will contact you soon to schedule an interview.' 
        + f'Your available date is {available_date} and your occupation is {occupation}. Best regards, Company X.'
        
        message = Message(subject='Form Submission',
                        sender=app.config['MAIL_USERNAME'],
                        recipients=[email],
                        body=message_body)
        
        mail.send(message)

        flash(f'Thank you {first_name} {last_name} for submitting your form!', 'success')


    return render_template('index.html')



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5000)