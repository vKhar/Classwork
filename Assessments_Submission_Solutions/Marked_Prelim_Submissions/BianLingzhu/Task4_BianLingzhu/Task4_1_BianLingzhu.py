from flask import Flask, render_template

import sqlite3
def openDB(db):
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    return con

app = Flask(__name__)

@app.route('/')
def root():
    con = openDB('TASK4.db')
    cur = con.execute('SELECT * FROM Event')
    rows = cur.fetchall()
    return render_template('Task4_1a.html',rows = rows)

@app.route(f'/dates/{id}')
def dates(id):
    cur = con.execute('SELECT * FROM TimeTable where event_id = ?',(id,))
    rows = cur.fetchall
    return render_template('Task4_1b.html',rows = rows)
    
    

app.run()
    
## line 18, incorrect syntax for the route decorator, wrong placeholder for argument in URL
## line 20, where is the con object created ?
## line 21, function call syntax
## always close the database before you return from the function
## html tag for link elment is wrong
## NO html output files created
## You are still making fundamental errors that you can afford to make
# [6m]
