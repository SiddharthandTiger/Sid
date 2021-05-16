import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="Sid@1122005+",database="emailids")
mycursor = mydb.cursor()
mycursor.execute('select * from passwords order by Email_id')

for i in mycursor:
    print(i)
