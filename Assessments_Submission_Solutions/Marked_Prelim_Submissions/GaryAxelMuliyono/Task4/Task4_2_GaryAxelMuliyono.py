import csv
import sqlite3
data = list(csv.reader(open("ADDITIONS.CSV")))
print(data)
conn = sqlite3.connect('TASK4.db')
conn.row_factory = sqlite3.Row
for item in data:
    cursor = conn.execute('SELECT id FROM EVENT WHERE name=(?)',(item[0],))
    cur_id = cursor.fetchone()
    print(cur_id['id'])
    
    conn.execute("INSERT INTO TimeTable (event_id,date,time,venue) VALUES (?,?,?,?);",(cur_id['id'],item[2],item[3],item[4]))
#assuming all the additions are already in Event table
conn.commit()
conn.close()

