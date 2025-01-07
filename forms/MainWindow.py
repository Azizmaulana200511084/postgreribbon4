from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QKeySequence as QKSec
from GUI.RibbonButton import RibbonButton
from GUI.Icons import get_icon
from GUI.RibbonTextbox import RibbonTextbox
from GUI.RibbonWidget import *
from panel.Panel import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.resize(1240, 1200)
        self.setWindowTitle("Aziz Maulana(200511084)")
        self.setDockNestingEnabled(True)
        self.setWindowIcon(get_icon("icon"))
        child_panels(self)
 
        # -------------      actions       -----------------

        self._buku_action = self.add_action("Buku", "buku", "Data Buku", True, self.on_buku)
        self._anggota_action = self.add_action("Anggota", "anggota", "Data Anggota", True, self.on_anggota)
        self._kategori_action = self.add_action("Kategori", "kategori", "Data Kategori", True, self.on_kategori)
        self._peminjaman_action = self.add_action("Peminjaman", "peminjaman", "Data Peminjaman", True, self.on_peminjaman)
        self._zoom_action = self.add_action("Search", "zoom", "Search", True, self.on_zoom)
        self._about_action = self.add_action("About", "about", "About QupyRibbon", True, self.on_about)
        self._users_action = self.add_action("Users", "users", "Users for this software", True, self.on_users)

        # Ribbon

        self._ribbon = RibbonWidget(self)
        self.addToolBar(self._ribbon)
        self.init_ribbon()

    def add_action(self, caption, icon_name, status_tip, icon_visible, connection, shortcut=None):
        action = QAction(get_icon(icon_name), caption, self)
        action.setStatusTip(status_tip)
        action.triggered.connect(connection)
        action.setIconVisibleInMenu(icon_visible)
        if shortcut is not None:
            action.setShortcuts(shortcut)
        self.addAction(action)
        return action

    def init_ribbon(self):
        home_tab = self._ribbon.add_ribbon_tab("Home")
        file_pane = home_tab.add_ribbon_pane("File")
        file_pane.add_ribbon_widget(RibbonButton(self, self._buku_action, True))
        file_pane.add_ribbon_widget(RibbonButton(self, self._anggota_action, True))

        edit_panel = home_tab.add_ribbon_pane("Edit")
        edit_panel.add_ribbon_widget(RibbonButton(self, self._kategori_action, True))
        edit_panel.add_ribbon_widget(RibbonButton(self, self._peminjaman_action, True))
        

        view_panel = home_tab.add_ribbon_pane("View")
        view_panel.add_ribbon_widget(RibbonButton(self, self._zoom_action, True))
        home_tab.add_spacer()

        about_tab = self._ribbon.add_ribbon_tab("About")
        info_panel = about_tab.add_ribbon_pane("Info")
        info_panel.add_ribbon_widget(RibbonButton(self, self._about_action, True))
        info_panel.add_ribbon_widget(RibbonButton(self, self._users_action, True))

       # -------------      Ribbon Button Functions      -----------------

    def closeEvent(self, close_event):
        pass

    def on_buku(self):
        buku_on(self)

    def on_save_to_excel(self):
        pass

    def on_anggota(self):
        anggota_on(self)   

    def on_kategori(self):
        kategori_on(self)

    def on_peminjaman(self):
        peminjaman_on(self)

    def on_zoom(self):
        pass

    def on_users(self):
        users_on(self)

    def on_about(self):
        text = "CRUD Perpustakaan PostgreSQL"
        text += "Copyright © 2022 Aziz Maulana"
        QMessageBox().about(self, "About App", text)
