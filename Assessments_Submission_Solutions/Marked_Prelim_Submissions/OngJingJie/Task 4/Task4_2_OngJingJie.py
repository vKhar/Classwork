import csv
import sqlite3

data = list(csv.reader(open("ADDITIONS.CSV")))

##assume database does not already contain the data from ADDITIONS.CSV
##assume no insertion errors

con = sqlite3.connect("TASK4.db")
for details in data:
    cur = con.execute("SELECT Event.id from Event WHERE Event.name = ?", (details[0],))
    event_id = cur.fetchall()[0][0]
    con.execute("INSERT INTO TimeTable(event_id, date, time, venue) VALUES(?,?,?,?)",(event_id, details[2], details[3], details[4]))
    con.commit()
con.close()

