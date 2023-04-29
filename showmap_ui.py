# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/gianschneider/temp_Macintosh_HD_gianschneider/uebungen programmieren/showmap.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(310, 130, 271, 114))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.laenge = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.laenge.setFont(font)
        self.laenge.setObjectName("laenge")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.laenge)
        self.breite = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.breite.setFont(font)
        self.breite.setObjectName("breite")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.breite)
        self.breiteLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.breiteLineEdit.setObjectName("breiteLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.breiteLineEdit)
        self.show_on_map = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.show_on_map.setFont(font)
        self.show_on_map.setObjectName("show_on_map")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.show_on_map)
        self.lNgeLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lNgeLineEdit.setObjectName("lNgeLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lNgeLineEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 33))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.laenge.setText(_translate("MainWindow", "Länge"))
        self.breite.setText(_translate("MainWindow", "Breite:"))
        self.show_on_map.setText(_translate("MainWindow", "auf Karte zeigen..."))

