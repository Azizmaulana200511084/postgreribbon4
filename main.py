import sys
from PyQt5.QtWidgets import *
from forms.MainWindow import MainWindow

__author__ = 'umc'

def main():
    a = QApplication(sys.argv)
    a.setQuitOnLastWindowClosed(True)
    main_window = MainWindow()
    main_window.show()
    sys.exit(a.exec_())

main()