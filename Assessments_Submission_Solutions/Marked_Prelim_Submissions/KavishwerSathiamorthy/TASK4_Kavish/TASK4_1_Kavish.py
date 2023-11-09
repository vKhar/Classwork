from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    db = sqlite3.connect("TASK4.db")
    data = db.execute("SELECT * FROM Event").fetchall()
    db.close()
    return render_template("index.html", data=data)

@app.route("/<event>", methods=["GET"])
def event(event):
    db = sqlite3.connect("TASK4.db")
    data = db.execute("SELECT * FROM TimeTable WHERE event_id = ?", (event,)).fetchall()
    db.close()
    return render_template("event.html", data=data)

app.run()
    