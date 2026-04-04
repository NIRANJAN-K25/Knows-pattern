import mysql.connector
from datetime import datetime,date
class datastore:
    def __init__(self,a):
        self.co=mysql.connector.connect(host="localhost",user="user",password="user_pipass",database="kd")
        self.cu=self.co.cursor()
        self.a=a
    def load(self,DATE,whens,expense,description):
        self.cu.execute(f"insert into {self.a} values(%s,%s,%s,%s)",(DATE,whens,expense,description))
        return "update Successfully"
class userlogindata:
    def __init__(self):
        self.con=mysql.connector.connect(host="localhost",user="user",password="user_pass",database="kd")
        self.cu=self.con.cursor()
        self.cu.execute("create table if not exists idpass(id varchar(50),password varchar(100), table_no int auto_increment primary key)")
    def userdata(self,a,b):
<<<<<<< HEAD
        if a.isidentifier():
            self.cu.execute("select * from idpass")
            for i in self.cu.fetchall():
                if i[0]==a:
                    return "user alreay exist"
            self.cu.execute("insert into idpass (id,password) values(%s,%s)",(a,b))
            self.cu.execute(f"create table if not exists {a} (DATE date,whens int,expense int,description char(50))")
            print("login account create succes")
                  
        return "special character not allowed instead ( _ ) and does not start with number"
=======
        self.cu.execute("insert into idpass (id,password) values(%s,%s)",(a,b))
        self.cu.execute(f"create table if not exists {a} (DATE date,whens int,expense int,description varchar(100))")
        print("login account create successfully")
        return datastore(a)
>>>>>>> 7b25fe607fe4cb3217e4bc7f8cd7642e3aaf0daa
    def check(self,a,b): 
        self.cu.execute("select * from idpass where id=%s and password=%s",(a,b))
        if(self.cu.fetchone()):
            print("login success")
            return datastore(a)
        else:
            return "login failed"
q=userlogindata()
while True:
    a=input("enter the name")
    b=input("enter the password")
    print()
    c=input("you are new here,---->type:  YES")
    if c.upper()=="YES":
        if a.isidentifier():
            q.cu.execute("select * from idpass")
            ch=True
            for i in q.cu.fetchall():
                if i[0]==a:
<<<<<<< HEAD
                    print( "user already exist" )
                    ch=False   
                    print()
                    break
            if ch==False:
                  continue 
=======
                    print( "user alreay exist" )
                    ch=False
                    print()
                    break
            if ch==False:
                continue
>>>>>>> d4939f079a783042f7895bbcdbb22336b839c6a5
            object=q.userdata(a,b)
            break
        print("special character not allowed instead ( _ ) and does not start with number")
        print()
        continue
    else:
        object=q.check(a,b)
        break
<<<<<<< HEAD
    else: 
        print("Enter valid number")
expense=int(input("Enter the money (in numbers): "))
description=input("Describe what u spent:")
if c=="yes" or c=="YES":
    q.userdata(a,b).load(DATE,whens,expense,description)
else:
    q.check(a,b).load(DATE,whens,expense,description)
q.con.commit()
q.cu.close()
q.con.close()

        
        
        


    
=======
while True:
    DATE=input("Enter the date:    or Enter K for current date")
<<<<<<< HEAD
    if DATE.uppper=="K":
=======
    if DATE.upper()=="K":
>>>>>>> d4939f079a783042f7895bbcdbb22336b839c6a5
        DATE=date.today()
    else:
        DATE=datetime.strptime(DATE,"%d/%m/%Y").date()
    print()
    print("WHEN THE MONEY SPEND: ")
    print()
    print("Morning------------> 5:00AM to 10:00AM (press 1)")
    print("StartAfternoon-----> 10:01AM to 11:30AM (press 2)")
    print("Afternoon----------> 11:31AM to 2:30PM (press 3)")
    print("EndAfternoon-------> 2:31PM to 4:30PM (press 4)")
    print("Evening------------> 4:31PM to 7:30PM (press 5)")
    print("Night--------------> 7:31PM to 11:59PM (press 6)")
    print("MidNight-----------> 12:00AM to 4:59AM (press 7)")
    while True:
        whens=int(input("--> "))
        if whens in [1,2,3,4,5,6,7]:
            break
        else: 
            print("Enter valid number")
    expense=int(input("Enter the money (in numbers): "))
    description=input("Describe why spend money: ")
    if c.upper()=="YES":
        print(object.load(DATE,whens,expense,description))
    else:
        print(object.load(DATE,whens,expense,description))
    print()
    again=input("Enter again --->yes")
    if again.lower()=="yes":
        continue
    break
object.co.commit()
object.cu.close()
object.co.close()
q.con.commit()   
q.cu.close()
q.con.close()
>>>>>>> 7b25fe607fe4cb3217e4bc7f8cd7642e3aaf0daa
