import db_man_projectv3_test
from package.Customs import CheckBoxWidget, MonoButtonWidget, setTable
from package import StandardMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem

def LoadItemAssignment(obj):
    obj.queryResult = db_man_projectv3_test.load_infos("items")

    if isinstance(obj.queryResult, str):
        StandardMessageBox.Error(obj, "Error", f"Error in 'load_infos'\n\nErr: {obj.queryResult}").exec()
        return
    
    if obj.queryResult == None or len(obj.queryResult) == 0:
        StandardMessageBox.NoResultsFound(obj).exec()
        return
    
    # There is no need for dynamic buttons in the side menu
    obj.desiredDynamicButtons = None

    # Do not forget to clear the record of the previous objects from the related
    # list, they are deleted, and cannot be used again.
    CheckBoxWidget.clearInstanceList()

    obj.lbl_table_1_header.setText("Item Assignment Registration")

    # selection column for dynamic widget
    tableHeaders = ["ID", "First Name", "Last Name", "Department", "Job Title", "Email", "Selection"]
    
    setTable(obj, table = obj.tableWidget_table_1, items = obj.queryResult, rowHeaders = None,
            columnHeaders = tableHeaders, cellWidgetAppend = True, ButtonWidgetType = "CheckBoxWidget",
            DynamicProperties={"checkState":False, "placedWidget":obj.tableWidget_item_assignment})

    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_table_1)

    # Open the buttons under the table
    obj.widget_table_1_btn_container.setVisible(True)

    # Make the second step ready in advance
    obj.listWidget_item_assignment.clear()
    obj.tableWidget_item_assignment.clearContents()
    obj.tableWidget_item_assignment.setRowCount(0)

def LoadItemAssignmentStep2(obj):
    totalEmployees = len(CheckBoxWidget.getInstances(Qt.CheckState.Checked))
    if totalEmployees == 0:
        StandardMessageBox.Warning(obj, "No Selection",
                                "You haven't selected any employees yet. Make your selection(s) and try again.").exec()
        return
    
    obj.spinBox_item_assignment_quantity.setValue(1)
    obj.items = db_man_projectv3_test.load_infos("items")
    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_item_assignment)
    obj.widget_table_1_btn_container.setVisible(False)
    obj.lbl_item_assignment_info.setText(f"Items will be assigned to {totalEmployees} employees.")
    obj.listWidget_item_assignment.addItems([item[1] for item in obj.items])

def addItemToSelectionTable(obj):
    # Get the total number of employees to whom items will be assigned
    totalEmployees = len(CheckBoxWidget.getInstances(Qt.CheckState.Checked))

    # Get the name of the selected item
    try:
        selectedItem = obj.listWidget_item_assignment.selectedItems()[0].text()
    except IndexError:
        StandardMessageBox.Warning(obj, "No Selection", "Select an item from the item list!").exec()
        return
    
    # Get the number of items to assign per employee
    desiredQuantity = int(obj.spinBox_item_assignment_quantity.text())
    
    # Loop through the items record to find the stock count of the selected item
    for item in obj.items:
        if item[1] == selectedItem:
            availableQuantity = item[2]
            break
    
    # If stock count is not sufficient, warn and return
    if (totalEmployees * desiredQuantity) > availableQuantity:
        stockError = "The number of items in stock is not suitable for the item assignment "\
                    "you requested. Check the stock status and item assignment quantities again."
        
        # Warn the user
        StandardMessageBox.Warning(obj, "Stock Error", stockError).exec()
        # Do not go further
        return

    # Insert a new row to the tableWidget and place the relevant data in the cells
    row_position = obj.tableWidget_item_assignment.rowCount() 
    obj.tableWidget_item_assignment.insertRow(row_position)
    obj.tableWidget_item_assignment.setItem(row_position, 0, QTableWidgetItem(selectedItem))
    obj.tableWidget_item_assignment.setItem(row_position, 1, QTableWidgetItem(str(desiredQuantity)))
    
    # Dynamic delete button to delete the selected item from the table
    btn = MonoButtonWidget(row_position, ([selectedItem, selectedItem]),
                            {"buttonType":"delete", "toolTip":"delete",
                            "placedWidget":obj.tableWidget_item_assignment})
    
    # Place the button
    obj.tableWidget_item_assignment.setCellWidget(row_position, 2, btn)

    # Connect the button to its relevant function
    btn.clicked_value.connect(obj.handleCellWidgetBtnClick)

    # Set table-related properties
    obj.tableWidget_item_assignment.setColumnWidth(3, 40)
    obj.tableWidget_item_assignment.setRowHeight(row_position, 36)

    # Once the selected item is added to the tableWidget, remove it from the listWidget
    obj.listWidget_item_assignment.takeItem(obj.listWidget_item_assignment.currentRow())

    # Clear selection
    obj.listWidget_item_assignment.clearSelection()
    
    # Update status
    obj.updateAssignStatus()

