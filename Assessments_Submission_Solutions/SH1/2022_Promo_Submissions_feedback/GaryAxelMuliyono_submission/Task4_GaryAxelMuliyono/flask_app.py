import sqlite3
from flask import *

def open_DB(db):
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    return connection
app = Flask(__name__)

@app.route("/",methods=["GET"])
def root():
    try:
        con = open_DB("Task4.db")
        cur = con.execute("SELECT * FROM Player")
        rows = cur.fetchall()
    except:
        print("ERROR")
    finally:
        con.close()
    return render_template("home.html",data=rows)

@app.route("/submit",methods=["POST"])
def submit():
    try:
        con = open_DB("Task4.db")
        con.execute("INSERT INTO Player(Name,CountryCode,Gender,DateOfBirth) VALUES(?,?,?,?)",(request.form["name"],request.form["code"],request.form["gender"],request.form["date"]))
        con.commit()
    except Exception as e:
        print(str(e))
    finally:
        con.close()
    return redirect("/")
app.run()
