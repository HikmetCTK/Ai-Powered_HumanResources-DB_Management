import db_man_projectv3_test
from package import StandardMessageBox
from package.Customs import setTable

def LoadAssignedItemsToEmployee(obj):
    obj.queryResult = db_man_projectv3_test.get_assigned_items(obj.currentEmployeeID)
    if not obj.queryResult:
        StandardMessageBox.NoResultsFound(obj).exec()
        return

    obj.lbl_table_1_header.setText(f"Items Assigned To You")
    obj.tableWidget_table_1.clear()
    tableHeaders = ["Assign ID", "Item Name", "Assignment Date"]
    setTable(obj, obj.tableWidget_table_1, obj.queryResult, None, tableHeaders, False)
    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_table_1)


# END