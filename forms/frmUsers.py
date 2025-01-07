import sys
import psycopg2 as mc
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from classes.Users import Users

qtcreator_file  = "ui/users.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class WindowUsers(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data) # Jika tombol cari diklik
        self.btnSimpan.clicked.connect(self.save_data) # Jika tombol simpan diklik
        self.txtKODEUSERS.returnPressed.connect(self.search_data) # Jika menekan tombol Enter saat berada di textbox NIM
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=""   
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("border: 2px solid goldenrod; border-radius: 10px; padding: 0 8px; background-color: gold; color: rgb(0, 0, 0);")

    def select_data(self):
        try:
            usr = Users()

            # Get all 
            result = usr.getAllData()

            self.gridUsers.setHorizontalHeaderLabels(['ID USERS', 'Username', 'Password'])
            self.gridUsers.setRowCount(0)
            

            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridUsers.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridUsers.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            username=self.txtKODEUSERS.text()           
            usr = Users()

            # search process
            result = usr.getByUSERS(username)
            a = usr.affected
            if(a>0):
                self.txtPsw.setText(result[2])
                self.btnSimpan.setText("Update")
                self.edit_mode=True
                self.btnHapus.setEnabled(True) # Aktifkan tombol hapus
                self.btnHapus.setStyleSheet("border: 2px solid goldenrod; border-radius: 10px; padding: 0 8px; background-color: gold; color: rgb(0, 0, 0);")
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtPsw.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False) # Matikan tombol hapus
                self.btnHapus.setStyleSheet("border: 2px solid goldenrod; border-radius: 10px; padding: 0 8px; background-color: gold; color: rgb(0, 0, 0);")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self, MainWindow):
        try:
            usr = Users()
            username=self.txtKODEUSERS.text()
            password1=self.txtPsw.text()
            
            if(self.edit_mode==False):   
                usr.username = username
                usr.password1 = password1
                a = usr.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Users Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Users Gagal Tersimpan")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            elif(self.edit_mode==True):
                usr.password1 = password1
                a = usr.updateByUSERNAME(username)
                if(a>0):
                    self.messagebox("SUKSES", "Data Users Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Users Gagal Diperbarui")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def delete_data(self, MainWindow):
        try:
            usr = Users()
            username=self.txtKODEUSERS.text()
                       
            if(self.edit_mode==True):
                a = usr.deleteByUSERNAME(username)
                if(a>0):
                    self.messagebox("SUKSES", "Data Users Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Users Gagal Dihapus")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def clear_entry(self, MainWindow):
        self.txtKODEUSERS.setText("")
        self.txtPsw.setText("")
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("border: 2px solid goldenrod; border-radius: 10px; padding: 0 8px; background-color: gold; color: rgb(0, 0, 0);")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()

Use = """ WindowAnggota, WindowBuku, WindowUsers, WindowKategori, WindowPeminjaman, MainWindow {
    border-image: url("ui/wpumc.jpeg") 0 0 0 0 stetch stretch; font-color: red; color: white; background-size: auto; background-position: center;
}"""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowUsers()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(Use)
    window = WindowUsers()