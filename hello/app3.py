#Adding a bit of dynamism
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    # request.args is a dictionary that has value pairs that might have come through the url
    # requests comes with a function called get you can pass an argument that tells you the value you want to get
    # If there is no key it wont return a key error. Its just gonna return None. It can also take a default value
    name = request.args.get("name", "world")
    return render_template("index.html")