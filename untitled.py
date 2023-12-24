# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import sys

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(835, 532)
        self.commandLinkButton = QCommandLinkButton(Form)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(QRect(700, 10, 101, 31))
        self.commandLinkButton.setStyleSheet(u"\n""font: 9pt \"\u534e\u6587\u7425\u73c0\";")
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(80, 60, 761, 471))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 759, 469))
        self.verticalScrollBar = QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(730, 0, 20, 471))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 131, 16))
        self.label.setStyleSheet(u"\n""font: 9pt \"\u9ed1\u4f53\";")
        self.graphicsView = QGraphicsView(Form)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(20, 490, 41, 41))
        self.listWidget = QListWidget(Form)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 60, 81, 431))
        self.listWidget.setMinimumSize(QSize(81, 431))
        self.listWidget.setStyleSheet(u"font: 9pt \"\u9ed1\u4f53\";")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.commandLinkButton.setText(QCoreApplication.translate("Form", u"\ud83d\udc0e", None))
        self.label.setText(QCoreApplication.translate("Form", u"\ud83d\udc0e\u5a18\u6280\u80fd\u8bc4\u4f30", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"\u8bf4\u660e", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"\u6e05\u9664\u7f13\u5b58", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainWindow()#注意窗口类型
    Window.show()
    app.exec_()

