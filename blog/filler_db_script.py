import psycopg2 as sql

conn = sql.connect(database='HT_10', user='postgres',
                   password='root', host='localhost', port=5432)
cursor = conn.cursor()
cursor.execute(sql.SQL("SELECT * FROM {}"))
