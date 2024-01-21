from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return "HELLO WORLD"

@app.route("/api/addRecord")
def addRecord():
    name = request.form.get("name")
    num = request.form.get("num")

    con = sqlite3.connect("database.db")
    cur = con.cursor()

    cur.execute("INSERT INTO CONTACTS VALUES(?, ?)", (name, num))

    con.commit()
    con.close()

@app.route("api/deleteRecord")
def deleteRecord():
    name = request.form.get("name")
    num = request.form.get("num")

    con = sqlite3.connect("database.db")
    cur = con.cursor()

    cur.execute("DELETE FROM CONTACTS WHERE NAME = ? AND NUM = ?", (name, num))

    con.commit()
    con.close()

@app.route("api/getRecord")
def getRecord():
    name = request.form.get("name")
    num = request.form.get("num")

    con = sqlite3.connect("database.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM CONTACTS WHERE NAME = ? AND NUM = ?", (name, num))

    return jsonify(cur.fetchall())

@app.route("api/updateRecord")
def updateRecord():
    name = request.form.get("name")
    num = request.form.get("num")

    new_name = request.form.get("newname")
    new_num = request.form.get("newnum")
    
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    cur.execute("UPDATE CONTACTS SET NAME = ?, NUM = ? WHERE NAME = ? AND NUM = ?",
                (new_name, new_num, name, num))

    con.commit()
    con.close()
