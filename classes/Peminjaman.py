from config.db import DBConnection as mydb

class Peminjaman:

    def __init__(self):
        self.__idpinjam=None
        self.__nomor_bukti=None
        self.__kode_anggota=None
        self.__tanggal_pinjam=None
        self.__tanggal_haruskembali=None
        self.__tanggal_dikembalikan=None
        self.__total_pinjam=None
        self.__kode_buku1=None
        self.__kode_buku2=None
        self.__kode_buku3=None
        self.__status_pinjam=None
        self.__iduser=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "No Bkti:" + self.__nomor_bukti + "\n" + "Kde Anggota:" + self.__kode_anggota + "\n" + "Tgl Pjm" + self.__tanggal_pinjam + "\n" + "Tgl HrsKmbli:" + self.__tanggal_haruskembali + "\n" + "Tgl Dikmblikn:" + self.__tanggal_dikembalikan + "\n" + "Total Pjm:" + self.__total_pinjam+ "\n" + "Kde Bku1:" + self.__kode_buku1+ "\n" + "Kde Bku2:" + self.__kode_buku2+ "\n" + "Kde Bku3:" + self.__kode_buku3+ "\n" + "Stts Pjm:" + self.__status_pinjam+ "\n" + "ID Usr:" + self.__iduser
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def idpinjam(self):
        return self.__idpinjam

    @property
    def nomor_bukti(self):
        return self.__nomor_bukti

    @nomor_bukti.setter
    def nomor_bukti(self, value):
        self.__nomor_bukti = value

    @property
    def kode_anggota(self):
        return self.__kode_anggota

    @kode_anggota.setter
    def kode_anggota(self, value):
        self.__kode_anggota = value

    @property
    def tanggal_pinjam(self):
        return self.__tanggal_pinjam

    @tanggal_pinjam.setter
    def tanggal_pinjam(self, value):
        self.__tanggal_pinjam = value

    @property
    def tanggal_haruskembali(self):
        return self.__tanggal_haruskembali

    @tanggal_haruskembali.setter
    def tanggal_haruskembali(self, value):
        self.__tanggal_haruskembali = value
        
    @property
    def tanggal_dikembalikan(self):
        return self.__tanggal_dikembalikan

    @tanggal_dikembalikan.setter
    def tanggal_dikembalikan(self, value):
        self.__tanggal_dikembalikan = value
        
    @property
    def total_pinjam(self):
        return self.__total_pinjam

    @total_pinjam.setter
    def total_pinjam(self, value):
        self.__total_pinjam = value

    @property
    def kode_buku1(self):
        return self.__kode_buku1

    @kode_buku1.setter
    def kode_buku1(self, value):
        self.__kode_buku1 = value

    @property
    def kode_buku2(self):
        return self.__kode_buku2

    @kode_buku2.setter
    def kode_buku2(self, value):
        self.__kode_buku2 = value

    @property
    def kode_buku3(self):
        return self.__kode_buku3

    @kode_buku3.setter
    def kode_buku3(self, value):
        self.__kode_buku3 = value

    @property
    def status_pinjam(self):
        return self.__status_pinjam

    @status_pinjam.setter
    def status_pinjam(self, value):
        self.__status_pinjam = value

    @property
    def iduser(self):
        return self.__iduser

    @iduser.setter
    def iduser(self, value):
        self.__iduser = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__nomor_bukti, self.__kode_anggota, self.__tanggal_pinjam, self.__tanggal_haruskembali, self.__tanggal_dikembalikan, self.__total_pinjam, self.__kode_buku1, self.__kode_buku2, self.__kode_buku3, self.__status_pinjam, self.__iduser)
        sql="INSERT INTO peminjaman (nomor_bukti, kode_anggota, tanggal_pinjam, tanggal_haruskembali, tanggal_dikembalikan, total_pinjam, kode_buku1, kode_buku2, kode_buku3, status_pinjam, iduser) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, idpinjam):
        self.conn = mydb()
        val = (self.__nomor_bukti, self.__kode_anggota, self.__tanggal_pinjam, self.__tanggal_haruskembali, self.__tanggal_dikembalikan, self.__total_pinjam, self.__kode_buku1, self.__kode_buku2, self.__kode_buku3, self.__status_pinjam, self.__iduser, idpinjam)
        sql="UPDATE peminjaman SET nomor_bukti = %s, kode_anggota = %s, tanggal_pinjam=%s, tanggal_haruskembali=%s, tanggal_dikembalikan=%s, total_pinjam=%s, kode_buku1=%s, kode_buku2=%s, kode_buku3=%s, status_pinjam=%s, iduser=%s WHERE idpinjam=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByKODEBUKU(self, nomor_bukti):
        self.conn = mydb()
        val = (self.__kode_anggota, self.__tanggal_pinjam, self.__tanggal_haruskembali, self.__tanggal_dikembalikan, self.__total_pinjam, self.__kode_buku1, self.__kode_buku2, self.__kode_buku3, self.__status_pinjam, self.__iduser, nomor_bukti)
        sql="UPDATE peminjaman SET kode_anggota = %s, tanggal_pinjam=%s, tanggal_haruskembali=%s, tanggal_dikembalikan=%s, total_pinjam=%s, kode_buku1=%s, kode_buku2=%s, kode_buku3=%s, status_pinjam=%s, iduser=%s WHERE nomor_bukti=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, idpinjam):
        self.conn = mydb()
        sql="DELETE FROM peminjaman WHERE idpinjam='" + str(idpinjam) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByKODEBUKU(self, nomor_bukti):
        self.conn = mydb()
        sql="DELETE FROM peminjaman WHERE nomor_bukti='" + str(nomor_bukti) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByIDBUKU(self, idpinjam):
        self.conn = mydb()
        sql="SELECT * FROM peminjaman WHERE idpinjam='" + str(idpinjam) + "'"
        self.result = self.conn.findOne(sql)
        self.__nomor_bukti = self.result[1]
        self.__kode_anggota = self.result[2]
        self.__tanggal_pinjam = self.result[3]
        self.__tanggal_haruskembali = self.result[4]
        self.__tanggal_dikembalikan = self.result[5]
        self.__total_pinjam = str(self.result[6])
        self.__kode_buku1 = self.result[7]
        self.__kode_buku2 = self.result[8]
        self.__kode_buku3 = self.result[9]
        self.__status_pinjam = self.result[10]
        self.__iduser = str(self.result[11])
        self.conn.disconnect
        return self.result

    def getByKODBUKU(self, nomor_bukti):
        a=str(nomor_bukti)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM peminjaman WHERE nomor_bukti='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nomor_bukti = self.result[1]
            self.__kode_anggota = self.result[2]
            self.__tanggal_pinjam = self.result[3]
            self.__tanggal_haruskembali = self.result[4]
            self.__tanggal_dikembalikan = self.result[5]
            self.__total_pinjam = str(self.result[6])
            self.__kode_buku1 = self.result[7]
            self.__kode_buku2 = self.result[8]
            self.__kode_buku3 = self.result[9]
            self.__status_pinjam = self.result[10]
            self.__iduser = str(self.result[11])
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nomor_bukti = ''
            self.__kode_anggota = ''
            self.__tanggal_pinjam = ''
            self.__tanggal_haruskembali = ''
            self.__tanggal_dikembalikan = ''
            self.__total_pinjam = ''
            self.__kode_buku1 = ''
            self.__kode_buku2 = ''
            self.__kode_buku3 = ''
            self.status_pinjam = ''
            self.__iduser = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM peminjaman"
        self.result = self.conn.findAll(sql)
        return self.result

pjm = Peminjaman()
a = mydb()
sql="SELECT * FROM peminjaman"
cur = a.findAll(sql)
# Get all 
result = pjm.getAllData()
print(result)