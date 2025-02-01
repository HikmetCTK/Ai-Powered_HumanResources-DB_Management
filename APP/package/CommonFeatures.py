from package.Customs import *
from package import StandardMessageBox
from package.PathHolder import *
import db_man_projectv3_test
import re
from time import strftime

"""
Some features that are commonly used by both the manager and employee sides are managed centrally here.
"""

def showUserRole(obj):
    # We can directly write the full form of user role in the long menu
    obj.lbl_long_menu_position.setText(f"{obj.role}")

    # For showing the role in the short menu we have to make some adjustments
    shortenedRole = obj.role
    if len(obj.role) > 10:
        shortenedRole = ""
        splittedRole = obj.role.split(" ")
        for word in splittedRole:
            # Just show initials separated by dots
            shortenedRole += word[0]
            shortenedRole += "."

    # Write the proper form of the role in the short menu

    obj.lbl_short_menu_position.setText(f"{shortenedRole}")

def on_preference_toggled(obj, checked):
    # Here we set the appearance preference of the menu and search bar

    action = obj.sender()
    if action.text() == "Show":
        obj.stackedWidget_header.setVisible(True)
    elif action.text() == "Hide":
        obj.stackedWidget_header.setVisible(False)
    elif action.text() == "Dynamic":
        obj.scrollArea_short_menu.setVisible(True)
        obj.scrollArea_long_menu.setVisible(False)
        obj.isMenuFixed = False
    elif action.text() == "Fixed":
        obj.scrollArea_short_menu.setVisible(False)
        obj.scrollArea_long_menu.setVisible(True)
        obj.isMenuFixed = True

def updateConnectionStatus(obj):
    try:
        if obj.sender().objectName() == "action_Refresh_Connection":
            addtInfo = f" - {strftime(r"%H:%M:%S")}"
        else:
            addtInfo = ""
    except:
        addtInfo = ""

    # Update the connection status and display it on the relevant label
    try:
        connection, msg = db_man_projectv3_test.connection_check()
    except:
        obj.lbl_connection_icon.setPixmap(obj.disconnectedIcon)
        obj.lbl_connection_status.setText(f"Not Connected (ERR){addtInfo}")
    else:
        if connection == True:
            obj.lbl_connection_icon.setPixmap(obj.connectedIcon)
            obj.lbl_connection_status.setText(f"Connected{addtInfo}")
        elif connection == False:
            obj.lbl_connection_icon.setPixmap(obj.disconnectedIcon)
            obj.lbl_connection_status.setText(f"Not Connected{addtInfo}")
        else:
            obj.lbl_connection_icon.setPixmap(obj.disconnectedIcon)
            obj.lbl_connection_status.setText(f"Not Connected (ERR){addtInfo}")

def shortMenuBarEnterEvent(obj, event):
    obj.scrollArea_long_menu.setVisible(True)
    obj.scrollArea_short_menu.setVisible(False)

    # Close all the submenus to provide a good-looking experience
    obj.toggleSubMenu()

def shortMenuBarLeaveEvent(obj, event):
    pass

def scrollAreaEnterEvent(obj, event):
    obj.scrollArea_long_menu.setVisible(True)
    obj.scrollArea_short_menu.setVisible(False)

def scrollAreaLeaveEvent(obj, event):
    if not obj.isMenuFixed:
        obj.scrollArea_long_menu.setVisible(False)
        obj.scrollArea_short_menu.setVisible(True)
    else:
        pass

def verify_email_pattern(email_addr:str) -> bool:
    email_pattern = re.compile(r"^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$")
    match = email_pattern.match(email_addr)
    if match:
        return True
    else:
        return False

def adjustEmailStatus(obj) -> None:
    sender = obj.sender()
    if sender.text().strip() == "":
        borderColor = r"be8af9"
    else:
        status = verify_email_pattern(sender.text())

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

def LoadUpcomingEvents(obj, externalResult:tuple|None = None):
    if externalResult:
        obj.queryResult = externalResult
    else:
        obj.queryResult = db_man_projectv3_test.see_events()
        if not obj.queryResult:
            StandardMessageBox.NoResultsFound().exec()
            return
    
    # There is no need for dynamic buttons in the side menu
    obj.desiredDynamicButtons = None

    obj.lbl_table_1_header.setText("Upcoming Events")
    obj.tableWidget_table_1.clear()
    tableHeaders = ["Event ID", "Event Name", "Details", "Date"]

    setTable(obj, table = obj.tableWidget_table_1,
                items = obj.queryResult, rowHeaders = None, columnHeaders = tableHeaders)
    
    # Close the control buttons under the table, because there is no need for them
    obj.widget_table_1_btn_container.setVisible(False)
    
    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_table_1)

