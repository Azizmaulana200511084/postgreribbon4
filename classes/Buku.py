from config.db import DBConnection as mydb

class Buku:

    def __init__(self):
        self.__idbuku=None
        self.__kodebuku=None
        self.__judul=None
        self.__idkategori=None
        self.__pengarang=None
        self.__penerbit=None
        self.__tahun=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "KODE BUKU:" + self.__kodebuku + "\n" + "Judul:" + self.__judul + "\n" + "ID Kategori" + self.__idkategori + "\n" + "Pengarang:" + self.__pengarang + "\n" + "Penerbit:" + self.__penerbit + "\n" + "Tahun:" + self.__tahun
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def idbuku(self):
        return self.__idbuku

    @property
    def kodebuku(self):
        return self.__kodebuku

    @kodebuku.setter
    def kodebuku(self, value):
        self.__kodebuku = value

    @property
    def judul(self):
        return self.__judul

    @judul.setter
    def judul(self, value):
        self.__judul = value

    @property
    def idkategori(self):
        return self.__idkategori

    @idkategori.setter
    def idkategori(self, value):
        self.__idkategori = value

    @property
    def pengarang(self):
        return self.__pengarang

    @pengarang.setter
    def pengarang(self, value):
        self.__pengarang = value
        
    @property
    def penerbit(self):
        return self.__penerbit

    @penerbit.setter
    def penerbit(self, value):
        self.__penerbit = value
        
    @property
    def tahun(self):
        return self.__tahun

    @tahun.setter
    def tahun(self, value):
        self.__tahun = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__kodebuku, self.__judul, self.__idkategori, self.__pengarang, self.__penerbit, self.__tahun)
        sql="INSERT INTO buku (kodebuku, judul, idkategori, pengarang, penerbit, tahun) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, idbuku):
        self.conn = mydb()
        val = (self.__kodebuku, self.__judul, self.__idkategori, self.__pengarang, self.__penerbit, self.__tahun, idbuku)
        sql="UPDATE buku SET kodebuku = %s, judul = %s, idkategori=%s, pengarang=%s, penerbit=%s, tahun=%s WHERE idbuku=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByKODEBUKU(self, kodebuku):
        self.conn = mydb()
        val = (self.__judul, self.__idkategori, self.__pengarang, self.__penerbit, self.__tahun, kodebuku)
        sql="UPDATE buku SET judul = %s, idkategori=%s, pengarang=%s, penerbit=%s, tahun=%s WHERE kodebuku=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, idbuku):
        self.conn = mydb()
        sql="DELETE FROM buku WHERE idbuku='" + str(idbuku) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByKODEBUKU(self, kodebuku):
        self.conn = mydb()
        sql="DELETE FROM buku WHERE kodebuku='" + str(kodebuku) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByIDBUKU(self, idbuku):
        a=str(idbuku)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM buku WHERE idbuku='" + b + "'"
        self.result = self.conn.findOne(sql)
        self.__kodebuku = self.result[1]
        self.__judul = self.result[2]
        self.__idkategori = str(self.result[3])
        self.__pengarang = self.result[4]
        self.__penerbit = self.result[5]
        self.__tahun = str(self.result[6])
        self.conn.disconnect
        return self.result

    def getByKODBUKU(self, kodebuku):
        a=str(kodebuku)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM buku WHERE kodebuku='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kodebuku = self.result[1]
            self.__judul = self.result[2]
            self.__idkategori = str(self.result[3])
            self.__pengarang = self.result[4]
            self.__penerbit = self.result[5]
            self.__tahun = str(self.result[6])
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kodebuku = ''
            self.__judul = ''
            self.__idkategori = ''
            self.__pengarang = ''
            self.__penerbit = ''
            self.__tahun = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM buku"
        self.result = self.conn.findAll(sql)
        return self.result

bk = Buku()
a = mydb()
sql="SELECT * FROM buku"
cur = a.findAll(sql)
# Get all 
result = bk.getAllData()
print(result)