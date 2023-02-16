from flask import Flask, url_for, render_template
from flask_wtf import FlaskForm

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('training.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('base.html', prof=prof.lower())


@app.route('/list_prof/<lst>')
def list_prof(lst):
    professions = ['Пилот', 'Штурман', 'Строитель', 'ученый', 'инженер']
    return render_template('list_prof.html', lst=lst, professions=professions)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')