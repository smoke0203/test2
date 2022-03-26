import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='smoke', passwd='hellomoto', database='student', autocommit = True)
cursor = mydb.cursor()

marks = 40

cursor.execute('select city from grade1 where firstName = "Mark"')
x = cursor.fetchone()
print(x)