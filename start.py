import mysql.connector
class userlogindata():
    def __init__(self):
        self.con=mysql.connector.connect(host="localhost",user="",password="",database="")
        self.cu=self.con.cursor()
        self.cu.execute("create table if not exists idpass(id char(20),password char(20))")
    def userdata(self,a,b):
        self.cu.execute("insert into idpass values(%s,%s)",(a,b))
        return ("login account create successfully")
q=userlogindata()
a=input("enter the name")
b=input("enter the password")
print()
c=input("you are new here,---->type:  YES")
if c=="yes" or c=="YES":
    q.userdata(a,b)
        