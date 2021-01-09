from flask import Flask

from taskid import Middleware

# Explicitly load tasks
import tasks.get_emails

app = Flask(__name__)

# Start the Taskid middleware
app.wsgi_app = Middleware(app.wsgi_app)

@app.route('/')
def hello_world():
    return 'Hello, World!'
