from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index_page():
   message = 'Добро пожаловать!'
   url = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.flaticon.com%2Ffree-icon%2Fgithub-logo_25231&psig=AOvVaw3mjTCC5S3CILtwV1zvffkx&ust=1740554781613000&source=images&cd=vfe&opi=89978449&ved=0CBYQjRxqFwoTCOil-f6l3osDFQAAAAAdAAAAABAE'
   return render_template('index.html', message=message, url=url)
