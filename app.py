from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index_page():
   message = 'Добро пожаловать!'
   url = 'static/github_black_logo_icon_147128.png'
   return render_template('index.html', message=message, url=url)
