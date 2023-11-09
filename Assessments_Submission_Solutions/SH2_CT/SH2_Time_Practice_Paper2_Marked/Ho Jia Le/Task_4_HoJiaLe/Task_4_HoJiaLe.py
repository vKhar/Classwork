from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def load_base_site():
    return render_template('base_site.html')
@app.route("/submit", methods = ["POST"])
def receive_form():
    GP = request.form.get["GP"]
    PW = request.form.get["PW"]
    return (GP,PW)
app.run()

''' 
- Wrong HTML syntax!!
- [2]

Total 2/20
'''