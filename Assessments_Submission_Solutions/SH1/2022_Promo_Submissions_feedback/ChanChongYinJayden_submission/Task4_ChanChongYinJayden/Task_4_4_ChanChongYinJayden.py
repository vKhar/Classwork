from flask import Flask, render_template, request
import sqlite3

app = Flask("__name__")

@app.route("/")
def root():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    pid = request.form.get("id")
    name = request.form.get("name")
    cc = request.form.get("cc")
    dob = request.form.get("dob")
    gender = request.form.get("gender")

    con = sqlite3.connect("Task4.db")
    con.execute("INSERT INTO Player VALUES (?,?,?,?,?)",(pid,name,cc,gender,dob))
    con.commit()
    con.close()
    return "Player added"

app.run()
