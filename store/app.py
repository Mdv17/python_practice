from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

# Configure app
app = Flask(__name__)

# Connect to database
db = SQL("sqlite:///store.db")

# Configure session
app.config("SESSION_PERMANENT") = False
app.config("SESSION_TYPE") = "filesystem"
Session(app)

@app.route("/")
def index():
    # Select all books from database
    books = db.execute("SELECT * FROM books")
    # Then rendering template called books.html passing as a placeholder for all books    
    return render_template("books.html", books=books)

# If the user submits via get or post
@app.route("/Cart", methods=["GET", "POST"])
def cart():

    # Ensure cart exists
    if "cart" not in session:
        # We gonna use a session object to store variable called cart. We are storing a cart key whose value is a list
        # This makes sure i have a least an empty list
        session["cart"] = []

    # POST
    if request.method == "POST":
        # Get id they posted
        id = request.form.get("id")
        # if is not empty
        if id:
            # Go into the shopping cart and append that id
            session["cart"].append(id)

        return redirect("/cart")

    # GET
    # This will output a comma selected list. Show me books in my cart
    books = db.execute("SELECT * FROM books WHERE id IN (?)", session["cart"])
    return render_template("cart.html", books=books)