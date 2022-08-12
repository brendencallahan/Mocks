import os
import requests
import urllib.parse

from cs50 import SQL
from flask import redirect, render_template, request, session
from functools import wraps
from datetime import datetime

db = SQL("sqlite:///finance.db")

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def lookup(symbol):
    """Look up quote for symbol."""

    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()
        return {
            "name": quote["companyName"],
            "price": float(quote["latestPrice"]),
            "symbol": quote["symbol"]
        }
    except (KeyError, TypeError, ValueError):
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"


def getPortfolio(userid):
    testPortfolio = db.execute("SELECT symbol, shares FROM portfolio WHERE id = ?", userid)
    return testPortfolio


def getCash(userid):
    cash = db.execute("SELECT cash FROM users WHERE id = ?", userid)[0]["cash"]
    return cash

def setCash(cash, total_price_setCash, userid):

    total_cash = round(cash + total_price_setCash, 2)

    db.execute("UPDATE users SET cash = ? WHERE id = ?", total_cash, userid)


def adjustPortfolio(userid, symbol, shares_wanted):

    # Get date for purchase history
    date_today_verbose = datetime.now()
    date_today = date_today_verbose.strftime("%d/%m/%Y/ %H:%M:%S")

    # Get stock price
    stock_info = lookup(symbol)
    price = stock_info["price"]

    cash = getCash(userid)

    if shares_wanted >= 1:
        total_price = round(price * shares_wanted, 2)
        total_price_setCash = round(price * shares_wanted * -1, 2)
        if total_price > cash:
            return apology("not enough cash", 403)
    else:
        total_price = round(price * shares_wanted * -1, 2)
        total_price_setCash = round(price * shares_wanted * -1, 2)



    try:
        shares_owned = db.execute("SELECT shares FROM portfolio WHERE symbol = ?", symbol)[0]["shares"]
    except (KeyError, TypeError, ValueError, IndexError):
        db.execute("INSERT INTO portfolio (id, symbol, shares) VALUES (?, ?, ?)", userid, symbol, shares_wanted)
        setCash(cash, total_price_setCash, userid)
        return goHome()

    if shares_owned <= 0:
        db.execute("DELETE FROM portfolio WHERE symbol = ?", symbol)

    if shares_owned + shares_wanted == 0:
        db.execute("DELETE FROM portfolio WHERE symbol = ?", symbol)
        setCash(cash, total_price_setCash, userid)
    elif shares_owned + shares_wanted < 0:
        return apology("not enough shares", 403)
    elif shares_owned + shares_wanted > 0:
        shares = shares_owned + shares_wanted
        db.execute("UPDATE portfolio SET shares = ? WHERE symbol = ? AND id = ?", shares, symbol, userid)
        setCash(cash, total_price_setCash, userid)

    # Insert into puchase history table on fincance database
    db.execute("INSERT INTO purchase_history (id, date, symbol, shares, price, total_price) VALUES (?, ?, ?, ?, ?, ?)", userid, date_today, symbol, shares_wanted, price, total_price)

    return goHome()



def goHome():
    cash = getCash(session["user_id"])

    portfolio = getPortfolio(session["user_id"])

    return render_template("index.html", cash=cash, portfolio=portfolio)