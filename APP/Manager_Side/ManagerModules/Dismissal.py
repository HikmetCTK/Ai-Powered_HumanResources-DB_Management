from package import StandardMessageBox
from PyQt6.QtWidgets import QMessageBox
import db_man_projectv3_test
from package.Customs import CheckBoxWidget
from PyQt6.QtCore import Qt
from Manager_Side.ManagerModules import ViewEmployees


def LoadDismissal(obj):
    # There is no need for dynamic buttons in the side menu
    obj.desiredDynamicButtons = None

    # For dismissing one employee, there is no need in bringing all the data
    # Offer 2 option for firing more than one employees or just one employee

    msg_box = QMessageBox(obj)
    msg_box.setWindowTitle("Dismissal Preference")

    msg = "You can use the <span style='color: #DD0ADD;'>@employees</span> filter to fire an individual. "\
        "We can bring in all employees to fire a group."
    msg_box.setText(msg)

    msg_box.setIcon(QMessageBox.Icon.Question)
    bring_them_all_btn = msg_box.addButton("Bring Them All", QMessageBox.ButtonRole.YesRole)
    ok_btn = msg_box.addButton("OK", QMessageBox.ButtonRole.NoRole)
    msg_box.setDefaultButton(ok_btn)
    msg_box.exec()

    if msg_box.clickedButton() == bring_them_all_btn:
        # We bring the employee records and add a selection column that is initially unchecked
        ViewEmployees.LoadViewEmployees(obj, cellWidgetAppend = True, ButtonWidgetType="CheckBoxWidget",
                                        DynamicProperties={"checkState":False, "placedWidget":obj.tableWidget_table_1},
                                        title = "Mass Dismissal")
        
        # Open the buttons under the table
        obj.widget_table_1_btn_container.setVisible(True)
    
    else:
        # Do nothing, user will use the search bar
        pass

def dismissEmployees(obj, externalEmpID:int|None = None):
    if externalEmpID:
        msg_box = QMessageBox(QMessageBox.Icon.Question,
                            "Dismissal Confirmation",
                            f"""You are about to <span style='color: #FF0000'>fire</span> the
                            employee with ID <span style='color: #FF0000'>{externalEmpID}</span>.
                            This action is irreversible. Are you sure?""",
                            QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No,
                            obj)
        # Set the focus to the "No" button
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)

        response = msg_box.exec()
        
        # Based on the response to the confirmation, fire the selected employees or pass
        if response == QMessageBox.StandardButton.Yes:
            db_man_projectv3_test.not_working(externalEmpID)
            StandardMessageBox.Successful(obj, reload=True).exec()
            return
        else:
            return False

    # Get the total number of selected employees
    total = len(CheckBoxWidget.getInstances(Qt.CheckState.Checked))

    # If no one is chosen, show a warning message
    if total == 0:
        # We do not care the returning value from the following messagebox
        QMessageBox(QMessageBox.Icon.Warning,
                    "No Selection",
                    "You haven't selected any employees yet. Make your selection(s) and try again.",
                    QMessageBox.StandardButton.Ok).exec()
        
        # Do not go further
        return
    
    # If there is a chosen one(s), continue by asking for a confirmation
    msg_box = QMessageBox(QMessageBox.Icon.Question,
                            "Mass Dismissal Confirmation",
                            f"""You are about to <span style='color: #FF0000'>fire {total} 
                            employee(s)</span> at once. This action is irreversible. 
                            Are you sure?""",
                            QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No,
                            obj)
    
    # Set the focus to the "No" button
    msg_box.setDefaultButton(QMessageBox.StandardButton.No)

    response = msg_box.exec()
    
    # Based on the response to the confirmation, fire the selected employees or pass
    if response == QMessageBox.StandardButton.Yes:
        selected_employees = CheckBoxWidget.getInstances(Qt.CheckState.Checked)
        ids = list()
        for employee in selected_employees:
            employee = employee.objectName()
            ids.append(int(employee[employee.find("_") + 1:]))
        
        for employee_id in ids:
            db_man_projectv3_test.not_working(employee_id)
        
        StandardMessageBox.Successful(obj, reload = False).exec()
    else:
        pass


# END