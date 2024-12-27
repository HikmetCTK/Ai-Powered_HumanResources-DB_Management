from PyQt6.QtWidgets import QMainWindow, QSpinBox, QMessageBox, QListWidgetItem, QApplication
from PyQt6.QtCore import pyqtSlot, QEvent
from PyQt6.QtGui import QPixmap
import initializer
from manager_ui_form import Ui_ManagerWindow
import datetime
import inspect
from customs import *
from path_holder import *
import db_man_projectv3_test
import StandardMessageBox
import search
import SideBarButtonFuctions
import expand_table
import initializer
import CommonFeatures

class ManagerApp(QMainWindow, Ui_ManagerWindow):
    func = None
    args = None
    kwargs = None
    def __init__(self, empId:int = 1111, name:str = "Fevzi", surname:str = "FİDAN", role:str = "Computer Engineer"):
        super().__init__()
        self.setupUi(self)

        # Store the ID of the current employee
        self.currentEmployeeID:int = empId
        self.name:str = name
        self.surname:str = surname
        self.role:str = role
        self.lbl_dashboard_header.setText(f"Welcome, {self.name}")
        self.lbl_short_menu_name.setText(f"{self.name} {self.surname}")
        self.lbl_long_menu_name.setText(f"{self.name} {self.surname}")
        self.showUserRole()
        self.queryResult = None
        self.previousIndex = -1
        self.connectedIcon = IconManager.getIcon("green_dot", "pixmap")
        self.disconnectedIcon = IconManager.getIcon("red_dot", "pixmap")
        initializer.ManagerInitializer.initializeMainScreen(self)

        # XXX Try to call initializer XXX

        # initializer.initializeManager(self)

        self.LoadDashboard()
    
    def showUserRole(self):
        # We can directly write the full form of user role in the long menu
        self.lbl_long_menu_position.setText(f"{self.role}")

        # For showing the role in the short menu we have to make some adjustments
        shortenedRole = self.role
        if len(self.role) > 10:
            shortenedRole = ""
            splittedRole = self.role.split(" ")
            for word in splittedRole:
                # Just show initials separated by dots
                shortenedRole += word[0]
                shortenedRole += "."

        # Write the proper form of the role in the short menu

        self.lbl_short_menu_position.setText(f"{shortenedRole}")

    def handler(func:callable):
        def innerWrapper(self, *args, **kwargs):
            stack = inspect.stack()
            callerName = stack[1].function
            if callerName != "<module>":
                ManagerApp.func = func
                ManagerApp.args = args
                ManagerApp.kwargs = kwargs
            else:
                for frame in stack[1:]:  # Start from the next frame
                    if frame.function != "<module>":
                        caller_name = frame.function
                        ManagerApp.func=callerName
                        break


            try:
                func(self, *args, **kwargs)
            except TypeError:
                func(self)
            except Exception as e:
                StandardMessageBox.Error(self, "Error (handler)", f"An error occurred during the latest process! | {str(e)}").exec()
            
        return innerWrapper
    
    def errorCatcher(func:callable):
        def innerWrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except TypeError:
                return func(self)
            except Exception as e:
                StandardMessageBox.Error(self, "Error (errorCatcher)", f"An error occurred during the latest process! | {str(e)}").exec()
        return innerWrapper
    
    @errorCatcher
    def reload(self):
        if ManagerApp.func:
            try:
                ManagerApp.func(self, *ManagerApp.args, **ManagerApp.kwargs)
            except TypeError:
                ManagerApp.func(self)
            except Exception as e:
                raise e
        else:
            self.LoadDashboard()
    
    @pyqtSlot(bool)
    def on_action_toggled(self, checked):
        action = self.sender()
        if checked:
            if action.text() == "Never":
                self.timer.stop()
                self.lbl_connection_icon.setPixmap(QPixmap(getPath("white_dot")))
                self.lbl_connection_status.setText("Not Controlled!")
            else:
                self.time_period = int(action.text()[0:action.text().find(" ")].strip()) * 1000
                self.timer.start(self.time_period)
    
    def on_preference_toggled(self, checked):
        action = self.sender()
        if action.text() == "Show":
            self.stackedWidget_header.setVisible(True)
        elif action.text() == "Hide":
            self.stackedWidget_header.setVisible(False)
        elif action.text() == "Dynamic":
            self.scrollArea_short_menu.setVisible(True)
            self.scrollArea_long_menu.setVisible(False)
            self.isMenuFixed = False
        elif action.text() == "Fixed":
            self.scrollArea_short_menu.setVisible(False)
            self.scrollArea_long_menu.setVisible(True)
            self.isMenuFixed = True
    
    @errorCatcher
    def updateConnectionStatus(self):
        connection, msg = db_man_projectv3_test.connection_check()
        if connection == True:
            self.lbl_connection_icon.setPixmap(self.connectedIcon)
            self.lbl_connection_status.setText("Connected")
        elif connection == False:
            self.lbl_connection_icon.setPixmap(self.disconnectedIcon)
            self.lbl_connection_status.setText("Not connected")
        else:
            pass

    def shortMenuBarEnterEvent(self, event):
        self.scrollArea_long_menu.setVisible(True)
        self.scrollArea_short_menu.setVisible(False)

        # Close all the submenus to provide a good-looking experience
        self.toggleSubMenu()

    def shortMenuBarLeaveEvent(self, event):
        pass
    
    def scrollAreaEnterEvent(self, event):
        self.scrollArea_long_menu.setVisible(True)
        self.scrollArea_short_menu.setVisible(False)

    def scrollAreaLeaveEvent(self, event):
        if not self.isMenuFixed:
            self.scrollArea_long_menu.setVisible(False)
            self.scrollArea_short_menu.setVisible(True)
        else:
            pass
    
    def toggleSubMenu(self):
        try:
            clickedMenu = self.sender().objectName()
        except AttributeError:
            # If the function has been called externally
            # to close all the submenus, we get
            # AttributeError in the try block.
            # We can continue by setting it None
            clickedMenu = None
        if clickedMenu == "btn_long_menu_general":
            relatedSubMenu = self.widget_submenu_1
        elif clickedMenu == "btn_long_menu_employment":
            relatedSubMenu = self.widget_submenu_2
        elif clickedMenu == "btn_long_menu_transactions":
            relatedSubMenu = self.widget_submenu_3
        elif clickedMenu == "btn_long_menu_plans":
            relatedSubMenu = self.widget_submenu_4
        elif clickedMenu == "btn_long_menu_communication":
            relatedSubMenu = self.widget_submenu_5
        elif clickedMenu == "btn_long_menu_item_assignments":
            relatedSubMenu = self.widget_submenu_6
        else:
            # Close all of the submenus

            i = 1
            while True:
                try:
                    # Get the submenu object
                    subMenu = getattr(self, f"widget_submenu_{i}")

                    # Close the submenu
                    subMenu.setVisible(False)

                    i += 1
                except AttributeError:
                    break
            
            # Set the currentlyOpenSubMenu to None
            self.currentlyOpenSubMenu = None

            # Do not go further
            return

        currentStatus = relatedSubMenu.isVisible()
        relatedSubMenu.setVisible(not currentStatus)
        
        if self.currentlyOpenSubMenu == None: pass
        else: self.currentlyOpenSubMenu.setVisible(False)

        if not currentStatus == True: self.currentlyOpenSubMenu = relatedSubMenu
        else: self.currentlyOpenSubMenu = None

        return
    
    def textEditTextChanged(self):
        CustomTextEdit.textChanged_(self)
    
    @errorCatcher
    def search(self):
        search.search(self)

    def filterTrigger(self):
        action = self.sender()
        self.textEdit_page_search_search.setText(f"@{action.text().capitalize()} | ")
        self.textEdit_page_search_search.setTextColorUntilIndex(len(self.textEdit_page_search_search.toPlainText())-1)
    
    def handleWidgetClick(self, value):
        CommonFeatures.handleWidgetClick(self, value)
    
    def handleCellClick(self, row, column):
        if self.stackedWidget_side_menu.currentWidget().objectName() == "page_money_transactions" and self.stackedWidget_side_menu.isVisible():
            return # We do not want this screen to change because it is needed
        
        for item in self.created_right_menu_dynamic_widgets:
            try:
                self.verticalLayout_17.removeWidget(item)
                item.disconnect()
                item.close()
                item.deleteLater()
            except:
                pass
        
        self.created_right_menu_dynamic_widgets.clear()

        if db_man_projectv3_test.arrangeText(self.lbl_table_1_header.text()) == db_man_projectv3_test.arrangeText("Incoming Messages"):
            expand_table.expand_message(self, row, column)

            # Do not go further. Below is for other standard expanding operations.
            return
        
        elif db_man_projectv3_test.arrangeText(self.lbl_table_1_header.text()) == db_man_projectv3_test.arrangeText("Upcoming Events"):
            expand_table.expand_event(self, row, column)

            # Do not go further. Below is for other standard expanding operations.
            return

        else:
            expand_table.expand_table(self, row, column)
    
    @errorCatcher
    def search_table(self, search_text:str, columnNumber:int|None = None):
        search.search_table(self, search_text, columnNumber)
        
    def eventFilter(self, obj, event):
        if obj == self.textEdit_page_search_search and event.type() == QEvent.Type.KeyPress:
            if event.key() == Qt.Key.Key_Backspace:
                self.textEditTextChanged()
        
        # We should show quick actions button if there are checkbox needs and side menu is visible        
        elif obj == self.stackedWidget_side_menu and event.type() == event.Type.ShowToParent:
            # Check whether the suitable objects exist or not
            # We have no business with dynamicLabels for this operation, but it is an
            # easy-to-reach indicative showing whether DoubleButtonWidgets exist or not
            if len(CheckBoxWidget.instances) or len(DoubleButtonWidget.dynamicLabelInstances):
                self.btn_quick_actions.setVisible(True)
                self.btn_quick_actions.setText("Quick Actions")
            
        return super().eventFilter(obj, event)

    @errorCatcher
    def handleDynamicButtonClick(self):
        """
        Triggers a function
        """
        outputList:list[str] = list()
        dynamicLineEdits = self.stackedWidget_side_menu.findChildren(QLineEdit)
        outputList.append(self.sender().objectName())

        # We need to trigger the proper button which exist on the table
        # in order to provide the same effect

        # We need to dive into the name pattern to reach the button
        # on the table

        # self.sender().objectName() -> btnDynamic_Reject / btnDynamic_Accept / btnDynamic_...
        # name pattern of the buttons on the table -> dynamicAccept_[id]

        # First column is the id

        for lineEdit in dynamicLineEdits:
            # QLineEdit can be exist in some components, like QSpinBox, that's why
            # we need to filter and keep only QLineEdit objects themselves.
            if not isinstance(lineEdit.parent(), QSpinBox):
                outputList.append(lineEdit.text())
        
        senderButtonType = outputList[0][outputList[0].find("_") + 1:] # Accept / Reject / ...
        id = outputList[1]
        
        if senderButtonType in ["Accept", "Reject"]:
            SideBarButtonFuctions.approval(senderButtonType, id)
        else:
            # Meaning that dynamic button is from MonoButtonWidget

            # Get the text on the button
            if senderButtonType == "Send Message":
                self.LoadDirectMessage()
                # Set to part to the name + surname of the employee
                self.lineEdit_direct_message_to.setText(outputList[2] + " " + outputList[3])
                # Set id part to the id of the employee
                self.lbl_direct_message_id.setText(outputList[1])
                # Set department / job part based on employee's information
                self.lbl_direct_message_department_job.setText(outputList[7] + " / " + outputList[6])
            elif senderButtonType == "Fire":
                res = self.dismissEmployees(int(outputList[1]))

                if res:
                    self.closeSideMenu()
                    StandardMessageBox.Successful(self).exec()


            elif senderButtonType == "Update":
                SideBarButtonFuctions.update(self.queryResult, outputList)
                StandardMessageBox.Successful(self).exec()
            elif senderButtonType == "Assigned Items":
                self.LoadAssignedItemsToEmployee(emp_id = id, name = outputList[2], surname = outputList[3])
            else:
                pass
            
    def showPeopleCardMenu(self):
        CommonFeatures.showPeopleCardMenu(self)
        
    def handlePeopleCardClick(self, value):
        CommonFeatures.handlePeopleCardClick(self, value)
    
    def LoadQuickActionsPage(self):
        if self.stackedWidget_side_menu.currentWidget() != self.page_quick_actions:
            self.previousSideMenuPage = self.stackedWidget_side_menu.currentWidget()
            self.stackedWidget_side_menu.setCurrentWidget(self.page_quick_actions)
            self.sender().setText("Back")
        else:
            self.stackedWidget_side_menu.setCurrentWidget(self.previousSideMenuPage)
            self.sender().setText("Quick Actions")
        
        # What is it needed for? DoubleButtonWidget or CheckBoxWidget?
        if len(CheckBoxWidget.instances):
            # If it is for CheckBoxWidget...
            hintText = "If you want to choose the majority excluding the minority, "\
                        "just select the minority and let us swap your choices.\n"\
                        "Filtering is taken into account, as always."
            self.lbl_page_hint_hint_1.setText(hintText)
            
            self.btn_hints_swap_choices.setVisible(True)

            self.btn_hints_select_all.setText("Select All")
            self.btn_hints_clear_all.setText("Clear All")
        else:
            # If it is for DoubleButtonWidget
            hintText = "You can accept or reject requests "\
                        "with one click. Filtering is taken into account, as always.\n"\
                        "Do not forget that once you select one of the choices, it is "\
                        "directly saved and cannot be changed again."
            self.lbl_page_hint_hint_1.setText(hintText)
            
            # Swap choices button is needed only for check boxes
            self.btn_hints_swap_choices.setVisible(False)

            # Rearrange the texts on the buttons
            self.btn_hints_select_all.setText("Accept All")
            self.btn_hints_clear_all.setText("Reject All")

    @errorCatcher
    def HandleTablePageController(self):
        header = self.lbl_table_1_header.text()
        if db_man_projectv3_test.arrangeText("Group Message") in db_man_projectv3_test.arrangeText(header):
            self.LoadDirectMessageSecondStep()
        
        elif db_man_projectv3_test.arrangeText("Group Email") in db_man_projectv3_test.arrangeText(header):
            self.LoadDirectMessageSecondStep()

        elif db_man_projectv3_test.arrangeText("Mass Dismissal") in db_man_projectv3_test.arrangeText(header):
            self.dismissEmployees()

        elif db_man_projectv3_test.arrangeText("Item Assignment") in db_man_projectv3_test.arrangeText(header):
            self.LoadItemAssignmentStep2()
        else:
            pass

    def clearDynamicInstances(self):
        # Clear all the objects that have been dynamically
        # created during runtime

        # They are cleared when they are no longer useless
        # or they are no longer needed

        CheckBoxWidget.clearInstanceList()
        MonoButtonWidget.clearInstanceList()
        DoubleButtonWidget.clearInstanceLists()

    def selectAll(self):
        # Perform an easy check to determine it is for checkboxes or accept buttons
        if db_man_projectv3_test.arrangeText(self.sender().text()) == db_man_projectv3_test.arrangeText("Accept All"):
            DoubleButtonWidget.acceptAll(self.tableWidget_table_1)
        else:
            CheckBoxWidget.checkAll(self.tableWidget_table_1)
    
    def clearAll(self):
        # Perform an easy check to determine it is for checkboxes or reject buttons
        if db_man_projectv3_test.arrangeText(self.sender().text()) == db_man_projectv3_test.arrangeText("Reject All"):
            DoubleButtonWidget.rejectAll(self.tableWidget_table_1)
        else:
            CheckBoxWidget.uncheckAll(self.tableWidget_table_1)
    
    def swapChoicesCheckBoxes(self):
        CheckBoxWidget.alternateSelection(self.tableWidget_table_1)

    @handler
    def LoadViewEmployees(self, cellWidgetAppend:bool = False, ButtonWidgetType:str|None = None,
                          DynamicProperties:dict|None = None, title:str="Employee List", externalResult:tuple|list|None = None):
        
        if externalResult:
            self.queryResult = externalResult
        else:
            self.queryResult = db_man_projectv3_test.load_employee()
            if not self.queryResult:
                StandardMessageBox.NoResultsFound(self).exec()
                return
        
        # There is no need for dynamic buttons in the side menu
        self.desiredDynamicButtons = ["Send Message", "Update", "Fire", "Assigned Items"]

        self.lbl_table_1_header.setText(title)
        self.tableWidget_table_1.clear()
        tableHeaders = ["ID", "First Name", "Last Name", "Date of Birth", "Gender", "Job Title", "Department",
                        "Salary", "Hire Date", "Email", "Phone Number", "Password", "Is Active"]

        if cellWidgetAppend: tableHeaders.append("Action")

        setTable(self, table = self.tableWidget_table_1, items = self.queryResult, rowHeaders = None,
                 columnHeaders = tableHeaders, cellWidgetAppend = cellWidgetAppend,
                 ButtonWidgetType = ButtonWidgetType, DynamicProperties = DynamicProperties)
        
        self.stackedWidget_main_screen.setCurrentWidget(self.page_table_1)


    @handler
    def LoadHiring(self):
        self.lineEdit_hiring_name.clear()
        self.lineEdit_hiring_surname.clear()
        self.lineEdit_hiring_phone_number.clear()
        self.lineEdit_hiring_department.clear()
        self.lineEdit_hiring_job_title.clear()
        self.lineEdit_hiring_salary.clear()
        self.lineEdit_hiring_email.clear()
        self.dateEdit_hiring_date_of_birth.clear()
        self.comboBox_hiring_gender.setCurrentIndex(0)
        self.comboBox_hiring_password_sending_preference.setCurrentIndex(0)

        self.stackedWidget_main_screen.setCurrentWidget(self.page_new_staff_registration)
    
    @errorCatcher
    def hire(self):
        gender = self.comboBox_hiring_gender.currentText()
        try:
            employeePassword = db_man_projectv3_test.generateRandomPassword(8)
            db_man_projectv3_test.hiring(name = self.lineEdit_hiring_name.text(),
                                    surname = self.lineEdit_hiring_surname.text(),
                                    birth = self.dateEdit_hiring_date_of_birth.text(),
                                    gender = gender,
                                    job_title = self.lineEdit_hiring_job_title.text(),
                                    derpatment = self.lineEdit_hiring_department.text(),
                                    salary = self.lineEdit_hiring_salary.text(),
                                    hire_date = datetime.datetime.now().strftime(r"%Y-%m-%d"),
                                    email = self.lineEdit_hiring_email.text(),
                                    phone_no = self.lineEdit_hiring_phone_number.text(),
                                    password = employeePassword)
        except Exception as e:
            StandardMessageBox.Error(self, "Hire Error", f"An error occurred while hiring! | {str(e)}").exec()
        else:
            # Get the password sending preference
            pref = self.comboBox_hiring_password_sending_preference.currentText()
            if pref == "Just Show":
                StandardMessageBox.Information(self, "Employee Password",
                                               f"Hiring successful! Employee's initial password: {employeePassword}").exec()
            elif pref == "Show and Send Email":
                StandardMessageBox.Information(self, "Employee Password",
                                               f"Hiring successful! Employee's initial password: {employeePassword}\n\nEmail including password has also been sent.").exec()
            else:
                StandardMessageBox.Information(self, "Employee Password",
                                               f"Hiring successful! Employee's initial password has been sent to them by email.").exec()


    @handler
    def LoadDismissal(self):
        # There is no need for dynamic buttons in the side menu
        self.desiredDynamicButtons = None

        # For dismissing one employee, there is no need in bringing all the data
        # Offer 2 option for firing more than one employees or just one employee

        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Dismissal Preference")
        msg_box.setText("You can use the <span style='color: #DD0ADD;'>@employees</span> filter to fire an individual. We can bring in all employees to fire a group.")
        msg_box.setIcon(QMessageBox.Icon.Question)
        bring_them_all_btn = msg_box.addButton("Bring Them All", QMessageBox.ButtonRole.YesRole)
        ok_btn = msg_box.addButton("OK", QMessageBox.ButtonRole.NoRole)
        msg_box.setDefaultButton(ok_btn)
        msg_box.exec()

        if msg_box.clickedButton() == bring_them_all_btn:
            # We bring the employee records and add a selection column that is initially unchecked
            res = db_man_projectv3_test.load_employee_is_active()
            self.LoadViewEmployees(cellWidgetAppend = True, ButtonWidgetType="CheckBoxWidget",
                                   DynamicProperties={"checkState":False}, title = "Mass Dismissal",
                                   externalResult = res)
            
            # Open the buttons under the table
            self.widget_table_1_btn_container.setVisible(True)
        
        else:
            # Do nothing, user will use the search bar
            pass

    @errorCatcher
    def dismissEmployees(self, externalEmpID:int|None = None):
        if externalEmpID:
            msg_box = QMessageBox(QMessageBox.Icon.Question,
                                "Dismissal Confirmation",
                                f"""You are about to <span style='color: #FF0000'>fire</span> the
                                employee with ID <span style='color: #FF0000'>{externalEmpID}</span>.
                                This action is irreversible. Are you sure?""",
                                QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No,
                                self)
            # Set the focus to the "No" button
            msg_box.setDefaultButton(QMessageBox.StandardButton.No)

            response = msg_box.exec()
            
            # Based on the response to the confirmation, fire the selected employees or pass
            if response == QMessageBox.StandardButton.Yes:
                db_man_projectv3_test.not_working(externalEmpID)
                return True
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
                                self)
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
            
            StandardMessageBox.Successful(self).exec()
        else:
            pass

    @handler
    def LoadAdvanceTransactions(self, externalResult:tuple|list|None = None):
        if externalResult:
            self.queryResult = externalResult
        else:
            self.queryResult = db_man_projectv3_test.get_pending_special_requests()
            if not self.queryResult:
                StandardMessageBox.NoResultsFound(self).exec()
                return
        
        self.desiredDynamicButtons = ["Accept", "Reject"]
        self.tableWidget_table_1.clear()
        self.lbl_table_1_header.setText("Special Requests")
        tableHeaders = ["Request ID", "Employee ID", "Request Type", "Request Amount", "Request Date", "Status",
                        "Approved By","Description","Answer Date", "Created At", "Answer"] # selection column for dynamic widget

        setTable(self, table = self.tableWidget_table_1,
                 items = self.queryResult, rowHeaders = None, columnHeaders = tableHeaders,
                 cellWidgetAppend = True, ButtonWidgetType = "DoubleButtonWidget")
        
        # Close the control buttons under the table because they are not needed
        self.widget_table_1_btn_container.setVisible(False)

        self.stackedWidget_main_screen.setCurrentWidget(self.page_table_1)
        self.stackedWidget_side_menu.setCurrentWidget(self.page_expand_table)

    @handler
    def LoadSalaryAdjustment(self):
        self.queryResult = db_man_projectv3_test.load_employee_for_salary_adjustment()
        if not self.queryResult:
            StandardMessageBox.NoResultsFound(self).exec()
            return
        
        # There is no need for dynamic buttons in the side menu
        self.desiredDynamicButtons = None

        self.lbl_table_1_header.setText("Update Registration")
        self.tableWidget_table_1.clear()
        tableHeaders = ["ID", "First Name", "Last Name", "Department", "Job Title", "Salary", "Selection"]

        setTable(self, table = self.tableWidget_table_1, items = self.queryResult, rowHeaders = None,
                 columnHeaders = tableHeaders, cellWidgetAppend = True, ButtonWidgetType = "CheckBoxWidget")
        
        self.stackedWidget_main_screen.setCurrentWidget(self.page_table_1)
        self.stackedWidget_side_menu.setCurrentWidget(self.page_money_transactions)

        self.stackedWidget_side_menu.setVisible(True)
        self.widget_page_table_1_hint_1_container.setVisible(False)
    
    @errorCatcher
    def updateSalaries(self):
        idNewSalary:dict = dict()
        
        operationType = self.comboBox_money_transactions_type_of_update.currentText()

        enteredAmount = float(self.spinBox_money_transactions_amount.text())

        employeesToBeUpdated = CheckBoxWidget.getInstances(Qt.CheckState.Checked)

        employee_ids:list = list()

        for checkBoxItem in employeesToBeUpdated:
            employee_ids.append(int(checkBoxItem.objectName()[checkBoxItem.objectName().find("_") + 1:]))
        
        for idToBeUpdated in employee_ids:
            for employeeRecord in self.queryResult:
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
        StandardMessageBox.Successful(self).exec()

    @handler
    def LoadEventScheduling(self):
        # Clear the input boxes
        self.lineEdit_event_name.clear()
        self.dateEdit_event_date.clear()
        self.textEdit_event_description.clear()
        
        # Open the related page
        self.stackedWidget_main_screen.setCurrentWidget(self.page_create_event)
        
        # Set focus on the line edit related to event name
        self.lineEdit_event_name.setFocus()

    @errorCatcher
    def ScheduleEvent(self):
        db_man_projectv3_test.add_event(event_name = self.lineEdit_event_name.text(),
                                   event_text = self.textEdit_event_description.toPlainText(),
                                   event_date = self.dateEdit_event_date.text())
        
        StandardMessageBox.Successful(self).exec()
        pass

    @handler
    def LoadUpcomingEvents(self, externalResult:tuple|list|None = None):
        CommonFeatures.LoadUpcomingEvents(self, externalResult)

    @handler
    def LoadIncomingMessages(self, externalResult:tuple|None = None):
        CommonFeatures.LoadIncomingMessages(self, externalResult)

    @handler
    def LoadDirectMessage(self):
        CommonFeatures.LoadDirectMessage(self)
    
    @errorCatcher
    def sendMessage(self):
        CommonFeatures.sendMessage(self)

    @handler
    def LoadGroupMessage(self):
        CommonFeatures.LoadGroupMessage(self)

    @handler
    def LoadGroupEmail(self):
        CommonFeatures.LoadGroupEmail(self)

    def LoadDirectMessageSecondStep(self):
        CommonFeatures.LoadDirectMessageSecondStep(self)
    
    @errorCatcher
    def sendGroupMessage(self):
        CommonFeatures.sendGroupMessage(self)

    def BackToGroupMessageEmployeeSelection(self):
        CommonFeatures.BackToGroupMessageEmployeeSelection(self)

    @errorCatcher    
    def replyMessage(self):
        CommonFeatures.replyMessage(self)

    @handler
    def LoadLeavePermissions(self, externalResult:tuple|list|None = None):
        if externalResult:
            self.queryResult = externalResult
        else:
            self.queryResult = db_man_projectv3_test.get_pending_leave_requests()
            if not self.queryResult:
                StandardMessageBox.NoResultsFound(self).exec()
                return
        
        self.tableWidget_table_1.clear()
        self.lbl_table_1_header.setText("Leave Requests")
        tableHeaders = ["ID", "Employee ID", "Status", "Request Date", "Approved By", "Approve Date", "Leave Type",
                        "Start Date", "End Date", "Total Dates", "Description", "Created At", "Answer"] # selection column for dynamic widget
        self.desiredDynamicButtons = ["Accept", "Reject"]

        setTable(self, table = self.tableWidget_table_1,
                 items = self.queryResult, rowHeaders = None, columnHeaders = tableHeaders,
                 cellWidgetAppend = True, ButtonWidgetType = "DoubleButtonWidget")
        
        # Close the control buttons under the table because they are not needed
        self.widget_table_1_btn_container.setVisible(False)

        self.stackedWidget_main_screen.setCurrentWidget(self.page_table_1)
        self.stackedWidget_side_menu.setCurrentWidget(self.page_expand_table)

    @errorCatcher
    def handleCellWidgetBtnClick(self, value):
        # value is a tuple returned from the special signal
        # where the first list is the row itself, second str
        # is the new status, e.g. accepted or rejected.
 
        # Update the sql record here
        if db_man_projectv3_test.arrangeText(value[1]) in ["accepted", "rejected"]:
            # That means it is a request approval
            if self.lbl_table_1_header.text() == "Special Requests":
                db_man_projectv3_test.process_special_request(request_id=int(value[0]),
                                                            status=value[1],
                                                            approved_by=int(self.currentEmployeeID))
            elif self.lbl_table_1_header.text() == "Leave Requests":
                db_man_projectv3_test.process_leave_request(leave_request_id=int(value[0]),
                                                            status_of_request=value[1],
                                                            approved_by=int(self.currentEmployeeID))
       
        if db_man_projectv3_test.arrangeText(value[1]) in ["delete", "remove"]:
            # That means something will be deleted
            # Check for the current page to determine the operation
            if self.stackedWidget_main_screen.currentWidget() == self.page_item_assignment:
                # If the current page is item assignment, delete button
                # is used to delete the items on the assignment table
                for row in range(self.tableWidget_item_assignment.rowCount()):
                    if db_man_projectv3_test.arrangeText(self.tableWidget_item_assignment.item(row, 0).text()) == db_man_projectv3_test.arrangeText(value[0]):
                        # Add the item back to the listWidget
                        self.listWidget_item_assignment.addItem(QListWidgetItem(value[0]))
                        # Clear selection
                        self.listWidget_item_assignment.clearSelection()
                        # Remove the item from the tableWidget
                        self.tableWidget_item_assignment.removeRow(row)
                        self.tableWidget_item_assignment.clearSelection()
                        # Update status
                        self.updateAssignStatus()
                       
            elif self.lbl_table_1_header.text() in ["Items Assigned to Employees", "Items Assigned to Employee"]:
                # Pass the proper value to the related function
                db_man_projectv3_test.remove_item_from_selected_employee(assign_id = int(value[0]))
                # After processing the function, hide the related row in order to avoid
                # any crash caused by repeating the process with the same assign_id
                for row in range(self.tableWidget_table_1.rowCount()):
                    if self.tableWidget_table_1.item(row, 0).text() == str(value[0]):
                        self.tableWidget_table_1.setRowHidden(row, True)
                        break

    @handler
    def LoadDashboard(self):
        self.stackedWidget_main_screen.setCurrentWidget(self.page_dashboard)
        self.stackedWidget_side_menu.setCurrentIndex(0)
        self.stackedWidget_side_menu.setVisible(False)

        self.lbl_count_pending_messages.setText(str(len(db_man_projectv3_test.see_messagev2(emp_id=self.currentEmployeeID))))
        self.lbl_count_pending_advance_requests.setText(str(len(db_man_projectv3_test.get_pending_special_requests())))
        self.lbl_count_pending_leave_permissions.setText(str(len(db_man_projectv3_test.get_pending_leave_requests())))
        self.lbl_count_upcoming_events.setText(str(len(db_man_projectv3_test.see_events())))
        
        # When the program loads the dashboard, dynamic objects are no longer needed
        clearDynamicInstances()

    @handler
    def LoadProfile(self):
        CommonFeatures.LoadProfile(self)

    @handler
    def LoadItemAssignment(self):
        self.queryResult = db_man_projectv3_test.load_employee_for_message_selection()
        if not self.queryResult:
            StandardMessageBox.NoResultsFound(self).exec()
            return
        
        # There is no need for dynamic buttons in the side menu
        self.desiredDynamicButtons = None

        # Do not forget to clear the record of the previous objects from the related
        # list, they are deleted, and cannot be used again.
        CheckBoxWidget.clearInstanceList()

        self.lbl_table_1_header.setText("Item Assignment Registration")
        tableHeaders = ["ID", "First Name", "Last Name", "Department", "Job Title", "Email", "Selection"] # selection column for dynamic widget
        
        setTable(self, table = self.tableWidget_table_1,
                 items = self.queryResult, rowHeaders = None, columnHeaders = tableHeaders, cellWidgetAppend = True,
                 ButtonWidgetType = "CheckBoxWidget", DynamicProperties={"checkState":False})

        self.stackedWidget_main_screen.setCurrentWidget(self.page_table_1)

        # Open the buttons under the table
        self.widget_table_1_btn_container.setVisible(True)

        # Make the second step ready in advance
        self.listWidget_item_assignment.clear()
        self.tableWidget_item_assignment.clearContents()
        self.tableWidget_item_assignment.setRowCount(0)
    
    def LoadItemAssignmentStep2(self):
        totalEmployees = len(CheckBoxWidget.getInstances(Qt.CheckState.Checked))
        if totalEmployees == 0:
            StandardMessageBox.Warning(self, "No Selection", "You haven't selected any employees yet. Make your selection(s) and try again.").exec()
            return
        self.items = db_man_projectv3_test.load_infos("items")
        self.stackedWidget_main_screen.setCurrentWidget(self.page_item_assignment)
        self.widget_table_1_btn_container.setVisible(False)
        self.lbl_item_assignment_info.setText(f"Items will be assigned to {totalEmployees} employees.")
        self.listWidget_item_assignment.addItems([item[1] for item in self.items])
    
    def add_item(self):
        totalEmployees = len(CheckBoxWidget.getInstances(Qt.CheckState.Checked))
        row_position = self.tableWidget_item_assignment.rowCount() 
        self.tableWidget_item_assignment.insertRow(row_position)
        try:
            selectedItem = self.listWidget_item_assignment.selectedItems()[0].text()
            desiredQuantity = self.spinBox_item_assignment_quantity.text()
            for item in self.items:
                if item[1] == selectedItem:
                    availableQuantity = item[2]
                    break
            if (totalEmployees * int(desiredQuantity)) > availableQuantity:
                stockError = "The number of items in stock is not suitable for the item assignment "\
                            "you requested. Check the stock status and item assignment quantities again."
                StandardMessageBox.Warning(self, "Stock Error", stockError).exec()
                raise IndexError()
            self.tableWidget_item_assignment.setItem(row_position, 0, QTableWidgetItem(selectedItem))
        except IndexError:
            # Delete the row added unnecessarily
            self.tableWidget_item_assignment.removeRow(row_position)
            # That means nothing selected on the listWidget. Ignore it
            return
        self.tableWidget_item_assignment.setItem(row_position, 1, QTableWidgetItem(desiredQuantity))

        btn = MonoButtonWidget(row_position, ([selectedItem, selectedItem]),
                               {"buttonType":"delete", "toolTip":"delete"})
        self.tableWidget_item_assignment.setCellWidget(row_position, 2, btn)
        btn.clicked_value.connect(self.handleCellWidgetBtnClick)
        self.tableWidget_item_assignment.setColumnWidth(3, 40)
        self.tableWidget_item_assignment.setRowHeight(row_position, 36)
        self.listWidget_item_assignment.takeItem(self.listWidget_item_assignment.currentRow())
        # Clear selection
        self.listWidget_item_assignment.clearSelection()
        # Update status
        self.updateAssignStatus()
    
    def resetAssignmentList(self):
        self.listWidget_item_assignment.clear()
        self.tableWidget_item_assignment.clearContents()
        self.tableWidget_item_assignment.setRowCount(0)
        MonoButtonWidget.clearInstanceList()
        self.lbl_item_assignment_overall.setText(f"Total 0 items with 0 pieces.")
        self.LoadItemAssignmentStep2()
    
    @errorCatcher
    def completeAssignment(self):
        if self.tableWidget_item_assignment.rowCount() == 0:
            StandardMessageBox.Warning(self, "No Selection", "You haven't selected any items yet. Make your selection(s) and try again.").exec()
            return
        # ID is used to assign items and names are also unique
        # Selection is made based on name
        # Get ids from names
        nameIDMatchDict = dict()
        for item in self.items:
            # names are the keys, values are the ids
            nameIDMatchDict[item[1]] = item[0]

        itemAssignDict = dict()
        for row in range(self.tableWidget_item_assignment.rowCount()):
            # Item name is present in the column with index 0
            itemName = self.tableWidget_item_assignment.item(row, 0).text()
            # Item quantity is present in the column with index 1
            itemQuantity = int(self.tableWidget_item_assignment.item(row, 1).text())
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
                db_man_projectv3_test.assign_item_to_employee_no_checking(id = employee_id, item_id = itemID, quantity = itemQuantity)
        
        StandardMessageBox.Successful(self).exec()
        

    def backToEmployeeSelection(self):
        self.stackedWidget_main_screen.setCurrentWidget(self.page_table_1)
        self.widget_table_1_btn_container.setVisible(True)
        # Make the second step ready in advance
        self.listWidget_item_assignment.clear()
        self.tableWidget_item_assignment.clearContents()
        self.tableWidget_item_assignment.setRowCount(0)

    def cancelItemAssignment(self):
        self.LoadDashboard()
    
    def updateAssignStatus(self):
        quantity = 0
        totalRow = self.tableWidget_item_assignment.rowCount()
        for row in range(self.tableWidget_item_assignment.rowCount()):
            quantity += int(self.tableWidget_item_assignment.item(row, 1).text())
        self.lbl_item_assignment_overall.setText(f"Total {totalRow} items with {quantity} pieces.")
    
    @handler    
    def LoadItemAssignmentList(self):
        self.queryResult = db_man_projectv3_test.load_item_list_with_name()
        if not self.queryResult:
            StandardMessageBox.NoResultsFound(self).exec()
            return

        self.desiredDynamicButtons = ["Delete Item"]
        self.lbl_table_1_header.setText("Items Assigned to Employees")
        self.tableWidget_table_1.clear()
        tableHeaders = ["Assign ID", "Employee ID", "First Name", "Last Name", "Item ID", "Item Name", "Quantity", "Assignment Date", "Action"]
        setTable(self, self.tableWidget_table_1, self.queryResult, None, tableHeaders, True, "MonoButtonWidget", {"buttonType":"delete", "toolTip":"delete"})
        self.stackedWidget_main_screen.setCurrentWidget(self.page_table_1)
    
    @handler    
    def LoadAssignedItemsToEmployee(self, emp_id, name:str = "", surname:str = ""):
        self.queryResult = db_man_projectv3_test.get_assigned_items(emp_id)
        if not self.queryResult:
            StandardMessageBox.NoResultsFound(self).exec()
            return
       
        if name == "" and surname == "":
            emp = "Employee"
        else:
            emp = " ".join([name, surname])
 
        self.desiredDynamicButtons = ["Delete Item"]
        self.lbl_table_1_header.setText(f"Items Assigned to Employee")
        self.tableWidget_table_1.clear()
        tableHeaders = ["Assign ID", "Item Name", "Assignment Date", "Action"]
        setTable(self, self.tableWidget_table_1, self.queryResult, None, tableHeaders, True, "MonoButtonWidget", {"buttonType":"delete", "toolTip":"delete"})
        self.stackedWidget_main_screen.setCurrentWidget(self.page_table_1)
    
    @handler
    def LoadTableView(self, externalResult:tuple|list, tableHeaders:list, header:str = "Results"):
        CommonFeatures.LoadTableView(self, externalResult, tableHeaders, header)

    @handler
    def LoadSignOut(self):
        print("Sign Out Requested!")

    def main_screen_changed(self, newIndex):
        # Each time main screen is changed, side menu restrictions should be removed
        self.closeSideMenu()

        # Each time main screen is changed, control buttons under the table should
        # automatically be opened. In cases that there is no need for them,
        # they are closed in the proper functions.
        self.widget_table_1_btn_container.setVisible(True)

        # Clear the search bar
        self.textEdit_page_search_search.setPlaceHolderText()

        # Close the buttons under the table
        self.widget_table_1_btn_container.setVisible(False) # XXX !!! XXX

        # Below, each time the main screen is changed, we disconnect
        # unnecessary signals and remove icons belonging to the previous
        # page for a better memory management. Likewise, we connect signals
        # and set icons belonging to the new page.

        if self.previousIndex != -1:
            initializer.ManagerInitializer.terminatePageWithIndex(self.previousIndex)(self)

        initializer.ManagerInitializer.initializePageWithIndex(newIndex)(self)

        self.previousIndex = newIndex
        

    def closeSideMenu(self):
        if self.previousSideMenuPage and self.previousSideMenuPage == self.page_money_transactions:
            if self.stackedWidget_side_menu.currentWidget() == self.page_quick_actions:
                # In this situation, closing the side menu has to open
                # the money transactions page. It cannot be closed
                self.stackedWidget_side_menu.setCurrentWidget(self.page_money_transactions)
                self.btn_quick_actions.setText("Quick Actions")
                # Do not go further.
                return
        # Do not care the sender. Just close the side menu.
        self.stackedWidget_side_menu.setVisible(False)

        # Set the sidemenu's current page to a page other than
        # money transactions, just in case
        self.stackedWidget_side_menu.setCurrentIndex(0)

        self.btn_quick_actions.setVisible(False)
        self.btn_quick_actions.setText("Quick Actions")


def main():
    import sys
    app = QApplication(sys.argv)
    window = ManagerApp()
    initializer.initializeManager(window)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()



