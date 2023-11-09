from flask import Flask, render_template
## What else do you need ??!!
app = Flask(__name__) 

app.route('/form',method = ["POST"])
def form():
    return render_template("form.html")
## How can you post data to the landing page !!

app.route('/submit_form')
def submit():
    gp = request.form['gp']
    pw = request.form['pw']
    firsth2 = request.form['1h2']
    sech2 = request.form['2h2']
    thirdh2 = request.form['3h2']
    h1 = request.form['h1']
    
    grades = ['A','B','C','D','E','S','U']
    total = (10-1.25*grades.index(gp)) + (10-1.25*grades.index(pw)) + (10-1.25*grades.index(h1)) +(60-1.5*(grades.index(firsth2)+grades.index(sech2)+grades.index(thirdh2)))
    return total
app.run()
'''
- incorrect lookup table, use a dict instead of this convoluted calculations
- how can you return a int to a web browser
- YOU NEED TO REVISE WEB APP THOROUGHLY !!!
- [0]
'''