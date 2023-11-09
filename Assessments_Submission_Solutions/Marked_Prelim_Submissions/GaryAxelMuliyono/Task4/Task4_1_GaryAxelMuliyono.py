from flask import *
import sqlite3

def open_db(filename):
    conn = sqlite3.connect(filename)
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route('/',methods=['GET'])
def root():
    try:
        conn = open_db('TASK4.db')
        cursor = conn.execute("SELECT * FROM Event;")
        data = cursor.fetchall()
        print(data)
    except:
        data = ""
    finally:
        conn.close()
    return render_template("home.html",data=data)

@app.route('/times/<id>',methods=['GET'])
def times(id):
    try:
        conn = open_db('TASK4.db')
        cursor = conn.execute("SELECT * FROM TimeTable INNER JOIN Event ON Event.id=TimeTable.event_id WHERE event_id=(?);",(id,))
        data = cursor.fetchall()
    except:
        data = ""
    finally:
        conn.close()
    return render_template("times.html",data=data)

app.run()

## No output html
# [9m]