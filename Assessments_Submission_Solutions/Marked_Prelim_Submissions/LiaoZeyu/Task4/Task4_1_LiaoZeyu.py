from flask import Flask, render_template
import sqlite3
app=Flask(__name__)
@app.route('/')
def root():
    try:
        db=sqlite3.connect("TASK4.db")
        events=list(db.execute("SELECT * FROM EVENT"))
    except:
        db.rollback()
    finally:
        db.close()
    print(events)
    return render_template("Task4_1a.html", eventL=events)
@app.route('/<id>')
def dates(id):
    try:
        db=sqlite3.connect("TASK4.db")
        date=list(db.execute("SELECT * FROM TimeTable WHERE event_id=?", (id,)))
        details=list(db.execute("SELECT * FROM Event WHERE id=?", (id,)))
    except:
        db.rollback()
    finally:
        db.close()
    return render_template("Task4_1b.html", name=details[0][1], dates=date)
app.run()

## Task4_1a/b.html is suppose to be the generated output from running you flask app!!
## you did not produce the output 
#9m