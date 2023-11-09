import sqlite3
con = sqlite3.connect("Task4.db")
with open("COUNTRY.TXT") as f:
    for line in f:
        cont = line.strip().split(",")
        con.execute("insert into Country (CountryCode,CountryName) values (?,?)",(cont[1],cont[0]))
        
con.commit()
con.close()
