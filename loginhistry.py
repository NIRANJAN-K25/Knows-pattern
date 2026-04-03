import mysql.connector
co=mysql.connector.connect(host="localhost",user="user",password="user_pass",database="kd")
cu=co.cursor()
cu.execute("select * from idpass")
for i in cu.fetchall():
    print (i)
cu.close()
co.close()