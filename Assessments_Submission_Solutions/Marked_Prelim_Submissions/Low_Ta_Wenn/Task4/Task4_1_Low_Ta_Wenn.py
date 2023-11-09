import sqlite3
from flask import Flask, render_template, request

app = Flask("__name__")

@app.route("/")
def root():
    con = sqlite3.connect("TASK4.db")
    events = list(con.execute("select name, artist, type, id from Event"))
    con.close()
    return render_template("root.html", events = events)

@app.route("/details")
def details(event_id):
    event_id = event_id
    con = sqlite3.connect("TASK4.db")
    details = list(con.execute("select date, time, venue from TimeTable where event_id=?", (event_id,)))
    con.close()
    return render_template("details.html", details = details)

app.run()
## what is the purpose of line 15 ???!!
## incorrect url in root.html to create dynamic url
## how do you pass the event_id to details()??
## NO generated html output
# 6m
'''
- use css [1]
- landing page html [1]
- db open/close [1]
- landing page view function [1]
- SQL select all events [1]
- SQL select dates for event [1]
'''