class SignupPage(QMainWindow):
    def __init__(self):
       super(SignupPage, self).__init__()
       self.SignupUI = Ui_SignupWindow()
       self.SignupUI.setupUi(self)

       # for when an input is invalid
       self.SignupUI.username_AE_textBrowser.hide()
       self.SignupUI.password_DNM_textBrowser.hide()
       self.SignupUI.answers_DNM_textBrowser.hide()

       # takes you to the login page
       self.SignupUI.login_pushButton.clicked.connect(self.login)

       # clears their respective inputs
       self.SignupUI.clear_create_username_pushButton.clicked.connect(self.clear_create_username)
       self.SignupUI.clear_create_password_pushButton.clicked.connect(self.clear_create_password)
       self.SignupUI.clear_confirm_password_pushButton.clicked.connect(self.clear_confirm_password)
       self.SignupUI.answer_clear_pushButton.clicked.connect(self.clear_create_answer)
       self.SignupUI.confirm_Answer_clear_pushButton.clicked.connect(self.clear_confirm_answer)
       self.SignupUI.clearAll_pushButton.clicked.connect(self.clear_all_fields)

       # two-factor authentication radio buttons
       self.tfa_buttons = QButtonGroup(self)
       self.tfa_buttons.addButton(self.SignupUI.TFA1_momsMaiden_radioButton, 1)
       self.tfa_buttons.addButton(self.SignupUI.TFA2_favPet_radioButton, 2)
       self.tfa_buttons.addButton(self.SignupUI.TFA3_parentHometown_radioButton, 3)
       self.tfa_buttons.addButton(self.SignupUI.TFA4_favGame_radioButton, 4)
       self.tfa_buttons.addButton(self.SignupUI.TFA5_favToy_radioButton, 5)
       self.tfa_buttons.addButton(self.SignupUI.TFA6_firstJob_radioButton, 6)
       self.tfa_buttons.addButton(self.SignupUI.TFA7_bestFriend_radioButton, 7)
       self.tfa_buttons.addButton(self.SignupUI.TFA8_firstSchool_radioButton, 8)
       self.tfa_buttons.addButton(self.SignupUI.TFA9_favTeam_radioButton, 9)
       self.tfa_buttons.addButton(self.SignupUI.TFA10_favCharacter_radioButton, 10)

       # dictionary containing all the corresponding questions for the TFA
       self.user_TFA_questions = {
           1: "What is your mother's maiden name?",
           2: "What is your favorite pet's name?",
           3: "What is your parent's hometown?",
           4: "What is your favorite game?",
           5: "What was your favorite childhood toy?",
           6: "What was your first job?",
           7: "What is your best friend's name?",
           8: "What was your first school's name?",
           9: "What is your favorite sports team?",
           10: "What is your favorite character?"
       }

       #
       self.SignupUI.continue_signup_pushButton.clicked.connect(self.are_fields_empty)

    def login(self):
        self.hide()
        login_window.show()

    def clear_create_username(self): # clears the username text input
        self.SignupUI.create_username_lineEdit.clear()

    def clear_create_password(self): # clears the password text input
        self.SignupUI.create_password_lineEdit.clear()

    def clear_confirm_password(self): # clears the password confirm text input
        self.SignupUI.confirm_password_lineEdit.clear()

    def clear_create_answer(self):
        self.SignupUI.TFA_setup_answer_lineEdit.clear()

    def clear_confirm_answer(self):
        self.SignupUI.TFA_setup_confirmAnswer_lineEdit.clear()

    def clear_all_fields(self): # Clears all inputs
        self.clear_create_username()
        self.clear_create_password()
        self.clear_confirm_password()
        self.clear_create_answer()
        self.clear_confirm_answer()
        print("1")



    def are_fields_empty(self): # checks to see if any inputs are missing
        self.username_input = self.SignupUI.create_username_lineEdit.text().strip()
        self.password_input = self.SignupUI.create_password_lineEdit.text()
        self.password_confirmation = self.SignupUI.confirm_password_lineEdit.text()
        self.user_TFA_option = int(self.tfa_buttons.checkedId())
        self.user_TFA_selection = self.user_TFA_questions.get(self.user_TFA_option)
        self.user_answer = self.SignupUI.TFA_setup_answer_lineEdit.text()
        self.answer_confirmation = self.SignupUI.TFA_setup_confirmAnswer_lineEdit.text()

        if all([self.username_input, self.password_input, self.password_confirmation,
                self.user_TFA_selection, self.user_answer, self.answer_confirmation]):
            if self.username_input == self.password_input:
                self.SignupUI.username_AE_textBrowser.show()
                self.SignupUI.username_AE_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Username and password cannot equal.</font>')
            elif self.username_input == self.user_answer:
                self.SignupUI.answers_DNM_textBrowser.show()
                self.SignupUI.answers_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Username and TFA answer cannot equal.</font>')
            elif self.password_input == self.user_answer:
                self.SignupUI.username_AE_textBrowser.hide()
                self.SignupUI.answers_DNM_textBrowser.show()
                self.SignupUI.answers_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Password and TFA answer cannot equal.</font>')
            else:
                self.SignupUI.username_AE_textBrowser.hide()
                self.SignupUI.password_DNM_textBrowser.hide()
                self.SignupUI.answers_DNM_textBrowser.hide()
                print("2")
                self.does_username_exist()
        else:
            if not self.username_input:
                self.SignupUI.username_AE_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Please put in a username.</font>')
                self.SignupUI.username_AE_textBrowser.show()
            if not self.password_input or not self.password_confirmation:
                self.SignupUI.password_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Please choose and confirm password.</font>')
                self.SignupUI.password_DNM_textBrowser.show()
            if not all([self.user_TFA_selection, self.user_answer, self.answer_confirmation]):
                self.SignupUI.answers_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Please finish filling this field.</font>')
                self.SignupUI.answers_DNM_textBrowser.show()

    def does_username_exist(self):
        self.username_found = False

        if os.path.exists(userInfo_file):
            with open(userInfo_file, "r") as info:
                contents = csv.reader(info)
                for content in contents:
                    if not any(content):
                        print("3")
                        pass
                    else:
                        if self.username_input == content[0]:
                            self.SignupUI.username_AE_textBrowser.show()
                            self.username_found = True
                            break
                        else:
                            self.username_found = False
                            continue
        if self.username_found == False:
            print("4")
            self.SignupUI.username_AE_textBrowser.hide()
            self.password_match()

    def password_match(self):
        print("5")
        self.special_chars = "\"!.?<>=+-*/%$'@&#_~^\\"
        self.nums = "1234567890"
        self.caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        if self.password_input != self.password_confirmation:
            self.SignupUI.password_DNM_textBrowser.show()
            self.SignupUI.password_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;Passwords do not match or are invalid.</font>')
            self.SignupUI.username_AE_textBrowser.hide()
        elif "Password" in self.password_input:
            self.SignupUI.password_DNM_textBrowser.show()
            self.SignupUI.password_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Password cannot contain "Password".</font>')
        elif "password" in self.password_input:
            self.SignupUI.password_DNM_textBrowser.show()
            self.SignupUI.password_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Password cannot contain "password".</font>')
        elif " " in self.password_input:
            self.SignupUI.password_DNM_textBrowser.show()
            self.SignupUI.password_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Password cannot contain whitespace.</font>')
        else:
            if len(self.password_input) > 7:
                print("6")
                self.chars = []
                self.spec_chars = []
                self.cap_chars = []
                self.num_chars = []
                for char in self.password_input:
                    self.chars.append(char)
                for i in self.chars:
                    if i in self.special_chars:
                        self.spec_chars.append(i)
                    elif i in self.caps:
                        self.cap_chars.append(i)
                    elif i in self.nums:
                        self.num_chars.append(i)
                if all([(len(self.spec_chars) > 0), (len(self.cap_chars) > 0), (len(self.num_chars)) > 1]):
                    print("7")
                    self.SignupUI.password_DNM_textBrowser.hide()
                    self.check_TFA()
                else:
                    self.SignupUI.password_DNM_textBrowser.show()
                    self.SignupUI.password_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Password does not meet criteria.</font>')

    def check_TFA(self):
        print("8")
        if self.user_answer != self.answer_confirmation:
            self.SignupUI.answers_DNM_textBrowser.show()
            self.SignupUI.answers_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Answers do not match. Please re-enter".</font>')
        elif "Answer" in self.user_answer:
            self.SignupUI.answers_DNM_textBrowser.show()
            self.SignupUI.answers_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Answer cannot contain "Answer".</font>')
        elif "answer" in self.user_answer:
            self.SignupUI.answers_DNM_textBrowser.show()
            self.SignupUI.answers_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Answer cannot contain "answer".</font>')
        else:
            if len(self.user_answer) > 4:
                print("9")
                self.SignupUI.answers_DNM_textBrowser.hide()
                self.account_creation()

    def account_creation(self):
        print("10")
        self.new_account_info = [self.username_input, self.password_input, self.user_TFA_selection,
                            self.user_answer]
        with open(userInfo_file, "a+", newline="") as accounts:
            print("11")
            try:
                print("12")
                accounts.seek(0)
                self.reader = csv.reader(accounts)
                print("13")
                self.appender = csv.writer(accounts)
                print("14")
                first_line = None
                try:
                    first_line = next(self.reader)
                    print("15")
                except Exception as e:
                    pass

                if not first_line:
                    print("16")
                    self.appender.writerow(["User", "Password", "Question", "Answer", "Status"])
                    self.appender.writerow(self.new_account_info)
                else:
                    print("17")
                    self.appender.writerow(self.new_account_info)

            except Exception as e:
                print(e)

        self.sign_in()

    def sign_in(self):
        signup_window.hide()  # Resets the sign-up page
        print("18")
        storage_window.show()

