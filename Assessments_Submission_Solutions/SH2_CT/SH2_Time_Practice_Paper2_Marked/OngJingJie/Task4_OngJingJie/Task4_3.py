import csv
import sqlite3
##assume no errors in opening, modifying and closing of database
data = list(csv.reader(open("IGP.CSV")))

con = sqlite3.connect("uni.db")
sql_statement = """INSERT INTO UAS('Uni','Course','Cutoff')
                Values(?,?,?);"""
for i in range(len(data)):
    con.execute(sql_statement, (data[i][0], data[i][1], data[i][2]))

con.commit()

con.close()
'''
[3]
'''