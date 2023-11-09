from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('form.html')


@app.route('/results', methods = ['POST'])
def show_results():
    department = request.form['department']

        # Connect to the database
    conn = sqlite3.connect('COMPANY.db')
    cursor = conn.cursor()

        # Execute the query to retrieve employee details for the specified department
    cursor.execute('''
        SELECT Employee.Employee_name, Employee_deployment.Date_of_joining
        FROM Employee
        JOIN Employee_deployment ON Employee.EmployeeID = Employee_deployment.EmployeeID
        JOIN Department ON Employee_deployment.DepartmentID = Department.DepartmentID
        WHERE Department.Department_name = ?
        ORDER BY Employee_deployment.Date_of_joining ASC
    ''', (department,))

        # Fetch all the results
    results = cursor.fetchall()

        # Close the connection
    conn.close()
    data = [department, results]
    return render_template('result.html', jin_data=data)

app.run()
