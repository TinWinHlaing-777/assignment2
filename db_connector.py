import mysql.connector

def connect():
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = ''
    )
    cursor = mydb.cursor()
    return cursor, mydb