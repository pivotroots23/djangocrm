import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'pivotroots',
    passwd = 'password@123'
)


#prepare a cursor object
cursorobject = database.cursor()

#Create a database
cursorobject.execute("CREATE DATABASE dcrm")
print("All Done")