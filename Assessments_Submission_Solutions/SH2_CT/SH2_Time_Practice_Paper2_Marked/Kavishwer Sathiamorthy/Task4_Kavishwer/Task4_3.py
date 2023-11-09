import csv
import sqlite3

courses = list(csv.reader(open("../../Resources/IGP.CSV")))
db = sqlite3.connect("uni.db")
db.execute("""
    CREATE TABLE UAS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uni TEXT,
        course TEXT,
        cutoff REAL
    )
""")
for course in courses:
    db.execute("""
        INSERT INTO UAS (uni, course, cutoff) VALUES (?, ?, ?)
    """, (course[0], course[1], float(course[2])))
db.commit()

#[3]