from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

g2rp = {
    "A": 10,
    "B": 8.75,
    "C": 7.5,
    "D": 6.25,
    "E": 5,
    "S": 2.5,
    "U": 0
}    

@app.route("/")
def index():
    return render_template("index.html")

# [2]

@app.route("/", methods=["POST"])
def uas():
    try:
        pw = request.form.get("PW")
        gp = request.form.get("GP")
        h2_1 = request.form.get("First H2")
        h2_2 = request.form.get("Second H2")
        h2_3 = request.form.get("Third H2")
        h1 = request.form.get("H1")
        
        calc = g2rp[pw] + g2rp[gp] + g2rp[h1] + 2*(g2rp[h2_1] + g2rp[h2_2] + g2rp[h2_3])
        db = sqlite3.connect("uni.db")
        courses = db.execute("SELECT uni, course FROM UAS WHERE cutoff <= ?", (calc,)).fetchall()
        return render_template("uas.html", data=(str(calc),courses))
    except:
        redirect("/")
## try not to use the same url as the previous view function
## please seperate your 4.1 solution from the 4.4 solution
        
app.run()

'''
4.1 [8]
4.4 [5]
Total 20/20
'''