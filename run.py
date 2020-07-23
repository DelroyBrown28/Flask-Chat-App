import os
from datetime import datetime
from os import getenv
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "RandoString123"
messages = []


def add_messages(username, message):
    """This takes username and message and adds to list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}): {}: {}".format(now, username, message))


def get_all_messages():
    """Gets all messages and seperates using a 'br'"""
    return "<br>".join(messages)


@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])

    return render_template('index.html')


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
