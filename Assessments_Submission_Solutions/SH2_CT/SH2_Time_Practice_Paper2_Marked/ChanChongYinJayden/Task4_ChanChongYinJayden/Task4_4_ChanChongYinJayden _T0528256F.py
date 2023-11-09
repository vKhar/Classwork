from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("form.html")

@app.route("/score",methods=["POST"])
def score():
    h1_grades = []
    h2_grades = []
    for i in ("gp","pw","h1"):
        h1_grades.append(float(request.form.get(i)))
    for i in range(1,4):
        h2_grades.append(float(request.form.get(f"h2_{i}")))
    score = sum(h1_grades) + sum(h2_grades)

    grades = []
    grades.append(float(request.form.get("h1")))
    for i in range(1,4):
        grades.append(float(request.form.get(f"h2_{i}")))
    uniScore = sum(grades)
    uniScore = 60
    conn = sqlite3.connect("uni.db")
    cur = conn.cursor()
    cur.execute("SELECT Uni, Course FROM UAS WHERE MinUAS <= ?",(uniScore,))
    courses = list(cur.fetchall())
    #
    print(f" UAS: {uniScore} courses {courses}")
    #
    return render_template("score_courses.html",score=score,courses=courses)


app.run()
'''
[5]

Total 14/20
'''