from PyQt6.QtWidgets import QMainWindow, QSpinBox, QMessageBox, QListWidgetItem, QApplication, QMenu
from PyQt6.QtCore import pyqtSlot, QEvent, QPoint
from PyQt6.QtGui import QPixmap
from employee_ui_form import Ui_EmployeeWindow
import db_man_projectv3_test, initializer, StandardMessageBox, search, expand_table, SideBarButtonFuctions, CommonFeatures
from path_holder import *
import datetime
import inspect
from customs import *


class EmployeeApp(QMainWindow, Ui_EmployeeWindow):
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
        initializer.EmployeeInitializer.initializeMainScreen(self)

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
                EmployeeApp.func = func
                EmployeeApp.args = args
                EmployeeApp.kwargs = kwargs
            try:
                func(self, *args, **kwargs)
            except TypeError:
                func(self)
            except Exception as e:
                StandardMessageBox.Error(self, "Error (handler)", f"An error occurred during the latest process! | {str(e)}").exec()
            
            # Delete unnecessary local variables
            del stack, callerName
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
        if EmployeeApp.func:
            try:
                EmployeeApp.func(self, *EmployeeApp.args, **EmployeeApp.kwargs)
            except TypeError:
                EmployeeApp.func(self)
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
        if clickedMenu == "btn_long_menu_leave_requests":
            relatedSubMenu = self.widget_submenu_1
        elif clickedMenu == "btn_long_menu_special_requests":
            relatedSubMenu = self.widget_submenu_2
        elif clickedMenu == "btn_long_menu_communication":
            relatedSubMenu = self.widget_submenu_3
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
        for item in self.created_right_menu_dynamic_widgets:
            try:
                self.expandTableVerticalLayout.removeWidget(item)
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
        CheckBoxWidget.checkAll(self.tableWidget_table_1)
    
    def clearAll(self):
        CheckBoxWidget.uncheckAll(self.tableWidget_table_1)
    
    def swapChoicesCheckBoxes(self):
        CheckBoxWidget.alternateSelection(self.tableWidget_table_1)

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

    @errorCatcher
    def handleCellWidgetBtnClick(self, value):
        # value is a tuple returned from the special signal
        # where the first list is the row itself, second str
        # is the new status, e.g. accepted or rejected.
        pass

    @handler
    def LoadDashboard(self):
        self.stackedWidget_main_screen.setCurrentWidget(self.page_dashboard)
        self.stackedWidget_side_menu.setCurrentIndex(0)
        self.stackedWidget_side_menu.setVisible(False)

        self.lbl_count_pending_messages.setText(str(len(db_man_projectv3_test.see_messagev2(emp_id=self.currentEmployeeID))))
        self.lbl_count_pending_advance_requests.setText(str(len(db_man_projectv3_test.pending_special_requests_for_employee(employee_id=self.currentEmployeeID))))
        self.lbl_count_pending_leave_permissions.setText(str(len(db_man_projectv3_test.pending_leave_requests_for_employee(employee_id=self.currentEmployeeID))))
        self.lbl_count_upcoming_events.setText(str(len(db_man_projectv3_test.see_events())))
        
        # When the program loads the dashboard, dynamic objects are no longer needed
        clearDynamicInstances()

    @handler
    def LoadProfile(self):
        CommonFeatures.LoadProfile(self)    

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
            initializer.EmployeeInitializer.terminatePageWithIndex(self.previousIndex)(self)

        initializer.EmployeeInitializer.initializePageWithIndex(newIndex)(self)

        self.previousIndex = newIndex
    
    @handler
    def LoadCreateNewLeaveRequest(self):
        self.comboBox_leave_request_leave_type.setCurrentIndex(0)
        self.dateEdit_leave_request_start_date.clear()
        self.dateEdit_leave_request_end_date.clear()
        self.textEdit_leave_request_description.clear()
        self.stackedWidget_main_screen.setCurrentWidget(self.page_leave_request)
    
    @errorCatcher
    def ApplyLeaveRequest(self):
        print(self.dateEdit_leave_request_end_date.text())
        db_man_projectv3_test.create_leave_request(employee_id=self.currentEmployeeID,
                                                   leave_type=self.comboBox_leave_request_leave_type.currentText(),
                                                   start_date = datetime.datetime.strptime(self.dateEdit_leave_request_start_date.text(), r"%Y-%m-%d").date(),
                                                   end_date = datetime.datetime.strptime(self.dateEdit_leave_request_end_date.text(), r"%Y-%m-%d").date(),
                                                   desc_request=self.textEdit_leave_request_description.toPlainText())
        
        StandardMessageBox.Successful(self).exec()
    
    @handler
    def LoadCreateNewSpecialRequest(self):
        self.comboBox_special_request_request_type.setCurrentIndex(0)
        self.spinBox_special_request_request_amount.clear()
        self.textEdit_special_request_description.clear()
        self.stackedWidget_main_screen.setCurrentWidget(self.page_special_request)
    
    @errorCatcher
    def ApplySpecialRequest(self):
        db_man_projectv3_test.create_special_request(employee_id=self.currentEmployeeID,
                                                     request_type=self.comboBox_special_request_request_type.currentText(),
                                                     request_amount=round(float(self.spinBox_special_request_request_amount.text()), 2),
                                                     description=self.textEdit_special_request_description.toPlainText())
        StandardMessageBox.Successful(self).exec()
    
    @handler
    def LoadPastLeaveRequests(self):
        self.queryResult = db_man_projectv3_test.leave_request_status_for_employee(employee_id=self.currentEmployeeID)
        if not self.queryResult:
            StandardMessageBox.NoResultsFound(self).exec()
            return
        
        self.lbl_table_1_header.setText("Leave Request Application History")
        self.tableWidget_table_1.clear()
        tableHeaders = ["Leave Type", "Application Status", "Request Date", "Answer Date"]
        setTable(self, self.tableWidget_table_1, self.queryResult, None, tableHeaders, False)
        self.stackedWidget_main_screen.setCurrentWidget(self.page_table_1)
    
    @handler
    def LoadPastSpecialRequests(self):
        self.queryResult = db_man_projectv3_test.special_request_status_for_employee(employee_id=self.currentEmployeeID)
        if not self.queryResult:
            StandardMessageBox.NoResultsFound(self).exec()
            return
        
        self.lbl_table_1_header.setText("Special Request Application History")
        self.tableWidget_table_1.clear()
        tableHeaders = ["Request Type", "Application Status", "Request Date", "Answer Date"]
        setTable(self, self.tableWidget_table_1, self.queryResult, None, tableHeaders, False)
        self.stackedWidget_main_screen.setCurrentWidget(self.page_table_1)
    
    @handler
    def LoadPendingLeaveRequests(self):
        self.queryResult = db_man_projectv3_test.pending_leave_requests_for_employee(employee_id=self.currentEmployeeID)
        if not self.queryResult:
            StandardMessageBox.NoResultsFound(self).exec()
            return
        
        self.lbl_table_1_header.setText("Your Pending Leave Requests")
        self.tableWidget_table_1.clear()
        tableHeaders = ["Leave Type", "Application Status", "Request Date", "Answer Date"]
        setTable(self, self.tableWidget_table_1, self.queryResult, None, tableHeaders, False)
        self.stackedWidget_main_screen.setCurrentWidget(self.page_table_1)
    
    @handler
    def LoadPendingSpecialRequests(self):
        self.queryResult = db_man_projectv3_test.pending_special_requests_for_employee(employee_id=self.currentEmployeeID)
        if not self.queryResult:
            StandardMessageBox.NoResultsFound(self).exec()
            return
        
        self.lbl_table_1_header.setText("Your Pending Special Requests")
        self.tableWidget_table_1.clear()
        tableHeaders = ["Request Type", "Application Status", "Request Date", "Answer Date"]
        setTable(self, self.tableWidget_table_1, self.queryResult, None, tableHeaders, False)
        self.stackedWidget_main_screen.setCurrentWidget(self.page_table_1)
    
    @handler
    def LoadAssignedItemsToEmployee(self):
        self.queryResult = db_man_projectv3_test.get_assigned_items(self.currentEmployeeID)
        if not self.queryResult:
            StandardMessageBox.NoResultsFound(self).exec()
            return

        self.lbl_table_1_header.setText(f"Items Assigned To You")
        self.tableWidget_table_1.clear()
        tableHeaders = ["Assign ID", "Item Name", "Assignment Date"]
        setTable(self, self.tableWidget_table_1, self.queryResult, None, tableHeaders, False)
        self.stackedWidget_main_screen.setCurrentWidget(self.page_table_1)
    
    @handler
    def LoadTableView(self, externalResult:tuple|list, tableHeaders:list, header:str = "Results"):
        CommonFeatures.LoadTableView(self, externalResult, tableHeaders, header)
        

    def closeSideMenu(self):
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
    window = EmployeeApp()
    initializer.initializeEmployee(window)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()



