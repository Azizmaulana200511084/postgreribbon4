import sys
import psycopg2 as mc
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from classes.Peminjaman import Peminjaman
from classes.Anggota import Anggota
from classes.Buku import Buku
from classes.Users import Users

qtcreator_file  = "ui/peminjaman.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class WindowPeminjaman(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data) # Jika tombol cari diklik
        self.btnSimpan.clicked.connect(self.save_data) # Jika tombol simpan diklik
        self.txtNomorBukti.returnPressed.connect(self.search_data) # Jika menekan tombol Enter saat berada di textbox NIM
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.btnCariKodeAnggota.clicked.connect(self.cari_anggota)
        self.btnCariKodeBuku1.clicked.connect(self.cari_buku1) 
        self.btnCariKodeBuku2.clicked.connect(self.cari_buku2) 
        self.btnCariKodeBuku3.clicked.connect(self.cari_buku3)
        self.edit_mode=""   
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("border: 2px solid goldenrod; border-radius: 10px; padding: 0 8px; background-color: gold; color: rgb(0, 0, 0);")

    def select_data(self):
        try:
            pjm = Peminjaman()

            # Get all 
            result = pjm.getAllData()

            self.gridPeminjaman.setHorizontalHeaderLabels(['ID Pjm', 'No Bkti', 'Kde Anggota', 'Tgl Pjm', 'Tgl HrsKmbli', 'Tgl Dikmblikn', 'Total Pjm', 'Kde Bku1', 'Kde Bku2', 'Kde Bku3', 'Stts Pjm', 'ID Usr'])
            self.gridPeminjaman.setRowCount(0)
            

            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridPeminjaman.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridPeminjaman.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def cari_anggota(self):
        try:           
            kode=self.txtKodeAnggota.text()           
            ang =Anggota()
            # search process
            result = ang.getByKodeAnggota(kode)           
            a = ang.affected
            
            if(a!=0):
                self.txtNamaAnggota.setText(ang.nama.strip())
            else:
                self.messagebox("INFO", "Data Anggota tidak ditemukan")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def cari_buku1(self):
        try:
            book = Buku()
            kode = self.txtKodeBuku1.text()
            book.getByKODBUKU(kode)
            a = book.affected
            if(a!=0):
                self.txtJudulBuku1.setText(book.judul.strip())                                              
            else:
                self.messagebox("INFO", "Judul Buku tidak ditemukan")

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def cari_buku2(self):
        try:
            book = Buku()
            kode = self.txtKodeBuku2.text()
            book.getByKODBUKU(kode)
            a = book.affected
            if(a!=0):
                self.txtJudulBuku2.setText(book.judul.strip())                                              
            else:
                self.messagebox("INFO", "Judul Buku tidak ditemukan")

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def cari_buku3(self):
        try:
            book = Buku()
            kode = self.txtKodeBuku3.text()
            book.getByKODBUKU(kode)
            a = book.affected
            if(a!=0):
                self.txtJudulBuku3.setText(book.judul.strip())                                              
            else:
                self.messagebox("INFO", "Judul Buku tidak ditemukan")

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def cari_idusers(self):
        try:           
            kode=self.txtIDUSER.text()           
            ang =Users()
            # search process
            result = ang.getByIDUSERNAME(kode)           
            a = ang.affected
            
            if(a!=0):
                self.txtKODEUSERS.setText(ang.username.strip())
            else:
                self.messagebox("INFO", "Data Users tidak ditemukan")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            nomor_bukti=self.txtNomorBukti.text()           
            pjm = Peminjaman()

            # search process
            result = pjm.getByKODBUKU(nomor_bukti)
            a = pjm.affected
            if(a>0):
                self.txtKodeAnggota.setText(result[2])
                self.cari_anggota()
                self.txtTglPjm.setDate(result[3])
                self.txtTglHrsKmbli.setDate(result[4])
                self.txtTglDiKmblkn.setDate(result[5])
                self.txtTtlPjm.setText(pjm.total_pinjam.strip())
                self.txtKodeBuku1.setText(result[7])
                a=self.txtKodeBuku1.text()
                if(a!=""):
                    self.cari_buku1()
                self.txtKodeBuku2.setText(result[8])
                b = self.txtKodeBuku2.text()
                if(b!=""):
                    self.cari_buku2()
                self.txtKodeBuku3.setText(result[9])
                c = self.txtKodeBuku3.text()
                if(c!=""):
                    self.cari_buku3()
                if(result[10]=="Y"):
                    self.optYes.setChecked(True)
                    self.optNo.setChecked(False)
                else:
                    self.optYes.setChecked(False)
                    self.optNo.setChecked(True)
                self.txtIDUSER.setText(pjm.iduser.strip())
                self.cari_idusers()
                self.btnSimpan.setText("Update")
                self.edit_mode=True
                self.btnHapus.setEnabled(True) # Aktifkan tombol hapus
                self.btnHapus.setStyleSheet("border: 2px solid goldenrod; border-radius: 10px; padding: 0 8px; background-color: gold; color: rgb(0, 0, 0);")
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtKodeAnggota.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False) # Matikan tombol hapus
                self.btnHapus.setStyleSheet("border: 2px solid goldenrod; border-radius: 10px; padding: 0 8px; background-color: gold; color: rgb(0, 0, 0);")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self, MainWindow):
        try:
            pjm = Peminjaman()
            nomor_bukti=self.txtNomorBukti.text()
            kode_anggota=self.txtKodeAnggota.text()
            tanggal_pinjam= self.txtTglPjm.date().toString("yyyy-MM-dd")
            tanggal_haruskembali= self.txtTglHrsKmbli.date().toString("yyyy-MM-dd")
            tanggal_dikembalikan= self.txtTglDiKmblkn.date().toString("yyyy-MM-dd")
            total_pinjam=self.txtTtlPjm.text()
            kode_buku1= self.txtKodeBuku1.text()
            kode_buku2=self.txtKodeBuku2.text()
            kode_buku3= self.txtKodeBuku3.text()
            if self.optYes.isChecked():
                status_pinjam="Y"
            if self.optNo.isChecked():
                status_pinjam="N"
            iduser= self.txtIDUSER.text()
            if(self.edit_mode==False):   
                pjm.nomor_bukti = nomor_bukti
                pjm.kode_anggota = kode_anggota
                pjm.tanggal_pinjam = tanggal_pinjam
                pjm.tanggal_haruskembali = tanggal_haruskembali
                pjm.tanggal_dikembalikan = tanggal_dikembalikan
                pjm.total_pinjam = total_pinjam
                pjm.kode_buku1 = kode_buku1
                pjm.kode_buku2 = kode_buku2
                pjm.kode_buku3 = kode_buku3
                pjm.status_pinjam = status_pinjam
                pjm.iduser = iduser
                a = pjm.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Peminjaman Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Peminjaman Gagal Tersimpan")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            elif(self.edit_mode==True):
                pjm.nomor_bukti = nomor_bukti
                pjm.kode_anggota = kode_anggota
                pjm.tanggal_pinjam = tanggal_pinjam
                pjm.tanggal_haruskembali = tanggal_haruskembali
                pjm.tanggal_dikembalikan = tanggal_dikembalikan
                pjm.total_pinjam = total_pinjam
                pjm.kode_buku1 = kode_buku1
                pjm.kode_buku2 = kode_buku2
                pjm.kode_buku3 = kode_buku3
                pjm.status_pinjam = status_pinjam
                pjm.iduser = iduser
                a = pjm.updateByKODEBUKU(nomor_bukti)
                if(a>0):
                    self.messagebox("SUKSES", "Data Peminjaman Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Peminjaman Gagal Diperbarui")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def delete_data(self, MainWindow):
        try:
            pjm = Peminjaman()
            nomor_bukti=self.txtNomorBukti.text()
                       
            if(self.edit_mode==True):
                a = pjm.deleteByKODEBUKU(nomor_bukti)
                if(a>0):
                    self.messagebox("SUKSES", "Data Peminjaman Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Peminjaman Gagal Dihapus")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def clear_entry(self, MainWindow):
        self.txtNomorBukti.setText("")
        self.txtKodeAnggota.setText("")
        self.txtNamaAnggota.setText("")
        self.txtTtlPjm.setText("")
        self.txtKodeBuku1.setText("")
        self.txtJudulBuku1.setText("")
        self.txtKodeBuku2.setText("")
        self.txtJudulBuku2.setText("")
        self.txtKodeBuku3.setText("")
        self.txtJudulBuku3.setText("")
        self.optYes.setChecked(False)
        self.optNo.setChecked(False)
        self.txtIDUSER.setText("")
        self.txtKODEUSERS.setText("")
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("border: 2px solid goldenrod; border-radius: 10px; padding: 0 8px; background-color: gold; color: rgb(0, 0, 0);")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()

Pem = """ WindowAnggota, WindowBuku, WindowUsers, WindowKategori, WindowPeminjaman, MainWindow {
    border-image: url("ui/wpumc.jpeg") 0 0 0 0 stetch stretch; font-color: red; color: white; background-size: auto; background-position: center;
}"""


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowPeminjaman()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(Pem)
    window = WindowPeminjaman()