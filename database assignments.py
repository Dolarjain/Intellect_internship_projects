# # Q.1 create database practice
# import mysql.connector as mysql

# database1=mysql.connect(host='localhost',user='root',password='Dolar.123')
# mycursor1=database1.cursor()
# mycursor1.execute('create database practice')
# print("database created succesfully")
# database1.close()


# # Q.2  Create table in practice database named as “stud” having column name(id,fname,lname,age,marks,contact).
# import mysql.connector as mysql

# database1=mysql.connect(
#                         host='localhost',
#                         user='root',
#                         password='Dolar.123',
#                         database='practice'
#                         )
# mycursor1=database1.cursor()

# mycursor1.execute('create table stud(student_id INT PRIMARY KEY,first_name varchar(25),last_name varchar(25),age int(2),marks int(2),contact varchar(10))')
# database1.commit()
# print("Table created successfully")
# database1.close()


# # Q3. Insert total 10 values in the above table

# import mysql.connector as mysql
# database1=mysql.connect(
#                         host='localhost',
#                         user='root',
#                         password='Dolar.123',
#                         database='practice'
#                         )
# mycursor1=database1.cursor()

# mycursor1.execute("insert into stud(student_id,first_name,last_name,age,marks,contact) values (121,  'rajesh',    'jain',     22,   90,    '1234567890')")
# mycursor1.execute("insert into stud(student_id,first_name,last_name,age,marks,contact) values (122,  'roshan',    'dodiya',   23,   90,    '0999934876')")
# mycursor1.execute("insert into stud(student_id,first_name,last_name,age,marks,contact) values (124,  'ashitosh',  'shinde',   22,   90,    '0999911190')")
# mycursor1.execute("insert into stud(student_id,first_name,last_name,age,marks,contact) values (126,  'tejas',     'kasare',   32,   50,    '0999923450')")
# mycursor1.execute("insert into stud(student_id,first_name,last_name,age,marks,contact) values (127,  'aniket',    'paluskar', 18,   99,    '0987654320')")
# mycursor1.execute("insert into stud(student_id,first_name,last_name,age,marks,contact) values (128,  'rahul',     'gupta',    25,   95,    '0526845670')")
# mycursor1.execute("insert into stud(student_id,first_name,last_name,age,marks,contact) values (129,  'sumit',     'sumit',    23,   98,    '0999575370')")
# mycursor1.execute("insert into stud(student_id,first_name,last_name,age,marks,contact) values (119,  'manish',    'jadhav',   24,   80,    '0923567780')")
# mycursor1.execute("insert into stud(student_id,first_name,last_name,age,marks,contact) values (130,  'dolar',     'jain',     21,   98,    '9898988980')")
# mycursor1.execute("insert into stud(student_id,first_name,last_name,age,marks,contact) values (111,  'd',         'j',        23,   80,    '8979898790')")
# database1.commit()
# print("record inserted successfully")
# database1.close()


# #Q4. Fetch all values in the table and display it onto the console

# import mysql.connector as mysql
# database1=mysql.connect(
#                         host='localhost',
#                         user='root',
#                         password='Dolar.123',
#                         database='practice'
#                         )
# mycursor1=database1.cursor()
# mycursor1.execute('select * from stud')
# data=mycursor1.fetchall()
# for row in data:
#     print(row)
# database1.close()


# # #Q5. Fetch particular value and display it onto the console

# import mysql.connector as mysql
# database1=mysql.connect(
#                         host='localhost',
#                         user='root',
#                         password='Dolar.123',
#                         database='practice'
#                         )
# mycursor1=database1.cursor()
# mycursor1.execute('select first_name from stud')
# one=mycursor1.fetchone()
# print(one)
# database1.close()


# #Q6. Update any value 

# import mysql.connector as mysql
# database1=mysql.connect(
#                         host='localhost',
#                         user='root',
#                         password='Dolar.123',
#                         database='practice'
#                         )
# mycursor1=database1.cursor()

# mycursor1.execute("update stud set first_name ='shree' where student_id = 121")
# database1.commit()
# print("updated successfully")
# database1.close()


# # #Q7. Sort the data according to their marks entered. 

# import mysql.connector as mysql
# database1=mysql.connect(
#                         host='localhost',
#                         user='root',
#                         password='Dolar.123',
#                         database='practice'
#                         )
# mycursor1=database1.cursor()

# mycursor1.execute('SELECT * FROM stud ORDER BY marks')
# myresult=mycursor1.fetchall()

# for x in myresult:
#     print(x)
# database1.close()


# #Q8. Do sum of marks of all records, and display it on console

# import mysql.connector as mysql
# database1=mysql.connect(
#                         host='localhost',
#                         user='root',
#                         password='Dolar.123',
#                         database='practice'
#                         )
# mycursor1=database1.cursor()

# mycursor1.execute("select sum(marks) from stud")
# print("sum of all marks = ",mycursor1.fetchall()[0][0])
# database1.close()


#Q9. Fetch all records and display it line by line without having tuple
# import mysql.connector as mysql
# database1=mysql.connect(
#                         host='localhost',
#                         user='root',
#                         password='Dolar.123',
#                         database='practice'
#                         )
# mycursor1=database1.cursor()

# mycursor1.execute('select * from stud')
# data=mycursor1.fetchall()
# for row in data:
#     row=list(row)
#     print(row)
# database1.close()


# # Q10. Remove particular value from the table.
# import mysql.connector as mysql
# database1=mysql.connect(
#                         host='localhost',
#                         user='root',
#                         password='Dolar.123',
#                         database='practice'
#                         )
# mycursor1=database1.cursor()

# mycursor1.execute("DELETE FROM stud WHERE last_name = 'shinde' ")

# database1.commit()
# print("value deleted successfully")
# database1.close()


# # Q11. Remove all records from the table.
# import mysql.connector as mysql
# database1=mysql.connect(
#                         host='localhost',
#                         user='root',
#                         password='Dolar.123',
#                         database='practice'
#                         )
# mycursor1=database1.cursor()
# mycursor1.execute("delete from stud")
# database1.commit()
# print("deleted successfully")
# database1.close()
