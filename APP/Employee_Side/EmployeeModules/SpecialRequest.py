import db_man_projectv3_test
from package import StandardMessageBox
from package.Customs import setTable

def LoadCreateNewSpecialRequest(obj):
    obj.comboBox_special_request_request_type.setCurrentIndex(0)
    obj.spinBox_special_request_request_amount.clear()
    obj.textEdit_special_request_description.clear()
    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_special_request)

def ApplySpecialRequest(obj):
    requestType = obj.comboBox_special_request_request_type.currentText()
    requestAmount = obj.spinBox_special_request_request_amount.text()
    description = obj.textEdit_special_request_description.toPlainText()

    if requestAmount == "":
        StandardMessageBox.Warning(obj, "Empty Request Amount", "Please provide the amount of your request.").exec()
        return
    
    else:
        try:
            requestAmount = round(float(obj.spinBox_special_request_request_amount.text()), 2)
        except:
            StandardMessageBox.Warning(obj, "Request Amount Type", "Request amount could not be converted to float!").exec()
            return
    
    if requestAmount <= 0:
        StandardMessageBox.Warning(obj, "Invalid Request Amount", "Request amount must be greater than 0.").exec()
        return
    
    if description == None or description == "":
        StandardMessageBox.Warning(obj, "Invalid Request Description", "A valid request description is required.").exec()
        return

    db_man_projectv3_test.create_special_request(employee_id = obj.currentEmployeeID,
                                                 request_type = requestType,
                                                 request_amount = requestAmount,
                                                 description = description)
    
    StandardMessageBox.Successful(obj).exec()

def LoadPastSpecialRequests(obj):
    obj.queryResult = db_man_projectv3_test.special_request_status_for_employee(employee_id=obj.currentEmployeeID)
    if not obj.queryResult:
        StandardMessageBox.NoResultsFound(obj).exec()
        return
    
    obj.lbl_table_1_header.setText("Special Request Application History")
    obj.tableWidget_table_1.clear()
    tableHeaders = ["Request Type", "Application Status", "Request Date", "Answer Date"]
    setTable(obj, obj.tableWidget_table_1, obj.queryResult, None, tableHeaders, False)
    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_table_1)

def LoadPendingSpecialRequests(obj):
    obj.queryResult = db_man_projectv3_test.pending_special_requests_for_employee(employee_id=obj.currentEmployeeID)
    if not obj.queryResult:
        StandardMessageBox.NoResultsFound(obj).exec()
        return
    
    obj.lbl_table_1_header.setText("Your Pending Special Requests")
    obj.tableWidget_table_1.clear()
    tableHeaders = ["Request Type", "Application Status", "Request Date", "Answer Date"]
    setTable(obj, obj.tableWidget_table_1, obj.queryResult, None, tableHeaders, False)
    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_table_1)


# END