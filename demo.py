from flask import Flask
from taskid_middleware import taskid_middleware
app = Flask(__name__)

app.wsgi_app = taskid_middleware(app.wsgi_app)

@app.route('/roberto')
def roberto():
    return 'Roberto'

@app.route('/')
def hello_world():
    return 'Hello, World!'
