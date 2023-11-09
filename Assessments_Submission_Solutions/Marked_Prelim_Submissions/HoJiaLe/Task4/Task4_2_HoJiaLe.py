#Task 4.2
import sqlite3
conn = sqlite3.connect('TASK4.db')
with open('ADDITIONS.CSV', 'r') as f:
    content = f.read().strip().split('\n')
events = [i.split(',') for i in content]
cur = conn.cursor()
eventid = []
for i in events:
    cur.execute("SELECT id FROM Events WHERE name = ?",(i[0],))
    eventid.append([cur.fetchone(), i])
for i in eventid:
    cur.execute("INSERT INTO TimeTable() VALUES (?, ? ,? ,?)",(i[0], i[1][2], i[1][3],i[1][4]))
conn.commit()
conn.close()

## line 11 , Do know what you are appending and what is i[0],..
## line 13, There are 5 columns in TimeTable, you are inserting only 4 columns??!!
## [2m]
