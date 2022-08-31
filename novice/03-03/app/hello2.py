from asyncore import read
from pickle import GET
from venv import create
from flask import Flask
app = Flask(__name__)

from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='alfi'))

if __name__ == "__main__":
    app.run()      

'''
Create = POST 
Read = GET   
Update = PUT
Delete = DELETE 
'''