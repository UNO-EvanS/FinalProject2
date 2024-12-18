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

    def clear_create_username(self): # clears the username area
        self.SignupUI.create_username_lineEdit.clear()

    def clear_create_password(self): # clears the password area
        self.SignupUI.create_password_lineEdit.clear()

    def clear_confirm_password(self): # clears the password confirm area
        self.SignupUI.confirm_password_lineEdit.clear()

    def clear_create_answer(self): # clear the answer area
        self.SignupUI.TFA_setup_answer_lineEdit.clear()

    def clear_confirm_answer(self): # clears the answer confirm area
        self.SignupUI.TFA_setup_confirmAnswer_lineEdit.clear()

    def clear_all_fields(self): # Clears all inputs
        self.clear_create_username()
        self.clear_create_password()
        self.clear_confirm_password()
        self.clear_create_answer()
        self.clear_confirm_answer()

    def are_fields_empty(self): # checks to see if any inputs are missing
        self.username_input = self.SignupUI.create_username_lineEdit.text().strip()
        self.password_input = self.SignupUI.create_password_lineEdit.text()
        self.password_confirmation = self.SignupUI.confirm_password_lineEdit.text()
        self.user_TFA_option = int(self.tfa_buttons.checkedId())
        self.user_TFA_selection = self.user_TFA_questions.get(self.user_TFA_option)
        self.user_answer = self.SignupUI.TFA_setup_answer_lineEdit.text()
        self.answer_confirmation = self.SignupUI.TFA_setup_confirmAnswer_lineEdit.text()

        if all([self.username_input, self.password_input, self.password_confirmation,
                self.user_TFA_selection, self.user_answer, self.answer_confirmation]): # if all values exist
            if self.username_input == self.password_input: # Username and password cannot be the same
                self.SignupUI.username_AE_textBrowser.show()
                self.SignupUI.username_AE_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Username and password cannot equal.</font>')
            elif self.username_input == self.user_answer: # Username and TFA answer cannot be the same
                self.SignupUI.answers_DNM_textBrowser.show()
                self.SignupUI.answers_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Username and TFA answer cannot equal.</font>')
            elif self.password_input == self.user_answer: # Password and TFA answer cannot be the same
                self.SignupUI.username_AE_textBrowser.hide()
                self.SignupUI.answers_DNM_textBrowser.show()
                self.SignupUI.answers_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Password and TFA answer cannot equal.</font>')
            else:
                self.SignupUI.username_AE_textBrowser.hide()
                self.SignupUI.password_DNM_textBrowser.hide()
                self.SignupUI.answers_DNM_textBrowser.hide()
                self.does_username_exist()
        else: # if one or more of the values are missing
            if not self.username_input: # no username provided
                self.SignupUI.username_AE_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Please put in a username.</font>')
                self.SignupUI.username_AE_textBrowser.show()
            if not self.password_input or not self.password_confirmation: # if password is not entered or confirmed
                self.SignupUI.password_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Please choose and confirm password.</font>')
                self.SignupUI.password_DNM_textBrowser.show()
            if not all([self.user_TFA_selection, self.user_answer, self.answer_confirmation]): # if TFA isn't filled in
                self.SignupUI.answers_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Please finish filling this field.</font>')
                self.SignupUI.answers_DNM_textBrowser.show()

    def does_username_exist(self):
        self.username_found = False

        if os.path.exists(userInfo_file):
            with open(userInfo_file, "r") as info:
                contents = csv.reader(info)
                for content in contents:
                    if not any(content):
                        pass
                    else:
                        if self.username_input == content[0]: # if the username already exists
                            self.SignupUI.username_AE_textBrowser.show()
                            self.username_found = True
                            break
                        else:
                            self.username_found = False
                            continue
        if self.username_found == False:
            self.SignupUI.username_AE_textBrowser.hide()
            self.password_match()

    def password_match(self):
        # at least one special character, two digits, and one capital letter are required in a password
        self.special_chars = "\"!.?<>=+-*/%$'@&#_~^\\" # all the special characters allowed
        self.nums = "1234567890" # digit values
        self.caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # capital letters

        if self.password_input != self.password_confirmation: # if the password inputs do not match
            self.SignupUI.password_DNM_textBrowser.show()
            self.SignupUI.password_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;Passwords do not match or are invalid.</font>')
            self.SignupUI.username_AE_textBrowser.hide()
        elif "Password" in self.password_input: # password cannot contain "Password"
            self.SignupUI.password_DNM_textBrowser.show()
            self.SignupUI.password_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Password cannot contain "Password".</font>')
        elif "password" in self.password_input: # password cannot contain "password"
            self.SignupUI.password_DNM_textBrowser.show()
            self.SignupUI.password_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Password cannot contain "password".</font>')
        elif " " in self.password_input: # password cannot contain any whitespace
            self.SignupUI.password_DNM_textBrowser.show()
            self.SignupUI.password_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Password cannot contain whitespace.</font>')
        else:
            if len(self.password_input) > 7: # minimum password length is 8 characters
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
                    self.SignupUI.password_DNM_textBrowser.hide()
                    self.check_TFA()
                else:
                    self.SignupUI.password_DNM_textBrowser.show()
                    self.SignupUI.password_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Password does not meet criteria.</font>')

    def check_TFA(self):
        if self.user_answer != self.answer_confirmation: # if TFA answer inputs do not match
            self.SignupUI.answers_DNM_textBrowser.show()
            self.SignupUI.answers_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Answers do not match. Please re-enter".</font>')
        elif "Answer" in self.user_answer: # answer cannot contain "Answer"
            self.SignupUI.answers_DNM_textBrowser.show()
            self.SignupUI.answers_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Answer cannot contain "Answer".</font>')
        elif "answer" in self.user_answer: # answer cannot contain "answer"
            self.SignupUI.answers_DNM_textBrowser.show()
            self.SignupUI.answers_DNM_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Answer cannot contain "answer".</font>')
        else:
            if len(self.user_answer) > 3: # answer must be at least 5 characters in length
                self.SignupUI.answers_DNM_textBrowser.hide()
                self.account_creation()

    def account_creation(self): # adds user information to the userInfo.csv file
        self.new_account_info = [self.username_input, self.password_input, self.user_TFA_selection, self.user_answer]
        with open(userInfo_file, "a+") as accounts:
            try:
                accounts.seek(0)
                self.reader = csv.reader(accounts)
                self.appender = csv.writer(accounts)
                first_line = None
                try:
                    first_line = next(self.reader)
                except:
                    pass

                if not first_line:
                    self.appender.writerow(["User", "Password", "Question", "Answer", "Status"])

                self.appender.writerow(self.new_account_info)
            except Exception:
                print(Exception)
                pass
        self.sign_in()

    def sign_in(self):
        self.clear_create_username()
        self.clear_create_password()
        self.clear_confirm_password()
        self.clear_create_answer()
        self.clear_confirm_answer()
        self.SignupUI.username_AE_textBrowser.hide()
        self.SignupUI.password_DNM_textBrowser.hide()
        self.SignupUI.answers_DNM_textBrowser.hide()
        self.hide()  # Resets the sign-up page
        storage_window.show()

