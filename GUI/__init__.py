from PyQt5.QtWidgets import *

__author__ = 'umc'


def gui_scale():
    screen = QApplication.screens()[0];
    dpi = screen.logicalDotsPerInch()
    return dpi / 120
