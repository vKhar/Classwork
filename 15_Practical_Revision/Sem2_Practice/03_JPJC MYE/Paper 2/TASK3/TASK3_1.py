from flask import Flask, request
import sqlite3

app = Flask(__name__)

def render(data):
    string = "<table>"
    string += """
        <tr>
            <td>artworkID</td>
            <td>Title</td>
            <td>Artist</td>
            <td>Price</td>
        </tr>
    """
    for item in data:
        string += f"""
        <tr>
            <td>{item[0]}</td>
            <td>{item[1]}</td>
            <td>{item[2]}</td>
            <td>{item[3]}</td>
        </tr>
        """
    string += "</table>"
    return string

@app.route("/", methods=["GET"])
def index():
    return """
        <a href="/artworks">View all artwork</a>
        <br/>
        <a href="/dimensions">View by dimensions</a>
    """

@app.route("/artworks", methods=["GET"])
def aw():
    db = sqlite3.connect("Paper 2/gallery.db")
    data = db.execute("""
        SELECT artworkID, Title, Artist, Price 
        FROM Artwork
    """).fetchall()
    db.close()

    return render(data)

@app.route("/dimensions", methods=["GET"])
def dim():
    return """
        <form action="/dimensions" method=POST>
            <label>Max Breadth</label>
            <input type=text name=b />
            <label>Max Length</label>
            <input type=text name=l />
            <input type=submit />
        </form>
    """

@app.route("/dimensions", methods=["POST"])
def dimpost():
    try:
        b = int(request.form["b"])
        l = int(request.form["l"])
    except:
        return "Try again with integer values"

    db = sqlite3.connect("Paper 2/gallery.db")
    data = db.execute("""
        SELECT artworkID, Title, Artist, Price 
        FROM Artwork
        WHERE Breadth < ?
        AND Length < ?
    """, (b, l)).fetchall()
    db.close()

    return render(data)

app.run()
