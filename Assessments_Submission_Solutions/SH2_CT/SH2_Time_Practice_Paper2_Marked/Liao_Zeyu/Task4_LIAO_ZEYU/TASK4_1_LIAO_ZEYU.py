from flask import Flask, render_template, redirect, request
map={'A':20, 'B':17.5,'C':15,'D':12.5, 'E':10, "S":5, "U":0} 
app=Flask(__name__)
@app.route('/')
def root():
    return render_template('main.html')
@app.route('/submit', methods=["POST"])
def calc(): ##assume inputs are correct
    pw=request.form.get('pw')
    gp=request.form.get('gp')
    one=request.form.get('one')
    two=request.form.get('two')
    three=request.form.get('three')
    four=request.form.get('four')
    UAS=map[pw]/2+map[gp]/2+map[four]/2+map[one]+map[two]+map[three]
    return f"your UAS is {UAS}"
app.run(debug=True)
'''
[8]
'''
