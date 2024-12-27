from PyQt6.QtWidgets import QMenu, QAbstractItemView
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QIcon, QAction, QActionGroup
from datetime import datetime
from customs import *
from path_holder import *
import db_man_projectv3_test

class ManagerInitializer:

    @staticmethod
    def initializeMainMenu(obj):
        obj.btn_long_menu_view_employees.clicked.connect(obj.LoadViewEmployees)
        obj.btn_long_menu_hiring.clicked.connect(obj.LoadHiring)
        obj.btn_long_menu_dismissal.clicked.connect(obj.LoadDismissal)
        obj.btn_long_menu_advance_transactions.clicked.connect(obj.LoadAdvanceTransactions)
        obj.btn_long_menu_salary_adjustment.clicked.connect(obj.LoadSalaryAdjustment)
        obj.btn_long_menu_event_scheduling.clicked.connect(obj.LoadEventScheduling)
        obj.btn_long_menu_upcoming_events.clicked.connect(obj.LoadUpcomingEvents)
        obj.btn_long_menu_incoming_messages.clicked.connect(obj.LoadIncomingMessages)
        obj.btn_long_menu_send_message.clicked.connect(obj.LoadDirectMessage)
        obj.btn_long_menu_send_group_message.clicked.connect(obj.LoadGroupMessage)
        obj.btn_long_menu_send_group_email.clicked.connect(obj.LoadGroupEmail)
        obj.btn_long_menu_leave_definitions.clicked.connect(obj.LoadLeavePermissions)
        obj.btn_long_menu_assign_items.clicked.connect(obj.LoadItemAssignment)
        obj.btn_long_menu_check_assigned_items.clicked.connect(obj.LoadItemAssignmentList)
        obj.btn_long_menu_home.clicked.connect(obj.LoadDashboard)
        obj.btn_long_menu_profile.clicked.connect(obj.LoadProfile)
        obj.btn_long_menu_sign_out.clicked.connect(obj.LoadSignOut)

        # Set all of the sub-menus' visibility to False
        obj.widget_submenu_1.setVisible(False)
        obj.widget_submenu_2.setVisible(False)
        obj.widget_submenu_3.setVisible(False)
        obj.widget_submenu_4.setVisible(False)
        obj.widget_submenu_5.setVisible(False)

        # Connect the textChanged signal of the search bar
        obj.textEdit_page_search_search.textChanged.connect(obj.textEditTextChanged)

        # In the beginning, short menu will be visible, long menu will be unvisible
        obj.scrollArea_short_menu.setVisible(True)
        obj.scrollArea_long_menu.setVisible(False)

        # Once a menu is clicked, its submenu should be opened. Connect the functions
        obj.btn_long_menu_general.clicked.connect(obj.toggleSubMenu)
        obj.btn_long_menu_employment.clicked.connect(obj.toggleSubMenu)
        obj.btn_long_menu_transactions.clicked.connect(obj.toggleSubMenu)
        obj.btn_long_menu_plans.clicked.connect(obj.toggleSubMenu)
        obj.btn_long_menu_communication.clicked.connect(obj.toggleSubMenu)
        obj.btn_long_menu_item_assignments.clicked.connect(obj.toggleSubMenu)

        # Right side menu is set invisible initially
        obj.closeSideMenu()

        # Set icons
        obj.btn_short_menu_general.setIcon(IconManager.getIcon("general"))
        obj.btn_short_menu_employment.setIcon(IconManager.getIcon("employment"))
        obj.btn_short_menu_transactions.setIcon(IconManager.getIcon("transactions"))
        obj.btn_short_menu_plans.setIcon(IconManager.getIcon("plan"))
        obj.btn_short_menu_communication.setIcon(IconManager.getIcon("messages_1"))
        obj.btn_short_menu_leave_definitions.setIcon(IconManager.getIcon("permission"))
        obj.btn_short_menu_item_assignments.setIcon(IconManager.getIcon("item"))
        obj.btn_short_menu_home.setIcon(IconManager.getIcon("home"))
        obj.btn_short_menu_profile.setIcon(IconManager.getIcon("profile_2"))
        obj.btn_short_menu_sign_out.setIcon(IconManager.getIcon("sign_out"))

        obj.btn_long_menu_general.setIcon(IconManager.getIcon("general"))
        obj.btn_long_menu_employment.setIcon(IconManager.getIcon("employment"))
        obj.btn_long_menu_transactions.setIcon(IconManager.getIcon("transactions"))
        obj.btn_long_menu_plans.setIcon(IconManager.getIcon("plan"))
        obj.btn_long_menu_communication.setIcon(IconManager.getIcon("messages_1"))
        obj.btn_long_menu_leave_definitions.setIcon(IconManager.getIcon("permission"))
        obj.btn_long_menu_item_assignments.setIcon(IconManager.getIcon("item"))
        obj.btn_long_menu_home.setIcon(IconManager.getIcon("home"))
        obj.btn_long_menu_profile.setIcon(IconManager.getIcon("profile_2"))
        obj.btn_long_menu_sign_out.setIcon(IconManager.getIcon("sign_out"))

        obj.btn_long_menu_view_employees.setIcon(IconManager.getIcon("view_employees"))
        obj.btn_long_menu_hiring.setIcon(IconManager.getIcon("hiring"))
        obj.btn_long_menu_dismissal.setIcon(IconManager.getIcon("dismissal"))
        obj.btn_long_menu_advance_transactions.setIcon(IconManager.getIcon("advance_transaction"))
        obj.btn_long_menu_salary_adjustment.setIcon(IconManager.getIcon("salary_adjustment"))
        obj.btn_long_menu_upcoming_events.setIcon(IconManager.getIcon("event"))
        obj.btn_long_menu_event_scheduling.setIcon(IconManager.getIcon("event_2"))
        obj.btn_long_menu_incoming_messages.setIcon(IconManager.getIcon("get_message"))
        obj.btn_long_menu_send_message.setIcon(IconManager.getIcon("send_message"))
        obj.btn_long_menu_send_group_message.setIcon(IconManager.getIcon("group"))
        obj.btn_long_menu_send_group_email.setIcon(IconManager.getIcon("email_2"))

    @staticmethod
    def terminateMainMenu(obj):
        obj.btn_long_menu_view_employees.clicked.disconnect()
        obj.btn_long_menu_hiring.clicked.disconnect()
        obj.btn_long_menu_dismissal.clicked.disconnect()
        obj.btn_long_menu_advance_transactions.clicked.disconnect()
        obj.btn_long_menu_salary_adjustment.clicked.disconnect()
        obj.btn_long_menu_event_scheduling.clicked.disconnect()
        obj.btn_long_menu_upcoming_events.clicked.disconnect()
        obj.btn_long_menu_incoming_messages.clicked.disconnect()
        obj.btn_long_menu_send_message.clicked.disconnect()
        obj.btn_long_menu_send_group_message.clicked.disconnect()
        obj.btn_long_menu_send_group_email.clicked.disconnect()
        obj.btn_long_menu_leave_definitions.clicked.disconnect()
        obj.btn_long_menu_item_assignments.clicked.disconnect()
        obj.btn_long_menu_home.clicked.disconnect()
        obj.btn_long_menu_profile.clicked.disconnect()
        obj.btn_long_menu_sign_out.clicked.disconnect()

        # Disconnect the textChanged signal of the search bar
        obj.textEdit_page_search_search.textChanged.disconnect()

        # Disconnect the signals of the buttons opening submenus
        obj.btn_long_menu_general.disconnect()
        obj.btn_long_menu_employment.disconnect()
        obj.btn_long_menu_transactions.disconnect()
        obj.btn_long_menu_plans.disconnect()
        obj.btn_long_menu_communication.disconnect()

    @staticmethod
    def initializeMainScreen(obj):
        # Connect the custom widget's clicked signals
        obj.m_widget_summary_pm.clickedValue.connect(obj.handleWidgetClick)
        obj.m_widget_summary_par.clickedValue.connect(obj.handleWidgetClick)
        obj.m_widget_summary_plp.clickedValue.connect(obj.handleWidgetClick)
        obj.m_widget_summary_ue.clickedValue.connect(obj.handleWidgetClick)

        # Set icons
        obj.lbl_summary_1_icon.setPixmap(IconManager.getIcon("messages_1", "pixmap"))
        obj.lbl_summary_2_icon.setPixmap(IconManager.getIcon("advance_transaction_1", "pixmap"))
        obj.lbl_summary_3_icon.setPixmap(IconManager.getIcon("permission", "pixmap"))
        obj.lbl_summary_4_icon.setPixmap(IconManager.getIcon("event", "pixmap"))

        expand_icon = IconManager.getIcon("expand_1", "pixmap")

        obj.lbl_dashboard_expand_icon_1.setPixmap(expand_icon)
        obj.lbl_dashboard_expand_icon_2.setPixmap(expand_icon)
        obj.lbl_dashboard_expand_icon_3.setPixmap(expand_icon)
        obj.lbl_dashboard_expand_icon_4.setPixmap(expand_icon)

    @staticmethod
    def terminateMainScreen(obj):
        # Disconnect the custom widget's clicked signals
        obj.m_widget_summary_pm.clickedValue.disconnect()
        obj.m_widget_summary_par.clickedValue.disconnect()
        obj.m_widget_summary_plp.clickedValue.disconnect()
        obj.m_widget_summary_ue.clickedValue.disconnect()

        # Remove icons
        obj.lbl_summary_1_icon.clear()
        obj.lbl_summary_2_icon.clear()
        obj.lbl_summary_3_icon.clear()
        obj.lbl_summary_4_icon.clear()

        obj.lbl_dashboard_expand_icon_1.clear()
        obj.lbl_dashboard_expand_icon_2.clear()
        obj.lbl_dashboard_expand_icon_3.clear()
        obj.lbl_dashboard_expand_icon_4.clear()

    @staticmethod
    def initializeHiring(obj):
        obj.btn_hiring_complete.clicked.connect(obj.hire)
        obj.btn_hiring_clear_all.clicked.connect(obj.LoadHiring)
        
        obj.btn_hiring_complete.setIcon(IconManager.getIcon("complete", "icon"))
        obj.btn_hiring_clear_all.setIcon(IconManager.getIcon("mop", "icon"))
    
    @staticmethod
    def terminateHiring(obj):
        obj.btn_hiring_complete.clicked.disconnect()
        obj.btn_hiring_clear_all.clicked.disconnect()

        obj.btn_hiring_complete.setIcon(QIcon())
        obj.btn_hiring_clear_all.setIcon(QIcon())
    
    @staticmethod
    def initializeDirectMessage(obj):
        obj.btn_direct_message_send.clicked.connect(obj.sendMessage)
        obj.btn_direct_message_cancel.clicked.connect(obj.LoadDashboard)

        # Set icons
        obj.btn_direct_message_cancel.setIcon(IconManager.getIcon("cancel", "icon"))
        obj.btn_direct_message_send.setIcon(IconManager.getIcon("complete", "icon"))
        obj.btn_phone_book.setIcon(IconManager.getIcon("phone_book", "icon"))

    @staticmethod
    def terminateDirectMessage(obj):
        obj.btn_direct_message_send.clicked.disconnect()
        obj.btn_direct_message_cancel.clicked.disconnect()

        # Remove icons
        obj.btn_direct_message_cancel.setIcon(QIcon())
        obj.btn_direct_message_send.setIcon(QIcon())
        obj.btn_phone_book.setIcon(QIcon())
    
    @staticmethod
    def initializeTablePage(obj):
        # Connect cellClicked signal of the table_1
        obj.tableWidget_table_1.cellClicked.connect(obj.handleCellClick)
        obj.btn_table_1_next.clicked.connect(obj.HandleTablePageController)
        obj.btn_table_1_cancel.clicked.connect(obj.LoadDashboard)

        # For reply button to appear, table_1 page should be opened.
        # When table_1 page is opened, connect the reply message signal

        obj.btn_reply_message.clicked.connect(obj.replyMessage)

        # Set icons
        obj.btn_table_1_cancel.setIcon(IconManager.getIcon("cancel" "icon"))
        obj.btn_table_1_next.setIcon(IconManager.getIcon("next", "icon"))
        obj.lbl_page_table_1_hint_1_icon.setPixmap(IconManager.getIcon("hint_icon", "pixmap"))
    
    @staticmethod
    def terminateTablePage(obj):
        # Disconnect cellClicked signal of the table_1
        obj.tableWidget_table_1.cellClicked.disconnect()
        obj.btn_table_1_next.clicked.disconnect()
        obj.btn_table_1_cancel.clicked.disconnect()

        # When the table_1 page is closed, reply message button can no longer be used
        # Disconnect the signal
        obj.btn_reply_message.clicked.disconnect()

        # Remove icons
        obj.btn_table_1_cancel.setIcon(QIcon())
        obj.btn_table_1_next.setIcon(QIcon())
        obj.lbl_page_table_1_hint_1_icon.clear()
    
    @staticmethod
    def initializeGroupMessage(obj):
        obj.btn_group_message_step_2_back.clicked.connect(obj.BackToGroupMessageEmployeeSelection)
        obj.btn_group_message_step_2_cancel.clicked.connect(obj.LoadDashboard)
        obj.btn_group_message_step_2_send.clicked.connect(obj.sendGroupMessage)

        # Set icons
        obj.lbl_group_message_step_2_info_icon.setPixmap(IconManager.getIcon("info", "pixmap"))
        obj.btn_group_message_step_2_cancel.setIcon(IconManager.getIcon("cancel", "icon"))
        obj.btn_group_message_step_2_back.setIcon(IconManager.getIcon("back", "icon"))
        obj.btn_group_message_step_2_send.setIcon(IconManager.getIcon("complete", "icon"))

    @staticmethod
    def terminateGroupMessage(obj):
        obj.btn_group_message_step_2_back.clicked.disconnect()
        obj.btn_group_message_step_2_cancel.clicked.disconnect()
        obj.btn_group_message_step_2_send.clicked.disconnect()

        # Remove icons
        obj.lbl_group_message_step_2_info_icon.clear()
        obj.btn_group_message_step_2_cancel.setIcon(QIcon())
        obj.btn_group_message_step_2_back.setIcon(QIcon())
        obj.btn_group_message_step_2_send.setIcon(QIcon())
    
    @staticmethod
    def initializeMoneyTransactions(obj):
        obj.btn_money_transactions_complete.clicked.connect(obj.updateSalaries)
        obj.btn_money_transactions_cancel.clicked.connect(obj.LoadDashboard)
    
    @staticmethod
    def terminateMoneyTransactions(obj):
        obj.btn_money_transactions_complete.clicked.disconnect()
        obj.btn_money_transactions_cancel.clicked.disconnect()
    
    @staticmethod
    def initializeEventScheduling(obj):
        obj.btn_event_scheduling_cancel.clicked.connect(obj.LoadDashboard)
        obj.btn_event_scheduling_complete.clicked.connect(obj.ScheduleEvent)

        # Set icons
        obj.btn_event_scheduling_cancel.setIcon(IconManager.getIcon("cancel", "icon"))
        obj.btn_event_scheduling_complete.setIcon(IconManager.getIcon("complete", "icon"))
        obj.lbl_event_scheduling_event_date_icon.setPixmap(IconManager.getIcon("calendar", "pixmap"))
        obj.lbl_event_scheduling_event_name_icon.setPixmap(IconManager.getIcon("event_name", "pixmap"))
    
    @staticmethod
    def terminateEventScheduling(obj):
        obj.btn_event_scheduling_cancel.clicked.disconnect()
        obj.btn_event_scheduling_complete.clicked.disconnect()

        # Remove icons
        obj.btn_event_scheduling_cancel.setIcon(QIcon())
        obj.btn_event_scheduling_complete.setIcon(QIcon())
        obj.lbl_event_scheduling_event_date_icon.clear()
        obj.lbl_event_scheduling_event_name_icon.clear()
    
    @staticmethod
    def initializeProfile(obj):
        # Set icons
        obj.lbl_profile_info_icon.setPixmap(IconManager.getIcon("info", "pixmap"))

    @staticmethod
    def terminateProfile(obj):
        # Remove icons
        obj.lbl_profile_info_icon.clear()
    
    @staticmethod
    def initializeSideMenuCloseButtons(obj):
        # Connect right menu close buttons to a common function
        obj.btn_right_menu_close_expand_table.clicked.connect(obj.closeSideMenu)
        obj.btn_right_menu_close_message_content.clicked.connect(obj.closeSideMenu)
        obj.btn_right_menu_close_event_content.clicked.connect(obj.closeSideMenu)
        obj.btn_right_menu_close_hints.clicked.connect(obj.closeSideMenu)

        # Note that, money_transactins page cannot be closed unless the related main
        # screen page changes. When that happens, it is automatically closed.
    
    @staticmethod
    def terminateSideMenuCloseButtons(obj):
        # Disconnect the signals of right menu close buttons
        obj.btn_right_menu_close_expand_table.clicked.disconnect()
        obj.btn_right_menu_close_message_content.clicked.disconnect()
        obj.btn_right_menu_close_event_content.clicked.disconnect()
        obj.btn_right_menu_close_hints.clicked.disconnect()
    
    @staticmethod
    def initializeQuickActionsButton(obj):
        # Connect the quick actions button
        obj.btn_quick_actions.clicked.connect(obj.LoadQuickActionsPage)
    
    @staticmethod
    def terminateQuickActionsButton(obj):
        # Disconnect the signal of quick actions button
        obj.btn_quick_actions.clicked.disconnect()
    
    @staticmethod
    def initializeQuickControls(obj):
        # Connect quick control buttons to the related functions
        obj.btn_hints_select_all.clicked.connect(obj.selectAll)
        obj.btn_hints_clear_all.clicked.connect(obj.clearAll)
        obj.btn_hints_swap_choices.clicked.connect(obj.swapChoicesCheckBoxes)
    
    @staticmethod
    def terminateQuickControls(obj):
        # Disconnect the signals of quick control buttons
        obj.btn_hints_select_all.clicked.disconnect()
        obj.btn_hints_clear_all.clicked.disconnect()
        obj.btn_hints_swap_choices.clicked.disconnect()
    
    @staticmethod
    def initializeSearchBar(obj):
        # Connect search bar related buttons
        obj.btn_page_search_clear.clicked.connect(obj.textEdit_page_search_search.setPlaceHolderText)
        
        # Some search bar buttons should be hidden when there is no need for them
        obj.btn_page_search_back.setVisible(False)
        obj.btn_page_search_search.setVisible(False)

        obj.btn_page_search_reload.setVisible(True)
        obj.btn_page_search_reload.clicked.connect(obj.reload)

        # Connect the search button to the related function
        obj.btn_page_search_search.clicked.connect(obj.search)
    
    @staticmethod
    def terminateSearchBar(obj):
        # Disconnect the signals of search bar related buttons
        obj.btn_page_search_clear.clicked.disconnect()
        
        # Hide search bar buttons because there is no need for them
        # when the search bar has been terminated
        obj.btn_page_search_back.setVisible(False)
        obj.btn_page_search_search.setVisible(False)

        obj.btn_page_search_reload.setVisible(True)
        obj.btn_page_search_reload.clicked.disconnect()

        # Disconnect the signal of search button
        obj.btn_page_search_search.clicked.disconnect()
    
    @staticmethod
    def initializeItemAssignment(obj):
        obj.btn_item_assignment_add.clicked.connect(obj.add_item)
        obj.btn_item_assignment_back.clicked.connect(obj.backToEmployeeSelection)
        obj.btn_item_assignment_cancel.clicked.connect(obj.cancelItemAssignment)
        obj.btn_item_assignment_complete.clicked.connect(obj.completeAssignment)
        obj.btn_item_assignment_reset.clicked.connect(obj.resetAssignmentList)

        # Set icons
        obj.btn_item_assignment_add.setIcon(IconManager.getIcon("right_arrow_3", "icon"))
        obj.lbl_item_assignment_info_icon.setPixmap(IconManager.getIcon("info", "pixmap"))
        obj.lbl_item_assignment_hint_1_icon.setPixmap(IconManager.getIcon("hint_icon", "pixmap"))
    
    @staticmethod
    def terminateItemAssignment(obj):
        obj.btn_item_assignment_add.clicked.disconnect()
        obj.btn_item_assignment_back.clicked.disconnect()
        obj.btn_item_assignment_cancel.clicked.disconnect()
        obj.btn_item_assignment_complete.clicked.disconnect()
        obj.btn_item_assignment_reset.clicked.disconnect()

        # Remove icons
        obj.btn_item_assignment_add.setIcon(QIcon())
        obj.lbl_item_assignment_info_icon.clear()
        obj.lbl_item_assignment_hint_1_icon.clear()
    
    @staticmethod
    def initializeFilterMenu(obj):
        obj.actionFilterEmployees.triggered.connect(obj.filterTrigger)
        obj.actionFilterMessages.triggered.connect(obj.filterTrigger)
        obj.actionSpecialRequests.triggered.connect(obj.filterTrigger)
        obj.actionFilterEvents.triggered.connect(obj.filterTrigger)
        obj.actionFilterEmployeeLeaves.triggered.connect(obj.filterTrigger)
        obj.actionFilterItems.triggered.connect(obj.filterTrigger)
    
    @staticmethod
    def terminateFilterMenu(obj):
        obj.actionFilterEmployees.triggered.disconnect()
        obj.actionFilterMessages.triggered.disconnect()
        obj.actionSpecialRequests.triggered.disconnect()
        obj.actionFilterEvents.triggered.disconnect()
        obj.actionFilterEmployeeLeaves.triggered.disconnect()
        obj.actionFilterItems.triggered.disconnect()
    
    initializers = {
        0: initializeMainScreen,
        1: initializeHiring,
        2: initializeDirectMessage,
        3: initializeGroupMessage,
        4: initializeTablePage,
        5: initializeEventScheduling,
        6: initializeProfile,
        7: initializeItemAssignment
    }

    terminators = {
        0: terminateMainScreen,
        1: terminateHiring,
        2: terminateDirectMessage,
        3: terminateGroupMessage,
        4: terminateTablePage,
        5: terminateEventScheduling,
        6: terminateProfile,
        7: terminateItemAssignment
        
    }

    @staticmethod
    def initializePageWithIndex(pageIndexNumber:int):
        return ManagerInitializer.initializers.get(pageIndexNumber)
    @staticmethod
    def terminatePageWithIndex(pageIndexNumber:int):
        return ManagerInitializer.terminators.get(pageIndexNumber)

