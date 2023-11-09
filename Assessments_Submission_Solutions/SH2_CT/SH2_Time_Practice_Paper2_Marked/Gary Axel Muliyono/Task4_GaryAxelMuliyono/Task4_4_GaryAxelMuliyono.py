from flask import *
import sqlite3

def open_db(filename):
    conn = sqlite3.connect(filename)
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def root():
    
    h2 = {'A':20,'B':17.5,'C':15,'D':12.5,'E':10,'S':5,'U':0}
    h1 = {'A':10,'B':8.75,'C':7.5,'D':6.25,'E':5,'S':2.5,'U':0}
    conn = open_db('uni.db')
    try:
        gp = request.form.get('gp')
        pw = request.form.get('pw')
        h21 = request.form.get('h21')
        h22 = request.form.get('h22')
        h23 = request.form.get('h23')
        hextra = request.form.get('hextra')
        data = h1[gp] + h1[pw] + h2[h21] + h2[h22] + h2[h23] + h1[hextra]
        weird_data = h2[h21] + h2[h22] + h2[h23] + h1[hextra]
        
        cur = conn.execute('SELECT * FROM UAS')
        data = cur.fetchall()
        new = []
        for thing in data:
            if float(thing['score']) < weird_data:
                new.append(thing)
        data = new
    except Exception as e:
        print(e)
        data = ""
    conn.close()
    return render_template('home1.html',data=data)

app.run()
''' 
[5]

Total 20/20
'''
