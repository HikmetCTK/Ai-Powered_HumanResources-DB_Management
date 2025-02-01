from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import pyqtSlot, QEvent
from PyQt6.QtGui import QPixmap
from Employee_Side.employee_ui_form import Ui_EmployeeWindow
from package import *
from package.Customs import *
from package.PathHolder import *
from package.Initializer.EmployeeInitializer import EmployeeInitializer
from package.Initializer import Terminator
from package.Wrapper import handler, errorCatcher

from Employee_Side.EmployeeModules import *

class EmployeeApp(QMainWindow, Ui_EmployeeWindow):
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
        self.previousIndex = -1
        
        # Store icons for connected, disconnected, and not controlled
        self.connectedIcon = QPixmap(":/newSource/icons/green_dot.png")
        self.disconnectedIcon = QPixmap(":/newSource/icons/red_dot.png")
        self.notControlledIcon = QPixmap(":/newSource/icons/white_dot.png")

        # Set the main table which will be used for the operations on table
        self.mainTable = self.tableWidget_table_1

        # Initialize main screen and make the program ready
        EmployeeInitializer.initializeMainScreen(self)
        
        # Load the main screen
        self.LoadDashboard()
    
    def showUserRole(self):
        CommonFeatures.showUserRole(self)
    
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
                self.lbl_connection_icon.setPixmap(self.notControlledIcon)
                self.lbl_connection_status.setText("Not Controlled!")
            else:
                self.time_period = int(action.text()[0:action.text().find(" ")].strip()) * 1000
                self.timer.start(self.time_period)
    
    def on_preference_toggled(self, checked):
        CommonFeatures.on_preference_toggled(self, checked)
    
    def updateConnectionStatus(self):
        CommonFeatures.updateConnectionStatus(self)

    def shortMenuBarEnterEvent(self, event):
        CommonFeatures.shortMenuBarEnterEvent(self, event)

        # Close all the submenus to provide a good-looking experience
        self.toggleSubMenu()

    def shortMenuBarLeaveEvent(self, event):
        pass
    
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
        CustomTextEdit.textChanged_(self, self.sender())
    
    @errorCatcher
    def search(self):
        Search.search(self)

    def filterTrigger(self):
        # Triggered by pop-up filter menu reached from search bar
        action = self.sender()
        self.textEdit_page_search_search.setText(f"@{action.text().capitalize()} | ")
        self.textEdit_page_search_search.setTextColorUntilIndex(len(self.textEdit_page_search_search.toPlainText())-1)
    
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
    
    def handleWidgetClick(self, value):
        CommonFeatures.handleWidgetClick(self, value)
    
    def handleCellClick(self, row, column):
        # Get the relevant table
        table = self.sender()

        self.clearSideBarDynamicWidgets()

        if EmployeeApp.func.__name__ == "LoadIncomingMessages":
            ExpandTable.expand_message(self, row, column, table)

            # Do not go further.
            return
        
        elif EmployeeApp.func.__name__ == "LoadUpcomingEvents":
            ExpandTable.expand_event(self, row, column, table)

            # Do not go further.
            return

        else:
            # Standard expand table operation
            ExpandTable.expand_table(self, row, column, table)
    
    @errorCatcher
    def search_table(self, search_text:str, columnNumber:int|None = None):
        Search.search_table(self, search_text, columnNumber)
        
    def eventFilter(self, obj, event):
        if obj == self.textEdit_page_search_search and event.type() == QEvent.Type.KeyPress:
            if event.key() == Qt.Key.Key_Backspace:
                self.textEditTextChanged()
            elif event.key() in [Qt.Key.Key_Return, Qt.Key.Key_Enter]:
                if self.btn_page_search_search.isVisible() == True:
                    self.btn_page_search_search.click()
        
        # We should show quick actions button if there are checkbox needs and side menu is visible        
        elif obj == self.stackedWidget_side_menu and event.type() == event.Type.ShowToParent:
            # Check whether the suitable objects exist or not
            # We have no business with dynamicLabels for this operation, but it is an
            # easy-to-reach indicative showing whether DoubleButtonWidgets exist or not
            if len(CheckBoxWidget.instances) or len(DoubleButtonWidget.dynamicLabelInstances):
                self.btn_quick_actions.setVisible(True)
                self.btn_quick_actions.setText("Quick Actions")
            
            elif event.type() == event.Type.Hide:
                # Once the side menu is closed in any way,
                # the dynamic objects placed within it must be deleted.
                self.clearSideBarDynamicWidgets()
            
        return super().eventFilter(obj, event)
            
    def showPeopleCardMenu(self):
        CommonFeatures.showPeopleCardMenu(self)
        
    def handlePeopleCardClick(self, value):
        CommonFeatures.handlePeopleCardClick(self, value)
    
    def LoadQuickActionsPage(self):
        CommonFeatures.LoadQuickActionsPage(self)

    @errorCatcher
    def HandleTablePageController(self):
        funcName = EmployeeApp.func.__name__

        if funcName == "LoadGroupMessage":
            self.LoadDirectMessageSecondStep()
        
        elif funcName == "LoadGroupEmail":
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
        CommonFeatures.selectAll(self, self.tableWidget_table_1)
    
    def clearAll(self):
        CommonFeatures.clearAll(self, self.tableWidget_table_1)
    
    def swapChoicesCheckBoxes(self):
        CommonFeatures.swapChoicesCheckBoxes(self, self.tableWidget_table_1)

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
        pass

    @handler
    def LoadDashboard(self):
        Dashboard.LoadDashboard(self)

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
        self.widget_table_1_btn_container.setVisible(False) # XXX

        # Below, each time the main screen is changed, we disconnect
        # unnecessary signals belonging to the previous page for a
        # better memory management. Likewise, we connect signals
        # belonging to the new page.

        if self.previousIndex != -1:
            Terminator.terminatePageWithIndex(self.stackedWidget_main_screen, self.previousIndex)

        EmployeeInitializer.initializePageWithIndex(newIndex)(self)

        self.previousIndex = newIndex
    
    @handler
    def LoadCreateNewLeaveRequest(self):
        LeaveRequest.LoadCreateNewLeaveRequest(self)
    
    @errorCatcher
    def ApplyLeaveRequest(self):
        LeaveRequest.ApplyLeaveRequest(self)
    
    @handler
    def LoadCreateNewSpecialRequest(self):
        SpecialRequest.LoadCreateNewSpecialRequest(self)
    
    @errorCatcher
    def ApplySpecialRequest(self):
        SpecialRequest.ApplySpecialRequest(self)
    
    @handler
    def LoadPastLeaveRequests(self):
        LeaveRequest.LoadPastLeaveRequests(self)
    
    @handler
    def LoadPastSpecialRequests(self):
        SpecialRequest.LoadPastSpecialRequests(self)
    
    @handler
    def LoadPendingLeaveRequests(self):
        LeaveRequest.LoadPendingLeaveRequests(self)
    
    @handler
    def LoadPendingSpecialRequests(self):
        SpecialRequest.LoadPendingSpecialRequests(self)
    
    @handler
    def LoadAssignedItemsToEmployee(self):
        ItemAssignment.LoadAssignedItemsToEmployee(self)
    
    @handler
    def LoadTableView(self, externalResult:tuple|list, tableHeaders:list, header:str = "Results"):
        CommonFeatures.LoadTableView(self, externalResult, tableHeaders, header)
        

    def closeSideMenu(self):
        self.stackedWidget_side_menu.setVisible(False)

        self.stackedWidget_side_menu.setCurrentIndex(0)

        self.btn_quick_actions.setVisible(False)
        self.btn_quick_actions.setText("Quick Actions")


if __name__ == "__main__":
    raise RuntimeError("Do not run this file as main!")


# END