def initializeManager(obj):
    # Store dynamically created side bar widgets to delete them when they are no longer needed        
    obj.created_right_menu_dynamic_widgets = []
    obj.tableWidget_table_1.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
    obj.textEdit_page_search_search.installEventFilter(obj)
    # Setting the name of the dynamic line edits that will be set to disabled
    obj.nameDisabledLineEdits = ["ID"]

    obj.desiredDynamicButtons = list()
    obj.desiredDynamicButtonContainerColumnSpan = 2
    obj.stackedWidget_side_menu.setCurrentWidget(obj.page_expand_table)
    # Get the signal when the visibility of the side menu changed
    obj.stackedWidget_side_menu.installEventFilter(obj)
    obj.stackedWidget_main_screen.currentChanged.connect(obj.main_screen_changed)
    # Hide quick actions and back buttons initially
    obj.btn_quick_actions.setVisible(False)
    obj.tableWidget_item_assignment.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
    # Store the name of the current open submenu in order to reach it later effectively
    obj.currentlyOpenSubMenu = None
    # Store the previous page of the side menu to turn back
    obj.previousSideMenuPage = None
    # Create people card menu
    obj.peopleCardMenu = QMenu(obj)

    # Visibility of short left menu and long left menu depends on the mouse event
    # Menus are toggled based on mouse enter and mouse leave event
    obj.scrollArea_short_menu.enterEvent = obj.shortMenuBarEnterEvent
    obj.scrollArea_short_menu.leaveEvent = obj.shortMenuBarLeaveEvent
    obj.scrollArea_long_menu.enterEvent = obj.scrollAreaEnterEvent
    obj.scrollArea_long_menu.leaveEvent = obj.scrollAreaLeaveEvent

    obj.filterMenu = QMenu(obj)

    # Add filter actions to the filterMenu
    obj.actionFilterEmployees = QAction(QIcon(getPath("view_employees")), "employees", obj)
    obj.actionFilterMessages = QAction(QIcon(getPath("messages_1")), "messages", obj)
    obj.actionSpecialRequests = QAction(QIcon(getPath("permission")), "special_requests", obj)
    obj.actionFilterEvents = QAction(QIcon(getPath("event")), "events_", obj)
    obj.actionFilterEmployeeLeaves = QAction(QIcon(getPath("permission")), "employee_leaves", obj)
    obj.actionFilterItems = QAction(QIcon(getPath("item")), "items", obj)

    

    obj.filterMenu.addAction(obj.actionFilterEmployees)
    obj.filterMenu.addAction(obj.actionFilterMessages)
    obj.filterMenu.addAction(obj.actionSpecialRequests)
    obj.filterMenu.addAction(obj.actionFilterEvents)
    obj.filterMenu.addAction(obj.actionFilterEmployeeLeaves)
    obj.filterMenu.addAction(obj.actionFilterItems)

    

    # Connect phonebook button to show peoplecards
    obj.btn_phone_book.clicked.connect(obj.showPeopleCardMenu)

    # Handle the contollers in the menu bar
    actionGroup = QActionGroup(obj)
    actionGroup.setExclusive(True)

    actionGroup.addAction(obj.action_3_sec)
    actionGroup.addAction(obj.action_5_sec)
    actionGroup.addAction(obj.action_10_sec)
    actionGroup.addAction(obj.action_30_sec)
    actionGroup.addAction(obj.action_60_sec)
    actionGroup.addAction(obj.action_90_sec)
    actionGroup.addAction(obj.action_120_sec)
    actionGroup.addAction(obj.action_Never)

    obj.action_3_sec.toggled.connect(obj.on_action_toggled)
    obj.action_5_sec.toggled.connect(obj.on_action_toggled)
    obj.action_10_sec.toggled.connect(obj.on_action_toggled)
    obj.action_30_sec.toggled.connect(obj.on_action_toggled)
    obj.action_60_sec.toggled.connect(obj.on_action_toggled)
    obj.action_90_sec.toggled.connect(obj.on_action_toggled)
    obj.action_120_sec.toggled.connect(obj.on_action_toggled)
    obj.action_Never.toggled.connect(obj.on_action_toggled)

    actionGroup2 = QActionGroup(obj)
    actionGroup2.setExclusive(True)

    actionGroup2.addAction(obj.actionOpen)
    actionGroup2.addAction(obj.actionHide)

    obj.actionOpen.toggled.connect(obj.on_preference_toggled)
    obj.actionHide.toggled.connect(obj.on_preference_toggled)

    obj.isMenuFixed = False

    actionGroup3 = QActionGroup(obj)
    actionGroup3.setExclusive(True)

    actionGroup3.addAction(obj.action_dynamic)
    actionGroup3.addAction(obj.action_fixed)

    obj.action_dynamic.toggled.connect(obj.on_preference_toggled)
    obj.action_fixed.toggled.connect(obj.on_preference_toggled)

    # Set a timer for connection check

    obj.time_period = 5000 # 5 sec is set initially

    obj.timer = QTimer()
    obj.timer.timeout.connect(obj.updateConnectionStatus)
    obj.timer.start(obj.time_period)
    
    # Set initial connection status
    obj.updateConnectionStatus()
    
    current_date = datetime.now()
    year = current_date.year
    month = str(current_date.month).zfill(2)
    day = str(current_date.day).zfill(2)
    day_name = current_date.strftime("%A")

    obj.lbl_datetime.setText(f"{year}/{month}/{day} - {day_name}")

    ManagerInitializer.initializeMainMenu(obj)
    ManagerInitializer.initializeSearchBar(obj)
    ManagerInitializer.initializeMoneyTransactions(obj)
    ManagerInitializer.initializeSideMenuCloseButtons(obj)
    ManagerInitializer.initializeQuickActionsButton(obj)
    ManagerInitializer.initializeQuickControls(obj)
    ManagerInitializer.initializeFilterMenu(obj)

    ManagerInitializer.initializePageWithIndex(0)(obj)
    ManagerInitializer.initializePageWithIndex(1)(obj)
    ManagerInitializer.initializePageWithIndex(2)(obj)
    ManagerInitializer.initializePageWithIndex(3)(obj)
    ManagerInitializer.initializePageWithIndex(4)(obj)
    ManagerInitializer.initializePageWithIndex(5)(obj)
    ManagerInitializer.initializePageWithIndex(6)(obj)
    ManagerInitializer.initializePageWithIndex(7)(obj)



