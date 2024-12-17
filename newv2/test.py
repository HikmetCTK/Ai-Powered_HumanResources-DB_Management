from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from login_form import Ui_LoginWindow
from path_holder import getPath
import re

class LoginApp(QtWidgets.QMainWindow, Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentWidget(self.page_login)
        validator = QIntValidator(0, 999999)
        self.lineEdit_passcode.setValidator(validator)

        self.action_Clear_All.triggered.connect(self.clear_all_lineEdits)

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

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_timeout)
        self.timer.start(5000)

        self.email_pattern = re.compile(r"^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$")

        self.lineEdit_email_page_login.textChanged.connect(self.adjustEmailStatus)
        self.lineEdit_email_page_reset.textChanged.connect(self.adjustEmailStatus)

        self._translate = QCoreApplication.translate
    
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
    
    def on_timeout(self):
        print("Triggered!")
    
    def clear_all_lineEdits(self):
        line_edits = self.findChildren(QtWidgets.QLineEdit)
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
            sender.setToolTip(self._translate("MainWindow", "Type your email address"))
        else:
            status = self.verify_email_pattern(sender.text())

            if status == False:
                borderColor = r"ff0000"
                sender.setToolTip(self._translate("MainWindow", "Invalid email address pattern!"))
            else:
                borderColor = r"008000"
                sender.setToolTip(self._translate("MainWindow", "Email address pattern is valid"))
        
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
        dialog.setIcon(icon)
        dialog.setWindowIcon(QIcon(getPath("management_system_2")))

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