from PyQt5 import QtWidgets, QtCore, QtGui
import time
from PyQt5.QtCore import QTimer, QEventLoop
count = 0

class Sun:
    def __init__(self, world_obj):
        super(Sun, self).__init__()
        self.world_obj = world_obj
        self.sun = QtWidgets.QPushButton(world_obj.centralwidget)
        self.sun.setGeometry(QtCore.QRect(10, 0, 102, 102))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.sun.setFont(font)
        self.sun.setStyleSheet(" background-color: grey;\n"
                               " border-style: solid;\n"
                               " border-width:1px;\n"
                               " border-radius:50px;\n"
                               "")
        self.sun.setText("")
        self.sun.setObjectName("sun")
        self.sun_state = QtWidgets.QLabel(world_obj.centralwidget)
        self.sun_state.setText("Sun is not shinning")
        self.sun_state.setGeometry(QtCore.QRect(120, 40, 130, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(True)
        self.sun_state.setFont(font)
        self.sun_state.setObjectName("sun_state")
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.sun_shine)
        self.timer.start(3000)
        self.timer2 = QtCore.QTimer()
        self.timer2.timeout.connect(self.sun_shine)
        self.timer2.start(3000)


    def sun_shine(self):
        global count
        count += 1
        if count > 5:
            self.world_obj.mainWindow.setStyleSheet("background:white")
            self.sun.setStyleSheet(" background-color: yellow;\n"
                                   " border-style: solid;\n"
                                   " border-width:1px;\n"
                                   " border-radius:50px;\n"
                                   "")
            self.sun_state.setText("Sun is shinning")
            self.world_obj.tree_obj.tree_state.setText("Tree produces oxygen")
            self.world_obj.frog_obj.frog_state.setText("Frog is eating")
            self.world_obj.frog_obj.frog.move(20 +2*count, 280)
            self.world_obj.frog_obj.frog_state.move(20 + 2*count, 240)
            if self.world_obj.oxygen_obj.oxygen < 25:
                self.world_obj.oxygen_obj.oxygen = self.world_obj.oxygen_obj.oxygen + 1
                self.world_obj.oxygen_obj.oxygen_state.setText(f"Oxygen : {self.world_obj.oxygen_obj.oxygen} %)")
            if len(self.world_obj.grass_obj.grass_list) != 1:
                self.world_obj.grass_obj.grass_list.pop().hide()
            else:
                self.world_obj.mainWindow.setStyleSheet("background:grey")
                self.sun.setStyleSheet(" background-color: grey;\n"
                                       " border-style: solid;\n"
                                       " border-width:1px;\n"
                                       " border-radius:50px;\n"
                                       "")
                self.sun_state.setText("Sun is not shinning")
                self.world_obj.frog_obj.frog_state.setGeometry(QtCore.QRect(20, 240, 111, 16))
                self.world_obj.frog_obj.frog.setGeometry(QtCore.QRect(20, 270, 81, 61))
                self.world_obj.oxygen_obj.oxygen_state.setText(f"Oxygen : {self.world_obj.oxygen_obj.oxygen} %)")
                self.world_obj.tree_obj.tree_state.setText("Tree does not\nproduce oxygen")
                self.world_obj.frog_obj.frog_state.setText("Frog is sleeping")


            self.timer.stop()
            return
        else:
            self.world_obj.oxygen_obj.oxygen = 21 - count
            self.world_obj.oxygen_obj.oxygen_state.setText(f"Oxygen : {self.world_obj.oxygen_obj.oxygen} %)")
            for i in self.world_obj.grass_obj.grass_list:
                i.show()

