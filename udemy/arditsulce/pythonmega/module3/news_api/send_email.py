import smtplib
import ssl
import os


def send_email(email, subject, message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("USER_MAIL")
    password = os.getenv("USER_MAIL_PASSWORD")

    receiver = email
    context = ssl.create_default_context()

    print(f"username={username}, password={password}")

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, f"Subject: {subject}\n\n{message}")

