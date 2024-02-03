from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/addRecord", methods=['POST'])
def addRecord():
    name = request.form.get("name")
    num = request.form.get("num")

    con = sqlite3.connect("database.db")
    cur = con.cursor()

    cur.execute("INSERT INTO CONTACTS VALUES(?, ?)", (name, num))

    con.commit()
    con.close()

    return "OK"

@app.route("/api/deleteRecord", methods=['POST'])
def deleteRecord():
    name = request.form.get("name")
    num = request.form.get("num")

    con = sqlite3.connect("database.db")
    cur = con.cursor()

    cur.execute("DELETE FROM CONTACTS WHERE NAME = ? AND NUM = ?", (name, num))

    con.commit()
    con.close()

    return "OK"

@app.route("/api/getRecord", methods=['POST'])
def getRecord():
    name = request.form.get("name")
    num = request.form.get("num")

    con = sqlite3.connect("database.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM CONTACTS WHERE NAME = ? AND NUM = ?", (name, num))

    data = cur.fetchall()

    return jsonify(data)

@app.route("/api/updateRecord", methods=['POST'])
def updateRecord():
    name = request.form.get("name")
    num = request.form.get("num")

    new_name = request.form.get("newname")
    new_num = request.form.get("newnum")

    print(name, num, new_name, new_num)
    
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    cur.execute("UPDATE CONTACTS SET NAME = ?, NUM = ? WHERE NAME = ? AND NUM = ?",
                (new_name, new_num, name, num))

    con.commit()
    con.close()

    return "OK"

if __name__ == '__main__':
    app.run()
