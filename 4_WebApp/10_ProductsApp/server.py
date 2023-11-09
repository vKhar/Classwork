from flask import Flask, render_template,request,redirect

app=Flask(__name__)
@app.route("/")
def root():
    f = open("products.txt","r")
    products_list =[ line.strip().split(",") for line in f]
    return render_template("products.html",products=products_list)
@app.route("/form")
def show_form():
    return render_template("form1.html")
@app.route("/submit", methods=["POST"])
def form_submit():
    file_name=""
    if "image" in request.files:
        file_obj = request.files["image"]
        file_name = file_obj.filename
        file_obj.save(f"static/images/{file_name}")
    f=open("products.txt","a")
    f.write(f"{request.form['product']},{request.form['description']},{request.form['price']},{file_name}\n")
    f.close()
    return redirect("/")
app.run()
