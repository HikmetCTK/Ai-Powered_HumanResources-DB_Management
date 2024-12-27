from PyQt6.QtWidgets import QMessageBox
import StandardMessageBox
import db_man_projectv3_test
from customs import *
from path_holder import *

def LoadUpcomingEvents(obj, externalResult:tuple|None = None):
    if externalResult:
        obj.queryResult = externalResult
    else:
        obj.queryResult = db_man_projectv3_test.see_events()
        if not obj.queryResult:
            StandardMessageBox.NoResultsFound(obj).exec()
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
            StandardMessageBox.NoResultsFound(obj).exec()
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
    db_man_projectv3_test.send_message_anyone(from_id = int(obj.currentEmployeeID),
                                         employee_ids = [int(obj.lbl_direct_message_id.text())],
                                         message = obj.textEdit_direct_message.toPlainText(),
                                         subject = obj.lineEdit_direct_message_subject.text())
    
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
    tableHeaders = ["ID", "First Name", "Last Name", "Department", "Job Title", "Email", "Selection"] # selection column for dynamic widget

    setTable(obj, table = obj.tableWidget_table_1, items = obj.queryResult, rowHeaders = None, columnHeaders = tableHeaders,
                cellWidgetAppend = True, ButtonWidgetType = "CheckBoxWidget", DynamicProperties={"checkState":False})

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
        # We do not care the returning value from the following messagebox
        QMessageBox(QMessageBox.Icon.Warning,
                    "No Selection",
                    "You haven't selected any employees yet. Make your selection(s) and try again.",
                    QMessageBox.StandardButton.Ok).exec()
        
        # Do not go further
        return
    obj.lineEdit_group_message_step_2_subject.clear()
    obj.textEdit_group_message.clear()
    if len(messageReceivers) == 0:
        # Print a warning message and do not go further.
        pass

    # Message type can be email or message
    messageType = obj.lbl_table_1_header.text().split(" ")[-1]
    obj.lbl_group_message_step_2_info.setText(f"{messageType} will be sent to {len(messageReceivers)} people.")

    obj.lbl_direct_message_step_2_header.setText(f"Group {messageType}")

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
            temp.append(rec[0])
            temp.append(rec[5])
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