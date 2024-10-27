from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import QPixmap
from login_form_new import Ui_MainWindow
import hs_managementv3

class LoginApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.current_page : QWidget = None

        # Set max lengths of inputs on UI
        self.lineEdit_email_page_login.setMaxLength(50)
        self.lineEdit_email_page_reset.setMaxLength(50)
        self.lineEdit_password_page_login.setMaxLength(50)
        self.lineEdit_new_password.setMaxLength(50)
        self.lineEdit_confirm_password.setMaxLength(50)
        self.lineEdit_passcode.setMaxLength(6)

        # Connect functions to input items on UI
        self.btn_forgot_password.clicked.connect(self.loadResetPasswordStep1)
        self.checkBox_show_password_page_login.checkStateChanged.connect(self.changePasswordEchoMode)
        self.btn_contact_back.clicked.connect(self.directToFromAboutPage)
        self.btn_cancel_page_reset.clicked.connect(self.loadLoginPage)
        self.btn_send_code.clicked.connect(self.loadResetPasswordStep2)
        self.btn_back_reset_step2.clicked.connect(self.loadResetPasswordStep1)
        self.btn_cancel_5.clicked.connect(self.loadLoginPage)
        self.btn_complete.clicked.connect(self.completeResetPassword)
        self.checkBox_show_password_reset_step2.clicked.connect(self.changePasswordEchoMode)
        self.btn_login.clicked.connect(self.login)
        self.btn_resend_code.clicked.connect(self.resendPassword)

        # Set a timer for connection check
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateConnectionStatus)
        self.timer.start(2000)
        
        # Set initial connection status
        self.updateConnectionStatus()
    
    def loadResetPasswordStep1(self):
        self.lineEdit_email_page_reset.clear()
        self.stackedWidget.setCurrentWidget(self.page_reset_password)
    
    def loadResetPasswordStep2(self):
        if len(self.lineEdit_email_page_reset.text()) == 0:
            self.showDialog("Warning", "Provide your email address that exists in the system!", "Email Error")
        else:
            msg = hs_managementv3.send_verification_code(self.lineEdit_email_page_reset.text())
            if isinstance(msg, int):
                self.verification_code = msg
            elif isinstance(msg, str):
                self.showDialog("Critical", msg, "Error")
            else:
                self.lineEdit_passcode.clear()
                self.lineEdit_new_password.clear()
                self.lineEdit_confirm_password.clear()
                self.stackedWidget.setCurrentWidget(self.page_reset_password_step2)
    
    def loadLoginPage(self):
        self.lineEdit_email_page_login.clear()
        self.lineEdit_password_page_login.clear()
        self.stackedWidget.setCurrentWidget(self.page_login)
    
    def changePasswordEchoMode(self):
        item = None
        if self.stackedWidget.currentWidget() == self.page_login:
            item = self.lineEdit_password_page_login
        
        elif self.stackedWidget.currentWidget() == self.page_reset_password_step2:
            item = self.lineEdit_new_password
        
        currentEchoMode = item.echoMode()
        if currentEchoMode == QLineEdit.EchoMode.Password:
            newMode = QLineEdit.EchoMode.Normal
        else:
            newMode = QLineEdit.EchoMode.Password

        item.setEchoMode(newMode)
        if self.stackedWidget.currentWidget() == self.page_reset_password_step2:
            self.lineEdit_confirm_password.setEchoMode(newMode)
    
    def completeResetPassword(self):
        connection, msg = hs_managementv3.connection_check()
        if connection != True:
            self.showDialog("Error", f"Database connection could not be established! Try again! -> {msg}", "DB Connection Error")
        elif len(self.lineEdit_passcode.text()) != 6 or self.lineEdit_passcode.text().isspace():
            self.showDialog("Error", "6-digit passcode must be provided!", title="Passcode Error")
        elif len(self.lineEdit_new_password.text()) == 0 or self.lineEdit_new_password.text().isspace():
            self.showDialog("Warning", "Set a new password!", title="New Password Error")
        elif len(self.lineEdit_confirm_password.text()) == 0 or self.lineEdit_confirm_password.text().isspace():
            self.showDialog("Warning", "Confirm your new password!", title="Password Confirmation Error")
        elif not (self.lineEdit_new_password.text() == self.lineEdit_confirm_password.text()):
            self.showDialog("Warning", "Your new password do not match with your confirmation!", title="Mismatched confirmation")
        else:
            res = hs_managementv3.reset_change_password(new_password=self.lineEdit_new_password.text(),
                                                        entered_code=self.lineEdit_passcode.text(),
                                                        verification_code=self.verification_code,
                                                        user_email=self.lineEdit_email_page_reset.text())
            if res == True:
                self.showDialog("Information", "Your password has been changed successfully!", "Information")
                self.stackedWidget.setCurrentWidget(self.page_login)
            elif res == False:
                self.showDialog("Warning", "One-time-password is wrong! Try again or get a new one.", "OTP Error")
            elif isinstance(res, str):
                self.showDialog("Error", "An error occurred during password resetting!", "Error")
    
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
    
    def login(self):
        connection, msg = hs_managementv3.connection_check()
        if connection != True:
             self.showDialog("Error", f"Database connection could not be established! Try again! -> {msg}", "DB Connection Error")
        elif len(self.lineEdit_email_page_login.text()) == 0 or self.lineEdit_email_page_login.text().isspace():
            self.showDialog("Warning", "Provide your email address!", "Error")
        elif len(self.lineEdit_password_page_login.text()) == 0 or self.lineEdit_password_page_login.text().isspace():
            self.showDialog("Warning", "Provide your password!", "Error")
        else:
            res = hs_managementv3.login(email=self.lineEdit_email_page_login.text(),
                                        password=self.lineEdit_password_page_login)
            if res == None:
                self.showDialog("Warning", "Mail address or password is wrong!", "Login Failed")
            elif res == "Human Resources" or res == "Employee":
                self.showDialog("Information", f"{res}", "Login Successful")
            else:
                self.showDialog("Error", "An error occurred during login! Please try again!", "Login Failed")
    
    def updateConnectionStatus(self):
        connection, msg = hs_managementv3.connection_check()
        if connection == True:
            self.lbl_connection_icon.setPixmap(QPixmap(r"icons/white_dot.png"))
            self.lbl_connection_status.setText("Connected")
        elif connection == False:
            self.lbl_connection_icon.setPixmap(QPixmap(r"icons/red_dot.png"))
            self.lbl_connection_status.setText("Not connected")
        else:
            self.showDialog("Critical", "An error occurred during database connection check!", "Connection Check Error")
    
    def resendPassword(self):
        msg = hs_managementv3.send_verification_code(self.lineEdit_email_page_reset.text())
        if isinstance(msg, int):
            self.verification_code = msg
        elif isinstance(msg, str):
            self.showDialog("Critical", msg, "Error")
    
    def showDialog(self, dialog_type:str, text:str, title:str = "Error"):
        if dialog_type == "Error":
            icon = QMessageBox.Icon.Critical
        elif dialog_type == "Warning":
            icon = QMessageBox.Icon.Warning
        elif dialog_type == "Information":
            icon = QMessageBox.Icon.Information
        
        dialog = QMessageBox()
        dialog.setText(text)
        dialog.setWindowTitle(title)
        dialog.setIcon(icon)
        dialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        res = dialog.exec()
        return res


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec())