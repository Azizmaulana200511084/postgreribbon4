import sys
import psycopg2 as mc
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from classes.Anggota import Anggota

qtcreator_file  = "ui/anggota.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class WindowAnggota(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data) # Jika tombol cari diklik
        self.btnSimpan.clicked.connect(self.save_data) # Jika tombol simpan diklik
        self.txtKodeAnggota.returnPressed.connect(self.search_data) # Jika menekan tombol Enter saat berada di textbox Kode Anggota
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=""   
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("border: 2px solid goldenrod; border-radius: 10px; padding: 0 8px; background-color: gold; color: rgb(0, 0, 0);")

    def select_data(self):
        try:
            agt = Anggota()

            # Get all 
            result = agt.getAllData()

            self.gridAnggota.setHorizontalHeaderLabels(['ID Anggota', 'Kode Anggota', 'Nama', 'Jenis Kelamin', 'Keterangan'])
            self.gridAnggota.setRowCount(0)
            

            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridAnggota.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridAnggota.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            kode_anggota =self.txtKodeAnggota.text()           
            agt = Anggota()

            # search process
            result = agt.getByKodeAnggota(kode_anggota)
            a = agt.affected
            if(a>0):
                self.txtNama.setText(result[2])
                if(result[3]=="L"):
                    self.optLaki.setChecked(True)
                    self.optPerempuan.setChecked(False)
                else:
                    self.optLaki.setChecked(False)
                    self.optPerempuan.setChecked(True)

                self.txtKeterangan.setText(result[4])
                self.btnSimpan.setText("Update")
                self.edit_mode=True
                self.btnHapus.setEnabled(True) # Aktifkan tombol hapus
                self.btnHapus.setStyleSheet("border: 2px solid goldenrod; border-radius: 10px; padding: 0 8px; background-color: gold; color: rgb(0, 0, 0);")
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtNama.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False) # Matikan tombol hapus
                self.btnHapus.setStyleSheet("border: 2px solid goldenrod; border-radius: 10px; padding: 0 8px; background-color: gold; color: rgb(0, 0, 0);")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self, MainWindow):
        try:
            agt = Anggota()
            kode_anggota=self.txtKodeAnggota.text()
            nama=self.txtNama.text()
            if self.optLaki.isChecked():
                jk="L"
            
            if self.optPerempuan.isChecked():
                jk="P"

            keterangan=self.txtKeterangan.text()
            
            if(self.edit_mode==False):   
                agt.kode_anggota = kode_anggota
                agt.nama = nama
                agt.jk = jk
                agt.keterangan = keterangan
                a = agt.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Anggota Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Anggota Gagal Tersimpan")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            elif(self.edit_mode==True):
                agt.nama = nama
                agt.jk = jk
                agt.keterangan = keterangan
                a = agt.updateByKodeAnggota(kode_anggota)
                if(a>0):
                    self.messagebox("SUKSES", "Data Anggota Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Anggota Gagal Diperbarui")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def delete_data(self, MainWindow):
        try:
            agt = Anggota()
            kode_anggota=self.txtKodeAnggota.text()
                       
            if(self.edit_mode==True):
                a = agt.deleteByKodeAnggota(kode_anggota)
                if(a>0):
                    self.messagebox("SUKSES", "Data Anggota Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Anggota Gagal Dihapus")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def clear_entry(self, MainWindow):
        self.txtKodeAnggota.setText("")
        self.txtNama.setText("")
        self.optLaki.setChecked(False)
        self.optPerempuan.setChecked(False)
        self.txtKeterangan.setText("")
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("border: 2px solid goldenrod; border-radius: 10px; padding: 0 8px; background-color: gold; color: rgb(0, 0, 0);")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()

ang = """ WindowAnggota, WindowBuku, WindowUsers, WindowKategori, WindowPeminjaman, MainWindow {
    border-image: url("ui/wpumc.jpeg") 0 0 0 0 stetch stretch; font-color: red; color: white; background-size: auto; background-position: center;
}"""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(ang)
    window = WindowAnggota()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(ang)
    window = WindowAnggota()