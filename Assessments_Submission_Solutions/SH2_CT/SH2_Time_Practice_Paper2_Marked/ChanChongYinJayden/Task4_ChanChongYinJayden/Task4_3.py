import csv, sqlite3
with open("../IGP.CSV") as f:
    reader = csv.reader(f)
    courses = list(reader)
    print(courses)

conn = sqlite3.connect("uni.db")
cur = conn.cursor()
for course in courses:
    params = tuple(course[:2]) + (float(course[2]),)
    cur.execute("INSERT INTO UAS Values(?,?,?)",params)

conn.commit()
conn.close()
'''
[3]
'''