def LoadIncomingMessages(obj, externalResult:tuple|None = None):
    if externalResult:
        obj.queryResult = externalResult
    else:
        obj.queryResult = db_man_projectv3_test.see_messagev2(emp_id = obj.currentEmployeeID)
        if not obj.queryResult:
            StandardMessageBox.NoResultsFound().exec()
            return
        
    # There is no need for dynamic buttons in the side menu
    obj.desiredDynamicButtons = None

    obj.lbl_table_1_header.setText("Incoming Messages")
    obj.tableWidget_table_1.clear()
    tableHeaders = ["Message ID", "Name", "Surname", "Subject", "Content", "Date", "From Employee ID"]

    setTable(obj, table = obj.tableWidget_table_1,
                items = obj.queryResult, rowHeaders = None, columnHeaders = tableHeaders)
    
    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_table_1)

def LoadDirectMessage(obj):
    obj.lineEdit_direct_message_to.clear()
    obj.lineEdit_direct_message_subject.clear()
    obj.lbl_direct_message_id.clear()
    obj.lbl_direct_message_department_job.clear()
    obj.textEdit_direct_message.clear()

    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_send_message)

def sendMessage(obj):
    fromID = int(obj.currentEmployeeID)

    try:
        employeeID = [int(obj.lbl_direct_message_id.text())]
    except Exception as e:
        StandardMessageBox.Warning(obj, "No Recipient Selected", "Select a recipient for the message!").exec()
        return

    messageSubject = obj.lineEdit_direct_message_subject.text()

    if messageSubject == None or messageSubject == "":
        StandardMessageBox.Warning(obj, "Invalid Message Subject", "Please provide a valid message subject to proceed.").exec()
        return
    
    messageContent = obj.textEdit_direct_message.toPlainText()

    if messageContent == None or messageContent == "":
        StandardMessageBox.Warning(obj, "Invalid Message Content", "Please provide a valid message content to proceed.").exec()
        return

    db_man_projectv3_test.send_message_anyone(from_id = fromID, employee_ids = employeeID, message = messageContent,
                                              subject = messageSubject)
    
    StandardMessageBox.Successful(obj).exec()

def LoadGroupMessage(obj):
    obj.queryResult = db_man_projectv3_test.load_employee_for_message_selection()
    if not obj.queryResult:
        StandardMessageBox.NoResultsFound(obj).exec()
        return
    
    # There is no need for dynamic buttons in the side menu
    obj.desiredDynamicButtons = None

    # Do not forget to clear the record of the previous objects from the related
    # list, they are deleted, and cannot be used again.
    CheckBoxWidget.clearInstanceList()

    obj.tableWidget_table_1.clear()
    obj.lbl_table_1_header.setText("Send Group Message")

    # selection column for dynamic widget
    tableHeaders = ["ID", "First Name", "Last Name", "Department", "Job Title", "Email", "Selection"]

    setTable(obj, table = obj.tableWidget_table_1, items = obj.queryResult, rowHeaders = None, columnHeaders = tableHeaders,
                cellWidgetAppend = True, ButtonWidgetType = "CheckBoxWidget",
                DynamicProperties={"checkState":False, "placedWidget":obj.tableWidget_table_1})

    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_table_1)

    # Open the buttons under the table
    obj.widget_table_1_btn_container.setVisible(True)

def LoadGroupEmail(obj):
    LoadGroupMessage(obj)
    obj.lbl_table_1_header.setText("Send Group Email")

def LoadDirectMessageSecondStep(obj):
    messageReceivers = CheckBoxWidget.getInstances(Qt.CheckState.Checked)
    # If no one is chosen, show a warning message
    if len(messageReceivers) == 0:
        StandardMessageBox.Warning(obj, "No Selection",
                                   "You haven't selected any employees yet. Make your selection(s) and try again.").exec()
        
        # Do not go further
        return
    
    # Prepare the page of second step before opening it
    obj.lineEdit_group_message_step_2_subject.clear()
    obj.textEdit_group_message.clear()

    # Message type can be email or message
    messageType = obj.lbl_table_1_header.text().split(" ")[-1]
    # Set the info message properly
    obj.lbl_group_message_step_2_info.setText(f"{messageType} will be sent to {len(messageReceivers)} people.")
    # Set the header properly
    obj.lbl_direct_message_step_2_header.setText(f"Group {messageType}")
    # Open the page of second step
    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_group_message_step_2)

