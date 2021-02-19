'''
author - Hari Prasad
Reference - 
https://www.sqlitetutorial.net/sqlite-python/creating-database/
https://stackoverflow.com/questions/38925115/sqlite3-operationalerror-near-syntax-error

'''

from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("create.html")

@app.route('/create', methods=['POST'])
def create():
    con = sqlite3.connect("database.db")
    try:
        message = None
        name = request.form.get('name')
        age = request.form.get('age')
        cur = con.cursor()
        cur.execute(f'INSERT INTO NAME (Name,Age) VALUES {name,age}')
        con.commit()
        message = "Record Added Successfully"
    except Error as e:
        print(e)
        con.rollback()
        message = "Can't Add Record"
    finally:
        return render_template("create.html", message=message)

@app.route('/readrecord', methods=['POST', 'GET'])
def read():
    con = sqlite3.connect("database.db")
    try:
        message = None
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM NAME")
        rows = cur.fetchall()
    except Error as e:
        print(e)
        con.rollback()
        message = "Can't Able to Read Records"
    finally:
        return render_template("read.html",rows = rows, message = message)

@app.route("/delete")  
def delete():  
    return render_template("delete.html")  
 
@app.route("/deleterecord",methods=["POST"])  
def deleterecord():
    con = sqlite3.connect("database.db")
    try:
        message = None
        name = request.form.get('name')
        cur = con.cursor()
        cur.execute("DELETE FROM NAME WHERE Name=?", (name,))
        con.commit()
        message = "Record Deleted Successfully"
    except Error as e:
        print(e)
        con.rollback()
        message = "Can't Able to Delete Record"  
    finally:
        return render_template("delete.html",message = message)

@app.route("/update")
def update():  
    return render_template("update.html")  
 
@app.route("/updaterecord",methods=["POST"])  
def updaterecord():
    con = sqlite3.connect("database.db")
    try:
        message = None
        old_name = request.form.get('old_name')
        updated_name = request.form.get('updated_name')
        age = request.form.get('age')
        cur = con.cursor()
        cur.execute("UPDATE NAME SET Name=? ,Age=?  WHERE Name=?", (updated_name,age,old_name,))
        con.commit()
        message = "Record Updated Successfully"
    except Error as e:
        print(e)
        con.rollback()
        message = "Can't Able to Update Record"  
    finally:
        return render_template("update.html",message = message)

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True, port=5000)