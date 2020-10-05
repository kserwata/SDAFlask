from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('index.html', name=name)


@app.route('/lista')
def lista():
    lista_uzytkownikow = [
        { "url": "index", "title": "Strona glowna" },
        { "url": "about", "title": "O nas"},
        { "url": "contact", "title": "Kontakt"}
    ]
    return render_template('lista.html', lista=lista_uzytkownikow)