import sqlite3
def openDB(db):
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    return con

f = open('ADDITIONS.CSV')
con = openDB('TASK4.db')

for line in f:
    data = line.strip('\n').split(',')
    event_id = con.execute('SELECT id from Event where name = ?', (data[0],))
    con.execute('INSERT INTO TimeTable VALUES(?,?,?,?)',(event_id, data[2],data[3],data[4],))
    con.commit()
# What is the datatype of event_id ?
# INSERT syntax is wrong ! the table has 5 columns, you are inserting 4 columns of data
# [4m]