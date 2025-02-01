import db_man_projectv3_test
from package import StandardMessageBox
from package.Customs import setTable, CheckBoxWidget
from PyQt6.QtCore import Qt

def LoadAdvanceTransactions(obj, externalResult:tuple|list|None = None):
    if externalResult:
        obj.queryResult = externalResult
    else:
        obj.queryResult = db_man_projectv3_test.get_pending_special_requests()
        if not obj.queryResult:
            StandardMessageBox.NoResultsFound(obj).exec()
            return
    
    obj.desiredDynamicButtons = ["Accept", "Reject"]
    obj.tableWidget_table_1.clear()
    obj.lbl_table_1_header.setText("Advance Requests")
    tableHeaders = ["Request ID", "Employee ID", "Request Type", "Request Amount", "Request Date", "Status",
                    "Approved By", "Answer Date", "Created At", "Selection"] # selection column for dynamic widget

    setTable(obj, table = obj.tableWidget_table_1,
                items = obj.queryResult, rowHeaders = None, columnHeaders = tableHeaders,
                cellWidgetAppend = True, ButtonWidgetType = "DoubleButtonWidget",
                DynamicProperties = {"placedWidget":obj.tableWidget_table_1})
    
    # Close the control buttons under the table because they are not needed
    obj.widget_table_1_btn_container.setVisible(False)

    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_table_1)
    obj.stackedWidget_side_menu.setCurrentWidget(obj.page_expand_table)

def LoadSalaryAdjustment(obj):
    obj.queryResult = db_man_projectv3_test.load_employee_for_salary_adjustment()
    if not obj.queryResult:
        StandardMessageBox.NoResultsFound(obj).exec()
        return
    
    # There is no need for dynamic buttons in the side menu
    obj.desiredDynamicButtons = None

    obj.lbl_table_1_header.setText("Update Registration")
    obj.tableWidget_table_1.clear()
    tableHeaders = ["ID", "First Name", "Last Name", "Department", "Job Title", "Salary", "Selection"]

    setTable(obj, table = obj.tableWidget_table_1, items = obj.queryResult, rowHeaders = None,
                columnHeaders = tableHeaders, cellWidgetAppend = True, ButtonWidgetType = "CheckBoxWidget",
                DynamicProperties = {"placedWidget":obj.tableWidget_table_1})
    
    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_table_1)
    obj.stackedWidget_side_menu.setCurrentWidget(obj.page_money_transactions)

    obj.stackedWidget_side_menu.setVisible(True)
    obj.widget_page_table_1_hint_1_container.setVisible(False)

def updateSalaries(obj):
    idNewSalary:dict = dict()
    
    operationType = obj.comboBox_money_transactions_type_of_update.currentText()

    enteredAmount = float(obj.spinBox_money_transactions_amount.text())

    employeesToBeUpdated = CheckBoxWidget.getInstances(Qt.CheckState.Checked)

    employee_ids:list = list()

    for checkBoxItem in employeesToBeUpdated:
        employee_ids.append(int(checkBoxItem.objectName()[checkBoxItem.objectName().find("_") + 1:]))
    
    for idToBeUpdated in employee_ids:
        for employeeRecord in obj.queryResult:
            if employeeRecord[0] == idToBeUpdated:
                if operationType == "=": newSalary = round(enteredAmount, 2)
                elif operationType == "+": newSalary = round(float(employeeRecord[-1]) + enteredAmount, 2)
                elif operationType == "%+": newSalary = round(float(employeeRecord[-1]) * ((100 + enteredAmount) / 100), 2)
                elif operationType == "%-": newSalary = round(float(employeeRecord[-1]) * ((100 - enteredAmount) / 100), 2)
                else: newSalary = round(float(employeeRecord[-1]) - enteredAmount, 2)

                idNewSalary[idToBeUpdated] = newSalary

                break

    for empID, salary in idNewSalary.items():
        empID = int(empID)
        db_man_projectv3_test.update_employee_salary(emp_id = empID, new_salary = salary)
    
    StandardMessageBox.Successful(obj).exec()


# END