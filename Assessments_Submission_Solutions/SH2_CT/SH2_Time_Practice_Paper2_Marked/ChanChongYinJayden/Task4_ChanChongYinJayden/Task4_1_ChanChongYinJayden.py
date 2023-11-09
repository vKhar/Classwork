from flask import Flask, render_template, request

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
    return render_template("score.html",score=score)


app.run()

'''
- form is for entering grade, not the score
- No lookup table, how do you convert a grade to a score
- Wrong UAS calculation
[6]
'''