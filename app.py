import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "GET":
        return render_template("buy.html")

    #Check for valid input (with lookup)
    stock_name = request.form.get("stock_name")
    shares_wanted = request.form.get("shares_wanted")

    if not stock_name or not shares_wanted:
        return apology("must enter valid Symbol", 403)

    stock_info = lookup(stock_name)
    if not stock_info:
        return apology("must enter valid Symbol", 403)

    cash_dict = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]
    cash = cash_dict["cash"]

    price = stock_info["price"]

    if (cash - price) > 0:
        cash = cash - price
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, session["user_id"])
        db.execute("")
    else:
        return apology("not enough money for this purchase", 403)
    return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must enter username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must enter password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""


    if request.method == "GET":
        return render_template("quote.html")

    # Check for symbol
    if not request.form.get("stock_name"):
        return apology("must enter name", 403)

    # Lookup clients requested stock
    stock_name = request.form.get("stock_name")
    stock_info = lookup(stock_name)

    # Check for valid symbol
    if not stock_info:
        return apology("must enter valid symbol", 403)

    # Insert stock info into html and render quoted.html
    name = stock_info["name"]
    price = stock_info["price"]
    symbol = stock_info["symbol"]
    return render_template("quoted.html", name=name, price=price, symbol=symbol)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user with encrpyted password"""


    if request.method == "GET":
        return render_template("register.html")

    # Check for valid username/password
    if not request.form.get("username"):
        return apology("must enter Username", 403)
    if not request.form.get("password") or not request.form.get("confirmation_password") or request.form.get("password") != request.form.get("confirmation_password"):
        return apology("must enter Password", 403)

    # Encrypt password
    hash_password = generate_password_hash(request.form.get("password"), method="sha256", salt_length=4)

    # Update database with new user
    db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get("username"), hash_password)

    return render_template("login.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")
