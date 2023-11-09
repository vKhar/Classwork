import csv
import sqlite3

with open("ADDITIONS.csv") as f:
    file = csv.reader(f,delimiter=",")

    file = list(file)

con = sqlite3.connect("TASK4.db")
for data in file:
    event_id = con.execute( "SELECT id from Event where name = ?",[data[0]]).fetchall()
    
    con.execute(''' INSERT INTO TimeTable (event_id,date,time,venue)
Values(?,?,?,?) 
''',[event_id[0][0],data[2],data[3],data[4]])

con.commit()
con.close()
