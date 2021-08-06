from flask import request, Flask, make_response
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/read')
def read():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp

@app.route('/store')
def store():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.