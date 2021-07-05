import mysql.connector

try:
  mydb = mysql.connector.connect(
    host="localhost",
    database="mysqldb",
    user="root",
    password="ba4569852",
    port=3308
  )

  mycursor = mydb.cursor()

  mycursor.execute("SHOW DATABASES")

  for x in mycursor:
    print(x)
except:
  print("Cannot connect to MySQL")