from PyQt5 import QtWidgets, QtCore, QtGui

class Oxygen:
    def __init__(self,centralwidget):
        self.oxygen_state = QtWidgets.QLabel(centralwidget)
        self.oxygen = 21
        self.oxygen_state.setText(f"Oxygen : {self.oxygen} %)")
        self.oxygen_state.setGeometry(QtCore.QRect(430, 15, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(True)
        self.oxygen_state.setFont(font)
        self.oxygen_state.setStyleSheet("background:rgb(64, 204, 16)")
        self.oxygen_state.setObjectName("oxygen_state")