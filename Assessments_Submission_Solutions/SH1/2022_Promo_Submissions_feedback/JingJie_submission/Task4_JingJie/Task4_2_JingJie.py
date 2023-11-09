import sqlite3

def open_db(db):
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    return connection

f = open("COUNTRY.TXT")
lines = f.readlines()
countries = []
for line in lines:
    countries.append(line.strip().split(","))
try:
    con = open_db("Task4.db")
    con.execute("PRAGMA Foreign_Keys = OFF")
    sql_str = "INSERT INTO Country(CountryCode, CountryName)\
    VALUES(?, ?);"
    for country in countries:
        con.execute(sql_str, (country[1], country[0]))
    con.commit()
except:
    print("Error")
    con.rollback()
finally:
    con.close()
        
