import mysql.connector
class userlogindata():
    def __init__(self):
        self.con=mysql.connector.connect(host="localhost",user="user",password="user_pass",database="kd")
        self.cu=self.con.cursor()
        self.cu.execute("create table if not exists idpass(id char(20),password char(20), table_no int auto_increment primary key)")
    def userdata(self,a,b):
        self.cu.execute("insert into idpass values(%s,%s)",(a,b))
        print("login account create successfully")
        k= i for i in range(1,10) i++
        return 
    def check(self,a,b):
        self.cu.execute("select * from idpass where id=%s and password=%s",(a,b))
        if(self.cu.fetchone()):
            return "login success"
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
q.con.commit()
q.cu.close()
q.con.close()



        