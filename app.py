from flask import Flask, render_template, request
from flask_mail import Mail, Message
import json
import os
app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False


mail = Mail(app)

def get_menu():
    return json.loads(open("content/menu.json").read())

@app.route('/')
@app.route('/<page>', methods=['GET', 'POST'])
def hello(page='index'):

    if request.method == "POST":
        sender = request.form['sender']
        title = request.form['title']
        content = request.form['content']
        msg = Message(subject=title,
                    body=content,
                    sender="%s@example.com" % sender,
                    recipients=["sda@kurs.pl"])
        mail.send(msg)
        print(sender, title, content)

    json_content = json.loads(open("content/pages/%s.json" % page).read())
    return render_template('static_page.html', content=json_content, menu=get_menu())


@app.route('/articles')
def articles():
    json_content = []
    for element in os.scandir("content/articles"):
        result = json.loads(open("content/articles/%s" % element.name).read())
        result['name'] = element.name.replace(".json", "")
        json_content.append(result)
    return render_template('articles.html', content=json_content, menu=get_menu())

@app.route('/article/<name>')
def article(name=''):
    json_content = json.loads(open("content/articles/%s.json" % name).read())
    return render_template('article.html', content=json_content, menu=get_menu())