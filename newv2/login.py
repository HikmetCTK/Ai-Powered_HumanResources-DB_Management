from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import QPixmap, QIntValidator, QIcon, QActionGroup
from login_form import Ui_LoginWindow
import db_man_projectv3
from path_holder import getPath
import re
from manager_test import ManagerApp

class LoginApp(QtWidgets.QMainWindow, Ui_LoginWindow):
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

        # Set a validator for passcode input
        passcode_validator = QIntValidator(0, 999999)
        self.lineEdit_passcode.setValidator(passcode_validator)

        # Connect functions to input items on UI
        self.btn_forgot_password.clicked.connect(self.loadResetPasswordStep1)
        self.checkBox_show_password_page_login.checkStateChanged.connect(self.changePasswordEchoMode)
        self.btn_contact_back.clicked.connect(self.directToFromAboutPage)
        self.btn_cancel_page_reset.clicked.connect(self.loadLoginPage)
        self.btn_send_code.clicked.connect(self.loadResetPasswordStep2)
        self.btn_back_reset_step2.clicked.connect(self.loadResetPasswordStep1)
        self.btn_cancel_page_reset_step_2.clicked.connect(self.loadLoginPage)
        self.btn_complete.clicked.connect(self.completeResetPassword)
        self.checkBox_show_password_reset_step2.clicked.connect(self.changePasswordEchoMode)
        self.btn_login.clicked.connect(self.login)
        self.btn_resend_code.clicked.connect(self.resendPassword)

        self.action_Refresh_Connection.triggered.connect(self.updateConnectionStatus)
        self.action_Clear_All.triggered.connect(self.clear_all_lineEdits)

        self.email_pattern = re.compile(r"^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$")

        self.lineEdit_email_page_login.textChanged.connect(self.adjustEmailStatus)
        self.lineEdit_email_page_reset.textChanged.connect(self.adjustEmailStatus)

        # -- QAction --

        actionGroup = QActionGroup(self)
        actionGroup.setExclusive(True)

        actionGroup.addAction(self.action_3_sec)
        actionGroup.addAction(self.action_5_sec)
        actionGroup.addAction(self.action_10_sec)
        actionGroup.addAction(self.action_30_sec)
        actionGroup.addAction(self.action_60_sec)
        actionGroup.addAction(self.action_90_sec)
        actionGroup.addAction(self.action_120_sec)
        actionGroup.addAction(self.action_Never)

        self.action_3_sec.toggled.connect(self.on_action_toggled)
        self.action_5_sec.toggled.connect(self.on_action_toggled)
        self.action_10_sec.toggled.connect(self.on_action_toggled)
        self.action_30_sec.toggled.connect(self.on_action_toggled)
        self.action_60_sec.toggled.connect(self.on_action_toggled)
        self.action_90_sec.toggled.connect(self.on_action_toggled)
        self.action_120_sec.toggled.connect(self.on_action_toggled)
        self.action_Never.toggled.connect(self.on_action_toggled)

        # -- QAction -end --

        self.action_Restart.triggered.connect(self.restart_request)

        # Set a timer for connection check

        self.time_period = 5000 # 5 sec is set initially

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateConnectionStatus)
        self.timer.start(self.time_period)
        
        # Set initial connection status
        self.updateConnectionStatus()
    
    @pyqtSlot(bool)
    def on_action_toggled(self, checked):
        action = self.sender()
        if checked:
            if action.text() == "Never":
                self.timer.stop()
                self.lbl_connection_icon.setPixmap(QPixmap(getPath("white_dot")))
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
    
    def verify_email_pattern(self, email_addr:str) -> bool:
        match = self.email_pattern.match(email_addr)
        if match:
            return True
        else:
            return False
    
    def adjustEmailStatus(self, status:bool) -> None:
        sender = self.sender()
        if sender.text().strip() == "":
            borderColor = r"be8af9"
        else:
            status = self.verify_email_pattern(sender.text())

            if status == False:
                borderColor = r"ff0000"
            else:
                borderColor = r"008000"
        
        sender.setStyleSheet(f"""
            QLineEdit {{ 
                    border:2px solid #555555;
                    border-radius:10px;
                    background-color:#555555;
                    color:#f0f0f0;
                    padding-left:8px;
                    }}
            QLineEdit:focus {{ 
                    border:1.5px solid #{borderColor};
                    border-radius:10px;
                    background-color:#555555;
                            }}
            """)
    
    def loadResetPasswordStep1(self):
        self.lineEdit_email_page_reset.clear()
        self.stackedWidget.setCurrentWidget(self.page_reset_password)
    
    def loadResetPasswordStep2(self):
        if len(self.lineEdit_email_page_reset.text()) == 0:
            self.showDialog("Warning", "Provide your email address that exists in the system!", "Error")
        elif self.verify_email_pattern(self.lineEdit_email_page_reset.text()) == False:
            self.showDialog("Warning", "The email address provided is not in a valid format!", "Error")
        else:
            msg = db_man_projectv3.send_verification_code(self.lineEdit_email_page_reset.text())
            if isinstance(msg, int):
                self.verification_code = msg
                self.lineEdit_passcode.clear()
                self.lineEdit_new_password.clear()
                self.lineEdit_confirm_password.clear()
                self.stackedWidget.setCurrentWidget(self.page_reset_password_step2)
            elif isinstance(msg, str):
                self.showDialog("Error", msg, "Error")
            else:
                self.showDialog("Error",
                                f"An unhandled case has occurred! Func: 'loadResetPasswordStep2' | msg: '{msg}' | Type: {type(msg)}",
                                "Unhandled Case Error")
    
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
            self.showDialog("Error",
                            f"Current widget is not suitable for 'changePasswordEchoMode'! CW: {self.stackedWidget.currentWidget()}",
                            "Error")
        
        currentEchoMode = item.echoMode()
        if currentEchoMode == QLineEdit.EchoMode.Password:
            newMode = QLineEdit.EchoMode.Normal
        else:
            newMode = QLineEdit.EchoMode.Password

        item.setEchoMode(newMode)
        if self.stackedWidget.currentWidget() == self.page_reset_password_step2:
            self.lineEdit_confirm_password.setEchoMode(newMode)
    
    def completeResetPassword(self):
        connection, msg = db_man_projectv3.connection_check()
        if connection != True:
            self.showDialog("Error", f"Database connection could not be established! Try again! -> {msg}", "DB Connection Error")
        elif len(self.lineEdit_passcode.text()) != 6 or self.lineEdit_passcode.text().isspace():
            self.showDialog("Error", "6-digit passcode must be provided!", title="Passcode Error")
            self.lineEdit_passcode.clear()
        elif len(self.lineEdit_new_password.text()) == 0 or self.lineEdit_new_password.text().isspace():
            self.showDialog("Warning", "Set a new password!", title="New Password Error")
        elif len(self.lineEdit_confirm_password.text()) == 0 or self.lineEdit_confirm_password.text().isspace():
            self.showDialog("Warning", "Confirm your new password!", title="Password Confirmation Error")
        elif not (self.lineEdit_new_password.text() == self.lineEdit_confirm_password.text()):
            self.showDialog("Warning", "Your new password do not match with your confirmation!", title="Mismatched Confirmation")
        else:
            res = db_man_projectv3.reset_change_password(new_password=self.lineEdit_new_password.text(),
                                                        entered_code=int(self.lineEdit_passcode.text()),
                                                        verification_code=self.verification_code,
                                                        user_email=self.lineEdit_email_page_reset.text())
            if res == True:
                self.showDialog("Information", "Your password has been changed successfully!", "Information")
                self.stackedWidget.setCurrentWidget(self.page_login)
            elif res == False:
                self.showDialog("Warning", "One-time-password is wrong! Try again or get a new one.", "OTP Error")
            elif isinstance(res, str):
                self.showDialog("Error", f"An error occurred during password resetting! -> {res}", "Error")
            else:
                self.showDialog("Error",
                                f"An unhandled case has occurred! Func: 'completeResetPassword' | res: '{res}' | Type: {type(res)}",
                                "Unhandled Case Error")
        
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
    
    def login(self):
        connection, msg = db_man_projectv3.connection_check()
        if connection != True:
            self.showDialog("Error", f"Database connection could not be established! Try again! -> {msg}", "DB Connection Error")
        elif len(self.lineEdit_email_page_login.text()) == 0 or self.lineEdit_email_page_login.text().isspace():
            self.showDialog("Warning", "Provide your email address!", "Error")
        elif self.verify_email_pattern(self.lineEdit_email_page_login.text()) == False:
            self.showDialog("Warning", "The email address provided is not in a valid format!", "Error")
        elif len(self.lineEdit_password_page_login.text()) == 0 or self.lineEdit_password_page_login.text().isspace():
            self.showDialog("Warning", "Provide your password!", "Error")
        else:
            res = db_man_projectv3.login(email=self.lineEdit_email_page_login.text(),
                                        password=self.lineEdit_password_page_login.text())
            if res == None:
                self.showDialog("Warning", "Mail address or password is wrong!", "Login Failed")
            elif isinstance(res, tuple):
                role, empID, name, surname = res
                print(role)
                if role == "Human resources":
                    self.main_form_2 = ManagerApp(empId=int(empID), name = name, surname = surname)
                    self.main_form_2.show()
                    self.close()
                else:
                    self.showDialog("Information", "Login successful but employee side is not ready for now!", "Login Successul")
            else:
                self.showDialog("Error", f"An error occurred during login! Please try again! -> {res} | {type(res)}", "Login Failed")
        
        # Clear password input box
        self.lineEdit_password_page_login.clear()
    
    def updateConnectionStatus(self):
        connection, msg = db_man_projectv3.connection_check()
        if connection == True:
            self.lbl_connection_icon.setPixmap(QPixmap(getPath("green_dot")))
            self.lbl_connection_status.setText("Connected")
        elif connection == False:
            self.lbl_connection_icon.setPixmap(QPixmap(getPath("red_dot")))
            self.lbl_connection_status.setText("Not connected")
        else:
            self.showDialog("Error",
                            f"An error occurred during database connection check! connection: {connection} -> {type(connection)} | msg: {msg} -> {type(msg)}",
                            "Connection Check Error")
    
    def resendPassword(self):
        msg = db_man_projectv3.send_verification_code(self.lineEdit_email_page_reset.text())
        if isinstance(msg, int):
            self.verification_code = msg
            self.showDialog("Information", "Your new one-time-password has been sent to your email address!", "Resend OTP")
            self.lineEdit_passcode.clear()
        elif isinstance(msg, str):
            self.showDialog("Error", msg, "Error")
        else:
            self.showDialog("Error",
                            f"An unhandled case has occurred! Func: 'resendPassword' | msg: '{msg}' | Type: {type(msg)}",
                            "Unhandled Case Error")
    
    def closeEvent(self, event):
        res = self.showDialog("YesNoQuestion", "Are you sure you want to exit?", "Exit")
        if res == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
    
    def showDialog(self, dialog_type:str, text:str, title:str = "Error"):
        if dialog_type == "Error":
            icon = QMessageBox.Icon.Critical
        elif dialog_type == "Warning":
            icon = QMessageBox.Icon.Warning
        elif dialog_type == "Information":
            icon = QMessageBox.Icon.Information
        elif dialog_type == "YesNoQuestion":
            icon = QMessageBox.Icon.Question
        else:
            icon = QMessageBox.Icon.Critical
        
        dialog = QMessageBox()
        dialog.setText(text)
        dialog.setWindowTitle(title)
        dialog.setWindowIcon(QIcon(getPath("management_system_2")))
        dialog.setIcon(icon)

        if dialog_type == "YesNoQuestion":
            dialog.setStandardButtons(QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No)
            dialog.setDefaultButton(QMessageBox.StandardButton.No)
        else:
            dialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        res = dialog.exec()
        return res


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec())