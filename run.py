import os
from os import getenv
from flask import Flask

app = Flask(__name__)
messages = []

def add_messages(username, message):
    """This takes username and message and adds to list"""
    messages.append("{}: {}".format(username, message))


@app.route('/')
def index():
    """Main page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"


@app.route('/<username>')
def user(username):
    """Display chat message"""
    return "Welcome, {0}".format(username, messages)


@app.route('/<username>/<message>')
def send_message(username, message):
    """Create new message and redirect back to chat page"""
    return "{0}: {1}".format(username, message)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT', 5000)), debug=True)
