from PyQt6 import QtCore, QtGui, QtWidgets

"""
Labels:
    - hello_user_label
    - greeting_label
    - item_label
    - quantity_label
    - account_contents_label
    - item_history_label
    - transaction_label
    - transaction_quantity_label
    - logout_question_label

Text browsers:
    - account_contents_textBrowser
    - alert_textBrowser
    - transaction_history_textBrowser

Line edits:
    - item_lineEdit
    - quantity_lineEdit

Radio buttons:
    - deposit_radioButton
    - withdraw_radioButton
    - transHist_radioButton
    - clearStorage_radioButton

Push buttons:
    - log_out_pushButton
    - confirm_pushButton
    - confirm_logout_pushButton
    - cancel_logout_pushButton
"""


class Ui_UserStorageWindow(object):
    def setupUi(self, UserStorageWindow):
        UserStorageWindow.setObjectName("UserStorageWindow")
        UserStorageWindow.resize(400, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UserStorageWindow.sizePolicy().hasHeightForWidth())
        UserStorageWindow.setSizePolicy(sizePolicy)
        UserStorageWindow.setMinimumSize(QtCore.QSize(400, 500))
        UserStorageWindow.setMaximumSize(QtCore.QSize(400, 500))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        UserStorageWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=UserStorageWindow)
        self.centralwidget.setObjectName("centralwidget")

        # hello_user_label
        self.hello_user_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.hello_user_label.setGeometry(QtCore.QRect(150, 0, 100, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hello_user_label.sizePolicy().hasHeightForWidth())
        self.hello_user_label.setSizePolicy(sizePolicy)
        self.hello_user_label.setMinimumSize(QtCore.QSize(100, 20))
        self.hello_user_label.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.hello_user_label.setFont(font)
        self.hello_user_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hello_user_label.setObjectName("hello_user_label")

        # greeting_label
        self.greeting_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.greeting_label.setGeometry(QtCore.QRect(90, 25, 220, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.greeting_label.sizePolicy().hasHeightForWidth())
        self.greeting_label.setSizePolicy(sizePolicy)
        self.greeting_label.setMinimumSize(QtCore.QSize(220, 20))
        self.greeting_label.setMaximumSize(QtCore.QSize(220, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.greeting_label.setFont(font)
        self.greeting_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.greeting_label.setObjectName("greeting_label")

        # account_contents_textBrowser
        self.account_contents_textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.account_contents_textBrowser.setGeometry(QtCore.QRect(100, 130, 200, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account_contents_textBrowser.sizePolicy().hasHeightForWidth())
        self.account_contents_textBrowser.setSizePolicy(sizePolicy)
        self.account_contents_textBrowser.setMinimumSize(QtCore.QSize(200, 100))
        self.account_contents_textBrowser.setMaximumSize(QtCore.QSize(200, 100))
        self.account_contents_textBrowser.setObjectName("account_contents_textBrowser")

        # item_label
        self.item_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.item_label.setEnabled(False)
        self.item_label.setGeometry(QtCore.QRect(85, 230, 30, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_label.sizePolicy().hasHeightForWidth())
        self.item_label.setSizePolicy(sizePolicy)
        self.item_label.setMinimumSize(QtCore.QSize(30, 20))
        self.item_label.setMaximumSize(QtCore.QSize(30, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.item_label.setFont(font)
        self.item_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.item_label.setObjectName("item_label")

        # quantity_label
        self.quantity_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.quantity_label.setEnabled(False)
        self.quantity_label.setGeometry(QtCore.QRect(275, 230, 50, 20))
        self.quantity_label.setMinimumSize(QtCore.QSize(50, 20))
        self.quantity_label.setMaximumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.quantity_label.setFont(font)
        self.quantity_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.quantity_label.setObjectName("quantity_label")

        # account_contents_label
        self.account_contents_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.account_contents_label.setEnabled(True)
        self.account_contents_label.setGeometry(QtCore.QRect(125, 110, 140, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account_contents_label.sizePolicy().hasHeightForWidth())
        self.account_contents_label.setSizePolicy(sizePolicy)
        self.account_contents_label.setMinimumSize(QtCore.QSize(140, 20))
        self.account_contents_label.setMaximumSize(QtCore.QSize(140, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.account_contents_label.setFont(font)
        self.account_contents_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.account_contents_label.setObjectName("account_contents_label")

        # log_out_pushButton
        self.log_out_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.log_out_pushButton.setGeometry(QtCore.QRect(0, 0, 50, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log_out_pushButton.sizePolicy().hasHeightForWidth())
        self.log_out_pushButton.setSizePolicy(sizePolicy)
        self.log_out_pushButton.setMinimumSize(QtCore.QSize(50, 20))
        self.log_out_pushButton.setMaximumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.log_out_pushButton.setFont(font)
        self.log_out_pushButton.setObjectName("log_out_pushButton")

        # item_lineEdit
        self.item_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.item_lineEdit.setGeometry(QtCore.QRect(50, 250, 100, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_lineEdit.sizePolicy().hasHeightForWidth())
        self.item_lineEdit.setSizePolicy(sizePolicy)
        self.item_lineEdit.setMinimumSize(QtCore.QSize(100, 20))
        self.item_lineEdit.setMaximumSize(QtCore.QSize(100, 20))
        self.item_lineEdit.setText("")
        self.item_lineEdit.setMaxLength(20)
        self.item_lineEdit.setObjectName("item_lineEdit")

        # quantity_lineEdit
        self.quantity_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.quantity_lineEdit.setGeometry(QtCore.QRect(250, 250, 100, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quantity_lineEdit.sizePolicy().hasHeightForWidth())
        self.quantity_lineEdit.setSizePolicy(sizePolicy)
        self.quantity_lineEdit.setMinimumSize(QtCore.QSize(100, 20))
        self.quantity_lineEdit.setMaximumSize(QtCore.QSize(100, 20))
        self.quantity_lineEdit.setMaxLength(2)
        self.quantity_lineEdit.setObjectName("quantity_lineEdit")

        # confirm_pushButton
        self.confirm_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.confirm_pushButton.setEnabled(True)
        self.confirm_pushButton.setGeometry(QtCore.QRect(175, 260, 50, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirm_pushButton.sizePolicy().hasHeightForWidth())
        self.confirm_pushButton.setSizePolicy(sizePolicy)
        self.confirm_pushButton.setMinimumSize(QtCore.QSize(50, 20))
        self.confirm_pushButton.setMaximumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.confirm_pushButton.setFont(font)
        self.confirm_pushButton.setObjectName("confirm_pushButton")

        # alert_textBrowser
        self.alert_textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.alert_textBrowser.setGeometry(QtCore.QRect(50, 280, 300, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alert_textBrowser.sizePolicy().hasHeightForWidth())
        self.alert_textBrowser.setSizePolicy(sizePolicy)
        self.alert_textBrowser.setMinimumSize(QtCore.QSize(300, 50))
        self.alert_textBrowser.setMaximumSize(QtCore.QSize(300, 50))
        self.alert_textBrowser.setObjectName("alert_textBrowser")

        # transaction_history_textBrowser
        self.transaction_history_textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.transaction_history_textBrowser.setGeometry(QtCore.QRect(60, 350, 280, 100))
        self.transaction_history_textBrowser.setMinimumSize(QtCore.QSize(280, 100))
        self.transaction_history_textBrowser.setMaximumSize(QtCore.QSize(280, 100))
        self.transaction_history_textBrowser.setObjectName("transaction_history_textBrowser")

        # item_history_label
        self.item_history_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.item_history_label.setEnabled(True)
        self.item_history_label.setGeometry(QtCore.QRect(160, 330, 30, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_history_label.sizePolicy().hasHeightForWidth())
        self.item_history_label.setSizePolicy(sizePolicy)
        self.item_history_label.setMinimumSize(QtCore.QSize(30, 20))
        self.item_history_label.setMaximumSize(QtCore.QSize(30, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.item_history_label.setFont(font)
        self.item_history_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.item_history_label.setObjectName("item_history_label")

        # transaction_label
        self.transaction_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.transaction_label.setEnabled(True)
        self.transaction_label.setGeometry(QtCore.QRect(60, 330, 75, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transaction_label.sizePolicy().hasHeightForWidth())
        self.transaction_label.setSizePolicy(sizePolicy)
        self.transaction_label.setMinimumSize(QtCore.QSize(75, 20))
        self.transaction_label.setMaximumSize(QtCore.QSize(75, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.transaction_label.setFont(font)
        self.transaction_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.transaction_label.setObjectName("transaction_label")

        # transaction_quantity_label
        self.transaction_quantity_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.transaction_quantity_label.setEnabled(True)
        self.transaction_quantity_label.setGeometry(QtCore.QRect(290, 330, 50, 20))
        self.transaction_quantity_label.setMinimumSize(QtCore.QSize(50, 20))
        self.transaction_quantity_label.setMaximumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.transaction_quantity_label.setFont(font)
        self.transaction_quantity_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.transaction_quantity_label.setObjectName("transaction_quantity_label")

        # confirm_logout_pushButton
        self.confirm_logout_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.confirm_logout_pushButton.setGeometry(QtCore.QRect(0, 15, 50, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirm_logout_pushButton.sizePolicy().hasHeightForWidth())
        self.confirm_logout_pushButton.setSizePolicy(sizePolicy)
        self.confirm_logout_pushButton.setMinimumSize(QtCore.QSize(50, 20))
        self.confirm_logout_pushButton.setMaximumSize(QtCore.QSize(50, 20))
        self.confirm_logout_pushButton.setObjectName("confirm_logout_pushButton")

        # cancel_logout_pushButton
        self.cancel_logout_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cancel_logout_pushButton.setGeometry(QtCore.QRect(0, 40, 40, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_logout_pushButton.sizePolicy().hasHeightForWidth())
        self.cancel_logout_pushButton.setSizePolicy(sizePolicy)
        self.cancel_logout_pushButton.setMinimumSize(QtCore.QSize(40, 20))
        self.cancel_logout_pushButton.setMaximumSize(QtCore.QSize(40, 20))
        self.cancel_logout_pushButton.setObjectName("cancel_logout_pushButton")

        # logout_question_label
        self.logout_question_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.logout_question_label.setEnabled(False)
        self.logout_question_label.setGeometry(QtCore.QRect(0, 0, 75, 15))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logout_question_label.sizePolicy().hasHeightForWidth())
        self.logout_question_label.setSizePolicy(sizePolicy)
        self.logout_question_label.setMinimumSize(QtCore.QSize(75, 15))
        self.logout_question_label.setMaximumSize(QtCore.QSize(75, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.logout_question_label.setFont(font)
        self.logout_question_label.setObjectName("logout_question_label")

        # deposit_radioButton
        self.deposit_radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.deposit_radioButton.setGeometry(QtCore.QRect(90, 50, 100, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deposit_radioButton.sizePolicy().hasHeightForWidth())
        self.deposit_radioButton.setSizePolicy(sizePolicy)
        self.deposit_radioButton.setMinimumSize(QtCore.QSize(100, 20))
        self.deposit_radioButton.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deposit_radioButton.setFont(font)
        self.deposit_radioButton.setObjectName("deposit_radioButton")

        # withdraw_radioButton
        self.withdraw_radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.withdraw_radioButton.setGeometry(QtCore.QRect(200, 50, 130, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.withdraw_radioButton.sizePolicy().hasHeightForWidth())
        self.withdraw_radioButton.setSizePolicy(sizePolicy)
        self.withdraw_radioButton.setMinimumSize(QtCore.QSize(130, 20))
        self.withdraw_radioButton.setMaximumSize(QtCore.QSize(130, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.withdraw_radioButton.setFont(font)
        self.withdraw_radioButton.setObjectName("withdraw_radioButton")

        # transHist_radioButton
        self.transHist_radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.transHist_radioButton.setGeometry(QtCore.QRect(90, 80, 150, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transHist_radioButton.sizePolicy().hasHeightForWidth())
        self.transHist_radioButton.setSizePolicy(sizePolicy)
        self.transHist_radioButton.setMinimumSize(QtCore.QSize(150, 20))
        self.transHist_radioButton.setMaximumSize(QtCore.QSize(150, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.transHist_radioButton.setFont(font)
        self.transHist_radioButton.setObjectName("transHist_radioButton")

        # clearStorage_radioButton
        self.clearStorage_radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.clearStorage_radioButton.setGeometry(QtCore.QRect(240, 80, 120, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearStorage_radioButton.sizePolicy().hasHeightForWidth())
        self.clearStorage_radioButton.setSizePolicy(sizePolicy)
        self.clearStorage_radioButton.setMinimumSize(QtCore.QSize(120, 20))
        self.clearStorage_radioButton.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clearStorage_radioButton.setFont(font)
        self.clearStorage_radioButton.setObjectName("clearStorage_radioButton")

        UserStorageWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=UserStorageWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        UserStorageWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=UserStorageWindow)
        self.statusbar.setObjectName("statusbar")
        UserStorageWindow.setStatusBar(self.statusbar)

        self.retranslateUi(UserStorageWindow)
        QtCore.QMetaObject.connectSlotsByName(UserStorageWindow)

    def retranslateUi(self, UserStorageWindow):
        _translate = QtCore.QCoreApplication.translate
        UserStorageWindow.setWindowTitle(_translate("UserStorageWindow", "Your storage"))

        self.hello_user_label.setText(_translate("UserStorageWindow", ""))

        self.greeting_label.setText(_translate("UserStorageWindow", "What would you like to do today?"))

        self.item_label.setText(_translate("UserStorageWindow", "Item"))

        self.quantity_label.setText(_translate("UserStorageWindow", "Quantity"))

        self.account_contents_label.setText(_translate("UserStorageWindow", "Currently in your account"))

        self.log_out_pushButton.setText(_translate("UserStorageWindow", "Log out"))

        self.confirm_pushButton.setText(_translate("UserStorageWindow", "Confirm"))

        self.alert_textBrowser.setHtml(_translate("UserStorageWindow","<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                  "p, li { white-space: pre-wrap; }\n"
                                                  "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
                                                  "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#9c1c1c;\"></span></p></body></html>"))

        self.transaction_history_textBrowser.setHtml(_translate("UserStorageWindow","<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                "p, li { white-space: pre-wrap; }\n"
                                                                "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
                                                                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"></span></p>\n"
                                                                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"></span></p>\n"
                                                                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"></span></p></body></html>"))

        self.item_history_label.setText(_translate("UserStorageWindow", "Item"))

        self.transaction_label.setText(_translate("UserStorageWindow", "Transaction"))

        self.transaction_quantity_label.setText(_translate("UserStorageWindow", "Quantity"))

        self.confirm_logout_pushButton.setText(_translate("UserStorageWindow", "Confirm"))

        self.cancel_logout_pushButton.setText(_translate("UserStorageWindow", "Cancel"))

        self.logout_question_label.setText(_translate("UserStorageWindow", "Are you sure?"))

        self.deposit_radioButton.setText(_translate("UserStorageWindow", "Make deposit"))
        self.withdraw_radioButton.setText(_translate("UserStorageWindow", "Make a withdrawal"))
        self.transHist_radioButton.setText(_translate("UserStorageWindow", "View transaction history"))
        self.clearStorage_radioButton.setText(_translate("UserStorageWindow", "Clear my storage"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    UserStorageWindow = QtWidgets.QMainWindow()
    ui = Ui_UserStorageWindow()
    ui.setupUi(UserStorageWindow)
    UserStorageWindow.show()
    sys.exit(app.exec())
