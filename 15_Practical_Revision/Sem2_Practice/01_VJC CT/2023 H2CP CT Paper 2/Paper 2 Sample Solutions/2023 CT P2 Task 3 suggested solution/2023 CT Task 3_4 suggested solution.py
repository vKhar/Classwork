from flask import Flask, render_template, request
import sqlite3, csv

connection = sqlite3.connect("COMPANY.db")
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')

    dept_name = request.form["name"]

    cursor = connection.execute("""SELECT Employee.Employee_name, Employee_deployment.Date_of_joining
                                  FROM Employee, Department, Employee_deployment 
                                  WHERE Employee.EmployeeID = Employee_deployment.EmployeeID and
                                    Department.DepartmentID = Employee_deployment.DepartmentID and
                                    Employee_deployment.Active = 1 and
                                    Department.Department_name = ?
                                    ORDER BY Employee_deployment.Date_of_joining ASC
                                """, (dept_name,))

    return render_template('index.html', details = list(cursor))


if __name__ == '__main__':
    app.run()
