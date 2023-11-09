#Task 4.4
from flask import Flask, request, render_template
import sqlite3
app = Flask(__name__)
@app.route("/")
def start():
    return render_template("start.html")

@app.route("/submit", methods=["POST"])
def submit():
    player_name = form.request["name"]
    country_code = form.request["country_code"]
    gender = form.request["gender"]
    date_of_birth = form.request["dob"]
    try:
        con = sqlite3.connect("Task4.db")
        con.execute("""
        insert into Player(Name, CountryCode, Gender, DateOfBirth)
        values(?,?,?,?)
        """, (player_name, country_code,gender,date_of_birth))
        con.commit
    except:
        print("unaccepted input")
    finally:
        con.close()
app.run



