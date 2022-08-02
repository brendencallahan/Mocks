# Mocks
## (Mock Stocks, "Where everythings made up and the points don't matter"*)

### Lookup, buy, and sell stocks with functioning login written in Flask.

This was an assignment for Harvard's Intro to Computer Science course. The only provided code was Bootstrap for the nav bar as well as several small functions. Everything else was written by me in Python using Flask and SQLite.

## What I did:

### Stored login info using SQLite

Using Flask and SQLite3 I stored the salted hash instead of the user's password. I also stored the username for obvious reasons. :)


![Screenshot 2022-08-02 104037](https://user-images.githubusercontent.com/47364240/182441788-b8e3b82c-155c-4367-a174-2d87b1a71bf5.png)


![Screenshot 2022-08-02 105407](https://user-images.githubusercontent.com/47364240/182441626-6c227fe4-b1f1-4233-bfa4-df3ca72afe7f.png)


### Implemented lookup feature

Added ability to see a company's current share price by looking up their symbol (i.e NFLX for Netflix) using IEX's API then displayed this JSON data using a table and the Jinja templating language.


![Screenshot 2022-08-02 104020](https://user-images.githubusercontent.com/47364240/182441836-7d575e47-5e3b-4b41-a9f3-b4bf31937002.png)


### Wrote buy/sell functionality

Also added ability to buy and sell desired number of shares for any given symbol at current market price using IEX's API. 

### Allowed users to see all current holdings/balances

Added main 'hub' that lets user's see the current price of all their shares as well as their current account balance. 

(Visit assignment page here, no login required) https://cs50.harvard.edu/x/2022/psets/9/finance/


* The money used in this is fake. You start with $10,000 fake USD when you register. There is no way to earn more money or anything like that. :)
