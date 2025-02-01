from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget, QLineEdit
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QPixmap
from Login.login_ui_form import Ui_LoginWindow
import db_man_projectv3_test
from package.Initializer import ManagerInitializer, EmployeeInitializer, LoginInitializer
from Manager_Side.manager_test import ManagerApp
from Employee_Side.employee_test import EmployeeApp
from package import StandardMessageBox, CommonFeatures
from package.Wrapper import errorCatcher

class LoginApp(QtWidgets.QMainWindow, Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Store icons for connected, disconnected, and not controlled
        self.connectedIcon = QPixmap(":/newSource/icons/green_dot.png")
        self.disconnectedIcon = QPixmap(":/newSource/icons/red_dot.png")
        self.notControlledIcon = QPixmap(":/newSource/icons/white_dot.png")

        LoginInitializer.initializeLogin(self)

        self.current_page : QWidget = None
    
    @pyqtSlot(bool)
    def on_action_toggled(self, checked):
        action = self.sender()
        if checked:
            if action.text() == "Never":
                self.timer.stop()
                self.lbl_connection_icon.setPixmap(self.notControlledIcon)
                self.lbl_connection_status.setText("Not Controlled!")
            else:
                self.time_period = int(action.text()[0:action.text().find(" ")].strip()) * 1000
                self.timer.start(self.time_period)
    
    def restart_request(self):
        print("Restart requested!")
    
    def clear_all_lineEdits(self):
        line_edits = self.findChildren(QLineEdit)
        for line_edit in line_edits:
            line_edit.clear()
    
    def adjustEmailStatus(self) -> None:
        CommonFeatures.adjustEmailStatus(self)
    
    def loadResetPasswordStep1(self):
        self.lineEdit_email_page_reset.clear()
        self.stackedWidget.setCurrentWidget(self.page_reset_password)

    @errorCatcher    
    def loadResetPasswordStep2(self):
        if len(self.lineEdit_email_page_reset.text()) == 0:
            StandardMessageBox.Warning(self, "Error", "Provide your email address that exists in the system!").exec()
        elif CommonFeatures.verify_email_pattern(self.lineEdit_email_page_reset.text()) == False:
            StandardMessageBox.Warning(self, "Error", "The email address provided is not in a valid format!").exec()
        else:
            msg = db_man_projectv3_test.send_verification_code(self.lineEdit_email_page_reset.text())
            if isinstance(msg, int):
                self.verification_code = msg
                self.lineEdit_passcode.clear()
                self.lineEdit_new_password.clear()
                self.lineEdit_confirm_password.clear()
                self.stackedWidget.setCurrentWidget(self.page_reset_password_step2)
            elif isinstance(msg, str):
                StandardMessageBox.Error(self, "Error", msg).exec()
            else:
                errMsg = f"An unhandled case has occurred! Func: 'loadResetPasswordStep2' | msg: '{msg}' | Type: {type(msg)}"
                StandardMessageBox.Error(self, "Unhandled Case Error", errMsg).exec()
    
    def loadLoginPage(self):
        self.lineEdit_email_page_login.clear()
        self.lineEdit_password_page_login.clear()
        self.stackedWidget.setCurrentWidget(self.page_login)
    
    def changePasswordEchoMode(self):
        item : QLineEdit = None
        if self.stackedWidget.currentWidget() == self.page_login:
            item = self.lineEdit_password_page_login
        
        elif self.stackedWidget.currentWidget() == self.page_reset_password_step2:
            item = self.lineEdit_new_password
        
        else:
            errMsg = f"Current widget is not suitable for 'changePasswordEchoMode'! CW: {self.stackedWidget.currentWidget()}"
            StandardMessageBox.Error(self, "Error", errMsg).exec()
        
        currentEchoMode = item.echoMode()
        if currentEchoMode == QLineEdit.EchoMode.Password:
            newMode = QLineEdit.EchoMode.Normal
        else:
            newMode = QLineEdit.EchoMode.Password

        item.setEchoMode(newMode)
        if self.stackedWidget.currentWidget() == self.page_reset_password_step2:
            self.lineEdit_confirm_password.setEchoMode(newMode)

    @errorCatcher    
    def completeResetPassword(self):
        connection, msg = db_man_projectv3_test.connection_check()
        if connection != True:
            StandardMessageBox.Error(self, "DB Connection Error", f"Database connection could not be established! Try again! -> {msg}").exec()

            # Do not go further
            return
        
        relevantTextBoxes = [self.lineEdit_passcode, self.lineEdit_new_password, self.lineEdit_confirm_password]
        for textBox in relevantTextBoxes:
            if len(textBox.text()) == 0 or textBox.text().isspace():
                StandardMessageBox.Warning(self, "Missing Information Error", "Please fill in all required fields to proceed.").exec()

                # Do not go further
                return
        
        if not (self.lineEdit_new_password.text() == self.lineEdit_confirm_password.text()):
            StandardMessageBox.Warning(self, "Mismatched Confirmation", "Your new password do not match with your confirmation!").exec()

            # Do not go further
            return

        res = db_man_projectv3_test.reset_change_password(new_password=self.lineEdit_new_password.text(),
                                                    entered_code=int(self.lineEdit_passcode.text()),
                                                    verification_code=self.verification_code,
                                                    user_email=self.lineEdit_email_page_reset.text())
        if res == True:
            StandardMessageBox.Successful(self, reload = None).exec()
            self.stackedWidget.setCurrentWidget(self.page_login)
        
        elif res == False:
            StandardMessageBox.Warning(self, "OTP Error", "One-time-password is wrong! Try again or get a new one.").exec()
        
        elif isinstance(res, str):
            StandardMessageBox.Error(self, "Error", f"An error occurred during password resetting! -> {res}").exec()
        
        else:
            errMsg = f"An unhandled case has occurred! Func: 'completeResetPassword' | res: '{res}' | Type: {type(res)}"
            StandardMessageBox.Error(self, "Unhandled Case Error", errMsg).exec()
        
        # Clear password-related input boxes
        self.lineEdit_new_password.clear()
        self.lineEdit_confirm_password.clear()
    
    def directToFromAboutPage(self):
        if not self.stackedWidget.currentWidget() == self.page_about:
            self.current_page = self.stackedWidget.currentWidget()
            self.lineEdit_email_page_login.clear()
            self.lineEdit_password_page_login.clear()
            self.stackedWidget.setCurrentWidget(self.page_about)
            self.btn_contact_back.setText("Back")
            self.lbl_contact_msg.setVisible(False)
        else:
            self.stackedWidget.setCurrentWidget(self.current_page)
            self.btn_contact_back.setText("Click here!")
            self.lbl_contact_msg.setVisible(True)
            self.current_page = None
    
    @errorCatcher    
    def login(self):
        connection, msg = db_man_projectv3_test.connection_check()
        if connection != True:
            StandardMessageBox.Error(self, "DB Connection Error", f"Database connection could not be established! Try again! -> {msg}").exec()
            return
        
        relevantTextBoxes = [self.lineEdit_email_page_login, self.lineEdit_password_page_login]
        for textBox in relevantTextBoxes:
            if len(textBox.text()) == 0 or textBox.text().isspace():
                StandardMessageBox.Warning(self, "Missing Information Error", "Please fill in all required fields to proceed.").exec()

                # Do not go further
                return
            
        if CommonFeatures.verify_email_pattern(self.lineEdit_email_page_login.text()) == False:
            StandardMessageBox.Warning(self, "Email Pattern Error", "The email address provided is not in a valid format!").exec()
            return
        
        res = db_man_projectv3_test.login(email=self.lineEdit_email_page_login.text(),
                                    password=self.lineEdit_password_page_login.text())
        
        if res == None:
            StandardMessageBox.Warning(self, "Login Failed", "Mail address or password is wrong!").exec()

            # Clear password input box
            self.lineEdit_password_page_login.clear()

            # Do not go further
            return
        
        elif isinstance(res, tuple):
            role, empID, name, surname = res
            if role == "Human resources":
                self.main_form_2 = ManagerApp(empId=int(empID), name = name, surname = surname, role = role)
                ManagerInitializer.initializeManager(self.main_form_2)
                self.main_form_2.show()
                self.close()
            else:
                self.main_form_2 = EmployeeApp(empId=int(empID), name = name, surname = surname, role = role)
                EmployeeInitializer.initializeEmployee(self.main_form_2)
                self.main_form_2.show()
                self.close()
        
        else:
            StandardMessageBox.Error(self, "Login Failed", f"An error occurred during login! Please try again! -> {res} | {type(res)}").exec()
            return

    @errorCatcher    
    def updateConnectionStatus(self):
        CommonFeatures.updateConnectionStatus(self)
    
    @errorCatcher    
    def resendPassword(self):
        msg = db_man_projectv3_test.send_verification_code(self.lineEdit_email_page_reset.text())

        if isinstance(msg, int):
            self.verification_code = msg
            StandardMessageBox.Information(self, "Resend OTP", "Your new one-time-password has been sent to your email address!").exec()
            self.lineEdit_passcode.clear()
        
        elif isinstance(msg, str):
            StandardMessageBox.Error(self, "Error", msg).exec()
        
        else:
            errMsg = f"An unhandled case has occurred! Func: 'resendPassword' | msg: '{msg}' | Type: {type(msg)}"
            StandardMessageBox.Error(self, "Unhandled Case Error", errMsg).exec()
    
    def closeEvent(self, event):
        super().closeEvent(event)


if __name__ == "__main__":
    raise RuntimeError("Do not run this file as main!")


# END