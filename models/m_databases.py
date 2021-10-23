import mysql.connector


def createDatabases(dataSesion,nameDatabase):
    DB = mysql.connector.connect(
    host=dataSesion['host'],
    user=dataSesion['user'],
    password=dataSesion['password'],
    port=dataSesion['port']
    )
    cursor = DB.cursor()
    cursor.execute('CREATE DATABASE '+nameDatabase)
    
    DB.commit()
    cursor.close()
    
    
def getDatabases(dataSesion):
    print('desde m_databases')
    print(dataSesion)
    DB = mysql.connector.connect(
    host=dataSesion['host'],
    user=dataSesion['user'],
    password=dataSesion['password'],
    port=dataSesion['port']
    )
    cursor = DB.cursor(dictionary=True)
    cursor.execute('SHOW DATABASES;')
    return cursor.fetchall()

hola = 'jeison'