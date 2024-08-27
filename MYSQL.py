import mysql.connector

dbConnection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="employee"
)
print(dbConnection)
cursorValue=dbConnection.cursor()

#query="insert into employee_details values(7,'Python','456','3456785678','Python@Python.com')"
#query="""insert into employee_details(id,Name,Employee_Id,Phone_No,Email) values(%s, %s, %s, %s, %s)"""
#values=[(10,"Python10","4567","3456785678","Python@Python.com"),        (11,"Python11","4567","3456785678","Python@Python.com")]
#cursorValue.execute(query)
#cursorValue.execute(query,values)
#cursorValue.executemany(query,values)
#dbConnection.commit()

#query= "select * from employee_details where employee_id=4567"
#cursorValue.execute(query)
#values=cursorValue.fetchall()
#values=cursorValue.fetchall()
#print(values)

#query= "select * from employee_details where employee_id=%s"
#val=("4567",)
#cursorValue.execute(query,val)
#values=cursorValue.fetchall()
#print(values)

#query= "delete from employee_details where employee_id=%s"
#val=("456",)
#cursorValue.execute(query,val)
#dbConnection.commit()
#print(cursorValue.rowcount)

query= "update employee_details set name='Newname' where employee_id=%s"
val=("1234",)
cursorValue.execute(query,val)
dbConnection.commit()
print(cursorValue.rowcount)




