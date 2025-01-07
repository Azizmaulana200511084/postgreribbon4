from config.db import DBConnection as mydb

class Users:

    def __init__(self):
        self.__iduser=None
        self.__username=None
        self.__password1=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "USERNAME:" + self.__username + "\n" + "PASSWORD:" + self.__password1
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def iduser(self):
        return self.__iduser

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password1(self):
        return self.__password1

    @password1.setter
    def password1(self, value):
        self.__password1 = value

   
    def simpan(self):
        self.conn = mydb()
        val = (self.__username, self.__password1)
        sql="INSERT INTO users (username, password1) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, iduser):
        self.conn = mydb()
        val = (self.__username, self.__password1, iduser)
        sql="UPDATE users SET username = %s, password1 = %s WHERE iduser=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByUSERNAME(self, username):
        self.conn = mydb()
        val = (self.__password1, username)
        sql="UPDATE users SET password1 = %s WHERE username=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, iduser):
        self.conn = mydb()
        sql="DELETE FROM users WHERE iduser='" + str(iduser) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByUSERNAME(self, username):
        self.conn = mydb()
        sql="DELETE FROM users WHERE username='" + str(username) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByIDUSERNAME(self, iduser):
        a=str(iduser)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM users WHERE iduser='" + b + "'"
        self.result = self.conn.findOne(sql)
        self.__iduser = str(self.result[0])
        self.__username = self.result[1]
        self.__password1 = self.result[2]
        self.conn.disconnect
        return self.result

    def getByUSERS(self, username):
        a=str(username)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM users WHERE username='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__iduser = str(self.result[0])
            self.__username = self.result[1]
            self.__password1 = self.result[2]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__username = ''
            self.__password1 = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM users"
        self.result = self.conn.findAll(sql)
        return self.result


"""usr = Users()
a = mydb()
sql="SELECT * FROM users"
cur = a.findAll(sql)
# Get all 
result = usr.getAllData()
print(result)"""