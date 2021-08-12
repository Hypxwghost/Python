from flask import abort, redirect, url_for
from flask.app import Flask

app = Flask(__name__)

@app.route('/')
def index():
   return redirect(url_for('login'))

@app.route('/login')
def login():
   abort(504)
   thisIsNeverExecuted()