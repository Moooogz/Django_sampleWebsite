import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'markodavid19'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE patientsDb")

print("All Done!")