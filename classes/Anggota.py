from config.db import DBConnection as mydb

class Anggota:

    def __init__(self):
        self.__idanggota=None
        self.__kode_anggota=None
        self.__nama=None
        self.__jk=None
        self.__keterangan=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "Kode Anggota:" + self.__kode_anggota + "\n" + "Nama:" + self.__nama + "\n" + "Jk" + self.__jk + "\n" + "Keterangan:" + self.__keterangan
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def idanggota(self):
        return self.__idanggota

    @property
    def kode_anggota(self):
        return self.__kode_anggota

    @kode_anggota.setter
    def kode_anggota(self, value):
        self.__kode_anggota = value

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
    def keterangan(self):
        return self.__keterangan

    @keterangan.setter
    def keterangan(self, value):
        self.__keterangan = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_anggota, self.__nama, self.__jk, self.__keterangan)
        sql="INSERT INTO anggota (kode_anggota, nama, jk, keterangan) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, idanggota):
        self.conn = mydb()
        val = (self.__kode_anggota, self.__nama, self.__jk, self.__keterangan, idanggota)
        sql="UPDATE anggota SET kode_anggota = %s, nama = %s, jk=%s, keterangan=%s WHERE idanggota=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByKodeAnggota(self, kode_anggota):
        self.conn = mydb()
        val = (self.__nama, self.__jk, self.__keterangan, kode_anggota)
        sql="UPDATE anggota SET nama = %s, jk=%s, keterangan=%s WHERE kode_anggota=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, idanggota):
        self.conn = mydb()
        sql="DELETE FROM anggota WHERE idanggota='" + str(idanggota) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByKodeAnggota(self, kode_anggota):
        self.conn = mydb()
        sql="DELETE FROM anggota WHERE kode_anggota='" + str(kode_anggota) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByIDAnggota(self, idanggota):
        self.conn = mydb()
        sql="SELECT * FROM anggota WHERE idanggota='" + str(idanggota) + "'"
        self.result = self.conn.findOne(sql)
        self.__kode_anggota = self.result[1]
        self.__nama = self.result[2]
        self.__jk = self.result[3]
        self.__keterangan = self.result[4]
        self.conn.disconnect
        return self.result

    def getByKodeAnggota(self, kode_anggota):
        self.conn = mydb()
        sql="SELECT * FROM anggota WHERE kode_anggota='" + str(kode_anggota) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_anggota = self.result[1]
            self.__nama = self.result[2]
            self.__jk = self.result[3]
            self.__keterangan = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_anggota = ''
            self.__nama = ''
            self.__jk = ''
            self.__keterangan = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM anggota"
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