def sendGroupMessage(obj):
    messageReceivers = CheckBoxWidget.getInstances(Qt.CheckState.Checked)

    subject = obj.lineEdit_group_message_step_2_subject.text()
    message = obj.textEdit_group_message.toPlainText()

    employee_ids:list = list()

    for checkBoxItem in messageReceivers:
        employee_ids.append(int(checkBoxItem.objectName()[checkBoxItem.objectName().find("_") + 1:]))
    
    if db_man_projectv3_test.arrangeText("email") in db_man_projectv3_test.arrangeText(obj.lbl_table_1_header.text()):
        # If the user wants to send group email
        receiverRecords = list()
        for item in CheckBoxWidget.instances:
            temp = list()
            rec = CheckBoxWidget.objectRowDataMatch[item.objectName()]
            temp.append(rec[0]) # to_emp_id
            temp.append(rec[5]) # to_email
            receiverRecords.append(temp)
        
        db_man_projectv3_test.send_email(receiverRecords, subject, message, int(obj.currentEmployeeID), obj.name, obj.surname, obj.role)
    else:
        # If the user wants to send group message
        db_man_projectv3_test.send_message_anyone(from_id = int(obj.currentEmployeeID), employee_ids = employee_ids,
                                                  subject = subject, message = message)
    
    StandardMessageBox.Successful(obj).exec()

def BackToGroupMessageEmployeeSelection(obj):
    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_table_1)

    # Open the buttons under the table
    obj.widget_table_1_btn_container.setVisible(True)

def LoadProfile(obj):
    obj.queryResult = db_man_projectv3_test.search(keyword = obj.currentEmployeeID, table_name = "employees", column_name = "employee_id")
    employee = obj.queryResult[0]
    
    # General Information part
    obj.lbl_profile_name_content.setText(str(employee[1]))
    obj.lbl_profile_surname_content.setText(str(employee[2]))
    obj.lbl_profile_date_of_birth_content.setText(str(employee[3]))
    obj.lbl_profile_email_content.setText(str(employee[9]))
    obj.lbl_profile_gender_content.setText(str(employee[4]))
    obj.lbl_profile_phone_number_content.setText(str(employee[10]))
    
    # Business Information part
    obj.lbl_profile_employee_id_content.setText(str(employee[0]))
    obj.lbl_profile_department_content.setText(str(employee[6]))
    obj.lbl_profile_job_title_content.setText(str(employee[5]))
    obj.lbl_profile_salary_content.setText(str(employee[7]))
    obj.lbl_profile_hire_date_content.setText(str(employee[8]))
    obj.lbl_profile_status_content.setText(str(employee[12]))
    
    # Open the related page
    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_profile)

def replyMessage(obj):
    # To reply a message, get the sender information from
    # the related label in expand_message screen in the side menu
    fromInfo = obj.lbl_expand_message_from_content.text()
    # John Doe - 1002
    empID = fromInfo[fromInfo.find("-") + 1:].strip()
    # Load direct message screen
    LoadDirectMessage(obj)
    # Get the whole record of the employee having the empID
    res = db_man_projectv3_test.search(keyword = empID, table_name = "employees", column_name = "employee_id")
    # Nested result... Get the inner and only result
    employee = res[0]
    # Place information needed in the direct message screen
    obj.lineEdit_direct_message_to.setText(str(employee[1]) + " " + str(employee[2]))
    obj.lbl_direct_message_id.setText(str(employee[0]))
    obj.lbl_direct_message_department_job.setText(str(employee[6]) + " / " + str(employee[5]))


def handleWidgetClick(obj, value):
    # Catch the values emitted by signals and run proper functions based on the values
    if value in ["e_widget_summary_pm", "m_widget_summary_pm"]:
        obj.LoadIncomingMessages()
    elif value in ["e_widget_summary_ue", "m_widget_summary_ue"]:
        obj.LoadUpcomingEvents()
    elif value == "m_widget_summary_par":
        obj.LoadAdvanceTransactions()
    elif value == "e_widget_summary_par":
        obj.LoadPendingSpecialRequests()
    elif value == "m_widget_summary_plp":
        obj.LoadLeavePermissions()
    elif value == "e_widget_summary_plp":
        obj.LoadPendingLeaveRequests()
    else:
        pass

