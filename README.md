# Mocks
## (Mock Stocks, "Where everythings made up and the points don't matter"*)

### Lookup, buy, and sell stocks with functioning login written in Flask.

This was an assignment for Harvard's Intro to Computer Science course. The only provided code was Bootstrap for the nav bar as well as several small functions. Everything else was written by me in Python using Flask and SQLite.

## What I did:

### Stored login info using SQLite

Using Flask and SQLite3 I stored the salted hash instead of the user's password. I also stored the user's name for obvious reasons. :)

### Implemented lookup feature

Added ability to see a company's current share price by looking up their symbol (i.e NFLX for Netflix) using IEX's API then displayed this JSON data using a table and the Jinja templating language.


### Wrote buy/sell functionality

Also added ability to buy and sell desired number of shares for any given symbol at current market price using IEX's API. 

### Allowed users to see all current holdings/balances

Added main 'hub' that lets user's see the current price of all their shares as well as their current account balance. 

(Visit assignment page here, no login required) https://cs50.harvard.edu/x/2022/psets/9/finance/


* The money used in this is fake. You start with $10,000 fake USD when you register. There is no way to earn more money or anything like that. :)
