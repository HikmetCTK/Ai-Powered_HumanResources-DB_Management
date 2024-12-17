from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from manager_ui_form import *
import inspect
import db_man_projectv3
import datetime
import initializer
import inspect
from customs import *
import StandardMessageBox
from path_holder import *


class ManagerApp(QtWidgets.QMainWindow, Ui_ManagerWindow):
    func = None
    args = None
    kwargs = None
    def __init__(self, empId:int = 2, name:str = "Fevzi", surname:str = "FİDAN"):
        super().__init__()
        self.setupUi(self)

        # Store the ID of the current employee
        self.currentEmployeeID:int = empId
        self.name:str = name
        self.surname:str = surname
        self.lbl_dashboard_header.setText(f"Welcome, {self.name}")
        self.lbl_short_menu_name.setText(f"{self.name} {self.surname}")
        self.lbl_long_menu_name.setText(f"{self.name} {self.surname}")
        self.queryResult = None

        # XXX Try to call initializer XXX

        initializer.initialize(self)
        self.LoadDashboard()
    
    def handler(func:callable):
        def innerWrapper(self, *args, **kwargs):
            stack = inspect.stack()
            callerName = stack[1].function
            if callerName == "<module>":
                ManagerApp.func = func
                ManagerApp.args = args
                ManagerApp.kwargs = kwargs
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
        connection, msg = db_man_projectv3.connection_check()
        if connection == True:
            self.lbl_connection_icon.setPixmap(QPixmap(getPath("green_dot")))
            self.lbl_connection_status.setText("Connected")
        elif connection == False:
            self.lbl_connection_icon.setPixmap(QPixmap(getPath("red_dot")))
            self.lbl_connection_status.setText("Not connected")
        else:
            pass
            # self.showDialog("Error",
            #                 f"An error occurred during database connection check! connection: {connection} -> {type(connection)} | msg: {msg} -> {type(msg)}",
            #                 "Connection Check Error")

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
        else:
            # Close all of the submenus

            for i in range(1,6): # There are 5 submenu currently
                # Get the submenu object
                subMenu = getattr(self, f"widget_submenu_{i}")

                # Close the submenu
                subMenu.setVisible(False)
            
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
    
    def lineEditTextChanged(self):
        if self.textEdit_page_search_search.toPlainText() == "@":            
            button_pos = self.textEdit_page_search_search.mapToGlobal(self.textEdit_page_search_search.rect().bottomLeft())
            self.filterMenu.exec(button_pos)
        
        if not self.textEdit_page_search_search.toPlainText().startswith("@"):
            self.search_table(search_text = self.textEdit_page_search_search.toPlainText(), columnNumber = None)
        
        if self.textEdit_page_search_search.toPlainText() != self.textEdit_page_search_search.placeHolderText:
            self.btn_page_search_search.setVisible(True)
        else:
            self.btn_page_search_search.setVisible(False)
    
    @errorCatcher
    def search(self):
        tableMatchTable = {
            "Employees"       :"employees",
            "Special_requests":"special_requests",
            "Items"           :"items",
            "Messages"        :"messages",
            "Events_"         :"events_",
            "Employee_leaves" :"employee_leaves"
        }
        
        columnMatchTable = {
            "Employees"       :"first_name",
            "Special_requests":"request_type",
            "Items"           :"item_name",
            "Messages"        :"from_emp_id",
            "Events_"         :"event_name",
            "Employee_leaves" :"leave_type"
            }
        
        text = self.textEdit_page_search_search.toPlainText()
        filterArea = text[text.find("@")+1:text.find(" ")]

        searchKeyword = text[text.find("|")+1:].strip()
        searchTable = tableMatchTable[filterArea]
        searchColumn = columnMatchTable[filterArea]

        if filterArea == "Messages":
            # If the filter is for messages
            # Filtering is done based on sender name which corresponds to column with index 1
            result = db_man_projectv3.see_message(emp_id = self.currentEmployeeID)
            filteredResult = list()

            for record in result:
                if db_man_projectv3.arrangeText(searchKeyword) in db_man_projectv3.arrangeText(record[1]):
                    filteredResult.append(record,)        

            self.LoadIncomingMessages(externalResult=filteredResult)
        
        else:
            result = db_man_projectv3.search(keyword = searchKeyword,
                                                  table_name = searchTable,
                                                  column_name = searchColumn)
            
            if filterArea == "Employees":
                self.LoadViewEmployees(externalResult = result)
            elif filterArea == "Special_requests":
                self.LoadAdvanceTransactions(externalResult = result)
            elif filterArea == "Events_":
                self.LoadIncomingEvents(externalResult = result)
            elif filterArea == "Employee_leaves":
                self.LoadLeaveDefinitions(externalResult = result)
            elif filterArea == "Items":
                pass
            else:
                return
            
        pass

    def filterTrigger(self):
        action = self.sender()
        self.textEdit_page_search_search.setText(f"@{action.text().capitalize()} | ")
        self.textEdit_page_search_search.setTextColorUntilIndex(len(self.textEdit_page_search_search.toPlainText())-1)
    
    def handleWidgetClick(self, value):
        # Catch the values emitted by signals and run proper functions based on the values
        if value == 10001:
            self.LoadIncomingMessages()
        elif value == 10002:
            self.LoadAdvanceTransactions()
        elif value == 10003:
            self.LoadLeaveDefinitions()
        elif value == 10004:
            self.LoadIncomingEvents()
        else:
            pass
    
    def handleCellClick(self, row, column):
        if self.stackedWidget_side_menu.currentWidget().objectName() == "page_money_transactions" and self.stackedWidget_side_menu.isVisible():
            return # We do not want this screen to change because it is needed
        
        for item in self.created_right_menu_dynamic_widgets:
            try:
                self.verticalLayout_17.removeWidget(item)
                item.deleteLater()
                del item
            except:
                pass

        row_contents_dict = dict()

        if db_man_projectv3.arrangeText(self.lbl_table_1_header.text()) == db_man_projectv3.arrangeText("Incoming Messages"):
            # m.id,e.first_name,e.last_name,m.message_text,m.message_date,m.subject
            # fromInfo = John DOE
            fromInfo = self.tableWidget_table_1.item(row, 1).text() + " " + self.tableWidget_table_1.item(row, 2).text()
            self.lbl_expand_message_from_content.setText(fromInfo)

            # Get the message subject from the table to the related label
            self.lbl_expand_message_subject_content.setText(self.tableWidget_table_1.item(row, 5).text())
            
            # Get the message date from the table to the related label
            self.lbl_expand_message_message_date_content.setText(self.tableWidget_table_1.item(row, 4).text())

            # Get the message content to the textEdit
            self.textEdit_expand_message.setText(self.tableWidget_table_1.item(row, 3).text())

            # Open the side menu with the correct page
            self.stackedWidget_side_menu.setCurrentWidget(self.page_expand_message)
            self.stackedWidget_side_menu.setVisible(True)

            # Set the message as read
            db_man_projectv3.mark_message_as_read(int(self.tableWidget_table_1.item(row, 0).text()))

            # Do not go further. Below is for other standard expanding operations.
            return
        
        elif db_man_projectv3.arrangeText(self.lbl_table_1_header.text()) == db_man_projectv3.arrangeText("Incoming Events"):
            # Get the event id to the related label
            self.lbl_expand_message_from_content_2.setText(self.tableWidget_table_1.item(row, 0).text())

            # Get the event name to the related label
            self.lbl_expand_message_message_date_content_3.setText(self.tableWidget_table_1.item(row, 1).text())

            # Get the event date to the related label
            self.lbl_expand_message_message_date_content_2.setText(self.tableWidget_table_1.item(row, 3).text())

            # Get the event details to the textEdit
            self.textEdit_expand_event.setText(self.tableWidget_table_1.item(row, 2).text())

            # Open the side menu with the correct page
            self.stackedWidget_side_menu.setCurrentWidget(self.page_expand_event)
            self.stackedWidget_side_menu.setVisible(True)

            # Do not go further. Below is for other standard expanding operations.
            return

        for col in range(self.tableWidget_table_1.columnCount()):
            activeColumnName = self.tableWidget_table_1.horizontalHeaderItem(col).text()
            if not activeColumnName.endswith(":"): activeColumnName = activeColumnName + " :"
            item = self.tableWidget_table_1.item(row, col)
            cellWidget = self.tableWidget_table_1.cellWidget(row, col)
            if cellWidget:
                continue
            if item is not None:
                row_contents_dict[activeColumnName] = item.text()
            else:
                row_contents_dict[activeColumnName] = ""

        createSideMenuWidgets(self, row_contents_dict, self.desiredDynamicButtons)

        self.stackedWidget_side_menu.setVisible(True)
    
    def makeAllRowsVisible(self, table:QTableWidget) -> None:
        for row in range(table.rowCount()):
            table.setRowHidden(row, False)
    
    @errorCatcher
    def search_table(self, search_text:str, columnNumber:int|None = None):
        frame = inspect.currentframe()
        caller_frame = frame.f_back
        caller_name = caller_frame.f_code.co_name
        if db_man_projectv3.arrangeText(caller_name) != db_man_projectv3.arrangeText("search_table"):
            # If it is not a recursive call, we start searching from scratch. Make all rows visible.
            self.makeAllRowsVisible(self.tableWidget_table_1)

        search_text = search_text.strip() # Remove leading and trailing unnecessary space characters
        
        if search_text == "" or search_text == " ":
            return
        
        if search_text == "Search something, @filter to filter":
            for row in range(self.tableWidget_table_1.rowCount()):
                self.tableWidget_table_1.setRowHidden(row, False)
            
            return
        
        if len(search_text.split(" ")) == 1:
            # If search_text is a one-word search...
            for row in range(self.tableWidget_table_1.rowCount()):
                if self.tableWidget_table_1.isRowHidden(row):
                    continue
                row_hidden = True
                for column in range(self.tableWidget_table_1.columnCount()):
                    if columnNumber and columnNumber != column:
                        continue
                    item = self.tableWidget_table_1.item(row, column)
                    if item:
                        item = db_man_projectv3.arrangeText(item.text())
                        search_text = db_man_projectv3.arrangeText(search_text)
                        if search_text in item:
                            row_hidden = False # If match, show the row
                            break
                
                self.tableWidget_table_1.setRowHidden(row, row_hidden)
        
        else:
            # If search_text is a multi-word search...
            for word in search_text.split(" "):
                self.search_table(word)
        
    def eventFilter(self, obj, event):
        if obj == self.textEdit_page_search_search and event.type() == QEvent.Type.KeyPress:
            if event.key() == Qt.Key.Key_Backspace:
                self.lineEditTextChanged()
        
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
            placeHolderLabel = DoubleButtonWidget.getInstance("dynamicPlaceholderLabel"+"_"+id)
            if placeHolderLabel and placeHolderLabel.isVisible():
                # Once the related placeholder label appeared, it cannot be updated.
                return

            # Merge the parts and create the button's name
            buttonName = "dynamic" + senderButtonType + "_" + id

            button = DoubleButtonWidget.getInstance(buttonName)

            if button: button.click() # Trigger the button
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
                if res: self.closeSideMenu()
            elif senderButtonType == "Update":
                for index in range(1, len(outputList)):
                    # Index 0 belongs to dynamic button
                    # Actual data starts at index 1

                    if self.queryResult[0][index - 1] == None:
                        outputList[index] = None
                    elif isinstance(self.queryResult[0][index - 1], datetime.date):
                        outputList[index] = datetime.datetime.strptime(outputList[index], r"%Y-%m-%d")
                    else:
                        data_type = type(self.queryResult[0][index - 1])
                        # In the original query result, data starts at index 0

                        # Set the new data type to the original data type
                        outputList[index] = data_type(outputList[index])
                
                db_man_projectv3.update_employee(employee_id = outputList[1],
                                                      first_name = outputList[2],
                                                      last_name = outputList[3],
                                                      date_of_birth = outputList[4],
                                                      gender = outputList[5],
                                                      job_title = outputList[6],
                                                      department = outputList[7],
                                                      salary = outputList[8],
                                                      hire_date = outputList[9],
                                                      email = outputList[10],
                                                      phone_number = outputList[11],
                                                      password = outputList[12],
                                                      is_active = outputList[13])
            
            else:
                pass
            
    def showMenu(self):
        # Get peoplecards
        PeopleCardWidget.getPeopleCard(self, self.lineEdit_direct_message_to.text())

        # Open the menu based on the caller

        if self.sender():
            # That means the sender is btn_phone_book because
            # it is connected to this function
            # Open the menu under the line_edit_direct_message_to
            item = self.lineEdit_direct_message_to
        
        else:
            # That means the caller is the search button of the search bar
            # Open the menu under the search bar
            # XXX This feature is not included in this version. Ready for a
            # future update. XXX
            item = self.textEdit_page_search_search

        self.peopleCardMenu.exec(item.mapToGlobal(item.rect().bottomLeft()))
        
    def handleMessagePeopleCardClick(self, value):
        # If the current page is not the direct message page, open it
        if self.stackedWidget_main_screen.currentWidget() != self.page_send_message:
            self.LoadDirectMessage()
        
        # Catch the object name
        objectName = self.sender().objectName()
        name, _id, addt_info = objectName.split("*")
        self.lineEdit_direct_message_to.setText(name)
        self.lbl_direct_message_id.setText(_id)
        self.lbl_direct_message_department_job.setText(addt_info)
    
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
        if db_man_projectv3.arrangeText("Group Message") in db_man_projectv3.arrangeText(header):
            self.LoadDirectMessageSecondStep()
        
        elif db_man_projectv3.arrangeText("Group Email") in db_man_projectv3.arrangeText(header):
            self.LoadDirectMessageSecondStep()

        elif db_man_projectv3.arrangeText("Mass Dismissal") in db_man_projectv3.arrangeText(header):
            self.dismissEmployees()

        elif db_man_projectv3.arrangeText("Item Assignment") in db_man_projectv3.arrangeText(header):
            self.LoadItemAssignmentStep2()
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
        if db_man_projectv3.arrangeText(self.sender().text()) == db_man_projectv3.arrangeText("Accept All"):
            DoubleButtonWidget.acceptAll(self.tableWidget_table_1)
        else:
            CheckBoxWidget.checkAll(self.tableWidget_table_1)
    
    def clearAll(self):
        # Perform an easy check to determine it is for checkboxes or reject buttons
        if db_man_projectv3.arrangeText(self.sender().text()) == db_man_projectv3.arrangeText("Reject All"):
            DoubleButtonWidget.rejectAll(self.tableWidget_table_1)
        else:
            CheckBoxWidget.uncheckAll(self.tableWidget_table_1)
    
    def swapChoicesCheckBoxes(self):
        CheckBoxWidget.alternateSelection(self.tableWidget_table_1)

    @handler
    def LoadViewEmployees(self, cellWidgetAppend:bool = False, ButtonWidgetType:str|None = None,
                          DynamicProperties:dict|None = None, title:str="Employee List", externalResult:tuple|list|None = None):
        # There is no need for dynamic buttons in the side menu
        self.desiredDynamicButtons = ["Send Message", "Update", "Fire"]

        self.lbl_table_1_header.setText(title)
        self.tableWidget_table_1.clear()
        tableHeaders = ["ID", "First Name", "Last Name", "Date of Birth", "Gender", "Job Title", "Department",
                        "Salary", "Hire Date", "Email", "Phone Number", "Password", "Is Active"]
        if externalResult:
            self.queryResult = externalResult
        else:
            self.queryResult = db_man_projectv3.load_employee()
        row_count = len(self.queryResult)
        column_count = len(self.queryResult[0])

        if cellWidgetAppend: tableHeaders.append("Action"); column_count += 1

        setTable(self, rowCount = row_count, columnCount = column_count, table = self.tableWidget_table_1,
                 items = self.queryResult, rowHeaders = None, columnHeaders = tableHeaders,
                 cellWidgetAppend = cellWidgetAppend, ButtonWidgetType = ButtonWidgetType,
                 DynamicProperties = DynamicProperties)
        
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
        self.radioButton_hiring_male.setChecked(True)
        self.radioButton_hiring_show_and_send_email.setChecked(True)

        self.stackedWidget_main_screen.setCurrentWidget(self.page_new_staff_registration)
    
    @errorCatcher
    def hire(self):
        gender = "Male" if self.radioButton_hiring_male.isChecked() == True else "Female"
        try:
            employeePassword = db_man_projectv3.generateRandomPassword(8)
            db_man_projectv3.hiring(name = self.lineEdit_hiring_name.text(),
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
            if self.radioButton_hiring_just_show.isChecked() == True:
                StandardMessageBox.Information(self, "Employee Password", f"Hiring successful! Employee's initial password: {employeePassword}").exec()
            elif self.radioButton_hiring_show_and_send_email.isChecked() == True:
                StandardMessageBox.Information(self, "Employee Password", f"Hiring successful! Employee's initial password: {employeePassword}\n\nEmail including password has also been sent.").exec()
            elif self.radioButton_hiring_just_send_email.isChecked() == True:
                StandardMessageBox.Information(self, "Employee Password", f"Hiring successful! Employee's initial password has been sent to them by email.").exec()
            else:
                pass

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
            self.LoadViewEmployees(cellWidgetAppend = True, ButtonWidgetType="CheckBoxWidget",
                                   DynamicProperties={"checkState":False}, title = "Mass Dismissal")
            
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
                db_man_projectv3.not_working(externalEmpID)
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
                db_man_projectv3.not_working(employee_id)
        else:
            pass

    @handler
    def LoadAdvanceTransactions(self, externalResult:tuple|list|None = None):
        self.desiredDynamicButtons = ["Accept", "Reject"]
        self.tableWidget_table_1.clear()
        self.lbl_table_1_header.setText("Advance Requests")
        tableHeaders = ["Request ID", "Employee ID", "Request Type", "Request Amount", "Request Date", "Status",
                        "Approved By", "Answer Date", "Created At", "Selection"] # selection column for dynamic widget
        if externalResult:
            self.queryResult = externalResult
        else:
            self.queryResult = db_man_projectv3.get_pending_special_requests()
        row_count = len(self.queryResult)
        column_count = len(self.queryResult[0]) + 1 # + 1 for dynamic widget

        setTable(self, rowCount = row_count, columnCount = column_count, table = self.tableWidget_table_1,
                 items = self.queryResult, rowHeaders = None, columnHeaders = tableHeaders,
                 cellWidgetAppend = True, ButtonWidgetType = "DoubleButtonWidget")
        
        # Close the control buttons under the table because they are not needed
        self.widget_table_1_btn_container.setVisible(False)

        self.stackedWidget_main_screen.setCurrentWidget(self.page_table_1)
        self.stackedWidget_side_menu.setCurrentWidget(self.page_expand_table)

    def LoadBonusTransactions(self):
        pass

    def LoadExpensePayBack(self):
        pass

    @handler
    def LoadSalaryAdjustment(self):
        # There is no need for dynamic buttons in the side menu
        self.desiredDynamicButtons = None

        self.lbl_table_1_header.setText("Update Registration")
        self.tableWidget_table_1.clear()
        tableHeaders = ["ID", "First Name", "Last Name", "Department", "Job Title", "Salary", "Selection"]
        self.queryResult = db_man_projectv3.load_employee_for_salary_adjustment()
        row_count = len(self.queryResult)
        column_count = len(self.queryResult[0]) + 1 #  + 1 for actionWidget
        setTable(self, rowCount = row_count, columnCount = column_count, table = self.tableWidget_table_1,
                 items = self.queryResult, rowHeaders = None, columnHeaders = tableHeaders,
                 cellWidgetAppend = True, ButtonWidgetType = "CheckBoxWidget")
        
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
            db_man_projectv3.update_employee_salary(emp_id = empID, new_salary = salary)

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
        db_man_projectv3.add_event(event_name = self.lineEdit_event_name.text(),
                                        event_text = self.textEdit_event_description.toPlainText(),
                                        event_date = self.dateEdit_event_date.text())
        pass

    @handler
    def LoadIncomingEvents(self, externalResult:tuple|list|None = None):
        # There is no need for dynamic buttons in the side menu
        self.desiredDynamicButtons = None

        self.lbl_table_1_header.setText("Incoming Events")
        self.tableWidget_table_1.clear()
        tableHeaders = ["Event ID", "Event Name", "Details", "Date"]
        if externalResult:
            self.queryResult = externalResult
        else:
            self.queryResult = db_man_projectv3.see_events()
        row_count = len(self.queryResult)
        column_count = len(self.queryResult[0])

        setTable(self, rowCount = row_count, columnCount = column_count, table = self.tableWidget_table_1,
                 items = self.queryResult, rowHeaders = None, columnHeaders = tableHeaders)
        
        # Close the control buttons under the table, because there is no need for them
        self.widget_table_1_btn_container.setVisible(False)
        
        self.stackedWidget_main_screen.setCurrentWidget(self.page_table_1)

    @handler
    def LoadIncomingMessages(self, externalResult:tuple|None = None):
        # There is no need for dynamic buttons in the side menu
        self.desiredDynamicButtons = None

        self.lbl_table_1_header.setText("Incoming Messages")
        self.tableWidget_table_1.clear()
        if externalResult:
            self.queryResult = externalResult
        else:
            self.queryResult = db_man_projectv3.see_message(emp_id = self.currentEmployeeID)
        tableHeaders = ["Message ID", "Name", "Surname", "Content", "Date"]
        column_count = len(self.queryResult[0])
        row_count = len(self.queryResult)

        setTable(self, rowCount = row_count, columnCount = column_count, table = self.tableWidget_table_1,
                 items = self.queryResult, rowHeaders = None, columnHeaders = tableHeaders)
        
        self.stackedWidget_main_screen.setCurrentWidget(self.page_table_1)

    @handler
    def LoadDirectMessage(self):
        self.lineEdit_direct_message_to.clear()
        self.lineEdit_direct_message_subject.clear()
        self.lbl_direct_message_id.clear()
        self.lbl_direct_message_department_job.clear()
        self.textEdit_direct_message.clear()

        self.stackedWidget_main_screen.setCurrentWidget(self.page_send_message)
    
    @errorCatcher
    def sendMessage(self):
        db_man_projectv3.send_message_anyone(from_id = int(self.currentEmployeeID),
                                             employee_ids = [int(self.lbl_direct_message_id.text())],
                                             message = self.textEdit_direct_message.toPlainText(),
                                             subject = self.lineEdit_direct_message_subject.text())
        
        # Show a message box and call LoadDirectMessage

    @handler
    def LoadGroupMessage(self):
        # There is no need for dynamic buttons in the side menu
        self.desiredDynamicButtons = None

        # Do not forget to clear the record of the previous objects from the related
        # list, they are deleted, and cannot be used again.
        CheckBoxWidget.clearInstanceList()

        self.tableWidget_table_1.clear()
        self.lbl_table_1_header.setText("Send Group Message")
        tableHeaders = ["ID", "First Name", "Last Name", "Department", "Job Title", "Selection"] # selection column for dynamic widget
        self.queryResult = db_man_projectv3.load_employee_for_message_selection()
        row_count = len(self.queryResult) + 1
        column_count = len(self.queryResult[0]) + 1 # +1 for selection column

        setTable(self, rowCount = row_count, columnCount = column_count, table = self.tableWidget_table_1,
                 items = self.queryResult, rowHeaders = None, columnHeaders = tableHeaders,
                 cellWidgetAppend = True, ButtonWidgetType = "CheckBoxWidget")

        self.stackedWidget_main_screen.setCurrentWidget(self.page_table_1)

        # Open the buttons under the table
        self.widget_table_1_btn_container.setVisible(True)

    @handler
    def LoadGroupEmail(self):
        self.LoadGroupMessage()
        self.lbl_table_1_header.setText("Send Group Email")
        pass

    def LoadDirectMessageSecondStep(self):
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
        self.lineEdit_group_message_step_2_subject.clear()
        self.textEdit_group_message.clear()
        if len(messageReceivers) == 0:
            # Print a warning message and do not go further.
            pass

        # Message type can be email or message
        messageType = self.lbl_table_1_header.text().split(" ")[-1]
        self.lbl_group_message_step_2_info.setText(f"{messageType} will be sent to {len(messageReceivers)} people.")

        self.lbl_direct_message_step_2_header.setText(f"Group {messageType}")

        self.stackedWidget_main_screen.setCurrentWidget(self.page_group_message_step_2)
    
    @errorCatcher
    def sendGroupMessage(self):
        messageReceivers = CheckBoxWidget.getInstances(Qt.CheckState.Checked)

        subject = self.lineEdit_direct_message_subject.text()
        message = self.textEdit_group_message.toPlainText()

        employee_ids:list = list()

        for checkBoxItem in messageReceivers:
            employee_ids.append(int(checkBoxItem.objectName()[checkBoxItem.objectName().find("_") + 1:]))
        
        if db_man_projectv3.arrangeText("email") in db_man_projectv3.arrangeText(self.lbl_table_1_header.text()):
            # If the user wants to send group email
            func = db_man_projectv3.send_email
        else:
            # If the user wants to send group message
            func = db_man_projectv3.send_message_anyone

        func(from_id = int(self.currentEmployeeID),
             employee_ids = employee_ids,
             subject = subject,
             message = message)
        
        # Show a message box and turn back to dashboard.

    def BackToGroupMessageEmployeeSelection(self):
        self.stackedWidget_main_screen.setCurrentWidget(self.page_table_1)

        # Open the buttons under the table
        self.widget_table_1_btn_container.setVisible(True)

    @handler
    def LoadLeaveDefinitions(self, externalResult:tuple|list|None = None):
        self.tableWidget_table_1.clear()
        self.lbl_table_1_header.setText("Leave Requests")
        tableHeaders = ["ID", "Employee ID", "Status", "Request Date", "Approved By", "Approve Date", "Leave Type",
                        "Start Date", "End Date", "Description", "Total Dates", "Created At", "Selection"] # selection column for dynamic widget
        self.desiredDynamicButtons = ["Accept", "Reject"]
        if externalResult:
            self.queryResult = externalResult
        else:
            self.queryResult = db_man_projectv3.get_pending_leave_requests()
        row_count = len(self.queryResult)
        column_count = len(self.queryResult[0]) + 1 # + 1 for dynamic widget

        setTable(self, rowCount = row_count, columnCount = column_count, table = self.tableWidget_table_1,
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
        print(value)
        # Update the sql record here
        if db_man_projectv3.arrangeText(value[1]) in ["accepted", "rejected"]:
            # That means it is a request approval
            
            db_man_projectv3.process_special_request(request_id=int(value[0]),
                                                        status=value[1],
                                                        approved_by=int(self.currentEmployeeID))
        
        if db_man_projectv3.arrangeText(value[1]) in ["delete", "remove"]:
            # That means something will be deleted
            # Check for the current page to determine the operation
            if self.stackedWidget_main_screen.currentWidget() == self.page_item_assignment:
                # If the current page is item assignment, delete button
                # is used to delete the items on the assignment table
                for row in range(self.tableWidget_item_assignment.rowCount()):
                    if db_man_projectv3.arrangeText(self.tableWidget_item_assignment.item(row, 0).text()) == db_man_projectv3.arrangeText(value[0]):
                        # Add the item back to the listWidget
                        self.listWidget_item_assignment.addItem(QListWidgetItem(value[0]))
                        # Clear selection
                        self.listWidget_item_assignment.clearSelection()
                        # Remove the item from the tableWidget
                        self.tableWidget_item_assignment.removeRow(row)
                        self.tableWidget_item_assignment.clearSelection()
                        # Update status
                        self.updateAssignStatus()
                        return

    @handler
    def LoadDashboard(self):
        self.stackedWidget_main_screen.setCurrentWidget(self.page_dashboard)
        self.stackedWidget_side_menu.setCurrentIndex(0)
        self.stackedWidget_side_menu.setVisible(False)

        self.lbl_count_pending_messages.setText(str(len(db_man_projectv3.see_message(emp_id=self.currentEmployeeID))))
        self.lbl_count_pending_advance_requests.setText(str(len(db_man_projectv3.get_pending_special_requests())))
        self.lbl_count_pending_leave_permissions.setText(str(len(db_man_projectv3.get_pending_leave_requests())))
        self.lbl_count_upcoming_events.setText(str(len(db_man_projectv3.see_events())))

    @handler
    def LoadProfile(self):
        self.queryResult = db_man_projectv3.search(keyword = self.currentEmployeeID, table_name = "employees", column_name = "employee_id")
        employee = self.queryResult[0]
        
        # General Information part
        self.lbl_profile_name_content.setText(str(employee[1]))
        self.lbl_profile_surname_content.setText(str(employee[2]))
        self.lbl_profile_date_of_birth_content.setText(str(employee[3]))
        self.lbl_profile_email_content.setText(str(employee[9]))
        self.lbl_profile_gender_content.setText(str(employee[4]))
        self.lbl_profile_phone_number_content.setText(str(employee[10]))
        
        # Business Information part
        self.lbl_profile_employee_id_content.setText(str(employee[0]))
        self.lbl_profile_department_content.setText(str(employee[6]))
        self.lbl_profile_job_title_content.setText(str(employee[5]))
        self.lbl_profile_salary_content.setText(str(employee[7]))
        self.lbl_profile_hire_date_content.setText(str(employee[8]))
        self.lbl_profile_status_content.setText(str(employee[12]))
        
        # Open the related page
        self.stackedWidget_main_screen.setCurrentWidget(self.page_profile)

    @handler
    def LoadItemAssignment(self):
        # There is no need for dynamic buttons in the side menu
        self.desiredDynamicButtons = None

        # Do not forget to clear the record of the previous objects from the related
        # list, they are deleted, and cannot be used again.
        CheckBoxWidget.clearInstanceList()

        self.tableWidget_table_1.clear()
        self.lbl_table_1_header.setText("Item Assignment Registration")
        tableHeaders = ["ID", "First Name", "Last Name", "Department", "Job Title", "Selection"] # selection column for dynamic widget
        self.queryResult = db_man_projectv3.load_employee_for_message_selection()
        row_count = len(self.queryResult)
        column_count = len(self.queryResult[0]) + 1 # +1 for selection column

        setTable(self, rowCount = row_count, columnCount = column_count, table = self.tableWidget_table_1,
                 items = self.queryResult, rowHeaders = None, columnHeaders = tableHeaders,
                 cellWidgetAppend = True, ButtonWidgetType = "CheckBoxWidget")

        self.stackedWidget_main_screen.setCurrentWidget(self.page_table_1)

        # Open the buttons under the table
        self.widget_table_1_btn_container.setVisible(True)

        # Make the second step ready in advance
        self.listWidget_item_assignment.clear()
        self.tableWidget_item_assignment.clearContents()
        self.tableWidget_item_assignment.setRowCount(0)
    
    def LoadItemAssignmentStep2(self):
        self.items = db_man_projectv3.load_infos("items")
        self.stackedWidget_main_screen.setCurrentWidget(self.page_item_assignment)
        self.widget_table_1_btn_container.setVisible(False)
        totalEmployees = len(CheckBoxWidget.getInstances(Qt.CheckState.Checked))
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
                db_man_projectv3.assign_item_to_employee_no_checking(id = employee_id, item_id = itemID, quantity = itemQuantity)

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
    def LoadSignOut(self):
        print("Sign Out Requested!")

    def main_screen_changed(self):
        # Each time main screen is changed, side menu restrictions should be removed
        self.closeSideMenu()

        # Each time main screen is changed, control buttons under the table should
        # automatically be opened. In cases that there is no need for them,
        # they are closed in the proper functions.
        self.widget_table_1_btn_container.setVisible(True)

        # Clear the search bar
        self.textEdit_page_search_search.setPlaceHolderText()

        # Close the buttons under the table
        self.widget_table_1_btn_container.setVisible(False)
    
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = ManagerApp()
    window.show()
    sys.exit(app.exec())



