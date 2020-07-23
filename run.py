import os
from os import getenv
from flask import Flask, redirect

app = Flask(__name__)
messages = []

def add_messages(username, message):
    """This takes username and message and adds to list"""
    messages.append("{}: {}".format(username, message))


def get_all_messages():
    """Gets all messages and seperates using a 'br'"""
    return "<br>".join(messages)


@app.route('/')
def index():
    """Main page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"


@app.route('/<username>')
def user(username):
    """Display chat message"""
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())


@app.route("/<username>/<message>")
def send_message(username, message):
    """Create new message and redirect back to chat page"""
    add_messages(username, message)
    return redirect("/" + username)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT', 5000)), debug=True)
