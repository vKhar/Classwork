import csv
import sqlite3

with open("ADDITIONS.csv") as f:
    data = list(csv.reader(f))
    
conn = sqlite3.connect("TASK4.db")
cur = conn.cursor()
for i in data:
    cur.execute("SELECT id FROM Event WHERE name = ? and artist = ?",(i[0],i[1]))
    event_id = cur.fetchone()[0]
    cur.execute("INSERT INTO TimeTable(event_id, date, time, venue) VALUES(?,?,?,?)",(event_id,i[2],i[3],i[4]))
    conn.commit()
    
cur.execute("Select * from TimeTable")
print(cur.fetchall())
conn.close()
