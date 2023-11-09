import sqlite3
import csv

data = list(csv.reader(open("ADDITIONS.CSV")))
db = sqlite3.connect("TASK4.db")
for datum in data:
    id = db.execute("SELECT id FROM Event WHERE name = ?", (datum[0],)).fetchone()
    datum.append(id[0])
    db.execute("INSERT INTO TimeTable (event_id, date, time, venue) VALUES (?, ?, ?, ?)", (datum[-1], datum[2], datum[3], datum[4]))
    db.commit()
db.close()