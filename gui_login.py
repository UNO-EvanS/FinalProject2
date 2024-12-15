"""
This is the login page that can be accessed from the startup menu or via the 'login' button in the create account menu.

- The user enters their username and password.
- If the username does not exist, an alert is shown below the username field.
- If the password is incorrect, an alert is shown beneath the password field.
- If either field is left blank, an alert is shown.
- The 'Clear' buttons clear the respective fields.

Once the correct username and password are entered, the user is prompted with the two-factor authentication question they set up.

The user can also go to the 'create an account' menu from this page.
"""
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        #LoginWindow
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(300, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        LoginWindow.setMinimumSize(QtCore.QSize(300, 400))
        LoginWindow.setMaximumSize(QtCore.QSize(300, 400))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        LoginWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=LoginWindow)
        self.centralwidget.setObjectName("centralwidget")

        # login_label
        self.login_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.login_label.setGeometry(QtCore.QRect(100, 10, 100, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_label.sizePolicy().hasHeightForWidth())
        self.login_label.setSizePolicy(sizePolicy)
        self.login_label.setMinimumSize(QtCore.QSize(100, 35))
        self.login_label.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.login_label.setFont(font)
        self.login_label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.login_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.login_label.setObjectName("login_label")

        # username_clear_pushButton
        self.username_clear_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.username_clear_pushButton.setGeometry(QtCore.QRect(240, 50, 40, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username_clear_pushButton.sizePolicy().hasHeightForWidth())
        self.username_clear_pushButton.setSizePolicy(sizePolicy)
        self.username_clear_pushButton.setMinimumSize(QtCore.QSize(40, 20))
        self.username_clear_pushButton.setMaximumSize(QtCore.QSize(40, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.username_clear_pushButton.setFont(font)
        self.username_clear_pushButton.setObjectName("username_clear_pushButton")

        # username_lineEdit
        self.username_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.username_lineEdit.setGeometry(QtCore.QRect(40, 50, 200, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username_lineEdit.sizePolicy().hasHeightForWidth())
        self.username_lineEdit.setSizePolicy(sizePolicy)
        self.username_lineEdit.setMinimumSize(QtCore.QSize(200, 20))
        self.username_lineEdit.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.username_lineEdit.setFont(font)
        self.username_lineEdit.setMaxLength(20)
        self.username_lineEdit.setObjectName("username_lineEdit")

        # password_lineEdit
        self.password_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.password_lineEdit.setGeometry(QtCore.QRect(40, 100, 200, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_lineEdit.sizePolicy().hasHeightForWidth())
        self.password_lineEdit.setSizePolicy(sizePolicy)
        self.password_lineEdit.setMinimumSize(QtCore.QSize(200, 20))
        self.password_lineEdit.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setMaxLength(20)
        self.password_lineEdit.setObjectName("password_lineEdit")

        # password_clear_pushButton
        self.password_clear_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.password_clear_pushButton.setGeometry(QtCore.QRect(240, 100, 40, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_clear_pushButton.sizePolicy().hasHeightForWidth())
        self.password_clear_pushButton.setSizePolicy(sizePolicy)
        self.password_clear_pushButton.setMinimumSize(QtCore.QSize(40, 20))
        self.password_clear_pushButton.setMaximumSize(QtCore.QSize(40, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.password_clear_pushButton.setFont(font)
        self.password_clear_pushButton.setObjectName("password_clear_pushButton")

        # username_alert_textBrowser
        self.username_alert_textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.username_alert_textBrowser.setEnabled(False)
        self.username_alert_textBrowser.setGeometry(QtCore.QRect(40, 75, 240, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username_alert_textBrowser.sizePolicy().hasHeightForWidth())
        self.username_alert_textBrowser.setSizePolicy(sizePolicy)
        self.username_alert_textBrowser.setMinimumSize(QtCore.QSize(240, 20))
        self.username_alert_textBrowser.setMaximumSize(QtCore.QSize(240, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.username_alert_textBrowser.setFont(font)
        self.username_alert_textBrowser.setObjectName("username_alert_textBrowser")

        # create_account_pushButton
        self.create_account_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.create_account_pushButton.setEnabled(True)
        self.create_account_pushButton.setGeometry(QtCore.QRect(100, 340, 100, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_account_pushButton.sizePolicy().hasHeightForWidth())
        self.create_account_pushButton.setSizePolicy(sizePolicy)
        self.create_account_pushButton.setMinimumSize(QtCore.QSize(100, 25))
        self.create_account_pushButton.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.create_account_pushButton.setFont(font)
        self.create_account_pushButton.setObjectName("create_account_pushButton")

        # continue_pushButton
        self.continue_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.continue_pushButton.setGeometry(QtCore.QRect(120, 150, 60, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.continue_pushButton.sizePolicy().hasHeightForWidth())
        self.continue_pushButton.setSizePolicy(sizePolicy)
        self.continue_pushButton.setMinimumSize(QtCore.QSize(60, 25))
        self.continue_pushButton.setMaximumSize(QtCore.QSize(60, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.continue_pushButton.setFont(font)
        self.continue_pushButton.setObjectName("continue_pushButton")

        # password_alert_textBrowser
        self.password_alert_textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.password_alert_textBrowser.setEnabled(False)
        self.password_alert_textBrowser.setGeometry(QtCore.QRect(40, 125, 240, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_alert_textBrowser.sizePolicy().hasHeightForWidth())
        self.password_alert_textBrowser.setSizePolicy(sizePolicy)
        self.password_alert_textBrowser.setMinimumSize(QtCore.QSize(240, 20))
        self.password_alert_textBrowser.setMaximumSize(QtCore.QSize(240, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.password_alert_textBrowser.setFont(font)
        self.password_alert_textBrowser.setObjectName("password_alert_textBrowser")

        # create_account_textBrowser
        self.create_account_textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.create_account_textBrowser.setEnabled(True)
        self.create_account_textBrowser.setGeometry(QtCore.QRect(50, 310, 200, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_account_textBrowser.sizePolicy().hasHeightForWidth())
        self.create_account_textBrowser.setSizePolicy(sizePolicy)
        self.create_account_textBrowser.setMinimumSize(QtCore.QSize(200, 25))
        self.create_account_textBrowser.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.create_account_textBrowser.setFont(font)
        self.create_account_textBrowser.setObjectName("create_account_textBrowser")

        # loginTFA_label
        self.loginTFA_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.loginTFA_label.setEnabled(False)
        self.loginTFA_label.setGeometry(QtCore.QRect(40, 180, 220, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginTFA_label.sizePolicy().hasHeightForWidth())
        self.loginTFA_label.setSizePolicy(sizePolicy)
        self.loginTFA_label.setMinimumSize(QtCore.QSize(220, 30))
        self.loginTFA_label.setMaximumSize(QtCore.QSize(220, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.loginTFA_label.setFont(font)
        self.loginTFA_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.loginTFA_label.setObjectName("loginTFA_label")

        # userChosen_question_textBrowser
        self.userChosen_question_textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.userChosen_question_textBrowser.setEnabled(False)
        self.userChosen_question_textBrowser.setGeometry(QtCore.QRect(50, 210, 200, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userChosen_question_textBrowser.sizePolicy().hasHeightForWidth())
        self.userChosen_question_textBrowser.setSizePolicy(sizePolicy)
        self.userChosen_question_textBrowser.setMinimumSize(QtCore.QSize(200, 25))
        self.userChosen_question_textBrowser.setMaximumSize(QtCore.QSize(200, 25))
        self.userChosen_question_textBrowser.setObjectName("userChosen_question_textBrowser")

        # TFA_lineEdit
        self.TFA_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.TFA_lineEdit.setEnabled(True)
        self.TFA_lineEdit.setGeometry(QtCore.QRect(50, 240, 150, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TFA_lineEdit.sizePolicy().hasHeightForWidth())
        self.TFA_lineEdit.setSizePolicy(sizePolicy)
        self.TFA_lineEdit.setMinimumSize(QtCore.QSize(150, 20))
        self.TFA_lineEdit.setMaximumSize(QtCore.QSize(150, 20))
        self.TFA_lineEdit.setText("")
        self.TFA_lineEdit.setMaxLength(20)
        self.TFA_lineEdit.setObjectName("TFA_lineEdit")

        # loginTFA_confirm_pushButton
        self.loginTFA_confirm_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.loginTFA_confirm_pushButton.setEnabled(True)
        self.loginTFA_confirm_pushButton.setGeometry(QtCore.QRect(200, 240, 50, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginTFA_confirm_pushButton.sizePolicy().hasHeightForWidth())
        self.loginTFA_confirm_pushButton.setSizePolicy(sizePolicy)
        self.loginTFA_confirm_pushButton.setMinimumSize(QtCore.QSize(50, 20))
        self.loginTFA_confirm_pushButton.setMaximumSize(QtCore.QSize(50, 20))
        self.loginTFA_confirm_pushButton.setObjectName("loginTFA_confirm_pushButton")

        # incorrect_answer_textBrowser
        self.incorrect_answer_textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.incorrect_answer_textBrowser.setEnabled(False)
        self.incorrect_answer_textBrowser.setGeometry(QtCore.QRect(55, 265, 190, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.incorrect_answer_textBrowser.sizePolicy().hasHeightForWidth())
        self.incorrect_answer_textBrowser.setSizePolicy(sizePolicy)
        self.incorrect_answer_textBrowser.setMinimumSize(QtCore.QSize(190, 25))
        self.incorrect_answer_textBrowser.setMaximumSize(QtCore.QSize(190, 25))
        self.incorrect_answer_textBrowser.setObjectName("textBrowser_2")

        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate

        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))

        self.login_label.setText(_translate("LoginWindow", "LOGIN"))

        self.username_clear_pushButton.setText(_translate("LoginWindow", "Clear"))

        self.username_lineEdit.setPlaceholderText(_translate("LoginWindow", "Username"))

        self.password_lineEdit.setPlaceholderText(_translate("LoginWindow", "Password"))

        self.password_clear_pushButton.setText(_translate("LoginWindow", "Clear"))

        self.username_alert_textBrowser.setHtml(_translate("LoginWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; color:#9c1c1c;\"></span></p></body></html>"))

        self.create_account_pushButton.setText(_translate("LoginWindow", "Create an account"))

        self.continue_pushButton.setText(_translate("LoginWindow", "Continue"))

        self.password_alert_textBrowser.setHtml(_translate("LoginWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; color:#9c1c1c;\"></span></p></body></html>"))

        self.create_account_textBrowser.setHtml(_translate("LoginWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">Don\'t have an account? Create one!</span></p></body></html>"))

        self.TFA_lineEdit.setPlaceholderText(_translate("LoginWindow", "Answer"))

        self.loginTFA_label.setText(_translate("LoginWindow", "Two-Factor Authentication"))

        self.userChosen_question_textBrowser.setHtml(_translate("LoginWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

        self.loginTFA_confirm_pushButton.setText(_translate("LoginWindow", "Confirm"))

        self.incorrect_answer_textBrowser.setHtml(_translate("LoginWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#aa0000;\">Incorrect answer.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec())
