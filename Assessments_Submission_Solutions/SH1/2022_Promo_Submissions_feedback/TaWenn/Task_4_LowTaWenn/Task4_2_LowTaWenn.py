lines = []
with open("COUNTRY.TXT") as f:
    for i in f:
          lines.append(i.strip().split(","))
print(lines)
import sqlite3

con = sqlite3.connect("Task4.db")

for i in range(0, len(lines)):
    con.execute("""
    insert into Country
    values(?,?,?)
    """, (lines[i][1],lines[i][0],0)) #assume team captain PlayerId is 0
    con.commit()
con.close()
