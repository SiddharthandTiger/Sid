import mysql.connector
a = mysql.connector.connect(host="localhost",user="root",passwd="Sid@1122005+",database="emailids")
b= a.cursor()
b.execute('select*from passwords ')
for i in b :
    print(i)