class StoragePage(QMainWindow):
    def __init__(self):
        super(StoragePage, self).__init__()
        self.StorageUI = Ui_UserStorageWindow()
        self.StorageUI.setupUi(self)

        self.logout_cancel()

        self.StorageUI.transaction_history_textBrowser.hide()


        self.operation_buttons = QButtonGroup(self)
        self.operation_buttons.addButton(self.StorageUI.deposit_radioButton, 1)
        self.operation_buttons.addButton(self.StorageUI.withdraw_radioButton, 2)
        self.operation_buttons.addButton(self.StorageUI.transHist_radioButton, 3)
        self.operation_buttons.addButton(self.StorageUI.clearStorage_radioButton, 4)

        self.StorageUI.log_out_pushButton.clicked.connect(self.logout_check)
        self.StorageUI.confirm_logout_pushButton.clicked.connect(self.logout_confirm)
        self.StorageUI.cancel_logout_pushButton.clicked.connect(self.logout_cancel)

    def retrieve_data(self, username, data):
        self.user = username
        self.user_data = data

    def logout_check(self):
        self.StorageUI.confirm_logout_pushButton.show()
        self.StorageUI.cancel_logout_pushButton.show()
        self.StorageUI.logout_question_label.show()

    def logout_confirm(self):
        self.hide()
        start_window.show()

    def logout_cancel(self):
        self.StorageUI.logout_question_label.hide()
        self.StorageUI.confirm_logout_pushButton.hide()
        self.StorageUI.cancel_logout_pushButton.hide()

    def display_data(self):
        self.storage_lines = []
        with open(userStorage_file, "r") as storage:
            storage_reader = csv.reader(storage)
            for line in storage_reader:
                self.storage_lines.append(line)
                if line[0] == self.user:
                    self.StorageUI.hello_user_label.setText(f"Hello, {self.user}!")

                    self.profile_contents = {}
                    self.browser_contents = ""

                    for i in range(3, len(line), 2):
                        self.item = line[i]
                        self.quantity = line[i+1]
                        self.profile_contents[self.item] = self.quantity

                    for key in self.profile_contents:
                        self.browser_contents += f"{key} \t{value}"

