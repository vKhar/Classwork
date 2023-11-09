import csv, sqlite3

data=list(csv.reader(open("IGP.csv")))
try:
    db=sqlite3.connect('uni.db')
    print('i')
    for i in data:
        db.execute("INSERT INTO Courses VALUES(?,?,?)", (i[0], i[1], float(i[2])))
    db.commit()
except:
    db.rollback()
finally:
    db.close()
'''
[3]

Total
12/20
'''