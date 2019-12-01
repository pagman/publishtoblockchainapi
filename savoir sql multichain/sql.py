import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="",
  database="test"
)

mycursor = mydb.cursor()

sql = "INSERT INTO data (input) VALUES (%s)"
val = ("John",)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")