import smtplib, ssl
import os
import pathlib


def change_dir_to_this_file():
    # getting the current working directory
    cwd = os.getcwd()
    path_of_this_file = pathlib.Path(__file__).parent
    if cwd != path_of_this_file:
        os.chdir(path_of_this_file)


def send_email(message):
    change_dir_to_this_file()
    host = "smtp.gmail.com"
    port = 465

    username = os.environ.get("USER_MAIL")
    password = os.environ.get("USER_MAIL_PASSWORD")

    receiver = os.environ.get("RECEIVER_MAIL")
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        
        server.sendmail(username, receiver, message)


if __name__ == "__main__":
    send_email("Subject:Test\n\nThis is a test email from Python.")