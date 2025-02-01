from PyQt6.QtWidgets import QMainWindow, QSpinBox, QListWidgetItem
from PyQt6.QtCore import pyqtSlot, QEvent
from Manager_Side.manager_ui_form import Ui_ManagerWindow
import db_man_projectv3_test
from package import *
from package.Customs import *
from package.PathHolder import *
from package.Initializer.ManagerInitializer import ManagerInitializer
from package.Initializer import Terminator
from package.Wrapper import handler, errorCatcher

from Manager_Side.ManagerModules import *

class ManagerApp(QMainWindow, Ui_ManagerWindow):
    func = None
    args = None
    kwargs = None
    def __init__(self, empId:int, name:str, surname:str, role:str):
        super().__init__()
        self.setupUi(self)

        # Store the important information of the current employee
        self.currentEmployeeID:int = empId
        self.name:str = name
        self.surname:str = surname
        self.role:str = role

        # Welcome the user
        self.lbl_dashboard_header.setText(f"Welcome, {self.name}")
        self.lbl_short_menu_name.setText(f"{self.name} {self.surname}")
        self.lbl_long_menu_name.setText(f"{self.name} {self.surname}")
        self.showUserRole()

        # Store the result of the lastly executed query
        self.queryResult = None

        # Page index, used to terminate the closed page
        self.previousIndex = 0

        # Store icons for connected, disconnected, and not controlled
        self.connectedIcon = QPixmap(":/newSource/icons/green_dot.png")
        self.disconnectedIcon = QPixmap(":/newSource/icons/red_dot.png")
        self.notControlledIcon = QPixmap(":/newSource/icons/white_dot.png")

        # Connect textChanged event of the lineEdit for email in hiring page
        # We connect it here because it is the only lineEdit whose signal
        # is connected to a function.
        # Once the signal is connected, it will not be disconnected again
        self.lineEdit_hiring_email.textChanged.connect(self.adjustEmailStatus)

        # Set the main table which will be used for the operations on table
        self.mainTable = self.tableWidget_table_1

        # Initialize main screen and make the program ready
        ManagerInitializer.initializeMainScreen(self)
        
        # Load the main screen
        self.LoadDashboard()
    
    def showUserRole(self):
        CommonFeatures.showUserRole(self)
    
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
            # Better to turn back to dashboard
            self.LoadDashboard()
    
    @pyqtSlot(bool)
    def on_action_toggled(self, checked):
        action = self.sender()
        if checked:
            if action.text() == "Never":
                self.timer.stop()
                self.lbl_connection_icon.setPixmap(self.notControlledIcon)
                self.lbl_connection_status.setText("Not Controlled!")
            else:
                self.time_period = int(action.text()[0:action.text().find(" ")].strip()) * 1000
                self.timer.start(self.time_period)
    
    def adjustEmailStatus(self):
        CommonFeatures.adjustEmailStatus(self)
    
    def on_preference_toggled(self, checked):
        CommonFeatures.on_preference_toggled(self, checked)
    
    def updateConnectionStatus(self):
        CommonFeatures.updateConnectionStatus(self)
    
    def clearDynamicInstances(self):
        # Clear all the objects that have been dynamically
        # created during runtime

        # They are cleared when they are no longer useless
        # or they are no longer needed

        CheckBoxWidget.clearInstanceList()
        MonoButtonWidget.clearInstanceList()
        DoubleButtonWidget.clearInstanceLists()
    
    def clearSideBarDynamicWidgets(self):
        # Clear all the objects that have been dynamically
        # created and placed in side menu during runtime

        for item in self.created_right_menu_dynamic_widgets:
            try:
                self.sideBarVerticalLayout.removeWidget(item)
                item.disconnect()
                item.close()
                item.deleteLater()
            except:
                pass
        
        self.created_right_menu_dynamic_widgets.clear()

    def shortMenuBarEnterEvent(self, event):
        CommonFeatures.shortMenuBarEnterEvent(self, event)

    def shortMenuBarLeaveEvent(self, event):
        CommonFeatures.shortMenuBarLeaveEvent(self, event)
    
    def scrollAreaEnterEvent(self, event):
        CommonFeatures.scrollAreaEnterEvent(self, event)

    def scrollAreaLeaveEvent(self, event):
        CommonFeatures.scrollAreaLeaveEvent(self, event)
    
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
        CustomTextEdit.textChanged_(self, self.sender())
    
    @errorCatcher
    def search(self):
        Search.search(self)

    def filterTrigger(self):
        # Triggered by pop-up filter menu reached from search bar
        action = self.sender()
        self.textEdit_page_search_search.setText(f"@{action.text().capitalize()} | ")
        self.textEdit_page_search_search.setTextColorUntilIndex(len(self.textEdit_page_search_search.toPlainText())-1)
    
    def eventFilter(self, obj, event):
        if obj == self.textEdit_page_search_search and event.type() == QEvent.Type.KeyPress:
            if event.key() == Qt.Key.Key_Backspace:
                self.textEditTextChanged()
            elif event.key() in [Qt.Key.Key_Return, Qt.Key.Key_Enter]:
                if self.btn_page_search_search.isVisible() == True:
                    self.btn_page_search_search.click()
        
        # We should show quick actions button if there are checkbox needs and side menu is visible        
        elif obj == self.stackedWidget_side_menu:
            if event.type() == event.Type.ShowToParent:
                # Check whether the suitable objects exist or not
                # We have no business with dynamicLabels for this operation, but it is an
                # easy-to-reach indicative showing whether quick actions button is needed or not
                if len(CheckBoxWidget.instances) or len(DoubleButtonWidget.dynamicLabelInstances):
                    self.btn_quick_actions.setVisible(True)
                    self.btn_quick_actions.setText("Quick Actions")
            
            elif event.type() == event.Type.Hide:
                # Once the side menu is closed in any way...

                # the dynamic objects placed within it must be deleted
                self.clearSideBarDynamicWidgets()
                
                # chatbot must be restarted
                self.restartChatBotAgent()
            
        return super().eventFilter(obj, event)
    
    def handleWidgetClick(self, value):
        CommonFeatures.handleWidgetClick(self, value)
    
    def handleCellClick(self, row, column):
        # Get the relevant table
        table = self.sender()

        if ManagerApp.func.__name__ == "LoadSalaryAdjustment":
            # We do not want the current screen of the side menu to change because it is needed
            return
        
        self.clearSideBarDynamicWidgets()

        if ManagerApp.func.__name__ == "LoadIncomingMessages":
            ExpandTable.expand_message(self, row, column, table)

            # Do not go further.
            return
        
        elif ManagerApp.func.__name__ == "LoadUpcomingEvents":
            ExpandTable.expand_event(self, row, column, table)

            # Do not go further.
            return

        else:
            # Standard expand table operation
            ExpandTable.expand_table(self, row, column, table)
    
    @errorCatcher
    def search_table(self, search_text:str, columnNumber:int|None = None):
        Search.search_table(self, search_text, columnNumber)

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
                # If the lineEdit is the one that we created dynamically
                if lineEdit.objectName().startswith("dynamic"):
                    outputList.append(lineEdit.text())
        
        senderButtonType = outputList[0][outputList[0].find("_") + 1:] # Accept / Reject / ...
        id = outputList[1]
        
        if senderButtonType in ["Accept", "Reject"]:
            SideBarButtonFunctions.approval(senderButtonType, id)
        else:
            # Meaning that the clicked button is not related with a
            # button that is present in the table

            # Get the text on the button
            if senderButtonType == "Send Message":
                # Load direct message page and fill in the required information
                self.LoadDirectMessage()
                # Set to part to the name + surname of the employee
                self.lineEdit_direct_message_to.setText(outputList[2] + " " + outputList[3])
                # Set id part to the id of the employee
                self.lbl_direct_message_id.setText(outputList[1])
                # Set department / job part based on employee's information
                self.lbl_direct_message_department_job.setText(outputList[7] + " / " + outputList[6])
            
            elif senderButtonType == "Fire":
                # Run a process to dismiss the related employee
                res = self.dismissEmployees(int(outputList[1]))
                if res: self.closeSideMenu(); StandardMessageBox.Successful(self).exec()
            
            elif senderButtonType == "Update":
                # Run a process to update the related records
                SideBarButtonFunctions.update(self.queryResult, outputList)
                StandardMessageBox.Successful(self).exec()
            
            elif senderButtonType == "Assigned Items":
                # Show items assigned to the related employee
                self.LoadAssignedItemsToEmployee(emp_id = id, name = outputList[2], surname = outputList[3])
            
            else:
                pass
            
    def showPeopleCardMenu(self):
        CommonFeatures.showPeopleCardMenu(self)
        
    def handlePeopleCardClick(self, value):
        CommonFeatures.handlePeopleCardClick(self, value)
    
    def LoadQuickActionsPage(self):
        CommonFeatures.LoadQuickActionsPage(self)

    @errorCatcher
    def HandleTablePageController(self):
        """
        In this function, we set the behavior of the next button
        on the table page. We determine the function that will be
        called based on the last executed function.
        """

        funcName = ManagerApp.func.__name__

        if funcName == "LoadGroupMessage":
            self.LoadDirectMessageSecondStep()
        
        elif funcName == "LoadGroupEmail":
            self.LoadDirectMessageSecondStep()

        elif funcName == "LoadDismissal":
            self.dismissEmployees()

        elif funcName == "LoadItemAssignment":
            self.LoadItemAssignmentStep2()
        
        else:
            pass

    def selectAll(self):
        CommonFeatures.selectAll(self, self.tableWidget_table_1)
    
    def clearAll(self):
        CommonFeatures.clearAll(self, self.tableWidget_table_1)
    
    def swapChoicesCheckBoxes(self):
        CommonFeatures.swapChoicesCheckBoxes(self, self.tableWidget_table_1)

    @handler
    def LoadViewEmployees(self, cellWidgetAppend:bool = False, ButtonWidgetType:str|None = None,
                          DynamicProperties:dict|None = None, title:str="Employee List",
                          externalResult:tuple|list|None = None):
                
        ViewEmployees.LoadViewEmployees(self, cellWidgetAppend, ButtonWidgetType, DynamicProperties,
                                        title, externalResult)

    @handler
    def LoadHiring(self):

        Hiring.LoadHiring(self)
    
    @errorCatcher
    def hire(self):
        
        Hiring.hire(self)

    @handler
    def LoadDismissal(self):

        Dismissal.LoadDismissal(self)

    @errorCatcher
    def dismissEmployees(self, externalEmpID:int|None = None):

        Dismissal.dismissEmployees(self, externalEmpID)

    @handler
    def LoadAdvanceTransactions(self, externalResult:tuple|list|None = None):

        Transactions.LoadAdvanceTransactions(self, externalResult)

    @handler
    def LoadSalaryAdjustment(self):

        Transactions.LoadSalaryAdjustment(self)
    
    @errorCatcher
    def updateSalaries(self):

        Transactions.updateSalaries(self)

    @handler
    def LoadEventScheduling(self):

        EventScheduling.LoadEventScheduling(self)

    @errorCatcher
    def ScheduleEvent(self):

        EventScheduling.ScheduleEvent(self)

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

        LeavePermissions.LoadLeavePermissions(self, externalResult)

    @errorCatcher
    def handleCellWidgetBtnClick(self, value):
        # value is a tuple returned from the special signal
        # where the first item is the id of the record, second
        # str is the operation name which can be a new status,
        # e.g. (accepted or rejected) or something like delete
        # or remove.

        # Get the id emitted by the signal (need the original
        # form, not the comparable form)
        _id = str(value[0])
        
        # Get the comparable form of the operation name
        operationName = db_man_projectv3_test.arrangeText(str(value[1]))

        # Update the sql record here
        if operationName in ["accepted", "rejected"]:
            # That means it is a request approval
            if ManagerApp.func.__name__ == "LoadAdvanceTransactions":
                db_man_projectv3_test.process_special_request(request_id=int(_id),
                                                              status=operationName,
                                                              approved_by=int(self.currentEmployeeID))
            elif ManagerApp.func.__name__ == "LoadLeavePermissions":
                db_man_projectv3_test.process_leave_request(leave_request_id=int(_id),
                                                            status_of_request=operationName,
                                                            approved_by=int(self.currentEmployeeID))
            # Do not go further
            return
        
        if operationName in ["delete", "remove"]:
            # Get the table that we are working on
            placedWidget = self.sender().placedWidget
            # We will need the corresponding record (row) in the table, find the row number
            for row in range(placedWidget.rowCount()):
                # Loop through the table to find the corresponding row number
                item = placedWidget.item(row, 0)
                if not item:
                    continue

                elif db_man_projectv3_test.arrangeText(item.text()) == db_man_projectv3_test.arrangeText(_id):
                    # Compare the record id emitted by the signal with the id of the
                    # record coming from the row in the table
                    rowNumber = row
                    break

                else:
                    rowNumber = None
            
            if rowNumber == None:
                StandardMessageBox.Warning(self, "Error",
                                           "Something went wrong with the table. Restart and try again.").exec()
                return

            # That means something will be deleted
            # Check for the current page to determine the operation
            if ManagerApp.func.__name__ == "LoadItemAssignment":
                # If the current page is item assignment, delete button
                # is used to delete the items on the assignment table
                
                # Add the item back to the listWidget
                # Note: In item assignment, item names are considered as their ids
                self.listWidget_item_assignment.addItem(QListWidgetItem(_id))
                # Clear selection
                self.listWidget_item_assignment.clearSelection()
                # Remove the item from the tableWidget
                placedWidget.removeRow(rowNumber)
                placedWidget.clearSelection()
                # Update status
                self.updateAssignStatus()
                        
            elif ManagerApp.func.__name__ in ["LoadItemAssignmentList", "LoadAssignedItemsToEmployee"]:
                # Pass the proper value to the related function
                db_man_projectv3_test.remove_item_from_selected_employee(assign_id = int(_id))
                # After processing the function, hide the related row in order to avoid
                # any crash caused by repeating the process with the same assign_id
                placedWidget.setRowHidden(rowNumber, True)

    @handler
    def LoadDashboard(self):

        Dashboard.LoadDashboard(self)

    @handler
    def LoadProfile(self):
        CommonFeatures.LoadProfile(self)

    @handler
    def LoadItemAssignment(self):

        ItemAssignment.LoadItemAssignment(self)
    
    def LoadItemAssignmentStep2(self):

        ItemAssignment.LoadItemAssignmentStep2(self)
    
    def add_item(self):

        ItemAssignment.addItemToSelectionTable(self)
    
    def resetAssignmentList(self):

        ItemAssignment.resetAssignmentTable(self)
    
    @errorCatcher
    def completeAssignment(self):

        ItemAssignment.completeAssignment(self)
        
    def backToEmployeeSelection(self):

        ItemAssignment.backToEmployeeSelection(self)

    def cancelItemAssignment(self):

        ItemAssignment.cancelItemAssignment(self)
    
    def updateAssignStatus(self):

        ItemAssignment.updateAssignStatus(self)
    
    @handler    
    def LoadItemAssignmentList(self):

        ItemAssignment.LoadItemAssignmentList(self)
    
    @handler    
    def LoadAssignedItemsToEmployee(self, emp_id, name:str = "", surname:str = ""):

        ItemAssignment.LoadAssignedItemsToEmployee(self, emp_id, name, surname)
    
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
        self.widget_table_1_btn_container.setVisible(False) # XXX

        # Below, each time the main screen is changed, we disconnect
        # unnecessary signals for a better memory management.
        # Likewise, we connect signals belonging to the new page.

        if self.previousIndex != -1:
            Terminator.terminatePageWithIndex(self.stackedWidget_main_screen, self.previousIndex)

        ManagerInitializer.initializePageWithIndex(newIndex)(self)

        self.previousIndex = newIndex
        

    def closeSideMenu(self):
        if ManagerApp.func.__name__ == "LoadSalaryAdjustment":
            # The salary adjustment page of the side menu belonging to salary adjustment
            # property is needed and cannot be closed until the current main screen
            # moves to another page.

            # If the close request came from the quick actions page, go back to
            # the salary adjustment page.
            self.stackedWidget_side_menu.setCurrentWidget(self.page_money_transactions)
            self.btn_quick_actions.setText("Quick Actions")
            return
        
        # Do not care the sender. Just close the side menu.
        self.stackedWidget_side_menu.setVisible(False)

        # Set the sidemenu's current page to a page other than
        # money transactions, just in case
        self.stackedWidget_side_menu.setCurrentIndex(0)

        self.btn_quick_actions.setVisible(False)
        self.btn_quick_actions.setText("Quick Actions")
    
    def addMessageToChatBotArea(self, msg, color = "#FFFFFF"):

        ChatBot.addMessageToChatBotArea(self, msg, color)
    
    def restartChatBotAgent(self):

        ChatBot.restartChatBotAgent(self)
    
    def getResponseFromChatBot(self, response):
        
        ChatBot.getResponseFromChatBot(self, response)
    
    def isChatBotInputPermitted(self, isWorking):
        
        ChatBot.isChatBotInputPermitted(self, isWorking)

    def sendMessageToChatBot(self):
        
        ChatBot.sendMessageToChatBot(self)
    
    def LoadChatBot(self):
        
        ChatBot.LoadChatBot(self)


if __name__ == "__main__":
    raise RuntimeError("Do not run this file as main!")


# END