def showPeopleCardMenu(obj):
        # Get peoplecards
        PeopleCardWidget.getPeopleCard(obj, obj.lineEdit_direct_message_to.text())

        # Open the menu based on the caller

        # The sender is btn_phone_book because
        # it is connected to this function (see initializer.py)
        # Open the menu under the line_edit_direct_message_to
        item = obj.lineEdit_direct_message_to

        obj.peopleCardMenu.exec(item.mapToGlobal(item.rect().bottomLeft()))
        
def handlePeopleCardClick(obj, value):
    # Created people card widgets are connected
    # to this function (see PeopleCardWidget class in customs.py)

    # Catch the object name
    objectName = obj.sender().objectName()
    # Object names are expressions that are combinations of
    # certain information separated by stars.
    # Separate the object name from the stars to extract the information
    name, _id, addt_info = objectName.split("*")
    # Place information in relevant places
    obj.lineEdit_direct_message_to.setText(name)
    obj.lbl_direct_message_id.setText(_id)
    obj.lbl_direct_message_department_job.setText(addt_info)


def LoadTableView(obj, externalResult, tableHeaders, header):
    obj.lbl_table_1_header.setText(header)
    obj.tableWidget_table_1.clear()
    setTable(obj, obj.tableWidget_table_1, externalResult, None, tableHeaders, False)
    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_table_1)


def LoadQuickActionsPage(obj):
    if obj.stackedWidget_side_menu.currentWidget() != obj.page_quick_actions:
        # Store the current page before changing it to quick actions page
        # to be able to turn back to it when back button is clicked
        obj.previousSideMenuPage = obj.stackedWidget_side_menu.currentWidget()

        # Open quick actions page
        obj.stackedWidget_side_menu.setCurrentWidget(obj.page_quick_actions)

        obj.sender().setText("Back")
    else:
        # Turn back to the previous page
        obj.stackedWidget_side_menu.setCurrentWidget(obj.previousSideMenuPage)

        obj.sender().setText("Quick Actions")
    
    # What is it needed for? DoubleButtonWidget or CheckBoxWidget?
    if len(CheckBoxWidget.instances):
        # If it is for CheckBoxWidget...
        hintText = "If you want to choose the majority excluding the minority, "\
                    "just select the minority and let us swap your choices.\n"\
                    "Filtering is taken into account, as always."
        obj.lbl_page_hint_hint_1.setText(hintText)
        
        obj.btn_hints_swap_choices.setVisible(True)

        obj.btn_hints_select_all.setText("Select All")
        obj.btn_hints_clear_all.setText("Clear All")
    else:
        # If it is for DoubleButtonWidget...
        hintText = "You can accept or reject requests "\
                    "with one click. Filtering is taken into account, as always.\n"\
                    "Do not forget that once you select one of the choices, it is "\
                    "directly saved and cannot be changed again."
        obj.lbl_page_hint_hint_1.setText(hintText)
        
        # Swap choices button is needed only for check boxes
        obj.btn_hints_swap_choices.setVisible(False)

        # Rearrange the texts on the buttons
        obj.btn_hints_select_all.setText("Accept All")
        obj.btn_hints_clear_all.setText("Reject All")


def selectAll(obj, table:QTableWidget):
    # Perform an easy check to determine it is for checkboxes or accept buttons

    # Start with getting the comparable forms of the texts
    senderText = db_man_projectv3_test.arrangeText(obj.sender().text())
    controlText = db_man_projectv3_test.arrangeText("Accept All")

    if senderText == controlText:
        DoubleButtonWidget.acceptAll(table)
    else:
        CheckBoxWidget.checkAll(table)

def clearAll(obj, table:QTableWidget):
    # Perform an easy check to determine it is for checkboxes or reject buttons

    # Start with getting the comparable forms of the texts
    senderText = db_man_projectv3_test.arrangeText(obj.sender().text())
    controlText = db_man_projectv3_test.arrangeText("Reject All")

    if senderText == controlText:
        DoubleButtonWidget.rejectAll(table)
    else:
        CheckBoxWidget.uncheckAll(table)

def swapChoicesCheckBoxes(obj, table:QTableWidget):
    CheckBoxWidget.alternateSelection(table)


# END