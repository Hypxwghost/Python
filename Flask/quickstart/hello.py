from flask import Flask
from flask import url_for
from flask.wrappers import Request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
   return 'index'

@app.route('/login')
def login():
    if Request.method == 'POST':
       return 'doTheLogin()'
    else:
        return 'showTheLoginForm()'

@app.route('/user/<username>')  
def profile(username):
   return f'{escape(username)}\'s profile'

@app.route('/post/<int:post_id>')
def showPost(post_id):
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def showSubpath(subpath):
    return f'Subpath {escape(subpath)}'

@app.route('/projects/')
def projects():
   return 'The project page'

@app.route('/about')
def about():
    return "The about page"

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Ghoste'))
    print(url_for('showPost', post_id=10))
    print(url_for('showSubpath', subpath='Hypxwghost/python/'))
    print(url_for('projects'))
    print(url_for('about'))