class LoginPage(QMainWindow):
    def __init__(self):
       super(LoginPage, self).__init__()
       self.LoginUI = Ui_LoginWindow()
       self.LoginUI.setupUi(self)

       # These will appear if username or password are not properly provided
       self.LoginUI.username_alert_textBrowser.hide()
       self.LoginUI.password_alert_textBrowser.hide()

       # TFA (will appear after an existing username and its password are correctly entered.)
       self.LoginUI.loginTFA_label.hide()
       self.LoginUI.userChosen_question_textBrowser.hide()
       self.LoginUI.TFA_lineEdit.hide()
       self.LoginUI.loginTFA_confirm_pushButton.hide()
       self.LoginUI.incorrect_answer_textBrowser.hide()

       # clear buttons
       self.LoginUI.username_clear_pushButton.clicked.connect(self.clear_username)
       self.LoginUI.password_clear_pushButton.clicked.connect(self.clear_password)

       # confirm buttons
       self.LoginUI.continue_pushButton.clicked.connect(self.attempt_continue)
       self.LoginUI.loginTFA_confirm_pushButton.clicked.connect(self.answer_check)

       # alternate to the signup page
       self.LoginUI.create_account_pushButton.clicked.connect(self.create_account)

    def create_account(self):
        # clear all inputs and hide any messages associated with them
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
        # collect text from entry boxes
        self.username =  self.LoginUI.username_lineEdit.text()
        self.password =  self.LoginUI.password_lineEdit.text()

        if not self.username: # if no username is provided
            self.LoginUI.username_alert_textBrowser.show()
            self.LoginUI.username_alert_textBrowser.setText("Please provide a username.")
        else:
            self.LoginUI.username_alert_textBrowser.hide()

        if not self.password:  # if no password is provided
            self.LoginUI.password_alert_textBrowser.show()
            self.LoginUI.password_alert_textBrowser.setText("Please provide a password.")
        else:
            self.LoginUI.password_alert_textBrowser.hide()

        if self.username and self.password:  # if a username and password are provided
            try:
                with open(userInfo_file, "r") as userInfo:
                    self.contents = csv.reader(userInfo, delimiter=",")
                    for content in self.contents:
                        if content[0] == self.username and content[1] == self.password: # if username and password are correct
                            self.TFA_question = content[2]
                            self.TFA_answer = content[3]
                            self.LoginUI.username_alert_textBrowser.hide()
                            self.LoginUI.password_alert_textBrowser.hide()
                            self.two_factor_authentication()
                            break
                        elif content[0] == self.username: # if a real username is provided but the password is incorrect
                            self.LoginUI.username_alert_textBrowser.hide()
                            self.LoginUI.password_alert_textBrowser.show()
                            self.LoginUI.password_alert_textBrowser.setText("Incorrect password.")
                            break
                        else: # will execute if the username does not exist
                            self.LoginUI.password_alert_textBrowser.hide()
                            self.LoginUI.username_alert_textBrowser.show()
                            self.LoginUI.username_alert_textBrowser.setText("Username does not exist.")

            except FileNotFoundError: # if the file does not exist, this means no accounts are available to be logged into
                    self.LoginUI.username_alert_textBrowser.show()
                    self.LoginUI.username_alert_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Congratulations!</font>')
                    self.LoginUI.password_alert_textBrowser.show()
                    self.LoginUI.password_alert_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">You are our first user!</font>')
                    self.LoginUI.incorrect_answer_textBrowser.show()
                    self.LoginUI.incorrect_answer_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Please alternate to the signup page.</font>')
        else: # if the user enters a correct username and password but then deletes them and tries to continue
            self.LoginUI.loginTFA_label.hide()
            self.LoginUI.userChosen_question_textBrowser.hide()
            self.LoginUI.TFA_lineEdit.hide()
            self.LoginUI.loginTFA_confirm_pushButton.hide()

    def two_factor_authentication(self):
        self.LoginUI.userChosen_question_textBrowser.setText(self.TFA_question)
        self.LoginUI.loginTFA_label.show()
        self.LoginUI.userChosen_question_textBrowser.show()
        self.LoginUI.TFA_lineEdit.show()
        self.LoginUI.loginTFA_confirm_pushButton.show()

    def answer_check(self):
        self.user_answer = self.LoginUI.TFA_lineEdit.text()
        if self.user_answer == self.TFA_answer:
           self.LoginUI.incorrect_answer_textBrowser.hide()
           self.find_user_profile()
        else: # if incorrect answer is provided
           self.LoginUI.incorrect_answer_textBrowser.show()
           self.LoginUI.incorrect_answer_textBrowser.setHtml('<font color="#9c1c1c" style="text-align: center;">Answer is not correct.</font>')

    def find_user_profile(self):
        try:
            with open(userStorage_file, "r") as find_user:
                self.user_locator = csv.reader(find_user)
                for line in self.user_locator:
                    if self.username == line[0]:
                        self.profile_data = line
                        storage_window.retrieve_data(self.username, self.profile_data)
                        storage_window.display_data()
                        self.hide()
                        storage_window.show()
        except FileNotFoundError:
           # create the file if it does not exist
           with open(userStorage_file, "w") as storage:
              writer = csv.writer(storage)
              writer.writerow(["Username","Total item types","Total quantity","Item 1","Quantity 1",
                               "Item 2","Quantity 2","Item 3","Quantity 3","Item 4","Quantity 4",
                               "Item 5","Quantity 5","Item 6","Quantity 6","Item 7","Quantity 7",
                               "Item 8","Quantity 8","Item 9","Quantity 9","Item 10","Quantity 10"])

