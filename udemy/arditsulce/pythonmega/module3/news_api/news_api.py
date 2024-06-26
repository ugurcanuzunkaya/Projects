import requests
import os
import pathlib
import json
from send_email import send_email


def change_dir_to_this_file():
    # getting the current working directory
    cwd = os.getcwd()
    path_of_this_file = pathlib.Path(__file__).parent
    if cwd != path_of_this_file:
        os.chdir(path_of_this_file)

change_dir_to_this_file()


topic = input('Enter a topic: ')
api_key = os.getenv('NEWSAPI_KEY')
url = f'https://newsapi.org/v2/everything?{topic}q=&from=2024-05-20&sortBy=publishedAt&apiKey={api_key}&language=en'

request = requests.get(url)
content = request.json()
content_json = json.dumps(content, indent=4)

with open('newstest.json', 'w') as f:
    f.write(content_json)

with open('news.txt', 'w') as f:
    for article in content['articles']:
        f.write("Subject: Today's News\n")
        f.write(article['title'])
        f.write('\n')
        f.write(article['description'] or 'No description available')
        f.write('\n')
        f.write(article['url'])
        f.write('\n')
        f.write('\n')


# Access the article titles and descriptions from the JSON file to create a mail body
mail_body = ''
for article in content['articles']:
    mail_body += article['title']
    mail_body += '\n'
    mail_body += article['description'] or 'No description available'
    mail_body += '\n\n'

mail_body = mail_body.encode('utf-8')
send_email(email=os.getenv('RECEIVER_MAIL'), subject='Today\'s News', message=mail_body)