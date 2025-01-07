from config.db import DBConnection as mydb

class Kategori:

    def __init__(self):
        self.__idkategori=None
        self.__nama_kategori=None
        self.__digunakan_untuk=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "Nama Kategori:" + self.__nama_kategori + "\n" + "Digunakan Untuk:" + self.__digunakan_untuk
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def idkategori(self):
        return self.__idkategori

    @property
    def nama_kategori(self):
        return self.__nama_kategori

    @nama_kategori.setter
    def nama_kategori(self, value):
        self.__nama_kategori = value

    @property
    def digunakan_untuk(self):
        return self.__digunakan_untuk

    @digunakan_untuk.setter
    def digunakan_untuk(self, value):
        self.__digunakan_untuk = value

   
    def simpan(self):
        self.conn = mydb()
        val = (self.__nama_kategori, self.__digunakan_untuk)
        sql="INSERT INTO kategori (nama_kategori, digunakan_untuk) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, idkategori):
        self.conn = mydb()
        val = (self.__nama_kategori, self.__digunakan_untuk, idkategori)
        sql="UPDATE kategori SET nama_kategori = %s, digunakan_untuk = %s WHERE idkategori=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByNameKategori(self, nama_kategori):
        self.conn = mydb()
        val = (self.__digunakan_untuk, nama_kategori)
        sql="UPDATE kategori SET digunakan_untuk = %s WHERE nama_kategori=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, idkategori):
        self.conn = mydb()
        sql="DELETE FROM kategori WHERE idkategori='" + str(idkategori) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNameKategori(self, nama_kategori):
        self.conn = mydb()
        sql="DELETE FROM kategori WHERE nama_kategori='" + str(nama_kategori) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByIDkategori(self, idkategori):
        a=str(idkategori)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM kategori WHERE idkategori='" + b + "'"
        self.result = self.conn.findOne(sql)
        self.__idkategori = str(self.result[0])
        self.__nama_kategori = self.result[1]
        self.__digunakan_untuk = self.result[2]
        self.conn.disconnect
        return self.result

    def getByNamekategori(self, nama_kategori):
        a=str(nama_kategori)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM kategori WHERE nama_kategori='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__idkategori = str(self.result[0])
            self.__nama_kategori = self.result[1]
            self.__digunakan_untuk = self.result[2]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nama_kategori = ''
            self.__digunakan_untuk = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM kategori"
        self.result = self.conn.findAll(sql)
        return self.result


ktr = Kategori()
a = mydb()
sql="SELECT * FROM kategori"
cur = a.findAll(sql)
# Get all 
result = ktr.getAllData()
print(result)