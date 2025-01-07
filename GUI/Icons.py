from PyQt5.QtGui import *

__author__ = 'umc'

icons_instance = None


def get_icon(name):
    global icons_instance
    if not icons_instance:
        icons_instance = Icons()
    return icons_instance.icon(name)


class Icons(object):
    def __init__(self):
        self._icons = {}
        self.make_icon("folder", "icons/folder.png")
        self.make_icon("open", "icons/folder.png")
        self.make_icon("save", "icons/save.png")
        self.make_icon("icon", "icons/icon.png")
        self.make_icon("exit", "icons/exit.png")
        self.make_icon("paste", "icons/paste.png")
        self.make_icon("zoom", "icons/zoom.png")
        self.make_icon("copy", "icons/copy.png")
        self.make_icon("about", "icons/about.png")
        self.make_icon("license", "icons/license.png")
        self.make_icon("default", "icons/folder.png")
        self.make_icon("mahasiswa", "icons/mahasiswa.png")
        self.make_icon("matakuliah", "icons/matakuliah.png")
        self.make_icon("dosen", "icons/dosen.png")
        self.make_icon("alumni", "icons/alumni.png")
        self.make_icon("buku", "icons/buku.png")
        self.make_icon("anggota", "icons/anggota.png")
        self.make_icon("kategori", "icons/kategori.png")
        self.make_icon("peminjaman", "icons/peminjaman.png")
        self.make_icon("users", "icons/users.png")

    def make_icon(self, name, path):
        icon = QIcon()
        icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)
        self._icons[name] = icon

    def icon(self, name):
        icon = self._icons["default"]
        try:
            icon = self._icons[name]
        except KeyError:
            print("icon " + name + " not found")
        return icon
