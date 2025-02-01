from PyQt6.QtGui import QIntValidator, QActionGroup
from PyQt6.QtCore import QTimer

def initializeLogin(obj):
    # Set max lengths of inputs on UI
    obj.lineEdit_email_page_login.setMaxLength(50)
    obj.lineEdit_email_page_reset.setMaxLength(50)
    obj.lineEdit_password_page_login.setMaxLength(50)
    obj.lineEdit_new_password.setMaxLength(50)
    obj.lineEdit_confirm_password.setMaxLength(50)
    obj.lineEdit_passcode.setMaxLength(6)

    # Set a validator for passcode input
    passcode_validator = QIntValidator(0, 999999)
    obj.lineEdit_passcode.setValidator(passcode_validator)

    # Connect functions to input items on UI
    obj.btn_forgot_password.clicked.connect(obj.loadResetPasswordStep1)
    obj.checkBox_show_password_page_login.checkStateChanged.connect(obj.changePasswordEchoMode)
    obj.btn_contact_back.clicked.connect(obj.directToFromAboutPage)
    obj.btn_cancel_page_reset.clicked.connect(obj.loadLoginPage)
    obj.btn_send_code.clicked.connect(obj.loadResetPasswordStep2)
    obj.btn_back_reset_step2.clicked.connect(obj.loadResetPasswordStep1)
    obj.btn_cancel_page_reset_step_2.clicked.connect(obj.loadLoginPage)
    obj.btn_complete.clicked.connect(obj.completeResetPassword)
    obj.checkBox_show_password_reset_step2.clicked.connect(obj.changePasswordEchoMode)
    obj.btn_login.clicked.connect(obj.login)
    obj.btn_resend_code.clicked.connect(obj.resendPassword)

    obj.action_Refresh_Connection.triggered.connect(obj.updateConnectionStatus)
    obj.action_Clear_All.triggered.connect(obj.clear_all_lineEdits)

    obj.lineEdit_email_page_login.textChanged.connect(obj.adjustEmailStatus)
    obj.lineEdit_email_page_reset.textChanged.connect(obj.adjustEmailStatus)

    # -- QAction --

    actionGroup = QActionGroup(obj)
    actionGroup.setExclusive(True)

    actionGroup.addAction(obj.action_3_sec)
    actionGroup.addAction(obj.action_5_sec)
    actionGroup.addAction(obj.action_10_sec)
    actionGroup.addAction(obj.action_30_sec)
    actionGroup.addAction(obj.action_60_sec)
    actionGroup.addAction(obj.action_90_sec)
    actionGroup.addAction(obj.action_120_sec)
    actionGroup.addAction(obj.action_Never)

    obj.action_3_sec.toggled.connect(obj.on_action_toggled)
    obj.action_5_sec.toggled.connect(obj.on_action_toggled)
    obj.action_10_sec.toggled.connect(obj.on_action_toggled)
    obj.action_30_sec.toggled.connect(obj.on_action_toggled)
    obj.action_60_sec.toggled.connect(obj.on_action_toggled)
    obj.action_90_sec.toggled.connect(obj.on_action_toggled)
    obj.action_120_sec.toggled.connect(obj.on_action_toggled)
    obj.action_Never.toggled.connect(obj.on_action_toggled)

    # -- QAction -end --

    obj.action_Restart.triggered.connect(obj.restart_request)

    # Set a timer for connection check

    obj.time_period = 5000 # 5 sec is set initially

    obj.timer = QTimer()
    obj.timer.timeout.connect(obj.updateConnectionStatus)
    obj.timer.start(obj.time_period)
    
    # Set initial connection status
    obj.updateConnectionStatus()


# END