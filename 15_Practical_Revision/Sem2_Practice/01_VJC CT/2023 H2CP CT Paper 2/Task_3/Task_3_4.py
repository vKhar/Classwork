from flask import Flask, render_template, request
import sqlite3

app = Flask("__name__")
@app.route("/")
def root():
    return render_template("root.html")

@app.route("/submit", methods = ["POST"])
def form_submit():
    depart_name = request.form["department"]
    con = sqlite3.connect("company.db")
    full_list = list(con.execute("""
select Employee.Employee_name, Employee_Deployment.Date_of_joining 
from Employee
inner join Employee_Deployment on Employee_Deployment.EmployeeID = Employee.EmployeeID
                                 
inner join Department on Employee_Deployment.DepartmentID = Department.DepartmentID
                                 
where Department.Department_name = ? and Employee_Deployment.Active = 'TRUE'
order by Employee_Deployment.Date_of_joining asc
""", (depart_name, )))
    
    return render_template("result.html", full_list=full_list)    

app.run()
