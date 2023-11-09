from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    conn = sqlite3.connect("TASK4.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM Event")
    data = cur.fetchall()
    conn.close()
    return render_template("index.html",data=data)

@app.route("/event/<event_id>")
def event(event_id):
    conn = sqlite3.connect("TASK4.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM TimeTable WHERE event_id = ?",(event_id,))
    data = cur.fetchall()
    cur.execute("SELECT name FROM Event WHERE id = ?",(event_id,))
    name = cur.fetchone()['name']
    conn.close()
    return render_template("event.html",data=data,name=name)

app.run()

## did  not use style sheet provided
#9m