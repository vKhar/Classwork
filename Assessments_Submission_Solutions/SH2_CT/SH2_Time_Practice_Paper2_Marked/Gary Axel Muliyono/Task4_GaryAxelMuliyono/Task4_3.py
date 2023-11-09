import csv,sqlite3
def open_db(filename):
    conn = sqlite3.connect(filename)
    conn.row_factory = sqlite3.Row
    return conn
#assume file is copied into directory
x = list(csv.reader(open("IGP.CSV")))
print(x)
cur = open_db('uni.db')
for line in x:
    try:
        cur.execute('INSERT INTO UAS (name, degree, score) VALUES (?,?,?)',(line[0],line[1],line[2]))
        cur.commit()
        print('good')
    except:
        print('shucks')
cur.close()

'''
[3]
'''
