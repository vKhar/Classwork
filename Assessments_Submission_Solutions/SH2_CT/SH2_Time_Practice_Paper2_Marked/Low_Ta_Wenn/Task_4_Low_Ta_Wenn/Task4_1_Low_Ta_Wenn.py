from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def root():
    return render_template("root.html")

@app.route("/submit", methods=["POST"])
def submit():
    gp = request.form["gp"]
    pw = request.form["pw"]
    first = request.form["first"]
    second = request.form["second"]
    third = request.form["third"]
    flex = request.form["convert"]
    h2 = {"A":20, "B":17.5, "C":15, "D":12.5, "E":10, "S":5, "U":0}
    h1 = {"A":10, "B":8.75, "C":7.5, "D":6.25, "E":5, "S":2.5, "U":0}
    score = h1[gp] + h1[pw] + h2[first] + h2[second] + h2[third] + h1[flex]
    return render_template("computed.html", score = score)

app.run()

'''
[8]
'''
