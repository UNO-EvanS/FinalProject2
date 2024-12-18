"""
This GUI acts as the starting page for when the application is first run.
It prompts the user to either login or create an account. When they click on one of them,
they will be taken to the appropriate page for what they wish to do.
This screen will also appear when a user logs out of their account.
"""

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt

class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        # StartWindow
        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(300, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StartWindow.sizePolicy().hasHeightForWidth())
        StartWindow.setSizePolicy(sizePolicy)
        StartWindow.setMinimumSize(QtCore.QSize(300, 150))
        StartWindow.setMaximumSize(QtCore.QSize(300, 150))
        self.centralwidget = QtWidgets.QWidget(parent=StartWindow)
        self.centralwidget.setObjectName("centralwidget")

        # start_welcome_label
        self.start_welcome_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.start_welcome_label.setGeometry(QtCore.QRect(85, 10, 130, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_welcome_label.sizePolicy().hasHeightForWidth())
        self.start_welcome_label.setSizePolicy(sizePolicy)
        self.start_welcome_label.setMinimumSize(QtCore.QSize(130, 35))
        self.start_welcome_label.setMaximumSize(QtCore.QSize(130, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.start_welcome_label.setFont(font)
        self.start_welcome_label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.start_welcome_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.start_welcome_label.setObjectName("start_welcome_label")

        # start_textBrowser
        self.start_textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.start_textBrowser.setGeometry(QtCore.QRect(75, 50, 150, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_textBrowser.sizePolicy().hasHeightForWidth())
        self.start_textBrowser.setSizePolicy(sizePolicy)
        self.start_textBrowser.setMinimumSize(QtCore.QSize(150, 25))
        self.start_textBrowser.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.start_textBrowser.setFont(font)
        self.start_textBrowser.setObjectName("start_textBrowser")

        # start_login_pushButton
        self.start_login_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.start_login_pushButton.setGeometry(QtCore.QRect(185, 80, 40, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_login_pushButton.sizePolicy().hasHeightForWidth())
        self.start_login_pushButton.setSizePolicy(sizePolicy)
        self.start_login_pushButton.setMinimumSize(QtCore.QSize(40, 25))
        self.start_login_pushButton.setMaximumSize(QtCore.QSize(40, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.start_login_pushButton.setFont(font)
        self.start_login_pushButton.setObjectName("start_login_pushButton")

        # start_create_account_pushButton
        self.start_create_account_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.start_create_account_pushButton.setGeometry(QtCore.QRect(75, 80, 100, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_create_account_pushButton.sizePolicy().hasHeightForWidth())
        self.start_create_account_pushButton.setSizePolicy(sizePolicy)
        self.start_create_account_pushButton.setMinimumSize(QtCore.QSize(100, 25))
        self.start_create_account_pushButton.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.start_create_account_pushButton.setFont(font)
        self.start_create_account_pushButton.setObjectName("start_create_account_pushButton")

        StartWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=StartWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 22))
        self.menubar.setObjectName("menubar")
        StartWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=StartWindow)
        self.statusbar.setObjectName("statusbar")
        StartWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StartWindow)
        QtCore.QMetaObject.connectSlotsByName(StartWindow)

    def retranslateUi(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "Start"))
        self.start_welcome_label.setText(_translate("StartWindow", "Welcome!"))
        self.start_textBrowser.setHtml(_translate("StartWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">What would you like to do?</p></body></html>"))
        self.start_login_pushButton.setText(_translate("StartWindow", "Log in"))
        self.start_create_account_pushButton.setText(_translate("StartWindow", "Create an account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartWindow = QtWidgets.QMainWindow()
    ui = Ui_StartWindow()
    ui.setupUi(StartWindow)
    StartWindow.show()
    sys.exit(app.exec())
