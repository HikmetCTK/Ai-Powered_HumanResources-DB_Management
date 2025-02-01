import db_man_projectv3_test
from package import StandardMessageBox
from package.Customs import setTable

def LoadViewEmployees(obj, cellWidgetAppend:bool = False, ButtonWidgetType:str|None = None,
                        DynamicProperties:dict|None = None, title:str="Employee List", externalResult:tuple|list|None = None):
    
    if externalResult:
        obj.queryResult = externalResult
    else:
        obj.queryResult = db_man_projectv3_test.load_employee_is_active()
        if not obj.queryResult:
            StandardMessageBox.NoResultsFound().exec()
            return
    
    # Set the desired buttons to be seen in the side menu
    obj.desiredDynamicButtons = ["Send Message", "Update", "Fire", "Assigned Items"]
    
    # Set the table properties
    obj.lbl_table_1_header.setText(title)
    obj.tableWidget_table_1.clear()
    tableHeaders = ["ID", "First Name", "Last Name", "Date of Birth", "Gender", "Job Title", "Department",
                    "Salary", "Hire Date", "Email", "Phone Number", "Password", "Is Active"]

    if cellWidgetAppend: tableHeaders.append("Action")

    setTable(obj, table = obj.tableWidget_table_1, items = obj.queryResult, rowHeaders = None,
                columnHeaders = tableHeaders, cellWidgetAppend = cellWidgetAppend,
                ButtonWidgetType = ButtonWidgetType, DynamicProperties = DynamicProperties)
    
    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_table_1)


# END