import db_man_projectv3_test
import datetime
from package import StandardMessageBox
from package.Customs import setTable
from PyQt6.QtCore import QDate

def LoadCreateNewLeaveRequest(obj):
    obj.comboBox_leave_request_leave_type.setCurrentIndex(0)
    obj.dateEdit_leave_request_start_date.clear()
    obj.dateEdit_leave_request_end_date.clear()
    obj.textEdit_leave_request_description.clear()

    obj.dateEdit_leave_request_start_date.setDate(QDate.currentDate())
    obj.dateEdit_leave_request_end_date.setDate(QDate.currentDate())

    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_leave_request)

def ApplyLeaveRequest(obj):    
    leaveType = obj.comboBox_leave_request_leave_type.currentText()
    startDate = datetime.datetime.strptime(obj.dateEdit_leave_request_start_date.text(), r"%Y-%m-%d")
    endDate = datetime.datetime.strptime(obj.dateEdit_leave_request_end_date.text(), r"%Y-%m-%d")

    description = obj.textEdit_leave_request_description.toPlainText()
    if description == None or description == "":
        StandardMessageBox.Warning(obj, "Invalid Description", "Please provide a valid description to proceed.").exec()
        return
    
    db_man_projectv3_test.create_leave_request(employee_id=obj.currentEmployeeID,
                                                leave_type=leaveType,
                                                start_date=startDate,
                                                end_date=endDate,
                                                desc_request = description)
    
    StandardMessageBox.Successful(obj).exec()

def LoadPastLeaveRequests(obj):
    obj.queryResult = db_man_projectv3_test.leave_request_status_for_employee(employee_id=obj.currentEmployeeID)
    if not obj.queryResult:
        StandardMessageBox.NoResultsFound(obj).exec()
        return
    
    obj.lbl_table_1_header.setText("Leave Request Application History")
    obj.tableWidget_table_1.clear()
    tableHeaders = ["Leave Type", "Application Status", "Request Date", "Answer Date"]
    setTable(obj, obj.tableWidget_table_1, obj.queryResult, None, tableHeaders, False)
    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_table_1)

def LoadPendingLeaveRequests(obj):
    obj.queryResult = db_man_projectv3_test.pending_leave_requests_for_employee(employee_id=obj.currentEmployeeID)
    if not obj.queryResult:
        StandardMessageBox.NoResultsFound(obj).exec()
        return
    
    obj.lbl_table_1_header.setText("Your Pending Leave Requests")
    obj.tableWidget_table_1.clear()
    tableHeaders = ["Leave Type", "Application Status", "Request Date", "Answer Date"]
    setTable(obj, obj.tableWidget_table_1, obj.queryResult, None, tableHeaders, False)
    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_table_1)


# END