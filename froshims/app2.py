from flask import Flask, render_template, request

app = Flask(__name__)
REGISTRANTS = {}
SPORTS = {
    "Basketball"
    "Soccer"
    "Ultimate Frisbee"
}

@app.route("/")
def index():
    # sports=SPORTS is what the sports the server will be supporting
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register:
    name = request.form.get("name")
    if not name:
        return render_template("failure.html")
    sport = request.form.get("sport")
    # It means you hacked me. Wont allow you to register
    if sport not in SPORTS:
        return render_template("failure.html")
    REGISTRANTS[name] = sport
    return render_template("success.html")

# To try check all registrants
@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)