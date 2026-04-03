import mysql.connector
class datastore:
    def __init__(self,a):
        #self.co=mysql.connector.connect(host="localhost",user="user",password="user_pass",database="kd")
        #self.cu=self.co.cursor()
        self.a=a
        #self.cu.execute(f"create table it not exists {self.a} ()")
        #print("success")
class userlogindata:
    def __init__(self):
        self.con=mysql.connector.connect(host="localhost",user="user",password="user_pass",database="kd")
        self.cu=self.con.cursor()
        self.cu.execute("create table if not exists idpass(id char(20),password char(20), table_no int auto_increment primary key)")
    def userdata(self,a,b):
        if a.isidentifier():
            self.cu.execute("insert into idpass (id,password) values(%s,%s)",(a,b))
            print("login account create successfully")
            return datastore(a)
        return "special character not allowed instead ( _ ) and does not start with number"
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
    print(q.userdata(a,b).a)
#print(q.check(a,b))
q.con.commit()
q.cu.close()
q.con.close()

        
        
        


        