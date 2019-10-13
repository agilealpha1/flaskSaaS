from flask import Flask, render_template,request, redirect,flash
from youtube_dl_master.youtube_dl import YoutubeDL
from youtube_dl_master.youtube_dl import *
from Forms import MusicSearchForm
from Forms import LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

"""
@app.route("login/",methods=['GET','POST'])

def index():
    form=form = LoginForm()
    search = MusicSearchForm(request.form)
"""
"""
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'cch'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)

"""
@app.route('/')
def home():
    return "welcome to first app"
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate():
         flash('Login requested for OpenID="%s", remember_me=%s' %(form.openid.data, str(form.remember_me.data)))
         return redirect('/index')

    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

if __name__ == "__main__":
    app.run(debug=True)
