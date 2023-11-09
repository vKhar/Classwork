from flask import Flask,request,render_template

app = Flask(__name__)
@app.route("/")
def root():
    return render_template('application.html')

@app.route("/Submit",methods=['GET','POST'])
def Submit():
    data = request.form
    d = list(data)
    print(d)
    for i in d:
        pass
    return "SUBMITTED"
app.run()
        
'''
line 8 why do you accept get request ?!!!
[2]
Total 2/20
'''      

