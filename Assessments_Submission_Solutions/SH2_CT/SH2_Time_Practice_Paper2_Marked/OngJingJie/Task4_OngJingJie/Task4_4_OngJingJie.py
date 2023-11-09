from flask import Flask, render_template, request,redirect

app = Flask(__name__)

@app.route("/", methods=["GET"])
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"]) ##assume the user always inputs valid grade
def calculation():
    h1 = [request.form.get("pw"),request.form.get("gp"),request.form.get("H1")]
    h2 = [request.form.get("H21"), request.form.get("H22"), request.form.get("H23")]
    grades = ["A", "B", "C", "D"]
    lower_grades = ["E", "S", "U"]
    score = 0
    for grade in h1:
        if grade in grades:
            score += 10-1.25*grades.index(grade)
        else:
            score += 5-2.5*lower_grades.index(grade)
    for grade in h2:
        if grade in grades:
            score += 20-2.5*grades.index(grade)
        else:
            score += 10-5*lower_grades.index(grade)
    return redirect(f"/{score}")

@app.route("/<result>", methods=["GET"])
def results(result):
    return render_template("score.html", data = result)


app.run()
'''
[0]

Total
11/20
'''