class EmployeeInitializer:
    @staticmethod
    def initializeMainMenu(obj):
        obj.btn_long_menu_create_new_leave_request.clicked.connect(obj.LoadCreateNewLeaveRequest)
        obj.btn_long_menu_see_past_leave_requests.clicked.connect(obj.LoadPastLeaveRequests)
        obj.btn_long_menu_create_new_special_request.clicked.connect(obj.LoadCreateNewSpecialRequest)
        obj.btn_long_menu_see_past_special_requests.clicked.connect(obj.LoadPastSpecialRequests)
        obj.btn_long_menu_upcoming_events.clicked.connect(obj.LoadUpcomingEvents)
        obj.btn_long_menu_incoming_messages.clicked.connect(obj.LoadIncomingMessages)
        obj.btn_long_menu_send_message.clicked.connect(obj.LoadDirectMessage)
        obj.btn_long_menu_send_group_message.clicked.connect(obj.LoadGroupMessage)
        obj.btn_long_menu_send_group_email.clicked.connect(obj.LoadGroupEmail)
        obj.btn_long_menu_assigned_items.clicked.connect(obj.LoadAssignedItemsToEmployee)
        obj.btn_long_menu_home.clicked.connect(obj.LoadDashboard)
        obj.btn_long_menu_profile.clicked.connect(obj.LoadProfile)
        obj.btn_long_menu_sign_out.clicked.connect(obj.LoadSignOut)

        # Set all of the sub-menus' visibility to False
        obj.widget_submenu_1.setVisible(False)
        obj.widget_submenu_2.setVisible(False)
        obj.widget_submenu_3.setVisible(False)

        # Connect the textChanged signal of the search bar
        obj.textEdit_page_search_search.textChanged.connect(obj.textEditTextChanged)

        # In the beginning, short menu will be visible, long menu will be unvisible
        obj.scrollArea_short_menu.setVisible(True)
        obj.scrollArea_long_menu.setVisible(False)

        # Once a menu is clicked, its submenu should be opened. Connect the functions
        obj.btn_long_menu_leave_requests.clicked.connect(obj.toggleSubMenu)
        obj.btn_long_menu_special_requests.clicked.connect(obj.toggleSubMenu)
        obj.btn_long_menu_communication.clicked.connect(obj.toggleSubMenu)

        # Right side menu is set invisible initially
        obj.closeSideMenu()

        # Set icons
        obj.btn_short_menu_leave_requests.setIcon(IconManager.getIcon("permission"))
        obj.btn_short_menu_special_requests.setIcon(IconManager.getIcon("permission"))
        obj.btn_short_menu_upcoming_events.setIcon(IconManager.getIcon("plan"))
        obj.btn_short_menu_communication.setIcon(IconManager.getIcon("messages_1"))
        obj.btn_short_menu_assigned_items.setIcon(IconManager.getIcon("item"))
        obj.btn_short_menu_home.setIcon(IconManager.getIcon("home"))
        obj.btn_short_menu_profile.setIcon(IconManager.getIcon("profile_2"))
        obj.btn_short_menu_sign_out.setIcon(IconManager.getIcon("sign_out"))

        obj.btn_long_menu_leave_requests.setIcon(IconManager.getIcon("permission"))
        obj.btn_long_menu_special_requests.setIcon(IconManager.getIcon("permission"))
        obj.btn_long_menu_upcoming_events.setIcon(IconManager.getIcon("plan"))
        obj.btn_long_menu_communication.setIcon(IconManager.getIcon("messages_1"))
        obj.btn_long_menu_assigned_items.setIcon(IconManager.getIcon("item"))
        obj.btn_long_menu_home.setIcon(IconManager.getIcon("home"))
        obj.btn_long_menu_profile.setIcon(IconManager.getIcon("profile_2"))
        obj.btn_long_menu_sign_out.setIcon(IconManager.getIcon("sign_out"))

        obj.btn_long_menu_create_new_leave_request.setIcon(IconManager.getIcon("create"))
        obj.btn_long_menu_see_past_leave_requests.setIcon(IconManager.getIcon("past"))
        obj.btn_long_menu_create_new_special_request.setIcon(IconManager.getIcon("create"))
        obj.btn_long_menu_see_past_special_requests.setIcon(IconManager.getIcon("past"))
        obj.btn_long_menu_incoming_messages.setIcon(IconManager.getIcon("get_message"))
        obj.btn_long_menu_send_message.setIcon(IconManager.getIcon("send_message"))
        obj.btn_long_menu_send_group_message.setIcon(IconManager.getIcon("group"))
        obj.btn_long_menu_send_group_email.setIcon(IconManager.getIcon("email_2"))
    
    @staticmethod
    def terminateMainMenu(obj):
        pass

    @staticmethod
    def initializeMainScreen(obj):
        # Connect the custom widget's clicked signals
        obj.e_widget_summary_pm.clickedValue.connect(obj.handleWidgetClick)
        obj.e_widget_summary_par.clickedValue.connect(obj.handleWidgetClick)
        obj.e_widget_summary_plp.clickedValue.connect(obj.handleWidgetClick)
        obj.e_widget_summary_ue.clickedValue.connect(obj.handleWidgetClick)

        # Set icons
        obj.lbl_summary_1_icon.setPixmap(IconManager.getIcon("messages_1", "pixmap"))
        obj.lbl_summary_2_icon.setPixmap(IconManager.getIcon("advance_transaction_1", "pixmap"))
        obj.lbl_summary_3_icon.setPixmap(IconManager.getIcon("permission", "pixmap"))
        obj.lbl_summary_4_icon.setPixmap(IconManager.getIcon("event", "pixmap"))

        expand_icon = IconManager.getIcon("expand_1", "pixmap")

        obj.lbl_dashboard_expand_icon_1.setPixmap(expand_icon)
        obj.lbl_dashboard_expand_icon_2.setPixmap(expand_icon)
        obj.lbl_dashboard_expand_icon_3.setPixmap(expand_icon)
        obj.lbl_dashboard_expand_icon_4.setPixmap(expand_icon)

    @staticmethod
    def terminateMainScreen(obj):
        # Disconnect the custom widget's clicked signals
        obj.e_widget_summary_pm.clickedValue.disconnect()
        obj.e_widget_summary_par.clickedValue.disconnect()
        obj.e_widget_summary_plp.clickedValue.disconnect()
        obj.e_widget_summary_ue.clickedValue.disconnect()

        # Remove icons
        obj.lbl_summary_1_icon.clear()
        obj.lbl_summary_2_icon.clear()
        obj.lbl_summary_3_icon.clear()
        obj.lbl_summary_4_icon.clear()

        obj.lbl_dashboard_expand_icon_1.clear()
        obj.lbl_dashboard_expand_icon_2.clear()
        obj.lbl_dashboard_expand_icon_3.clear()
        obj.lbl_dashboard_expand_icon_4.clear()
    
    @staticmethod
    def initializeDirectMessage(obj):
        obj.btn_direct_message_send.clicked.connect(obj.sendMessage)
        obj.btn_direct_message_cancel.clicked.connect(obj.LoadDashboard)

        # Set icons
        obj.btn_direct_message_cancel.setIcon(IconManager.getIcon("cancel", "icon"))
        obj.btn_direct_message_send.setIcon(IconManager.getIcon("complete", "icon"))
        obj.btn_phone_book.setIcon(IconManager.getIcon("phone_book", "icon"))

    @staticmethod
    def terminateDirectMessage(obj):
        obj.btn_direct_message_send.clicked.disconnect()
        obj.btn_direct_message_cancel.clicked.disconnect()

        # Remove icons
        obj.btn_direct_message_cancel.setIcon(QIcon())
        obj.btn_direct_message_send.setIcon(QIcon())
        obj.btn_phone_book.setIcon(QIcon())
    
    @staticmethod
    def initializeTablePage(obj):
        # Connect cellClicked signal of the table_1
        obj.tableWidget_table_1.cellClicked.connect(obj.handleCellClick)
        obj.btn_table_1_next.clicked.connect(obj.HandleTablePageController)
        obj.btn_table_1_cancel.clicked.connect(obj.LoadDashboard)

        # For reply button to appear, table_1 page should be opened.
        # When table_1 page is opened, connect the reply message signal

        obj.btn_reply_message.clicked.connect(obj.replyMessage)

        # Set icons
        obj.btn_table_1_cancel.setIcon(IconManager.getIcon("cancel" "icon"))
        obj.btn_table_1_next.setIcon(IconManager.getIcon("next", "icon"))
        obj.lbl_page_table_1_hint_1_icon.setPixmap(IconManager.getIcon("hint_icon", "pixmap"))
    
    @staticmethod
    def terminateTablePage(obj):
        # Disconnect cellClicked signal of the table_1
        obj.tableWidget_table_1.cellClicked.disconnect()
        obj.btn_table_1_next.clicked.disconnect()
        obj.btn_table_1_cancel.clicked.disconnect()

        # When the table_1 page is closed, reply message button can no longer be used
        # Disconnect the signal
        obj.btn_reply_message.clicked.disconnect()

        # Remove icons
        obj.btn_table_1_cancel.setIcon(QIcon())
        obj.btn_table_1_next.setIcon(QIcon())
        obj.lbl_page_table_1_hint_1_icon.clear()
    
    @staticmethod
    def initializeGroupMessage(obj):
        obj.btn_group_message_step_2_back.clicked.connect(obj.BackToGroupMessageEmployeeSelection)
        obj.btn_group_message_step_2_cancel.clicked.connect(obj.LoadDashboard)
        obj.btn_group_message_step_2_send.clicked.connect(obj.sendGroupMessage)

        # Set icons
        obj.lbl_group_message_step_2_info_icon.setPixmap(IconManager.getIcon("info", "pixmap"))
        obj.btn_group_message_step_2_cancel.setIcon(IconManager.getIcon("cancel", "icon"))
        obj.btn_group_message_step_2_back.setIcon(IconManager.getIcon("back", "icon"))
        obj.btn_group_message_step_2_send.setIcon(IconManager.getIcon("complete", "icon"))

    @staticmethod
    def terminateGroupMessage(obj):
        obj.btn_group_message_step_2_back.clicked.disconnect()
        obj.btn_group_message_step_2_cancel.clicked.disconnect()
        obj.btn_group_message_step_2_send.clicked.disconnect()

        # Remove icons
        obj.lbl_group_message_step_2_info_icon.clear()
        obj.btn_group_message_step_2_cancel.setIcon(QIcon())
        obj.btn_group_message_step_2_back.setIcon(QIcon())
        obj.btn_group_message_step_2_send.setIcon(QIcon())
    
    @staticmethod
    def initializeLeaveRequest(obj):
        obj.lbl_leave_request_leave_type_icon.setPixmap(IconManager.getIcon("request_type", "pixmap"))
        obj.lbl_leave_request_start_date_icon.setPixmap(IconManager.getIcon("calendar", "pixmap"))
        obj.lbl_leave_request_end_date_icon.setPixmap(IconManager.getIcon("calendar", "pixmap"))

        obj.btn_leave_request_cancel.setIcon(IconManager.getIcon("cancel", "icon"))
        obj.btn_leave_request_complete.setIcon(IconManager.getIcon("complete", "icon"))

        obj.btn_leave_request_cancel.clicked.connect(obj.LoadDashboard)
        obj.btn_leave_request_complete.clicked.connect(obj.ApplyLeaveRequest)

    @staticmethod
    def terminateLeaveRequest(obj):
        obj.lbl_leave_request_leave_type_icon.clear()
        obj.lbl_leave_request_start_date_icon.clear()
        obj.lbl_leave_request_end_date_icon.clear()

        obj.btn_leave_request_cancel.setIcon(QIcon())
        obj.btn_leave_request_complete.setIcon(QIcon())

        obj.btn_leave_request_cancel.clicked.disconnect()
        obj.btn_leave_request_complete.clicked.disconnect()

    @staticmethod
    def initializeSpecialRequest(obj):
        obj.lbl_special_request_request_type_icon.setPixmap(IconManager.getIcon("request_type", "pixmap"))
        obj.lbl_special_request_request_amount_icon.setPixmap(IconManager.getIcon("advance_transaction_2", "pixmap"))

        obj.btn_special_request_cancel.setIcon(IconManager.getIcon("cancel", "icon"))
        obj.btn_special_request_complete.setIcon(IconManager.getIcon("complete", "icon"))

        obj.btn_special_request_cancel.clicked.connect(obj.LoadDashboard)
        obj.btn_special_request_complete.clicked.connect(obj.ApplySpecialRequest)

    @staticmethod
    def terminateSpecialRequest(obj):
        obj.lbl_special_request_request_type_icon.clear()
        obj.lbl_special_request_request_amount_icon.clear()

        obj.btn_special_request_cancel.setIcon(QIcon())
        obj.btn_special_request_complete.setIcon(QIcon())

        obj.btn_special_request_cancel.clicked.disconnect()
        obj.btn_special_request_complete.clicked.disconnect()

    @staticmethod
    def initializeProfile(obj):
        # Set icons
        obj.lbl_profile_info_icon.setPixmap(IconManager.getIcon("info", "pixmap"))

    @staticmethod
    def terminateProfile(obj):
        # Remove icons
        obj.lbl_profile_info_icon.clear()
    
    @staticmethod
    def initializeSideMenuCloseButtons(obj):
        # Connect right menu close buttons to a common function
        obj.btn_right_menu_close_expand_table.clicked.connect(obj.closeSideMenu)
        obj.btn_right_menu_close_message_content.clicked.connect(obj.closeSideMenu)
        obj.btn_right_menu_close_event_content.clicked.connect(obj.closeSideMenu)
        obj.btn_right_menu_close_hints.clicked.connect(obj.closeSideMenu)
    
    @staticmethod
    def terminateSideMenuCloseButtons(obj):
        # Disconnect the signals of right menu close buttons
        obj.btn_right_menu_close_expand_table.clicked.disconnect()
        obj.btn_right_menu_close_message_content.clicked.disconnect()
        obj.btn_right_menu_close_event_content.clicked.disconnect()
        obj.btn_right_menu_close_hints.clicked.disconnect()
    
    @staticmethod
    def initializeQuickActionsButton(obj):
        # Connect the quick actions button
        obj.btn_quick_actions.clicked.connect(obj.LoadQuickActionsPage)
    
    @staticmethod
    def terminateQuickActionsButton(obj):
        # Disconnect the signal of quick actions button
        obj.btn_quick_actions.clicked.disconnect()
    
    @staticmethod
    def initializeQuickControls(obj):
        # Connect quick control buttons to the related functions
        obj.btn_hints_select_all.clicked.connect(obj.selectAll)
        obj.btn_hints_clear_all.clicked.connect(obj.clearAll)
        obj.btn_hints_swap_choices.clicked.connect(obj.swapChoicesCheckBoxes)
    
    @staticmethod
    def terminateQuickControls(obj):
        # Disconnect the signals of quick control buttons
        obj.btn_hints_select_all.clicked.disconnect()
        obj.btn_hints_clear_all.clicked.disconnect()
        obj.btn_hints_swap_choices.clicked.disconnect()
    
    @staticmethod
    def initializeSearchBar(obj):
        # Connect search bar related buttons
        obj.btn_page_search_clear.clicked.connect(obj.textEdit_page_search_search.setPlaceHolderText)
        
        # Some search bar buttons should be hidden when there is no need for them
        obj.btn_page_search_back.setVisible(False)
        obj.btn_page_search_search.setVisible(False)

        obj.btn_page_search_reload.setVisible(True)
        obj.btn_page_search_reload.clicked.connect(obj.reload)

        # Connect the search button to the related function
        obj.btn_page_search_search.clicked.connect(obj.search)
    
    @staticmethod
    def terminateSearchBar(obj):
        # Connect search bar related buttons
        obj.btn_page_search_clear.clicked.disconnect()
        
        # Hide search bar buttons because there is no need for them
        # when the search bar has been terminated
        obj.btn_page_search_back.setVisible(False)
        obj.btn_page_search_search.setVisible(False)

        obj.btn_page_search_reload.setVisible(True)
        obj.btn_page_search_reload.clicked.disconnect()

        # Connect the search button to the related function
        obj.btn_page_search_search.clicked.disconnect()
    
    @staticmethod
    def initializeFilterMenu(obj):
        obj.actionFilterMessages.triggered.connect(obj.filterTrigger)
        obj.actionFilterEvents.triggered.connect(obj.filterTrigger)
        obj.actionFilterItems.triggered.connect(obj.filterTrigger)
    
    @staticmethod
    def terminateFilterMenu(obj):
        obj.actionFilterMessages.triggered.disconnect()
        obj.actionFilterEvents.triggered.disconnect()
        obj.actionFilterItems.triggered.disconnect()
    
    initializers = {
        0: initializeMainScreen,
        1: initializeDirectMessage,
        2: initializeGroupMessage,
        3: initializeTablePage,
        4: initializeLeaveRequest,
        5: initializeSpecialRequest,
        6: initializeProfile
    }

    terminators = {
        0: terminateMainScreen,
        1: terminateDirectMessage,
        2: terminateGroupMessage,
        3: terminateTablePage,
        4: terminateLeaveRequest,
        5: terminateSpecialRequest,
        6: terminateProfile
    }

    @staticmethod
    def initializePageWithIndex(pageIndexNumber:int):
        return EmployeeInitializer.initializers.get(pageIndexNumber)
    @staticmethod
    def terminatePageWithIndex(pageIndexNumber:int):
        return EmployeeInitializer.terminators.get(pageIndexNumber)




