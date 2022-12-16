from PyQt5 import QtWidgets, QtCore, QtGui

class Frog:
    def __init__(self,centralwidget):
        self.frog = QtWidgets.QPushButton(centralwidget)
        self.frog.setGeometry(QtCore.QRect(20, 270, 81, 61))
        self.frog.setAutoFillBackground(False)
        self.frog.setStyleSheet("background: transparent")
        self.frog.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../content/frog.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frog.setIcon(icon)
        self.frog.setIconSize(QtCore.QSize(80, 80))
        self.frog.setObjectName("frog")
        self.frog_state = QtWidgets.QLabel(centralwidget)
        self.frog_state.setText("Frog is sleeping")
        self.frog_state.setGeometry(QtCore.QRect(20, 240, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(True)
        self.frog_state.setFont(font)
        self.frog_state.setObjectName("frog_state")