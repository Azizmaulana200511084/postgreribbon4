import sys
import psycopg2 as mc
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from classes.Alumni import Alumni

qtcreator_file  = "ui/alumni.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class WindowAlumni(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data)
        self.btnCari.setStyleSheet("color:black;background-color : gold") # Jika tombol cari diklik
        self.btnSimpan.clicked.connect(self.save_data) # Jika tombol simpan diklik
        self.txtKODEALUMNI.returnPressed.connect(self.search_data) # Jika menekan tombol Enter saat berada di textbox NIM
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=""   
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : grey")

    def select_data(self):
        try:
            alm = Alumni()

            # Get all 
            result = alm.getAllData()

            self.gridAlumni.setHorizontalHeaderLabels(['ID ALUMNI', 'Kode Alumni', 'Nama', 'Jenis Kelamin', 'Tempat Kerja', 'Jabatan', 'Bekerja Sejak', 'Telepon', 'Email'])
            self.gridAlumni.setRowCount(0)
            

            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridAlumni.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridAlumni.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            kode_alumni=self.txtKODEALUMNI.text()           
            alm = Alumni()

            # search process
            result = alm.getByKODEALUMNI(kode_alumni)
            a = alm.affected
            if(a>0):
                self.txtNama.setText(result[2])
                if(result[3]=="L"):
                    self.optLaki.setChecked(True)
                    self.optPerempuan.setChecked(False)
                else:
                    self.optLaki.setChecked(False)
                    self.optPerempuan.setChecked(True)

                self.cboKerja.setText(result[4])
                self.cboJabatan.setCurrentText(result[5])
                self.cboBekerjaSejak.setText(result[6])
                self.cboTelepon.setText(result[7])
                self.cboEmail.setText(result[8])
                self.btnSimpan.setText("Update")
                self.edit_mode=True
                self.btnHapus.setEnabled(True) # Aktifkan tombol hapus
                self.btnHapus.setStyleSheet("background-color : red")
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtNama.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False) # Matikan tombol hapus
                self.btnHapus.setStyleSheet("color:black;background-color : grey")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self, MainWindow):
        try:
            alm = Alumni()
            kode_alumni=self.txtKODEALUMNI.text()
            nama=self.txtNama.text()
            if self.optLaki.isChecked():
                jk="L"
            
            if self.optPerempuan.isChecked():
                jk="P"

            tempat_kerja=self.cboKerja.text()
            jabatan=self.cboJabatan.currentText()
            bekerja_sejak=self.cboBekerjaSejak.text()
            telepon=self.cboTelepon.text()
            email=self.cboEmail.text()
            
            if(self.edit_mode==False):   
                alm.kode_alumni = kode_alumni
                alm.nama = nama
                alm.jk = jk
                alm.tempat_kerja = tempat_kerja
                alm.jabatan = jabatan
                alm.bekerja_sejak = bekerja_sejak
                alm.telepon = telepon
                alm.email = email
                a = alm.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Alumni Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Alumni Gagal Tersimpan")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            elif(self.edit_mode==True):
                alm.nama = nama
                alm.jk = jk
                alm.tempat_kerja = tempat_kerja
                alm.jabatan = jabatan
                alm.bekerja_sejak = bekerja_sejak
                alm.telepon = telepon
                alm.email = email
                a = alm.updateByKODEALUMNI(kode_alumni)
                if(a>0):
                    self.messagebox("SUKSES", "Data Alumni Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Alumni Gagal Diperbarui")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def delete_data(self, MainWindow):
        try:
            alm = Alumni()
            kode_alumni=self.txtKODEALUMNI.text()
                       
            if(self.edit_mode==True):
                a = alm.deleteByKODEALUMNI(kode_alumni)
                if(a>0):
                    self.messagebox("SUKSES", "Data Alumni Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Alumni Gagal Dihapus")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def clear_entry(self, MainWindow):
        self.txtKODEALUMNI.setText("")
        self.txtNama.setText("")
        self.optLaki.setChecked(False)
        self.optPerempuan.setChecked(False)
        self.cboKerja.setText("")
        self.cboJabatan.setCurrentText("")
        self.cboBekerjaSejak.setText("")
        self.cboTelepon.setText("")
        self.cboEmail.setText("")
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : grey")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()

st = """ WindowAlumni, WindowDosen, WindowMatakuliah, MahasiswaWindow, MainWindow {
    border-image: url("ui/wpumc.jpeg") 0 0 0 0 stetch stretch; font-color: red; color: white; background-size: auto; background-position: center;
}"""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(st)
    window = WindowAlumni()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(st)
    window = WindowAlumni()