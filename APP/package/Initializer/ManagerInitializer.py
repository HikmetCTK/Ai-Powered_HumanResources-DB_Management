from PyQt6.QtWidgets import QMenu, QAbstractItemView
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QIcon, QAction, QActionGroup
from datetime import datetime
import ChatBotExecutor

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
        obj.btn_long_menu_chatbot.clicked.connect(obj.LoadChatBot)

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

    @staticmethod
    def initializeMainScreen(obj):
        # Connect the custom widget's clicked signals
        obj.m_widget_summary_pm.clickedValue.connect(obj.handleWidgetClick)
        obj.m_widget_summary_par.clickedValue.connect(obj.handleWidgetClick)
        obj.m_widget_summary_plp.clickedValue.connect(obj.handleWidgetClick)
        obj.m_widget_summary_ue.clickedValue.connect(obj.handleWidgetClick)

    @staticmethod
    def initializeHiring(obj):
        obj.btn_hiring_complete.clicked.connect(obj.hire)
        obj.btn_hiring_clear_all.clicked.connect(obj.LoadHiring)
    
    @staticmethod
    def initializeDirectMessage(obj):
        obj.btn_direct_message_send.clicked.connect(obj.sendMessage)
        obj.btn_direct_message_cancel.clicked.connect(obj.LoadDashboard)
        obj.btn_phone_book.clicked.connect(obj.showPeopleCardMenu)
    
    @staticmethod
    def initializeTablePage(obj):
        # Connect cellClicked signal of the table_1
        obj.tableWidget_table_1.cellClicked.connect(obj.handleCellClick)
        obj.btn_table_1_next.clicked.connect(obj.HandleTablePageController)
        obj.btn_table_1_cancel.clicked.connect(obj.LoadDashboard)

        # For reply button to appear, table_1 page should be opened.
        # When table_1 page is opened, connect the reply message signal

        obj.btn_reply_message.clicked.connect(obj.replyMessage)
    
    @staticmethod
    def initializeGroupMessage(obj):
        obj.btn_group_message_step_2_back.clicked.connect(obj.BackToGroupMessageEmployeeSelection)
        obj.btn_group_message_step_2_cancel.clicked.connect(obj.LoadDashboard)
        obj.btn_group_message_step_2_send.clicked.connect(obj.sendGroupMessage)
    
    @staticmethod
    def initializeMoneyTransactions(obj):
        obj.btn_money_transactions_complete.clicked.connect(obj.updateSalaries)
        obj.btn_money_transactions_cancel.clicked.connect(obj.LoadDashboard)
    
    @staticmethod
    def initializeEventScheduling(obj):
        obj.btn_event_scheduling_cancel.clicked.connect(obj.LoadDashboard)
        obj.btn_event_scheduling_complete.clicked.connect(obj.ScheduleEvent)
    
    @staticmethod
    def initializeProfile(obj):
        pass
    
    @staticmethod
    def initializeSideMenu(obj):
        # Connect right menu close buttons to a common function
        obj.btn_right_menu_close_expand_table.clicked.connect(obj.closeSideMenu)
        obj.btn_right_menu_close_message_content.clicked.connect(obj.closeSideMenu)
        obj.btn_right_menu_close_event_content.clicked.connect(obj.closeSideMenu)
        obj.btn_right_menu_close_hints.clicked.connect(obj.closeSideMenu)
        obj.btn_right_menu_close_chatbot.clicked.connect(obj.closeSideMenu)

        # Connect chatbot related buttons and icons
        obj.btn_chatbot_send.clicked.connect(obj.sendMessageToChatBot)

        # Note that, money_transactins page cannot be closed unless the related main
        # screen page changes. When that happens, it is automatically closed.
    
    @staticmethod
    def initializeQuickActionsButton(obj):
        # Connect the quick actions button
        obj.btn_quick_actions.clicked.connect(obj.LoadQuickActionsPage)
    
    @staticmethod
    def initializeQuickControls(obj):
        # Connect quick control buttons to the related functions
        obj.btn_hints_select_all.clicked.connect(obj.selectAll)
        obj.btn_hints_clear_all.clicked.connect(obj.clearAll)
        obj.btn_hints_swap_choices.clicked.connect(obj.swapChoicesCheckBoxes)
    
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
    def initializeItemAssignment(obj):
        obj.btn_item_assignment_add.clicked.connect(obj.add_item)
        obj.btn_item_assignment_back.clicked.connect(obj.backToEmployeeSelection)
        obj.btn_item_assignment_cancel.clicked.connect(obj.cancelItemAssignment)
        obj.btn_item_assignment_complete.clicked.connect(obj.completeAssignment)
        obj.btn_item_assignment_reset.clicked.connect(obj.resetAssignmentList)
    
    @staticmethod
    def initializeFilterMenu(obj):
        obj.actionFilterEmployees.triggered.connect(obj.filterTrigger)
        obj.actionFilterMessages.triggered.connect(obj.filterTrigger)
        obj.actionSpecialRequests.triggered.connect(obj.filterTrigger)
        obj.actionFilterEvents.triggered.connect(obj.filterTrigger)
        obj.actionFilterEmployeeLeaves.triggered.connect(obj.filterTrigger)
        obj.actionFilterItems.triggered.connect(obj.filterTrigger)
    
    @staticmethod
    def initializeChatBot(obj):
        obj.chatBotAgent = ChatBotExecutor.ChatBotWorker()
        obj.chatBotAgent.setTerminationEnabled(True)
        obj.chatBotAgent.response.connect(obj.getResponseFromChatBot)
        obj.chatBotAgent.isWorking.connect(obj.isChatBotInputPermitted)
    
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

    @staticmethod
    def initializePageWithIndex(pageIndexNumber:int):
        return ManagerInitializer.initializers.get(pageIndexNumber)

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
    obj.actionFilterEmployees = QAction(QIcon(":/newSource/icons/view_employees.png"), "employees", obj)
    obj.actionFilterMessages = QAction(QIcon(":/newSource/icons/messages_1.png"), "messages", obj)
    obj.actionSpecialRequests = QAction(QIcon(":/newSource/icons/permission.png"), "special_requests", obj)
    obj.actionFilterEvents = QAction(QIcon(":/newSource/icons/event.png"), "events_", obj)
    obj.actionFilterEmployeeLeaves = QAction(QIcon(":/newSource/icons/permission.png"), "employee_leaves", obj)
    obj.actionFilterItems = QAction(QIcon(":/newSource/icons/item.png"), "items", obj)

    obj.filterMenu.addAction(obj.actionFilterEmployees)
    obj.filterMenu.addAction(obj.actionFilterMessages)
    obj.filterMenu.addAction(obj.actionSpecialRequests)
    obj.filterMenu.addAction(obj.actionFilterEvents)
    obj.filterMenu.addAction(obj.actionFilterEmployeeLeaves)
    obj.filterMenu.addAction(obj.actionFilterItems)

    obj.action_Try_to_Reconnect.triggered.connect(obj.updateConnectionStatus)

    # Handle the contollers in the menu bar
    # ActionGroup for connection check interval
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
    
    # Action group for search bar visibility preference
    actionGroup2 = QActionGroup(obj)
    actionGroup2.setExclusive(True)

    actionGroup2.addAction(obj.actionOpen)
    actionGroup2.addAction(obj.actionHide)

    obj.actionOpen.toggled.connect(obj.on_preference_toggled)
    obj.actionHide.toggled.connect(obj.on_preference_toggled)

    obj.isMenuFixed = False
    
    # Action group for main menu visibility preference
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

    # Get current date
    current_date = datetime.now()
    year = current_date.year
    month = str(current_date.month).zfill(2)
    day = str(current_date.day).zfill(2)
    day_name = current_date.strftime("%A")
    
    # Set date
    obj.lbl_datetime.setText(f"{year}/{month}/{day} - {day_name}")
    
    # Initialize the remaining parts of the program to make it ready to run
    ManagerInitializer.initializeMainMenu(obj)
    ManagerInitializer.initializeSearchBar(obj)
    ManagerInitializer.initializeMoneyTransactions(obj)
    ManagerInitializer.initializeSideMenu(obj)
    ManagerInitializer.initializeQuickActionsButton(obj)
    ManagerInitializer.initializeQuickControls(obj)
    ManagerInitializer.initializeFilterMenu(obj)
    ManagerInitializer.initializeChatBot(obj)


# END