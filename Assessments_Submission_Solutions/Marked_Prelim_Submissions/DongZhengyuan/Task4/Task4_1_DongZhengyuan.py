#Task 4.1
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    try:
        con = sqlite3.connect("TASK4.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM Event")
        data = cur.fetchall()
        con.close()
    except Exception as e:
        print(e)
        con.close()
        return render_template("home.html")
    return render_template("home.html", jin_data = data)

@app.route("/<eventid>", methods=["GET"])
def details(eventid):
    try:
        con = sqlite3.connect("TASK4.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM TimeTable WHERE event_id = ?",[eventid])
        data = cur.fetchall()
        con.close()
    except Exception as e:
        print(e)
        con.close()
        return render_template("details.html")
    return render_template("details.html", jin_data = data)
app.run()

## You never read and understand the table relationship for the application !!
## To retrieve the corresponding dates for a event use the event id {{i[0]}} and not the name!
## [9m]