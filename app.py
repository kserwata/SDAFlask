from flask import Flask, render_template
import json
import os
app = Flask(__name__)

@app.route('/')
@app.route('/<page>')
def hello(page='index'):
    json_content = json.loads(open("content/pages/%s.json" % page).read())
    return render_template('static_page.html', content=json_content)


@app.route('/articles')
def articles():
    json_content = []
    for element in os.scandir("content/articles"):
        result = json.loads(open("content/articles/%s" % element.name).read())
        result['name'] = element.name.replace(".json", "")
        json_content.append(result)
    return render_template('articles.html', content=json_content)

@app.route('/article/<name>')
def article(name=''):
    json_content = json.loads(open("content/articles/%s.json" % name).read())
    return render_template('article.html', content=json_content)