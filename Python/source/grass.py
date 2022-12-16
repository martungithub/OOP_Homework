from PyQt5 import QtWidgets, QtCore


class Grass:
    def __init__(self, centralwidget):
        self.green = QtWidgets.QFrame(centralwidget)
        self.green.setGeometry(QtCore.QRect(0, 360, 631, 20))
        self.green.setStyleSheet("background: rgb(64, 204, 16)")
        self.green.setLineWidth(0)
        self.green.setFrameShape(QtWidgets.QFrame.HLine)
        self.green.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.green.setObjectName("green")
        self.horizontalLayoutWidget = QtWidgets.QWidget(centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 329, 631, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.grass_list = [] * 8
        for i in range(8):
            i = QtWidgets.QFrame(self.horizontalLayoutWidget)
            i.setStyleSheet("background: rgb(64, 204, 16)")
            i.setLineWidth(0)
            i.setFrameShape(QtWidgets.QFrame.VLine)
            i.setFrameShadow(QtWidgets.QFrame.Sunken)
            i.setObjectName("grass")
            self.horizontalLayout.addWidget(i)
            i.hide()
            self.grass_list.append(i)
