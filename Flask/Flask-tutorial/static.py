import re
from flask import Flask, app, render_template
from flask import url_for

app = Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html')
   
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
