from flask import Flask , render_template
import sqlite3

app = Flask(__name__)

@app.route('/',methods=["GET"])
def root():
    con = sqlite3.connect("TASK4.db")
    data = con.execute(''' SELECT name,artist,type FROM Event''').fetchall()
    con.close()
    return render_template('root.html',jin_data = data)

@app.route('/view/<page>')
def view(page):
    con = sqlite3.connect("TASK4.db")
    event_id = con.execute(''' Select id from Event where name=?''',[page]).fetchall()
    data = con.execute(''' Select date, time, venue from TimeTable where
event_id = ?''',[event_id[0][0]])
    return render_template("view.html",jin_data = data)



app.run()
