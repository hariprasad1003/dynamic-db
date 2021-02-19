import sqlite3
con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute('CREATE TABLE NAME (Name text, Age text)')
con.commit()
print("Database Created")