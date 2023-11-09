#Task 4.4
from flask import Flask, request, render_template, redirect
import sqlite3
app = Flask(__name__)
@app.route("/")
def start():
    return render_template("start.html")

@app.route("/submit", methods=["POST"])
def submit():
    player_name = request.form["name"]
    country_code = request.form["country_code"]
    gender = request.form["gender"]
    date_of_birth = request.form["dob"]
    try:
        con = sqlite3.connect("Task4.db")
        con.execute("""
        insert into Player(Name, CountryCode, Gender, DateOfBirth)
        values(?,?,?,?)
        """, (player_name, country_code,gender,date_of_birth))
        con.commit
        return redirect("/")
    except:
        print("unaccepted input")
    finally:
        con.close()
app.run()



