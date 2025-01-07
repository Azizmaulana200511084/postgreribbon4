from config.db import DBConnection as mydb

class Dosen:

    def __init__(self):
        self.__iddosen=None
        self.__nidn=None
        self.__nama=None
        self.__jk=None
        self.__kode_prodi=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "NIDN:" + self.__nidn + "\n" + "Nama:" + self.__nama + "\n" + "Jk" + self.__jk + "\n" + "Kode Prodi:" + self.__kode_prodi
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def iddosen(self):
        return self.__iddosen

    @property
    def nidn(self):
        return self.__nidn

    @nidn.setter
    def nidn(self, value):
        self.__nidn = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value

    @property
    def kode_prodi(self):
        return self.__kode_prodi

    @kode_prodi.setter
    def kode_prodi(self, value):
        self.__kode_prodi = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__nidn, self.__nama, self.__jk, self.__kode_prodi)
        sql="INSERT INTO dosen (nidn, nama, jk, kode_prodi) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, iddosen):
        self.conn = mydb()
        val = (self.__nidn, self.__nama, self.__jk, self.__kode_prodi, iddosen)
        sql="UPDATE dosen SET nidn = %s, nama = %s, jk=%s, kode_prodi=%s WHERE iddosen=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByNIDN(self, nidn):
        self.conn = mydb()
        val = (self.__nama, self.__jk, self.__kode_prodi, nidn)
        sql="UPDATE dosen SET nama = %s, jk=%s, kode_prodi=%s WHERE nidn=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, iddosen):
        self.conn = mydb()
        sql="DELETE FROM dosen WHERE iddosen='" + str(iddosen) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNIDN(self, nidn):
        self.conn = mydb()
        sql="DELETE FROM dosen WHERE nidn='" + str(nidn) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByIDDOSEN(self, iddosen):
        self.conn = mydb()
        sql="SELECT * FROM dosen WHERE iddosen='" + str(iddosen) + "'"
        self.result = self.conn.findOne(sql)
        self.__nidn = self.result[1]
        self.__nama = self.result[2]
        self.__jk = self.result[3]
        self.__kode_prodi = self.result[4]
        self.conn.disconnect
        return self.result

    def getByNIDN(self, nidn):
        self.conn = mydb()
        sql="SELECT * FROM dosen WHERE nidn='" + str(nidn) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nidn = self.result[1]
            self.__nama = self.result[2]
            self.__jk = self.result[3]
            self.__kode_prodi = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nidn = ''
            self.__nama = ''
            self.__jk = ''
            self.__kode_prodi = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM dosen"
        self.result = self.conn.findAll(sql)
        return self.result
"""
dsn = Dosen()
a = mydb()
sql="SELECT * FROM dosen"
cur = a.findAll(sql)
# Get all 
result = dsn.getAllData()
print(result)
"""