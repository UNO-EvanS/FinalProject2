"""
This is the signup page, accessible from the startup menu or via the 'signup' button in the login menu.

* The user enters a username and password.
    - If the username exists or is "Username", they are informed.
    - If the password doesn't meet criteria, they are alerted.
    - After a valid username and password, they confirm the password.
    - If passwords don't match, they are asked to re-enter.
* After selecting a username and password, the user picks one of ten two-factor authentication questions.
    - They enter an answer and confirm it.
    - If the answers don't match, they are informed.
* Once all requirements are met, the account information is saved in a file.

The user can also navigate to the 'login' menu from this page.

GUI Elements:
       * Labels
         - signup_label
         - TFA_setup_label

       * Line Edits
         - create_username_lineEdit
         - create_password_lineEdit
         - confirm_password_lineEdit
         - TFA_setup_answer_lineEdit
         - TFA_setup_confirmAnswer_lineEdit

       * Push Buttons
         - clear_create_username_pushButton
         - clear_create_password_pushButton
         - clear_confirm_password_pushButton
         - answer_clear_pushButton
         - confirm_Answer_clear_pushButton
         - clearAll_pushButton
         - continue_signup_pushButton
         - login_pushButton

       * Radio Buttons (TFA questions)
         - TFA1_momsMaiden_radioButton: Mother's maiden name.
         - TFA2_favPet_radioButton: Favorite pet's name.
         - TFA3_parentHometown_radioButton: Parent's hometown.
         - TFA4_favGame_radioButton: Favorite game.
         - TFA5_favToy_radioButton: Favorite childhood toy.
         - TFA6_firstJob_radioButton: First job.
         - TFA7_bestFriend_radioButton: Best friend's name.
         - TFA8_firstSchool_radioButton: First school's name.
         - TFA9_favTeam_radioButton: Favorite sports team.
         - TFA10_favCharacter_radioButton: Favorite character.

       * Text Browsers
         - answers_DNM_textBrowser (do not match)
         - password_criteria_textBrowser
         - password_DNM_textBrowser
         - username_AE_textBrowser
         - login_textBrowser: can login if you already have an account
         - TFA_criteria_textBrowser
"""

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SignupWindow(object):
    def setupUi(self, SignupWindow):
        # SignupWindow
        SignupWindow.setObjectName("SignupWindow")
        SignupWindow.resize(300, 625)
        SignupWindow.setMinimumSize(QtCore.QSize(300, 625))
        SignupWindow.setMaximumSize(QtCore.QSize(300, 625))
        self.centralwidget = QtWidgets.QWidget(parent=SignupWindow)
        self.centralwidget.setObjectName("centralwidget")

        # signup_label
        self.signup_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.signup_label.setGeometry(QtCore.QRect(100, 10, 100, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signup_label.sizePolicy().hasHeightForWidth())
        self.signup_label.setSizePolicy(sizePolicy)
        self.signup_label.setMinimumSize(QtCore.QSize(100, 35))
        self.signup_label.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.signup_label.setFont(font)
        self.signup_label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.signup_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.signup_label.setObjectName("signup_label")

        # create_username_lineEdit
        self.create_username_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.create_username_lineEdit.setGeometry(QtCore.QRect(40, 50, 200, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_username_lineEdit.sizePolicy().hasHeightForWidth())
        self.create_username_lineEdit.setSizePolicy(sizePolicy)
        self.create_username_lineEdit.setMinimumSize(QtCore.QSize(200, 20))
        self.create_username_lineEdit.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.create_username_lineEdit.setFont(font)
        self.create_username_lineEdit.setMaxLength(20)
        self.create_username_lineEdit.setObjectName("create_username_lineEdit")

        # username_AE_textBrowser (AE = already exists)
        self.username_AE_textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.username_AE_textBrowser.setEnabled(False)
        self.username_AE_textBrowser.setGeometry(QtCore.QRect(40, 75, 240, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username_AE_textBrowser.sizePolicy().hasHeightForWidth())
        self.username_AE_textBrowser.setSizePolicy(sizePolicy)
        self.username_AE_textBrowser.setMinimumSize(QtCore.QSize(240, 20))
        self.username_AE_textBrowser.setMaximumSize(QtCore.QSize(240, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.username_AE_textBrowser.setFont(font)
        self.username_AE_textBrowser.setObjectName("username_AE_textBrowser")

        # clear_create_username_pushButton
        self.clear_create_username_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clear_create_username_pushButton.setGeometry(QtCore.QRect(240, 50, 40, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_create_username_pushButton.sizePolicy().hasHeightForWidth())
        self.clear_create_username_pushButton.setSizePolicy(sizePolicy)
        self.clear_create_username_pushButton.setMinimumSize(QtCore.QSize(40, 20))
        self.clear_create_username_pushButton.setMaximumSize(QtCore.QSize(40, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.clear_create_username_pushButton.setFont(font)
        self.clear_create_username_pushButton.setObjectName("clear_create_username_pushButton")

        # create_password_lineEdit
        self.create_password_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.create_password_lineEdit.setGeometry(QtCore.QRect(40, 100, 200, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_password_lineEdit.sizePolicy().hasHeightForWidth())
        self.create_password_lineEdit.setSizePolicy(sizePolicy)
        self.create_password_lineEdit.setMinimumSize(QtCore.QSize(200, 20))
        self.create_password_lineEdit.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.create_password_lineEdit.setFont(font)
        self.create_password_lineEdit.setMaxLength(20)
        self.create_password_lineEdit.setObjectName("create_password_lineEdit")

        # clear_create_password_pushButton
        self.clear_create_password_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clear_create_password_pushButton.setGeometry(QtCore.QRect(240, 100, 40, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_create_password_pushButton.sizePolicy().hasHeightForWidth())
        self.clear_create_password_pushButton.setSizePolicy(sizePolicy)
        self.clear_create_password_pushButton.setMinimumSize(QtCore.QSize(40, 20))
        self.clear_create_password_pushButton.setMaximumSize(QtCore.QSize(40, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.clear_create_password_pushButton.setFont(font)
        self.clear_create_password_pushButton.setObjectName("clear_create_password_pushButton")

        # password_criteria_textBrowser
        self.password_criteria_textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.password_criteria_textBrowser.setEnabled(False)
        self.password_criteria_textBrowser.setGeometry(QtCore.QRect(40, 155, 240, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_criteria_textBrowser.sizePolicy().hasHeightForWidth())
        self.password_criteria_textBrowser.setSizePolicy(sizePolicy)
        self.password_criteria_textBrowser.setMinimumSize(QtCore.QSize(240, 40))
        self.password_criteria_textBrowser.setMaximumSize(QtCore.QSize(240, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.password_criteria_textBrowser.setFont(font)
        self.password_criteria_textBrowser.setObjectName("password_criteria_textBrowser")

        # confirm_password_lineEdit
        self.confirm_password_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.confirm_password_lineEdit.setGeometry(QtCore.QRect(40, 200, 200, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirm_password_lineEdit.sizePolicy().hasHeightForWidth())
        self.confirm_password_lineEdit.setSizePolicy(sizePolicy)
        self.confirm_password_lineEdit.setMinimumSize(QtCore.QSize(200, 20))
        self.confirm_password_lineEdit.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.confirm_password_lineEdit.setFont(font)
        self.confirm_password_lineEdit.setMaxLength(20)
        self.confirm_password_lineEdit.setObjectName("confirm_password_lineEdit")

        #continue_signup_pushButton
        self.continue_signup_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.continue_signup_pushButton.setGeometry(QtCore.QRect(75, 500, 60, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.continue_signup_pushButton.sizePolicy().hasHeightForWidth())
        self.continue_signup_pushButton.setSizePolicy(sizePolicy)
        self.continue_signup_pushButton.setMinimumSize(QtCore.QSize(60, 25))
        self.continue_signup_pushButton.setMaximumSize(QtCore.QSize(60, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.continue_signup_pushButton.setFont(font)
        self.continue_signup_pushButton.setObjectName("continue_signup_pushButton")

        # clear_confirm_password_pushButton
        self.clear_confirm_password_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clear_confirm_password_pushButton.setGeometry(QtCore.QRect(240, 200, 40, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_confirm_password_pushButton.sizePolicy().hasHeightForWidth())
        self.clear_confirm_password_pushButton.setSizePolicy(sizePolicy)
        self.clear_confirm_password_pushButton.setMinimumSize(QtCore.QSize(40, 20))
        self.clear_confirm_password_pushButton.setMaximumSize(QtCore.QSize(40, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.clear_confirm_password_pushButton.setFont(font)
        self.clear_confirm_password_pushButton.setObjectName("clear_confirm_password_pushButton")

        # password_DNM_textBrowser (DNM = Does Not Match)
        self.password_DNM_textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.password_DNM_textBrowser.setEnabled(False)
        self.password_DNM_textBrowser.setGeometry(QtCore.QRect(40, 125, 240, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_DNM_textBrowser.sizePolicy().hasHeightForWidth())
        self.password_DNM_textBrowser.setSizePolicy(sizePolicy)
        self.password_DNM_textBrowser.setMinimumSize(QtCore.QSize(240, 25))
        self.password_DNM_textBrowser.setMaximumSize(QtCore.QSize(240, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.password_DNM_textBrowser.setFont(font)
        self.password_DNM_textBrowser.setObjectName("password_DNM_textBrowser")

        # login_textBrowser
        self.login_textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.login_textBrowser.setGeometry(QtCore.QRect(25, 550, 200, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_textBrowser.sizePolicy().hasHeightForWidth())
        self.login_textBrowser.setSizePolicy(sizePolicy)
        self.login_textBrowser.setMinimumSize(QtCore.QSize(200, 25))
        self.login_textBrowser.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.login_textBrowser.setFont(font)
        self.login_textBrowser.setObjectName("login_textBrowser")

        # login_pushButton
        self.login_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.login_pushButton.setGeometry(QtCore.QRect(225, 550, 50, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_pushButton.sizePolicy().hasHeightForWidth())
        self.login_pushButton.setSizePolicy(sizePolicy)
        self.login_pushButton.setMinimumSize(QtCore.QSize(50, 25))
        self.login_pushButton.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.login_pushButton.setFont(font)
        self.login_pushButton.setObjectName("login_pushButton")

        # TFA_setup_label
        self.TFA_setup_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.TFA_setup_label.setGeometry(QtCore.QRect(20, 225, 260, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TFA_setup_label.sizePolicy().hasHeightForWidth())
        self.TFA_setup_label.setSizePolicy(sizePolicy)
        self.TFA_setup_label.setMinimumSize(QtCore.QSize(260, 20))
        self.TFA_setup_label.setMaximumSize(QtCore.QSize(260, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.TFA_setup_label.setFont(font)
        self.TFA_setup_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TFA_setup_label.setObjectName("TFA_setup_label")

        # TFA1_momsMaiden_radioButton
        self.TFA1_momsMaiden_radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.TFA1_momsMaiden_radioButton.setGeometry(QtCore.QRect(20, 250, 120, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TFA1_momsMaiden_radioButton.sizePolicy().hasHeightForWidth())
        self.TFA1_momsMaiden_radioButton.setSizePolicy(sizePolicy)
        self.TFA1_momsMaiden_radioButton.setMinimumSize(QtCore.QSize(120, 20))
        self.TFA1_momsMaiden_radioButton.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.TFA1_momsMaiden_radioButton.setFont(font)
        self.TFA1_momsMaiden_radioButton.setObjectName("TFA1_momsMaiden_radioButton")

        # TFA2_favPet_radioButton
        self.TFA2_favPet_radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.TFA2_favPet_radioButton.setGeometry(QtCore.QRect(160, 250, 110, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TFA2_favPet_radioButton.sizePolicy().hasHeightForWidth())
        self.TFA2_favPet_radioButton.setSizePolicy(sizePolicy)
        self.TFA2_favPet_radioButton.setMinimumSize(QtCore.QSize(110, 20))
        self.TFA2_favPet_radioButton.setMaximumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.TFA2_favPet_radioButton.setFont(font)
        self.TFA2_favPet_radioButton.setObjectName("TFA2_favPet_radioButton")

        # TFA3_parentHometown_radioButton
        self.TFA3_parentHometown_radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.TFA3_parentHometown_radioButton.setGeometry(QtCore.QRect(20, 280, 110, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TFA3_parentHometown_radioButton.sizePolicy().hasHeightForWidth())
        self.TFA3_parentHometown_radioButton.setSizePolicy(sizePolicy)
        self.TFA3_parentHometown_radioButton.setMinimumSize(QtCore.QSize(110, 20))
        self.TFA3_parentHometown_radioButton.setMaximumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.TFA3_parentHometown_radioButton.setFont(font)
        self.TFA3_parentHometown_radioButton.setObjectName("TFA3_parentHometown_radioButton")

        # TFA4_favGame_radioButton
        self.TFA4_favGame_radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.TFA4_favGame_radioButton.setGeometry(QtCore.QRect(160, 280, 90, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TFA4_favGame_radioButton.sizePolicy().hasHeightForWidth())
        self.TFA4_favGame_radioButton.setSizePolicy(sizePolicy)
        self.TFA4_favGame_radioButton.setMinimumSize(QtCore.QSize(0, 20))
        self.TFA4_favGame_radioButton.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.TFA4_favGame_radioButton.setFont(font)
        self.TFA4_favGame_radioButton.setObjectName("TFA4_favGame_radioButton")

        # TFA5_favToy_radioButton
        self.TFA5_favToy_radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.TFA5_favToy_radioButton.setGeometry(QtCore.QRect(20, 310, 120, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TFA5_favToy_radioButton.sizePolicy().hasHeightForWidth())
        self.TFA5_favToy_radioButton.setSizePolicy(sizePolicy)
        self.TFA5_favToy_radioButton.setMinimumSize(QtCore.QSize(120, 20))
        self.TFA5_favToy_radioButton.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.TFA5_favToy_radioButton.setFont(font)
        self.TFA5_favToy_radioButton.setObjectName("TFA5_favToy_radioButton")

        # TFA5_firstJob_radioButton
        self.TFA6_firstJob_radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.TFA6_firstJob_radioButton.setGeometry(QtCore.QRect(160, 310, 60, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TFA6_firstJob_radioButton.sizePolicy().hasHeightForWidth())
        self.TFA6_firstJob_radioButton.setSizePolicy(sizePolicy)
        self.TFA6_firstJob_radioButton.setMinimumSize(QtCore.QSize(60, 20))
        self.TFA6_firstJob_radioButton.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.TFA6_firstJob_radioButton.setFont(font)
        self.TFA6_firstJob_radioButton.setObjectName("TFA6_firstJob_radioButton")

        # TFA7_bestFriend_radioButton
        self.TFA7_bestFriend_radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.TFA7_bestFriend_radioButton.setGeometry(QtCore.QRect(20, 340, 100, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TFA7_bestFriend_radioButton.sizePolicy().hasHeightForWidth())
        self.TFA7_bestFriend_radioButton.setSizePolicy(sizePolicy)
        self.TFA7_bestFriend_radioButton.setMinimumSize(QtCore.QSize(100, 20))
        self.TFA7_bestFriend_radioButton.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.TFA7_bestFriend_radioButton.setFont(font)
        self.TFA7_bestFriend_radioButton.setObjectName("TFA7_bestFriend_radioButton")

        # TFA8_firstSchool_radioButton
        self.TFA8_firstSchool_radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.TFA8_firstSchool_radioButton.setGeometry(QtCore.QRect(160, 340, 110, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TFA8_firstSchool_radioButton.sizePolicy().hasHeightForWidth())
        self.TFA8_firstSchool_radioButton.setSizePolicy(sizePolicy)
        self.TFA8_firstSchool_radioButton.setMinimumSize(QtCore.QSize(110, 20))
        self.TFA8_firstSchool_radioButton.setMaximumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.TFA8_firstSchool_radioButton.setFont(font)
        self.TFA8_firstSchool_radioButton.setObjectName("TFA8_firstSchool_radioButton")

        # TFA9_favTeam_radioButton
        self.TFA9_favTeam_radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.TFA9_favTeam_radioButton.setGeometry(QtCore.QRect(20, 370, 110, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TFA9_favTeam_radioButton.sizePolicy().hasHeightForWidth())
        self.TFA9_favTeam_radioButton.setSizePolicy(sizePolicy)
        self.TFA9_favTeam_radioButton.setMinimumSize(QtCore.QSize(110, 20))
        self.TFA9_favTeam_radioButton.setMaximumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.TFA9_favTeam_radioButton.setFont(font)
        self.TFA9_favTeam_radioButton.setObjectName("TFA9_favTeam_radioButton")

        # TFA10_favCharacter_radioButton
        self.TFA10_favCharacter_radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.TFA10_favCharacter_radioButton.setGeometry(QtCore.QRect(160, 370, 100, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TFA10_favCharacter_radioButton.sizePolicy().hasHeightForWidth())
        self.TFA10_favCharacter_radioButton.setSizePolicy(sizePolicy)
        self.TFA10_favCharacter_radioButton.setMinimumSize(QtCore.QSize(100, 20))
        self.TFA10_favCharacter_radioButton.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.TFA10_favCharacter_radioButton.setFont(font)
        self.TFA10_favCharacter_radioButton.setObjectName("TFA10_favCharacter_radioButton")

        # TFA_criteria_textBrowser
        self.TFA_criteria_textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.TFA_criteria_textBrowser.setGeometry(QtCore.QRect(25, 390, 250, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TFA_criteria_textBrowser.sizePolicy().hasHeightForWidth())
        self.TFA_criteria_textBrowser.setSizePolicy(sizePolicy)
        self.TFA_criteria_textBrowser.setMinimumSize(QtCore.QSize(250, 40))
        self.TFA_criteria_textBrowser.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.TFA_criteria_textBrowser.setFont(font)
        self.TFA_criteria_textBrowser.setObjectName("TFA_criteria_textBrowser")

        # TFA_setup_answer_lineEdit
        self.TFA_setup_answer_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.TFA_setup_answer_lineEdit.setGeometry(QtCore.QRect(40, 450, 200, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TFA_setup_answer_lineEdit.sizePolicy().hasHeightForWidth())
        self.TFA_setup_answer_lineEdit.setSizePolicy(sizePolicy)
        self.TFA_setup_answer_lineEdit.setMinimumSize(QtCore.QSize(200, 20))
        self.TFA_setup_answer_lineEdit.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.TFA_setup_answer_lineEdit.setFont(font)
        self.TFA_setup_answer_lineEdit.setText("")
        self.TFA_setup_answer_lineEdit.setMaxLength(20)
        self.TFA_setup_answer_lineEdit.setObjectName("TFA_setup_answer_lineEdit")

        # answer_clear_pushButton
        self.answer_clear_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.answer_clear_pushButton.setGeometry(QtCore.QRect(240, 450, 40, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer_clear_pushButton.sizePolicy().hasHeightForWidth())
        self.answer_clear_pushButton.setSizePolicy(sizePolicy)
        self.answer_clear_pushButton.setMinimumSize(QtCore.QSize(40, 20))
        self.answer_clear_pushButton.setMaximumSize(QtCore.QSize(40, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.answer_clear_pushButton.setFont(font)
        self.answer_clear_pushButton.setObjectName("answer_clear_pushButton")

        # confirm_Answer_clear_pushButton
        self.confirm_Answer_clear_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.confirm_Answer_clear_pushButton.setGeometry(QtCore.QRect(240, 475, 40, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirm_Answer_clear_pushButton.sizePolicy().hasHeightForWidth())
        self.confirm_Answer_clear_pushButton.setSizePolicy(sizePolicy)
        self.confirm_Answer_clear_pushButton.setMinimumSize(QtCore.QSize(40, 20))
        self.confirm_Answer_clear_pushButton.setMaximumSize(QtCore.QSize(40, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.confirm_Answer_clear_pushButton.setFont(font)
        self.confirm_Answer_clear_pushButton.setObjectName("confirm_Answer_clear_pushButton")

        # clearAll_pushButton
        self.clearAll_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clearAll_pushButton.setGeometry(QtCore.QRect(165, 500, 60, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearAll_pushButton.sizePolicy().hasHeightForWidth())
        self.clearAll_pushButton.setSizePolicy(sizePolicy)
        self.clearAll_pushButton.setMinimumSize(QtCore.QSize(60, 25))
        self.clearAll_pushButton.setMaximumSize(QtCore.QSize(60, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.clearAll_pushButton.setFont(font)
        self.clearAll_pushButton.setObjectName("clearAll_pushButton")

        # TFA_setup_confirmAnswer_lineEdit
        self.TFA_setup_confirmAnswer_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.TFA_setup_confirmAnswer_lineEdit.setGeometry(QtCore.QRect(40, 475, 200, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TFA_setup_confirmAnswer_lineEdit.sizePolicy().hasHeightForWidth())
        self.TFA_setup_confirmAnswer_lineEdit.setSizePolicy(sizePolicy)
        self.TFA_setup_confirmAnswer_lineEdit.setMinimumSize(QtCore.QSize(200, 20))
        self.TFA_setup_confirmAnswer_lineEdit.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.TFA_setup_confirmAnswer_lineEdit.setFont(font)
        self.TFA_setup_confirmAnswer_lineEdit.setText("")
        self.TFA_setup_confirmAnswer_lineEdit.setMaxLength(20)
        self.TFA_setup_confirmAnswer_lineEdit.setObjectName("TFA_setup_confirmAnswer_lineEdit")

        # answers_DNM_textBrowser
        self.answers_DNM_textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.answers_DNM_textBrowser.setEnabled(False)
        self.answers_DNM_textBrowser.setGeometry(QtCore.QRect(30, 525, 240, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answers_DNM_textBrowser.sizePolicy().hasHeightForWidth())
        self.answers_DNM_textBrowser.setSizePolicy(sizePolicy)
        self.answers_DNM_textBrowser.setMinimumSize(QtCore.QSize(240, 20))
        self.answers_DNM_textBrowser.setMaximumSize(QtCore.QSize(240, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.answers_DNM_textBrowser.setFont(font)
        self.answers_DNM_textBrowser.setObjectName("answers_DNM_textBrowser")

        SignupWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=SignupWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 22))
        self.menubar.setObjectName("menubar")
        SignupWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=SignupWindow)
        self.statusbar.setObjectName("statusbar")
        SignupWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SignupWindow)
        QtCore.QMetaObject.connectSlotsByName(SignupWindow)

    def retranslateUi(self, SignupWindow):
        _translate = QtCore.QCoreApplication.translate
        SignupWindow.setWindowTitle(_translate("SignupWindow", "Signup"))

        self.signup_label.setText(_translate("SignupWindow", "Signup"))

        self.create_username_lineEdit.setPlaceholderText(_translate("SignupWindow", "Create username"))

        self.username_AE_textBrowser.setHtml(_translate("SignupWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; color:#9c1c1c;\">This username is taken.</span></p></body></html>"))

        self.confirm_Answer_clear_pushButton.setText(_translate("SignupWindow", "Clear"))

        self.create_password_lineEdit.setPlaceholderText(_translate("SignupWindow", "Answer"))

        self.TFA_setup_answer_lineEdit.setPlaceholderText(_translate("SignupWindow", "Answer"))

        self.TFA_setup_confirmAnswer_lineEdit.setPlaceholderText(_translate("SignupWindow", "Confirm answer"))

        self.clear_create_username_pushButton.setText(_translate("SignupWindow", "Clear"))

        self.create_password_lineEdit.setPlaceholderText(_translate("SignupWindow", "Create strong password"))

        self.clear_create_password_pushButton.setText(_translate("SignupWindow", "Clear"))

        self.password_criteria_textBrowser.setHtml(_translate("SignupWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; color:#000000;\">Password must be between 8-20 characters and must contain at least one capital letter, 2 digits, and one special character (e.g. &quot;!&quot;, &quot;&amp;&quot;). Cannot contain 'Password' or 'password'.</span></p></body></html>"))

        self.confirm_password_lineEdit.setPlaceholderText(_translate("SignupWindow", "Confirm password"))

        self.continue_signup_pushButton.setText(_translate("SignupWindow", "Continue"))

        self.clear_confirm_password_pushButton.setText(_translate("SignupWindow", "Clear"))

        self.answer_clear_pushButton.setText(_translate("SignupWindow", "Clear"))

        self.clearAll_pushButton.setText(_translate("SignupWindow", "Clear all"))

        self.password_DNM_textBrowser.setHtml(_translate("SignupWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; color:#9c1c1c;\">Passwords do not match or are invalid. Please re-enter.</span></p></body></html>"))

        self.login_textBrowser.setHtml(_translate("SignupWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">Already have an account? Log in!</span></p></body></html>"))

        self.login_pushButton.setText(_translate("SignupWindow", "Log in"))

        self.TFA_setup_label.setText(_translate("SignupWindow", "Set up two-factor authentication"))

        self.TFA1_momsMaiden_radioButton.setText(_translate("SignupWindow", "Mother\'s maiden name"))
        self.TFA2_favPet_radioButton.setText(_translate("SignupWindow", "Favorite pet\'s name"))
        self.TFA3_parentHometown_radioButton.setText(_translate("SignupWindow", "Parent\'s hometown"))
        self.TFA4_favGame_radioButton.setText(_translate("SignupWindow", "Favorite game"))
        self.TFA5_favToy_radioButton.setText(_translate("SignupWindow", "Favorite childhood toy"))
        self.TFA6_firstJob_radioButton.setText(_translate("SignupWindow", "First job"))
        self.TFA7_bestFriend_radioButton.setText(_translate("SignupWindow", "Best friend\'s name"))
        self.TFA8_firstSchool_radioButton.setText(_translate("SignupWindow", "First school\'s name"))
        self.TFA9_favTeam_radioButton.setText(_translate("SignupWindow", "Favorite sports team"))
        self.TFA10_favCharacter_radioButton.setText(_translate("SignupWindow", "Favorite character"))

        self.TFA_criteria_textBrowser.setHtml(_translate("SignupWindow","<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Answer must be between 4 and 20 characters in length.</p></body></html>"))

        self.answers_DNM_textBrowser.setHtml(_translate("SignupWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; color:#9c1c1c;\">The two answers do not match. Please re-enter.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignupWindow = QtWidgets.QMainWindow()
    ui = Ui_SignupWindow()
    ui.setupUi(SignupWindow)
    SignupWindow.show()
    sys.exit(app.exec())
