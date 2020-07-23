import os
from os import getenv
from flask import Flask

app = Flask (__name__)

@app.route('/')
def index():
    return "<h1>Hello, There!</h1>"

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT', 5000)), debug=True)