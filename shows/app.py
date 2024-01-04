# Searhes for shows
from flask import Flask, request, render_template
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///shows.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    # %...% this is a wild card. this gives all titles like in %..%
    shows = db.execute("SELECT * FROM shows WHERE title LIKE ?", "%" + request.args.get("q") + ("%"))
    return render_template("search.html", shows=shows)