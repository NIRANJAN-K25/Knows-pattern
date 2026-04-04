import mysql.connector
from datetime import datetime,date
class datastore:
    def __init__(self,a):
        self.co=mysql.connector.connect(host="localhost",user="user",password="user_pipass",database="kd")
        self.cu=self.co.cursor()
        self.a=a
    def load(self,DATE,when,expense,description):
        self.cu.execute(f"insert into {self.a} values(%s,%s,%s,%s)",(DATE,when,expense,description))
        self.co.commit()
        self.co.close()
        self.cu.close()
class userlogindata:
    def __init__(self):
        self.con=mysql.connector.connect(host="localhost",user="user",password="user_pass",database="kd")
        self.cu=self.con.cursor()
        self.cu.execute("create table if not exists idpass(id char(20),password char(20), table_no int auto_increment primary key)")
    def userdata(self,a,b):
        if a.isidentifier():
            self.cu.execute("select * from idpass")
            for i in self.cu.fetchall():
                if i[0]==a:
                    return "user alreay exist"
            self.cu.execute("insert into idpass (id,password) values(%s,%s)",(a,b))
            self.cu.execute(f"create table it not exists {a} (DATE date,when int,expense int,description char(50))")
            print("login account create successfully")
            return datastore(a)
        return "special character not allowed instead ( _ ) and does not start with number"
    def check(self,a,b):
        self.cu.execute("select * from idpass where id=%s and password=%s",(a,b))
        if(self.cu.fetchone()):
            print("login success")
            return datastore(a)
        else:
            return "login failed"
q=userlogindata()
a=input("enter the name")
b=input("enter the password")
print()
c=input("you are new here,---->type:  YES")
if c=="yes" or c=="YES":
    print(q.userdata(a,b))
print(q.check(a,b))
DATE=input("Enter the date:    or Enter K for current date")
if DATE=="k":
    DATE=date.today()
else:
    DATE=datetime.strptime(DATE,"%d/%m/%Y").date()
print()
print("WHEN THE MONEY SPEND: ")
print()
print("Morning----->6:00AM to 10:00AM (press 1)")
print("Morning----->10:01AM to 12:00PM (press 2)")
print("Afternoon--->12:01PM to 6:00PM (press 3)")
print("Evening----->6:01pM to 10:00pM (press 4)")
print("Night------->10:01PM to 5:59AM (press 5)")
while True:
    when=int(input("--> "))
    if when==1 or 2 or 3 or 4 or 5:
        break
    else: 
        print("Enter valid number")
expense=int(input("Enter the money (in numbers): "))
description=input("Describe what u spent:")
if c=="yes" or c=="YES":
    q.userdata().load(DATE,when,expense,description)
q.check().load(DATE,when,expense,description)
q.con.commit()
q.cu.close()
q.con.close()

        
        
        


        