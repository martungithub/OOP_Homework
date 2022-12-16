import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer

import source.sun
import source.tree
import source.frog
import source.grass
import source.oxygen

class World(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("background: grey")
        MainWindow.setFixedSize(600, 380)
        self.mainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.grass_obj =source.grass.Grass(self.centralwidget)
        self.sun_obj = source.sun.Sun(self)
        self.frog_obj =source.frog.Frog(self.centralwidget)
        self.tree_obj = source.tree.Tree(self.centralwidget)
        self.oxygen_obj = source.oxygen.Oxygen(self.centralwidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "World"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QMainWindow()
    ui = World()
    ui.setupUi(Frame)
    Frame.show()
    timer = QTimer()
    sys.exit(app.exec_())
