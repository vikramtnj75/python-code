import mysql.connector

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Max12345@",
    database="Student"
)
cursor=connection.cursor()
#cursor.execute("create database Student")
#name='TestThree'
#cursor.execute("CREATE TABLE Student_details(FIRST_NAME CHAR(20) NOT NULL,LAST_NAME CHAR(20),AGE INT,SEX CHAR(1))");
#query="insert into student_details(FIRST_NAME,LAST_NAME,AGE,SEX) values('VIKRAM','ASOKAN','48','M')"
query="insert into student_details(FIRST_NAME,LAST_NAME,AGE,SEX) values(%s,%s,%s,%s)"
value=[('KALAI','SELVAN','37','M'),('SYED','IMRAN','51','M')]
cursor.executemany(query,value)
connection.commit()
print(cursor.rowcount)

#query="select * from studentdetails"
#cursor.execute(query)
#returnValues=cursor.fetchall()
#print(returnValues)