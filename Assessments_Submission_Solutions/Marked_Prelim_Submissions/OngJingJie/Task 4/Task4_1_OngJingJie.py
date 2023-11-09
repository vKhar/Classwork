from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def landing():
    con = sqlite3.connect("TASK4.db")
    cur = con.execute("SELECT Event.id, Event.name, Event.artist, Event.type FROM Event")
    data = cur.fetchall()
    con.close()
    return render_template("landing.html", jin_data = data)

@app.route("/<event_id>")
def event(event_id):
    con = sqlite3.connect("TASK4.db")
    cur = con.execute("SELECT Event.name, TimeTable.date, TimeTable.time, TimeTable.venue\
                        FROM Event, TimeTable\
                        WHERE Event.id = TimeTable.event_id and TimeTable.event_id = ?", (event_id,))
    data = cur.fetchall()
    con.close()
    return render_template("event.html", jin_data = data)

app.run()