def initializeEmployee(obj):
    # Store dynamically created side bar widgets to delete them when they are no longer needed        
    obj.created_right_menu_dynamic_widgets = []
    obj.tableWidget_table_1.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
    obj.textEdit_page_search_search.installEventFilter(obj)
    # Setting the name of the dynamic line edits that will be set to disabled
    obj.nameDisabledLineEdits = ["ID"]

    obj.desiredDynamicButtons = list()
    obj.desiredDynamicButtonContainerColumnSpan = 2
    obj.stackedWidget_side_menu.setCurrentWidget(obj.page_expand_table)
    # Get the signal when the visibility of the side menu changed
    obj.stackedWidget_side_menu.installEventFilter(obj)
    obj.stackedWidget_main_screen.currentChanged.connect(obj.main_screen_changed)
    # Hide quick actions and back buttons initially
    obj.btn_quick_actions.setVisible(False)
    # Store the name of the current open submenu in order to reach it later effectively
    obj.currentlyOpenSubMenu = None
    # Store the previous page of the side menu to turn back
    obj.previousSideMenuPage = None
    # Create people card menu
    obj.peopleCardMenu = QMenu(obj)

    # Visibility of short left menu and long left menu depends on the mouse event
    # Menus are toggled based on mouse enter and mouse leave event
    obj.scrollArea_short_menu.enterEvent = obj.shortMenuBarEnterEvent
    obj.scrollArea_short_menu.leaveEvent = obj.shortMenuBarLeaveEvent
    obj.scrollArea_long_menu.enterEvent = obj.scrollAreaEnterEvent
    obj.scrollArea_long_menu.leaveEvent = obj.scrollAreaLeaveEvent

    obj.filterMenu = QMenu(obj)

    # Add filter actions to the filterMenu
    obj.actionFilterMessages = QAction(QIcon(getPath("messages_1")), "messages", obj)
    obj.actionFilterEvents = QAction(QIcon(getPath("event")), "events_", obj)
    obj.actionFilterItems = QAction(QIcon(getPath("item")), "items", obj)

    

    obj.filterMenu.addAction(obj.actionFilterMessages)
    obj.filterMenu.addAction(obj.actionFilterEvents)
    obj.filterMenu.addAction(obj.actionFilterItems)

    

    # Connect phonebook button to show peoplecards
    obj.btn_phone_book.clicked.connect(obj.showPeopleCardMenu)

    # Handle the contollers in the menu bar
    actionGroup = QActionGroup(obj)
    actionGroup.setExclusive(True)

    actionGroup.addAction(obj.action_3_sec)
    actionGroup.addAction(obj.action_5_sec)
    actionGroup.addAction(obj.action_10_sec)
    actionGroup.addAction(obj.action_30_sec)
    actionGroup.addAction(obj.action_60_sec)
    actionGroup.addAction(obj.action_90_sec)
    actionGroup.addAction(obj.action_120_sec)
    actionGroup.addAction(obj.action_Never)

    obj.action_3_sec.toggled.connect(obj.on_action_toggled)
    obj.action_5_sec.toggled.connect(obj.on_action_toggled)
    obj.action_10_sec.toggled.connect(obj.on_action_toggled)
    obj.action_30_sec.toggled.connect(obj.on_action_toggled)
    obj.action_60_sec.toggled.connect(obj.on_action_toggled)
    obj.action_90_sec.toggled.connect(obj.on_action_toggled)
    obj.action_120_sec.toggled.connect(obj.on_action_toggled)
    obj.action_Never.toggled.connect(obj.on_action_toggled)

    actionGroup2 = QActionGroup(obj)
    actionGroup2.setExclusive(True)

    actionGroup2.addAction(obj.actionOpen)
    actionGroup2.addAction(obj.actionHide)

    obj.actionOpen.toggled.connect(obj.on_preference_toggled)
    obj.actionHide.toggled.connect(obj.on_preference_toggled)

    obj.isMenuFixed = False

    actionGroup3 = QActionGroup(obj)
    actionGroup3.setExclusive(True)

    actionGroup3.addAction(obj.action_dynamic)
    actionGroup3.addAction(obj.action_fixed)

    obj.action_dynamic.toggled.connect(obj.on_preference_toggled)
    obj.action_fixed.toggled.connect(obj.on_preference_toggled)

    # Set a timer for connection check

    obj.time_period = 5000 # 5 sec is set initially

    obj.timer = QTimer()
    obj.timer.timeout.connect(obj.updateConnectionStatus)
    obj.timer.start(obj.time_period)
    
    # Set initial connection status
    obj.updateConnectionStatus()
    
    current_date = datetime.now()
    year = current_date.year
    month = str(current_date.month).zfill(2)
    day = str(current_date.day).zfill(2)
    day_name = current_date.strftime("%A")

    obj.lbl_datetime.setText(f"{year}/{month}/{day} - {day_name}")

    EmployeeInitializer.initializeMainMenu(obj)
    EmployeeInitializer.initializeSearchBar(obj)
    EmployeeInitializer.initializeSideMenuCloseButtons(obj)
    EmployeeInitializer.initializeQuickActionsButton(obj)
    EmployeeInitializer.initializeQuickControls(obj)
    EmployeeInitializer.initializeFilterMenu(obj)