if __name__ == "__main__":
    userInfo_file = "StorageFiles/userInfo.csv"
    accountHistory_file = "StorageFiles/accountHistory.csv"
    userStorage_file = "StorageFiles/userStorage.csv"
    application = QApplication(sys.argv)
    start_window = StartProgram() # gui_startup
    signup_window = SignupPage() # gui_signup
    login_window = LoginPage() # gui_login
    storage_window = StoragePage()  # gui_storage
    start_window.show()

    sys.exit(application.exec())


from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup
import sys
import csv
import os.path

from gui_login import *
from gui_signup import *
from gui_startup import *
from gui_storage import *

class StartProgram(QMainWindow):
    def __init__(self):
        super(StartProgram, self).__init__()
        self.StartupUI = Ui_StartWindow()
        self.StartupUI.setupUi(self)

        self.StartupUI.start_login_pushButton.clicked.connect(self.login)  # Directs user to login page
        self.StartupUI.start_create_account_pushButton.clicked.connect(self.create_account)  # Directs the user to signup page

    def login(self):
        self.hide()
        login_window.show()

    def create_account(self):
        self.hide()
        signup_window.show()

class LoginPage(QMainWindow):
    def __init__(self):
       super(LoginPage, self).__init__()
       self.LoginUI = Ui_LoginWindow()
       self.LoginUI.setupUi(self)

       # for wrong passwords or TFA answers
       self.LoginUI.username_alert_textBrowser.hide()
       self.LoginUI.password_alert_textBrowser.hide()

       # for all other TFA stuff (will appear after an existing username and its password are correctly entered.)
       self.LoginUI.loginTFA_label.hide()
       self.LoginUI.userChosen_question_textBrowser.hide()
       self.LoginUI.TFA_lineEdit.hide()
       self.LoginUI.loginTFA_confirm_pushButton.hide()
       self.LoginUI.incorrect_answer_textBrowser.hide()

       # clear button
       self.LoginUI.username_clear_pushButton.clicked.connect(self.clear_username)
       self.LoginUI.password_clear_pushButton.clicked.connect(self.clear_password)

        # continue
       self.LoginUI.continue_pushButton.clicked.connect(self.attempt_continue)
       self.LoginUI.loginTFA_confirm_pushButton.clicked.connect(self.answer_check)

       self.LoginUI.create_account_pushButton.clicked.connect(self.create_account)

    def create_account(self):
        self.LoginUI.username_lineEdit.clear()
        self.LoginUI.username_alert_textBrowser.hide()
        self.LoginUI.password_lineEdit.clear()
        self.LoginUI.password_alert_textBrowser.hide()
        self.LoginUI.incorrect_answer_textBrowser.clear()
        self.LoginUI.incorrect_answer_textBrowser.hide()

        self.hide()
        signup_window.show()

    def clear_username(self):
        self.LoginUI.username_lineEdit.clear()
        self.LoginUI.username_alert_textBrowser.hide()

    def clear_password(self):
        self.LoginUI.password_lineEdit.clear()
        self.LoginUI.password_alert_textBrowser.hide()

    def attempt_continue(self):
        self.username =  self.LoginUI.username_lineEdit.text()
        self.password =  self.LoginUI.password_lineEdit.text()

        if not self.username:
            self.LoginUI.username_alert_textBrowser.show()
            self.LoginUI.username_alert_textBrowser.setText("Please provide a username.")
        else:
            self.LoginUI.username_alert_textBrowser.hide()

        if not self.password:  # if the password field is left blank
            self.LoginUI.password_alert_textBrowser.show()
            self.LoginUI.password_alert_textBrowser.setText("Please provide a password.")
        else:
            self.LoginUI.password_alert_textBrowser.hide()

        if self.username and self.password:  # if a username and password are provided
            try:
                with open(userInfo_file, "r") as userInfo:
                    self.contents = csv.reader(userInfo, delimiter=",")
                    for content in self.contents:
                        if content[0] == self.username: # if the input username matches the account name in the file
                            self.LoginUI.username_alert_textBrowser.hide()
                            if content[1] == self.password: # if the input password matches the password for that account in the file
                                self.TFA_question = content[2]
                                self.TFA_answer = content[3]
                                self.two_factor_authentication(self.TFA_question, self.TFA_answer)
                            else:
                                self.LoginUI.password_alert_textBrowser.show()
                                self.LoginUI.password_alert_textBrowser.setText("Incorrect password.")
                        else:
                            self.LoginUI.username_alert_textBrowser.show()
                            self.LoginUI.username_alert_textBrowser.setText("Username does not exist.")
            except FileNotFoundError:
                    self.LoginUI.username_alert_textBrowser.show()
                    self.LoginUI.username_alert_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Congratulations!</font>')
                    self.LoginUI.password_alert_textBrowser.show()
                    self.LoginUI.password_alert_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">You are our first user!</font>')
                    self.LoginUI.incorrect_answer_textBrowser.show()
                    self.LoginUI.incorrect_answer_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Please alternate to the signup page.</font>')

    def two_factor_authentication(self, question, answer):
        self.correct_answer = answer
        self.LoginUI.userChosen_question_textBrowser.setText(question)
        self.LoginUI.loginTFA_label.show()
        self.LoginUI.userChosen_question_textBrowser.show()
        self.LoginUI.TFA_lineEdit.show()
        self.LoginUI.loginTFA_confirm_pushButton.show()

    def answer_check(self, answer):
        self.user_answer = self.LoginUI.TFA_lineEdit.text().strip()
        if self.user_answer == answer:
            self.LoginUI.incorrect_answer_textBrowser.hide()
            find_user_profile()

    def find_user_profile(self):
        try:
            with open(userStorage_file, "r") as find_user:
                self.user_locator = csv.reader(find_user)
                for line in self.user_locator:
                    if self.username == line[0]:
                        self.profile_data = line
                        storage_window.retrieve_data(self.username, self.profile_data)
                        self.hide()
                        storage_window.show()
        except FileNotFoundError:
            print('IDK')