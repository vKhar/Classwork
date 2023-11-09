'''
Task 4.3 Marking Scheme [Total: 12m]
•	HMTL title [1m]
•	Show which user we are searching for now (E.g. User ID 2 is following the following users) - must be dynamic [1m]
•	Table headers [1m]
•	Loop [1m]
•	Content of each row [1m]
•	Correct GET at start with no values for parameters [1m]
•	Right action & method = ‘POST’ for form [1m]
•	Creation of text box & submit button [1m]
•	Extraction of the user's input to be used for querying [1m]
•	Correct querying of people user is following (SQL) [1m]
•	When user_input is blank, hide the sentence and table - using Jinja if statements or otherwise [1m]
•	Flask related statements [1m]

import flask
from flask import render_template, request
import sqlite3

app = flask.Flask(__name__)

@app.route('/', methods=['GET','POST'])

&
 if __name__ == '__main__':
    app.run()
'''

import flask
from flask import render_template, request
import sqlite3

app = flask.Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():

    if request.method == "GET":

        return render_template('home.html')

    if 'userid' in request.form:
        userid_input = request.form['userid']

        # create database connection
        connection = sqlite3.connect("photogram.db")

        # execute SQL query
        cursor = connection.execute("Select User.UserID, Name, Gender, Country from Following, User\
									WHERE Following.Following_UserID = User.UserID\
									AND Following.UserID = ?", (userid_input,))

        records = cursor.fetchall()

        return render_template('home.html', user_id = userid_input, records = records)
        


if __name__ == '__main__':
    app.run()

