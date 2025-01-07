import sys
import psycopg2 as mc
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from classes.Buku import Buku
from classes.Kategori import Kategori

qtcreator_file  = "ui/buku.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class WindowBuku(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data) # Jika tombol cari diklik
        self.btnSimpan.clicked.connect(self.save_data) # Jika tombol simpan diklik
        self.txtKODEBUKU.returnPressed.connect(self.search_data) # Jika menekan tombol Enter saat berada di textbox NIM
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=""   
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("border: 2px solid goldenrod; border-radius: 10px; padding: 0 8px; background-color: gold; color: rgb(0, 0, 0);")

    def select_data(self):
        try:
            bku = Buku()

            # Get all 
            result = bku.getAllData()

            self.gridBuku.setHorizontalHeaderLabels(['ID BUKU', 'Kode Buku', 'Judul', 'ID Kategori', 'Pengarang', 'Penerbit', 'Tahun'])
            self.gridBuku.setRowCount(0)
            

            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridBuku.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridBuku.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def cari_idkategori(self):
        try:           
            kode=self.txtIDKATEGORI.text()           
            ang =Kategori()
            # search process
            ang.getByIDkategori(kode)           
            a = ang.affected
            
            if(a!=0):
                self.txtNamaKategori.setText(ang.nama_kategori.strip())
            else:
                self.messagebox("INFO", "Data kategori tidak ditemukan")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            kodebuku=self.txtKODEBUKU.text()           
            bku = Buku()

            # search process
            result = bku.getByKODBUKU(kodebuku)
            a = bku.affected
            if(a>0):
                self.txtJudul.setText(result[2])
                self.txtIDKATEGORI.setText(bku.idkategori.strip())
                self.cari_idkategori()
                self.txtPENGARANG.setText(result[4])
                self.txtPENERBIT.setText(result[5])
                self.txtTAHUN.setText(bku.tahun.strip())
                self.btnSimpan.setText("Update")
                self.edit_mode=True
                self.btnHapus.setEnabled(True) # Aktifkan tombol hapus
                self.btnHapus.setStyleSheet("border: 2px solid goldenrod; border-radius: 10px; padding: 0 8px; background-color: gold; color: rgb(0, 0, 0);")
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtJudul.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False) # Matikan tombol hapus
                self.btnHapus.setStyleSheet("border: 2px solid goldenrod; border-radius: 10px; padding: 0 8px; background-color: gold; color: rgb(0, 0, 0);")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self, MainWindow):
        try:
            bku = Buku()
            kodebuku=self.txtKODEBUKU.text()
            judul=self.txtJudul.text()
            idkategori=self.txtIDKATEGORI.text()
            pengarang=self.txtPENGARANG.text()
            penerbit=self.txtPENERBIT.text()
            tahun=self.txtTAHUN.text()
            
            if(self.edit_mode==False):   
                bku.kodebuku = kodebuku
                bku.judul = judul
                bku.idkategori = idkategori
                bku.pengarang = pengarang
                bku.penerbit = penerbit
                bku.tahun = tahun
                a = bku.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Buku Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Buku Gagal Tersimpan")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            elif(self.edit_mode==True):
                bku.judul = judul
                bku.idkategori = idkategori
                bku.pengarang = pengarang
                bku.penerbit = penerbit
                bku.tahun = tahun
                a = bku.updateByKODEBUKU(kodebuku)
                if(a>0):
                    self.messagebox("SUKSES", "Data Buku Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Buku Gagal Diperbarui")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def delete_data(self, MainWindow):
        try:
            bku = Buku()
            kodebuku=self.txtKODEBUKU.text()
                       
            if(self.edit_mode==True):
                a = bku.deleteByKODEBUKU(kodebuku)
                if(a>0):
                    self.messagebox("SUKSES", "Data Buku Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Buku Gagal Dihapus")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def clear_entry(self, MainWindow):
        self.txtKODEBUKU.setText("")
        self.txtJudul.setText("")
        self.txtIDKATEGORI.setText("")
        self.txtNamaKategori.setText("")
        self.txtPENGARANG.setText("")
        self.txtPENERBIT.setText("")
        self.txtTAHUN.setText("")
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("border: 2px solid goldenrod; border-radius: 10px; padding: 0 8px; background-color: gold; color: rgb(0, 0, 0);")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()

Buk = """ WindowAnggota, WindowBuku, WindowUsers, WindowKategori, WindowPeminjaman, MainWindow {
    border-image: url("ui/wpumc.jpeg") 0 0 0 0 stetch stretch; font-color: red; color: white; background-size: auto; background-position: center;
}"""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(Buk)
    window = WindowBuku()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(Buk)
    window = WindowBuku()