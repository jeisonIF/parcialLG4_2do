import mysql.connector

DB = mysql.connector.connect(
   host='localhost',
    user='jeison',
    password='sele'
)
def getDatabases():
    cursor = DB.cursor(dictionary=True)
    cursor.execute('SHOW DATABASES;')
    return cursor.fetchall()

hola = 'jeison'