from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index_page():
   message = 'Добро пожаловать!'
   url = 'https://icon-icons.com/icons2/2428/PNG/512/github_black_logo_icon_147128.png'
   return render_template('index.html', message=message, url=url)
