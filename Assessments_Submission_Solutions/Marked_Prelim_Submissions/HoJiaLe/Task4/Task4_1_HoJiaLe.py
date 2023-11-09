from flask import Flask, render_template
import sqlite3
app = Flask(__name__)
@app.route('/')
def render_base_site():
    conn = sqlite3.connect('TASK4.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Event")
    events = cur.fetchall()
    for i in events:
        events.append('/' + str(i[0]))
    conn.close()
    return render_template('base.html')
@app.route('/a')
def render_event_details(a):
    conn = sqlite3.connect('Task4.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM TimeTable WHERE TimeTable.eventID = ?",(a,))
    timetable = cur.fetchall()
    cur.execyte("SELECT name FROM Event WHERE Event.id = ?",(a,))
    eventname = cur.fetchone()
    conn.close()
    return render_template('event_details.html',eventname = eventname, timetable = timetable)
app.run()

## line 10: do you know what is the datatype for events
## line 13: you didn;t past any data to your jinja template
# no output htm
## line 14, incorrect decorator
## line 23, mismatched jinja variables names

## You don't seems to know your sqlite3 and jinja
## [5m]