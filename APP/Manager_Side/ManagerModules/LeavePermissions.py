import db_man_projectv3_test
from package import StandardMessageBox
from package.Customs import setTable

def LoadLeavePermissions(obj, externalResult:tuple|list|None = None):
    if externalResult:
        obj.queryResult = externalResult
    else:
        obj.queryResult = db_man_projectv3_test.get_pending_leave_requests()

        if isinstance(obj.queryResult, str):
            StandardMessageBox.Error(obj, "Error", f"Error in 'get_pending_leave_requests'\n\nErr: {obj.queryResult}").exec()
            return
        
        if obj.queryResult == None or len(obj.queryResult) == 0:
            StandardMessageBox.NoResultsFound(obj).exec()
            return
    
    obj.tableWidget_table_1.clear()
    obj.lbl_table_1_header.setText("Leave Requests")

    # selection column for dynamic widget
    tableHeaders = ["ID", "Employee ID", "Status", "Request Date", "Approved By", "Approve Date", "Leave Type",
                    "Start Date", "End Date", "Description", "Total Dates", "Created At", "Selection"]
    
    obj.desiredDynamicButtons = ["Accept", "Reject"]

    setTable(obj, table = obj.tableWidget_table_1,
                items = obj.queryResult, rowHeaders = None, columnHeaders = tableHeaders,
                cellWidgetAppend = True, ButtonWidgetType = "DoubleButtonWidget",
                DynamicProperties = {"placedWidget":obj.tableWidget_table_1})
    
    # Close the control buttons under the table because they are not needed
    obj.widget_table_1_btn_container.setVisible(False)

    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_table_1)
    obj.stackedWidget_side_menu.setCurrentWidget(obj.page_expand_table)


# END