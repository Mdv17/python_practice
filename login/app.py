from flask import Flask, redirect, render_template, request, session
from flask_session import session

# Configure app
app = Flask(__name__)

# Configure session
app.config("SESSION_PERMANENT") = False 
app.config("SESSION_TYPE") = "filesystem"
Session(app)

# If you are automatically redirected to login page if dont have those web cookies or you never logged in
@app.route("/")
def index():
    # If no name in shopping cart return the user to login
    if not session.get("name"):
        return redirect("/login")
    return render_template["index.html"]

# If the user visits login via get or post call login
@app.route("/login", methods=["GET", "POST"])
def login():
    # if the user submists via post
    if request.method == "POST":
        # store in special session variable that comes with flask a name key and store in it the user's name
        session["name"] = request.form.get("name")
        # Redirect the user to /
        return redirect("/")
    # if the user submits via get, show him the login screen
    return render_template("login.html")

# Clicks the logout link
@app.route("/logout")
def logout():
    # Change that key to be None
    session["name"] = None
    return redirect("/")