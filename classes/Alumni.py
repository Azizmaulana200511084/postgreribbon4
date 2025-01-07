from config.db import DBConnection as mydb

class Alumni:

    def __init__(self):
        self.__idalumni=None
        self.__kode_alumni=None
        self.__nama=None
        self.__jk=None
        self.__tempat_kerja=None
        self.__jabatan=None
        self.__bekerja_sejak=None
        self.__telepon=None
        self.__email=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "KODE ALUMNI:" + self.__kode_alumni + "\n" + "Nama:" + self.__nama + "\n" + "Jk" + self.__jk + "\n" + "Tempat Kerja:" + self.__tempat_kerja + "\n" + "Tempat Kerja:" + self.__jabatan + "\n" + "Tempat Kerja:" + self.__bekerja_sejak + "\n" + "Tempat Kerja:" + self.__telepon + "\n" + "Tempat Kerja:" + self.__email
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def idalumni(self):
        return self.__idalumni

    @property
    def kode_alumni(self):
        return self.__kode_alumni

    @kode_alumni.setter
    def kode_alumni(self, value):
        self.__kode_alumni = value

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
    def tempat_kerja(self):
        return self.__tempat_kerja

    @tempat_kerja.setter
    def tempat_kerja(self, value):
        self.__tempat_kerja = value
        
    @property
    def jabatan(self):
        return self.__jabatan

    @tempat_kerja.setter
    def jabatan(self, value):
        self.__jabatan = value
        
    @property
    def bekerja_sejak(self):
        return self.__bekerja_sejak

    @tempat_kerja.setter
    def bekerja_sejak(self, value):
        self.__bekerja_sejak = value
        
    @property
    def telepon(self):
        return self.__telepon

    @tempat_kerja.setter
    def telepon(self, value):
        self.__telepon = value
        
    @property
    def email(self):
        return self.__email

    @tempat_kerja.setter
    def email(self, value):
        self.__email = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_alumni, self.__nama, self.__jk, self.__tempat_kerja, self.__jabatan, self.__bekerja_sejak, self.__telepon, self.__email)
        sql="INSERT INTO alumni (kode_alumni, nama, jk, tempat_kerja, jabatan, bekerja_sejak, telepon, email) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, idalumni):
        self.conn = mydb()
        val = (self.__kode_alumni, self.__nama, self.__jk, self.__tempat_kerja, self.__jabatan, self.__bekerja_sejak, self.__telepon, self.__email, idalumni)
        sql="UPDATE alumni SET kode_alumni = %s, nama = %s, jk=%s, tempat_kerja=%s, jabatan=%s, bekerja_sejak=%s, telepon=%s, email=%s WHERE idalumni=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByKODEALUMNI(self, kode_alumni):
        self.conn = mydb()
        val = (self.__nama, self.__jk, self.__tempat_kerja, self.__jabatan, self.__bekerja_sejak, self.__telepon, self.__email, kode_alumni)
        sql="UPDATE alumni SET nama = %s, jk=%s, tempat_kerja=%s, jabatan=%s, bekerja_sejak=%s, telepon=%s, email=%s WHERE kode_alumni=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, idalumni):
        self.conn = mydb()
        sql="DELETE FROM alumni WHERE idalumni='" + str(idalumni) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByKODEALUMNI(self, kode_alumni):
        self.conn = mydb()
        sql="DELETE FROM alumni WHERE kode_alumni='" + str(kode_alumni) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByIDALUMNI(self, idalumni):
        self.conn = mydb()
        sql="SELECT * FROM alumni WHERE idalumni='" + str(idalumni) + "'"
        self.result = self.conn.findOne(sql)
        self.__kode_alumni = self.result[1]
        self.__nama = self.result[2]
        self.__jk = self.result[3]
        self.__tempat_kerja = self.result[4]
        self.__jabatan = self.result[5]
        self.__bekerja_sejak = self.result[6]
        self.__telepon = self.result[7]
        self.__email = self.result[8]
        self.conn.disconnect
        return self.result

    def getByKODEALUMNI(self, kode_alumni):
        self.conn = mydb()
        sql="SELECT * FROM alumni WHERE kode_alumni='" + str(kode_alumni) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_alumni = self.result[1]
            self.__nama = self.result[2]
            self.__jk = self.result[3]
            self.__tempat_kerja = self.result[4]
            self.__jabatan = self.result[5]
            self.__bekerja_sejak = self.result[6]
            self.__telepon = self.result[7]
            self.__email = self.result[8]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_alumni = ''
            self.__nama = ''
            self.__jk = ''
            self.__tempat_kerja = ''
            self.__jabatan = ''
            self.__bekerja_sejak = ''
            self.__telepon = ''
            self.__email = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM alumni"
        self.result = self.conn.findAll(sql)
        return self.result
"""
alm = Alumni()
a = mydb()
sql="SELECT * FROM alumni"
cur = a.findAll(sql)
# Get all 
result = alm.getAllData()
print(result)
"""