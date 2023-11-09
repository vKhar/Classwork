import sqlite3
import csv

additions = list(csv.reader(open("ADDITIONS.csv")))

for addition in additions:
    con = sqlite3.connect("TASK4.db")#assume event is already in database, as only new performances are addded
    addition_event_id = list(con.execute("select id from Event where name = ?", (addition[0],)))
    con.execute("insert into TimeTable(event_id, date, time, venue) values (?,?,?,?)", (addition_event_id[0][0], addition[2], addition[3], addition[4]))
    con.commit()
    con.close()