def resetAssignmentTable(obj):
    obj.listWidget_item_assignment.clear()
    obj.tableWidget_item_assignment.clearContents()
    obj.tableWidget_item_assignment.setRowCount(0)
    MonoButtonWidget.clearInstanceList()
    obj.lbl_item_assignment_overall.setText(f"Total 0 items with 0 pieces.")
    obj.LoadItemAssignmentStep2()

def completeAssignment(obj):
    if obj.tableWidget_item_assignment.rowCount() == 0:
        StandardMessageBox.Warning(obj, "No Selection",
                                    "You haven't selected any items yet. Make your selection(s) and try again.").exec()
        return
    
    # ID is used to assign items and names are also unique
    # Selection is made based on name
    # Get ids from names
    nameIDMatchDict = dict()
    for item in obj.items:
        # names are the keys, values are the ids
        nameIDMatchDict[item[1]] = item[0]

    itemAssignDict = dict()
    for row in range(obj.tableWidget_item_assignment.rowCount()):
        # Item name is present in the column with index 0
        itemName = obj.tableWidget_item_assignment.item(row, 0).text()
        # Item quantity is present in the column with index 1
        itemQuantity = int(obj.tableWidget_item_assignment.item(row, 1).text())
        # Set the id-quantity pair
        itemAssignDict[nameIDMatchDict[itemName]] = itemQuantity
    
    # Get the employees to be processed
    employees = CheckBoxWidget.getInstances(Qt.CheckState.Checked)
    
    # Define an id list to store the ids of employees
    employee_ids:list = list()
    
    # Extract employee ids and store
    for checkBoxItem in employees:
        employee_ids.append(int(checkBoxItem.objectName()[checkBoxItem.objectName().find("_") + 1:]))
    
    # Assign items to employees
    for employee_id in employee_ids:
        for itemID, itemQuantity in itemAssignDict.items():
            ret = db_man_projectv3_test.assign_item_to_employee_no_checking(id = employee_id, item_id = itemID, quantity = itemQuantity)
            if isinstance(ret, str):
                StandardMessageBox.Error(obj, "Error", f"Error in 'assign_item_to_employee_no_checking'\n\nErr: {ret}").exec()
                return
    
    StandardMessageBox.Successful(obj).exec()

def backToEmployeeSelection(obj):
    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_table_1)
    obj.widget_table_1_btn_container.setVisible(True)
    # Make the second step ready in advance
    obj.listWidget_item_assignment.clear()
    obj.tableWidget_item_assignment.clearContents()
    obj.tableWidget_item_assignment.setRowCount(0)

def updateAssignStatus(obj):
    quantity = 0
    totalRow = obj.tableWidget_item_assignment.rowCount()
    for row in range(obj.tableWidget_item_assignment.rowCount()):
        quantity += int(obj.tableWidget_item_assignment.item(row, 1).text())
    obj.lbl_item_assignment_overall.setText(f"Total {totalRow} items with {quantity} pieces.")

def cancelItemAssignment(obj):
    obj.LoadDashboard()


def LoadItemAssignmentList(obj):
    obj.queryResult = db_man_projectv3_test.load_item_list_with_name()
    if isinstance(obj.queryResult, str):
        StandardMessageBox.Error(obj, "Error",
                                 f"Error in 'load_item_list_with_name'\n\nErr: {obj.queryResult}").exec()
        return
    
    if obj.queryResult == None or len(obj.queryResult) == 0:
        StandardMessageBox.NoResultsFound(obj).exec()
        return

    obj.desiredDynamicButtons = ["Delete Item"]
    obj.lbl_table_1_header.setText("Items Assigned to Employees")
    obj.tableWidget_table_1.clear()
    tableHeaders = ["Assign ID", "Employee ID", "First Name", "Last Name", "Item ID", "Item Name", "Quantity", "Assignment Date", "Action"]
    setTable(obj, obj.tableWidget_table_1, obj.queryResult, None, tableHeaders, True,
                "MonoButtonWidget", {"buttonType":"delete", "toolTip":"delete", "placedWidget":obj.tableWidget_table_1})
    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_table_1)

def LoadAssignedItemsToEmployee(obj, emp_id, name:str = "", surname:str = ""):
    obj.queryResult = db_man_projectv3_test.get_assigned_items(emp_id)
    if isinstance(obj.queryResult, str):
        StandardMessageBox.Error(obj, "Error", f"Error in 'get_assigned_items'\n\nErr: {obj.queryResult}").exec()
        return
    
    if obj.queryResult == None or len(obj.queryResult) == 0:
        StandardMessageBox.NoResultsFound(obj).exec()
        return
    
    if name == "" and surname == "":
        emp = "Employee"
    else:
        emp = " ".join([name, surname])

    obj.desiredDynamicButtons = ["Delete Item"]
    obj.lbl_table_1_header.setText(f"Items Assigned to {emp}")
    obj.tableWidget_table_1.clear()
    tableHeaders = ["Assign ID", "Item Name", "Assignment Date", "Action"]
    setTable(obj, obj.tableWidget_table_1, obj.queryResult, None, tableHeaders, True,
                "MonoButtonWidget", {"buttonType":"delete", "toolTip":"delete", "placedWidget":obj.tableWidget_table_1})
    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_table_1)


# END