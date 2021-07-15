import psycopg2
from decouple import config

HOST        = config("HOST")
PORT        = int(config("PORT"))
DATABASE    = config("DATABASE")
DB_USER     = config("DB_USER")
DB_PASSWORD = config("DB_PASSWORD")

# print(DB_USER, DB_PASSWORD)

conn = psycopg2.connect(
    
    host     = HOST,
    port     = PORT,
    database = DATABASE,
    user     = DB_USER,
    password = DB_PASSWORD
    
    )

cur = conn.cursor()

cur.execute("""SELECT * FROM Students""")
query_results = cur.fetchall()
print(query_results)

cur.close()
conn.close()
