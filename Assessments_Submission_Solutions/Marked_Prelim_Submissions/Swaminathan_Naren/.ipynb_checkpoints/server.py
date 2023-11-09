from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    db_con = sqlite3.connect("TASK4.db")
    cur = db_con.cursor()
    cur.execute("""SELECT * from Event""")
    data = cur.fetchall()
    #cur.commit()
    db_con.close()
    return render_template("index.html", jin_data = data)
@app.route("/<id>")
def show(id):
    db_con = sqlite3.connect("TASK4.db")
    cur = db_con.cursor()
    cur.execute("""
                SELECT Event.name ,TimeTable.date, TimeTable.time, TimeTable.venue From
                TimeTable INNER JOIN Event ON Event.id = TimeTable.event_id WHERE Event.id = ?
                """, (id,))
    data = cur.fetchall()
    db_con.close()
    return render_template("show.html", jin_data=data)

app.run(debug=True)
