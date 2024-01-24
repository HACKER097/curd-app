from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return 200

@app.route("/api/addRecord", methods=['POST', 'GET'])
def addRecord():
    name = request.args.get("name")
    num = request.args.get("num")

    con = sqlite3.connect("database.db")
    cur = con.cursor()

    cur.execute("INSERT INTO CONTACTS VALUES(?, ?)", (name, num))

    con.commit()
    con.close()

    return "OK"

@app.route("/api/deleteRecord")
def deleteRecord():
    name = request.args.get("name")
    num = request.args.get("num")

    con = sqlite3.connect("database.db")
    cur = con.cursor()

    cur.execute("DELETE FROM CONTACTS WHERE NAME = ? AND NUM = ?", (name, num))

    con.commit()
    con.close()

    return "OK"

@app.route("/api/getRecord")
def getRecord():
    name = request.args.get("name")
    num = request.args.get("num")

    con = sqlite3.connect("database.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM CONTACTS WHERE NAME = ? AND NUM = ?", (name, num))

    data = cur.fetchall()

    return jsonify(data)

@app.route("/api/updateRecord")
def updateRecord():
    name = request.args.get("name")
    num = request.args.get("num")

    new_name = request.args.get("newname")
    new_num = request.args.get("newnum")

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
