import sqlite3
import csv
f = list(csv.reader(open("ADDITIONS.CSV","r"))) #Event, artist, date, time, venue
con = sqlite3.connect("TASK4.db")
cur = con.cursor()
for event in f:
    cur.execute("INSERT INTO TimeTable(event_id, date, time, venue) VALUES (?,?,?,?)",[event[0],event[2],event[3],event[4]])
con.commit()
con.close()
## you overite the original table !! event_id is the foreign key into the Events table and yu overwrote it !!
## 0m