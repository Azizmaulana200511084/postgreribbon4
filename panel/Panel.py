from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from forms.frmAnggota import WindowAnggota
from forms.frmBuku import WindowBuku
from forms.frmKategori import WindowKategori
from forms.frmPeminjaman import WindowPeminjaman
from forms.frmUsers import WindowUsers
dock = QtWidgets.QDockWidget()
def child_panels(self):   
    buku_panel(self)
    anggota_panel(self)
    kategori_panel(self)
    peminjaman_panel(self)
    users_panel(self)

def anggota_panel(self):     
    anggota_widget = WindowAnggota()
    anggota_widget.select_data()
    self.centralwidget = anggota_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)
        
def buku_panel(self):
    buku_widget = WindowBuku()
    buku_widget.select_data()
    self.centralwidget = buku_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def kategori_panel(self):
    kategori_widget = WindowKategori()
    kategori_widget.select_data()
    self.centralwidget = kategori_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def peminjaman_panel(self):
    peminjaman_widget = WindowKategori()
    peminjaman_widget.select_data()
    self.centralwidget = peminjaman_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def users_panel(self):
    users_widget = WindowUsers()
    users_widget.select_data()
    self.centralwidget = users_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def anggota_on(self):
    anggota_widget = WindowAnggota()
    anggota_widget.select_data()
    self.centralwidget = anggota_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()

def buku_on(self):
    buku_widget = WindowBuku()
    buku_widget.select_data()
    self.centralwidget = buku_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()

def kategori_on(self):
    kategori_widget = WindowKategori()
    kategori_widget.select_data()
    self.centralwidget = kategori_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()

def peminjaman_on(self):
    peminjaman_widget = WindowPeminjaman()
    peminjaman_widget.select_data()
    self.centralwidget = peminjaman_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()

def users_on(self):
    users_widget = WindowUsers()
    users_widget.select_data()
    self.centralwidget = users_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()




        
     