import re
from datetime import datetime

import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Enter a name after the URL. For example, localhost:5000/Bob"

@app.route("/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        ### complete code here
        clean_name = "Friend"

    content = f"Hello there, {clean_name}! It's {formatted_now}."
    
    return content