class StoragePage(QMainWindow):
    def __init__(self):
        super(StoragePage, self).__init__()
        self.StorageUI = Ui_UserStorageWindow()
        self.StorageUI.setupUi(self)

        self.logout_cancel()

        self.StorageUI.transaction_history_textBrowser.hide()
        self.StorageUI.item_history_label.hide()
        self.StorageUI.transaction_label.hide()
        self.StorageUI.transaction_quantity_label.hide()

        self.StorageUI.alert_textBrowser.hide()


        self.operation_buttons = QButtonGroup(self)
        self.operation_buttons.addButton(self.StorageUI.deposit_radioButton, 1)
        self.operation_buttons.addButton(self.StorageUI.withdraw_radioButton, 2)
        self.operation_buttons.addButton(self.StorageUI.transHist_radioButton, 3)
        self.operation_buttons.addButton(self.StorageUI.clearStorage_radioButton, 4)

        self.transaction_types = {
            1: self.deposit,
            2: self.withdraw,
            3: self.view_history,
            4: self.clear_contents
        }

        self.StorageUI.log_out_pushButton.clicked.connect(self.logout_check)
        self.StorageUI.confirm_logout_pushButton.clicked.connect(self.logout_confirm)
        self.StorageUI.cancel_logout_pushButton.clicked.connect(self.logout_cancel)

        self.StorageUI.confirm_pushButton.clicked.connect(self.check_inputs)

    def logout_check(self):
        self.StorageUI.log_out_pushButton.hide()
        self.StorageUI.confirm_logout_pushButton.show()
        self.StorageUI.cancel_logout_pushButton.show()
        self.StorageUI.logout_question_label.show()

    def logout_confirm(self):
        login_window.clear_username()
        login_window.clear_password()
        login_window.LoginUI.TFA_lineEdit.clear()
        login_window.LoginUI.userChosen_question_textBrowser.clear()

        login_window.LoginUI.loginTFA_label.hide()
        login_window.LoginUI.userChosen_question_textBrowser.hide()
        login_window.LoginUI.TFA_lineEdit.hide()
        login_window.LoginUI.loginTFA_confirm_pushButton.hide()
        login_window.LoginUI.incorrect_answer_textBrowser.hide()

        self.hide()
        start_window.show()

    def logout_cancel(self):
        self.StorageUI.log_out_pushButton.show()
        self.StorageUI.logout_question_label.hide()
        self.StorageUI.confirm_logout_pushButton.hide()
        self.StorageUI.cancel_logout_pushButton.hide()

    def retrieve_data(self, username, data):
        self.user = username
        self.user_data = data

    def display_data(self):
        self.storage_lines = []
        with open(userStorage_file, "r") as storage:
            storage_reader = csv.reader(storage)
            for line in storage_reader:
                self.storage_lines.append(line)
                if line[0] == self.user:
                    self.StorageUI.hello_user_label.setText(f"Hello, {self.user}!")

                    self.profile_contents = {}
                    self.total_quant = 0
                    self.browser_contents = ""

                    for i in range(3, len(line), 2):
                        item = line[i]
                        quantity = line[i + 1]
                        try:
                            quantity = int(line[i + 1])
                        except ValueError:
                            quantity = 0
                        self.profile_contents[item] = quantity

                    for key, value in self.profile_contents.items():
                        self.browser_contents += f"{key} \t{value}\n"
                        self.total_quant += value

                    self.browser_contents += f"\nTotal: \t{self.total_quant}"
                    self.StorageUI.account_contents_textBrowser.setText(self.browser_contents)

    def check_inputs(self):
        try:
            self.user_item = self.StorageUI.item_lineEdit.text().strip()
            self.user_quantity = self.StorageUI.quantity_lineEdit.text().strip()

            if not self.user_quantity:
                self.user_quantity = None
            else:
                try:
                    self.user_quantity = int(self.user_quantity)
                except ValueError:
                    self.user_quantity = None
                    self.StorageUI.alert_textBrowser.show()
                    self.StorageUI.alert_textBrowser.setHtml("<p align=\"center\" style=\"margin: 0; font-size: 8pt; color: #9c1c1c;\">"
                        "Quantity must be an integer value.</p>")
                    return

            self.selected_operation = self.operation_buttons.checkedId()
            self.selected_transaction = self.transaction_types.get(self.selected_operation)

            if self.selected_operation == -1:
                self.StorageUI.alert_textBrowser.show()
                self.StorageUI.alert_textBrowser.setHtml("<p align=\"center\" style=\"margin: 0; font-size: 8pt; color: #9c1c1c;\">"
                    "Please choose an operation.</p>")
                return

            if self.selected_operation in [3, 4]:
                if self.selected_transaction:
                    self.selected_transaction()

            if not self.user_item:
                self.StorageUI.alert_textBrowser.show()
                self.StorageUI.alert_textBrowser.setHtml("<p align=\"center\" style=\"margin: 0; font-size: 8pt; color: #9c1c1c;\">"
                    "Must provide an item.</p>")
            elif self.user_quantity is None:
                self.StorageUI.alert_textBrowser.show()
                self.StorageUI.alert_textBrowser.setHtml("<p align=\"center\" style=\"margin: 0; font-size: 8pt; color: #9c1c1c;\">"
                    "Must provide a quantity of items.</p>")
            else:
                self.StorageUI.alert_textBrowser.hide()
                if self.selected_transaction:
                    self.selected_transaction(self.user_item, self.user_quantity)
                else:
                    self.StorageUI.alert_textBrowser.show()
                    self.StorageUI.alert_textBrowser.setHtml("<p align=\"center\" style=\"margin: 0; font-size: 8pt; color: #9c1c1c;\">"
                                                 "Must choose an operation.</p>")
        except Exception as e:
            print(f"Error: {e}")
            self.StorageUI.alert_textBrowser.show()
            self.StorageUI.alert_textBrowser.setHtml("<p align=\"center\" style=\"margin: 0; font-size: 8pt; color: #9c1c1c;\">"
                "An error occurred. Please try again.</p>")

    def deposit(self, object, count):
        self.user_transaction = "Deposit"
        if self.total_quant >= 50:
            self.StorageUI.alert_textBrowser.show()
            self.StorageUI.alert_textBrowser.setHtml("<p align=\"center\" style=\"margin: 0; font-size: 8pt; color: #9c1c1c;\">"
                "Account is full. Please withdraw items or create an additional account.</p>")

        elif count + self.total_quant >= 50:
            self.StorageUI.alert_textBrowser.show()
            self.StorageUI.alert_textBrowser.setHtml("<p align=\"center\" style=\"margin: 0; font-size: 8pt; color: #9c1c1c;\">"
                "Not enough room in account.</p>")

        elif len(self.profile_contents) >= 10:
            if object in self.profile_contents:
                self.profile_contents[object] += count
                self.StorageUI.alert_textBrowser.show()
                self.StorageUI.alert_textBrowser.setText(f"x{count} {object}(s) deposited!")
            else:
                self.StorageUI.alert_textBrowser.show()
                self.StorageUI.alert_textBrowser.setHtml("<p align=\"center\" style=\"margin: 0; font-size: 8pt; color: #9c1c1c;\">"
                    "Can only hold ten types of items.</p>")
        else:
            if self.user_item in self.profile_contents:
                self.profile_contents[object] += count
            else:
                self.profile_contents[object] = count

            self.update_storage()

            self.StorageUI.alert_textBrowser.show()
            self.StorageUI.alert_textBrowser.setText(f"x{count} {object}(s) deposited!")

    def withdraw(self, object, count):
        self.user_transaction = "Withdrawal"
        if object not in self.profile_contents:
            self.StorageUI.alert_textBrowser.show()
            self.StorageUI.alert_textBrowser.setHtml("<p align=\"center\" style=\"margin: 0; font-size: 8pt; color: #9c1c1c;\">"
                "Item not found.</p>")
        elif self.profile_contents[object] - count < 0:
            self.StorageUI.alert_textBrowser.show()
            self.StorageUI.alert_textBrowser.setHtml("<p align=\"center\" style=\"margin: 0; font-size: 8pt; color: #9c1c1c;\">"
                "Insufficient items to withdraw. Please adjust the quantity.</p>")
        elif len(self.profile_contents) == 0:
            self.StorageUI.alert_textBrowser.show()
            self.StorageUI.alert_textBrowser.setHtml("<p align=\"center\" style=\"margin: 0; font-size: 8pt; color: #9c1c1c;\">"
                "Account is currently empty. Cannot withdraw.</p>")
        else:
            self.profile_contents[object] -= count
            self.StorageUI.alert_textBrowser.show()
            self.StorageUI.alert_textBrowser.setText(f"x{count} {object}(s) withdrawn!")

            self.update_storage()
            self.write_history(self.user_transaction, object, count)

    def view_history(self):
        self.StorageUI.transaction_label.show()
        self.StorageUI.item_history_label.show()
        self.StorageUI.transaction_quantity_label.show()

        try:
            self.StorageUI.alert_textBrowser.hide()
            self.user_history_lines = []
            self.history = ""
            with open(accountHistory_file, "r") as hist:
                self.hist_reader = csv.reader(hist)
                for line in self.hist_reader:
                    if line[0] == self.user:
                        self.user_history_lines.append(line)
                for line in self.user_history_lines:
                    self.transaction = line[1]
                    self.transaction_item = line[2]
                    self.transaction_quantity = line[3]
                    self.history += f"{self.transaction}\t{self.transaction_item}\t{self.transaction_quantity}"
                self.StorageUI.transaction_history_textBrowser.show()
                self.StorageUI.transaction_history_textBrowser.setText(self.history)
        except FileNotFoundError:
            with open(accountHistory_file, "w") as user_hist:
                hist_writer = csv.writer(user_hist)
                hist_writer.writerow(["Username", "Transaction type", "Item", "Quantity"])

    def clear_contents(self): # empties the user's account
        self.user_transaction = "Clear"
        try:
            if len(self.profile_contents) != 0:
                self.lines = []
                with open(userStorage_file, "r") as content:
                    self.reader = csv.reader(content)
                    for line in self.reader:
                        if line[0] != self.user:
                            self.lines.append(line)
                        else:
                            self.items_cleared = line[2]
                            line = [self.user, 0, 0]
                            self.lines.append(line)
                with open(userStorage_file, "w", newline="") as content:
                    self.writer = csv.writer(content)
                    self.writer.writerows(self.lines)

                self.write_history(self.user_transaction, "All", self.items_cleared)

            else:
                self.StorageUI.alert_textBrowser.show()
                self.StorageUI.alert_textBrowser.setHtml("<p align=\"center\" style=\"margin: 0; font-size: 8pt; color: #9c1c1c;\">"
                    "Your account is empty.</p>")
        except FileNotFoundError:
            self.StorageUI.alert_textBrowser.show()
            self.StorageUI.alert_textBrowser.setHtml("<p align=\"center\" style=\"margin: 0; font-size: 8pt; color: #9c1c1c;\">"
                "Your account is empty.</p>")

    def update_storage(self):
        self.lines = []
        with open(userStorage_file, "r") as storage:
            self.reader = csv.reader(storage)
            for line in self.reader:
                if line[0] == self.user:
                    self.updated_line = [self.user] + self.profile_contents
                    self.lines.append(updated_line)
                else:
                    self.lines.append(line)
        with open(userStorage_file, "w", newline="") as storage:
            self.writer = csv.writer(storage)
            self.writer.writerows(lines)

    def write_history(self, transaction, object, count):
        try: # check if file exists
            with open(accountHistory_file, "a") as user_hist:
                hist_appender = csv.writer(user_hist)
                hist_appender.writerow([self.user, transaction, object, count])
        except FileNotFoundError: # create file
            with open(accountHistory_file, "w") as user_hist:
                hist_writer = csv.writer(user_hist)
                hist_writer.writerow(["Username","Transaction type","Item","Quantity"])
                hist_writer.writerow([self.user, transaction, object, count])


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
