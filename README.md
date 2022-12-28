# Mocks
## https://mocks.up.railway.app
### To test
### username: test
### password: 123

(Data may not persist if server provider restarts)


## (Mock Stocks, "Where everything's made up and the points don't matter")

### Look-up, buy, and sell stocks with functioning login written in Flask.

This was an assignment for Harvard's Intro to Computer Science course. It uses fake money but real data. The only provided code was Bootstrap for the nav bar as well as several small functions. Everything else was written by me in Python.


## What I did:

### Stored login info using SQLite

Using Flask and SQLite3 I stored the salted hash instead of the user's password. I also stored the username for obvious reasons. :)


![Screenshot 2022-08-02 104037](https://user-images.githubusercontent.com/47364240/182441788-b8e3b82c-155c-4367-a174-2d87b1a71bf5.png)


![Screenshot 2022-08-02 105407](https://user-images.githubusercontent.com/47364240/182441626-6c227fe4-b1f1-4233-bfa4-df3ca72afe7f.png)


### Implemented look-up feature

Added ability to see a company's current share price by looking up their symbol (i.e NFLX for Netflix) using IEX's API then displayed this JSON data using a table and the Jinja templating language.


![Screenshot 2022-08-12 161008](https://user-images.githubusercontent.com/47364240/184456194-7af366b5-4bf0-4548-92ec-b821b9f89fb2.png)



### Wrote buy/sell functionality

Also added ability to buy and sell desired number of shares for any given symbol at current market price using IEX's API. 


![Screenshot 2022-08-12 161030](https://user-images.githubusercontent.com/47364240/184456220-14c50bd8-1042-475c-99b0-7a8ee4bc0f4b.png)

![Screenshot 2022-08-12 161118](https://user-images.githubusercontent.com/47364240/184456225-5b162262-760e-440c-a7ed-08faebf8c96d.png)


### Allowed users to see a breakdown of their portfolio

Added main 'hub' that lets users see the current price of all their shares as well as their current account balance. 


![Screenshot 2022-08-12 161050](https://user-images.githubusercontent.com/47364240/184456231-0daada41-0f98-467b-8da7-19a86f66f99e.png)


### Implemented a history page where users can see all previous transactions


![Screenshot 2022-08-12 190328](https://user-images.githubusercontent.com/47364240/184464434-689a915d-6d80-4b51-bea6-aa27c691d33a.png)


## To run locally:

``` 
$ git clone https://github.com/brendencallahan/Mocks
```
```
$ pip3 install cs50 flask flask_sessions
```
```
$ export API_KEY=xxxxxxxxxxxxxxxxxxxxxxx
```
```
$ flask run
```


(Visit assignment page here, no login required) https://cs50.harvard.edu/x/2022/psets/9/finance/


* The money used in this is not real. You start with $10,000 fake USD when you register. :)
