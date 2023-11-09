import csv
import sqlite3

lines = list(csv.reader(open("IGP.CSV")))
print(lines)
con = sqlite3.connect("uni.db")
for line in lines:
    con.execute("INSERT INTO UAS VALUES (?,?,?)", line)
    con.commit()
con.close()
'''
[3]
'''
