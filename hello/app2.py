#Adding a bit of dynamism
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    # request.args is a dictionary that has value pairs that might have come through the url
    # check if there is akey in request.arg else ste name to world
    if "name" in request.args:
        name = request.args["name"]
    else:
        name = "world"
    return render_template("index.html")