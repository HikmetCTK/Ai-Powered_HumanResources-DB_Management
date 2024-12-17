from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from datetime import datetime
def initialize(obj):
    # Store the previous page of the side menu to turn back
    obj.previousSideMenuPage = None

    # Create people card menu
    obj.peopleCardMenu = QMenu(obj)
    
    # Set all of the sub-menus' visibility to False
    obj.widget_submenu_1.setVisible(False)
    obj.widget_submenu_2.setVisible(False)
    obj.widget_submenu_3.setVisible(False)
    obj.widget_submenu_4.setVisible(False)
    obj.widget_submenu_5.setVisible(False)

    # In the beginning, short menu will be visible, long menu will be unvisible
    obj.scrollArea_short_menu.setVisible(True)
    obj.scrollArea_long_menu.setVisible(False)

    # Store the name of the current open submenu in order to reach it later effectively
    obj.currentlyOpenSubMenu = None
    
    # Once a menu is clicked, its submenu should be opened. Connect the functions
    obj.btn_long_menu_general.clicked.connect(obj.toggleSubMenu)
    obj.btn_long_menu_employment.clicked.connect(obj.toggleSubMenu)
    obj.btn_long_menu_transactions.clicked.connect(obj.toggleSubMenu)
    obj.btn_long_menu_plans.clicked.connect(obj.toggleSubMenu)
    obj.btn_long_menu_communication.clicked.connect(obj.toggleSubMenu)
    
    # Visibility of short left menu and long left menu depends on the mouse event
    # Menus are toggled based on mouse enter and mouse leave event
    obj.scrollArea_short_menu.enterEvent = obj.shortMenuBarEnterEvent
    obj.scrollArea_short_menu.leaveEvent = obj.shortMenuBarLeaveEvent
    obj.scrollArea_long_menu.enterEvent = obj.scrollAreaEnterEvent
    obj.scrollArea_long_menu.leaveEvent = obj.scrollAreaLeaveEvent

    obj.textEdit_page_search_search.textChanged.connect(obj.lineEditTextChanged)

    obj.filterMenu = QMenu(obj)

    # Add filter actions to the filterMenu
    actionFilterEmployees = QAction(QIcon(r"C:\Users\fevzi\Downloads\view_employees_2.png"), "employees", obj)
    actionFilterMessages = QAction(QIcon(r"C:\Users\fevzi\Downloads\messages_2.png"), "messages", obj)
    actionSpecialRequests = QAction(QIcon(r"C:\Users\fevzi\Downloads\permission_2.png"), "special_requests", obj)
    actionFilterEvents = QAction(QIcon(r"C:\Users\fevzi\Downloads\event_2.png"), "events_", obj)
    actionFilterEmployeeLeaves = QAction(QIcon(r"C:\Users\fevzi\Downloads\permission_2.png"), "employee_leaves", obj)
    actionFilterItems = QAction(QIcon(r"C:\Users\fevzi\Downloads\item.png"), "items", obj)

    actionFilterEmployees.triggered.connect(obj.filterTrigger)
    actionFilterMessages.triggered.connect(obj.filterTrigger)
    actionSpecialRequests.triggered.connect(obj.filterTrigger)
    actionFilterEvents.triggered.connect(obj.filterTrigger)
    actionFilterEmployeeLeaves.triggered.connect(obj.filterTrigger)
    actionFilterItems.triggered.connect(obj.filterTrigger)

    obj.filterMenu.addAction(actionFilterEmployees)
    obj.filterMenu.addAction(actionFilterMessages)
    obj.filterMenu.addAction(actionSpecialRequests)
    obj.filterMenu.addAction(actionFilterEvents)
    obj.filterMenu.addAction(actionFilterEmployeeLeaves)
    obj.filterMenu.addAction(actionFilterItems)
    
    # Right side menu is set invisible initially
    obj.closeSideMenu()

    obj.widget_summary_1.clickedValue.connect(obj.handleWidgetClick)
    obj.widget_summary_2.clickedValue.connect(obj.handleWidgetClick)
    obj.widget_summary_3.clickedValue.connect(obj.handleWidgetClick)
    obj.widget_summary_4.clickedValue.connect(obj.handleWidgetClick)

    # Store dynamically created side bar widgets to delete them when they are no longer needed        
    obj.created_right_menu_dynamic_widgets = []
    obj.tableWidget_table_1.cellClicked.connect(obj.handleCellClick)
    obj.tableWidget_table_1.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

    obj.textEdit_page_search_search.installEventFilter(obj)

    # Setting the name of the dynamic line edits that will be set to disabled
    obj.nameDisabledLineEdits = ["ID"]

    obj.desiredDynamicButtons = list()
    obj.desiredDynamicButtonContainerColumnSpan = 2

    # Set home page
    obj.LoadDashboard()

    obj.btn_long_menu_view_employees.clicked.connect(obj.LoadViewEmployees)
    obj.btn_long_menu_hiring.clicked.connect(obj.LoadHiring)
    obj.btn_long_menu_dismissal.clicked.connect(obj.LoadDismissal)
    obj.btn_long_menu_advance_transactions.clicked.connect(obj.LoadAdvanceTransactions)
    obj.btn_long_menu_bonus_transactions.clicked.connect(obj.LoadBonusTransactions)
    obj.btn_long_menu_expense_pay_back.clicked.connect(obj.LoadExpensePayBack)
    obj.btn_long_menu_salary_adjustment.clicked.connect(obj.LoadSalaryAdjustment)
    obj.btn_long_menu_event_scheduling.clicked.connect(obj.LoadEventScheduling)
    obj.btn_long_menu_upcoming_events.clicked.connect(obj.LoadIncomingEvents)
    obj.btn_long_menu_incoming_messages.clicked.connect(obj.LoadIncomingMessages)
    obj.btn_long_menu_send_message.clicked.connect(obj.LoadDirectMessage)
    obj.btn_long_menu_send_group_message.clicked.connect(obj.LoadGroupMessage)
    obj.btn_long_menu_send_group_email.clicked.connect(obj.LoadGroupEmail)
    obj.btn_long_menu_leave_definitions.clicked.connect(obj.LoadLeaveDefinitions)
    obj.btn_long_menu_home.clicked.connect(obj.LoadDashboard)
    obj.btn_long_menu_profile.clicked.connect(obj.LoadProfile)
    obj.btn_long_menu_sign_out.clicked.connect(obj.LoadSignOut)

    obj.btn_hiring_complete.clicked.connect(obj.hire)
    obj.btn_hiring_clear_all.clicked.connect(obj.LoadHiring)

    obj.btn_direct_message_send.clicked.connect(obj.sendMessage)
    obj.btn_direct_message_cancel.clicked.connect(obj.LoadDashboard)

    obj.btn_table_1_next.clicked.connect(obj.HandleTablePageController)
    obj.btn_table_1_cancel.clicked.connect(obj.LoadDashboard)
    obj.btn_group_message_step_2_back.clicked.connect(obj.BackToGroupMessageEmployeeSelection)
    obj.btn_group_message_step_2_cancel.clicked.connect(obj.LoadDashboard)
    obj.btn_group_message_step_2_send.clicked.connect(obj.sendGroupMessage)
    

    obj.btn_money_transactions_complete.clicked.connect(obj.updateSalaries)

    obj.btn_event_scheduling_cancel.clicked.connect(obj.LoadDashboard)
    obj.btn_event_scheduling_complete.clicked.connect(obj.ScheduleEvent)

    obj.stackedWidget_side_menu.setCurrentWidget(obj.page_expand_table)

    # Get the signal when the visibility of the side menu changed
    obj.stackedWidget_side_menu.installEventFilter(obj)

    obj.stackedWidget_main_screen.currentChanged.connect(obj.main_screen_changed)

    # Connect right menu close buttons to a common function
    obj.btn_right_menu_close_expand_table.clicked.connect(obj.closeSideMenu)
    obj.btn_right_menu_close_message_content.clicked.connect(obj.closeSideMenu)
    obj.btn_right_menu_close_event_content.clicked.connect(obj.closeSideMenu)
    obj.btn_right_menu_close_hints.clicked.connect(obj.closeSideMenu)

    # Note that, money_transactins page cannot be closed unless the related main
    # screen page changes. When that happens, it is automatically closed.

    # Hide quick actions and back buttons initially
    obj.btn_quick_actions.setVisible(False)

    # Connect the quick actios button
    obj.btn_quick_actions.clicked.connect(obj.LoadQuickActionsPage)

    # Connect search bar related buttons
    obj.btn_page_search_clear.clicked.connect(obj.textEdit_page_search_search.setPlaceHolderText)
    
    # Some search bar buttons should be hidden when there is no need for them
    obj.btn_page_search_back.setVisible(False)
    obj.btn_page_search_search.setVisible(False)

    obj.btn_page_search_reload.setVisible(True)
    obj.btn_page_search_reload.clicked.connect(obj.reload)

    # Connect the search button to the related function
    obj.btn_page_search_search.clicked.connect(obj.search)

    # Connect quick control buttons to the related functions
    obj.btn_hints_select_all.clicked.connect(obj.selectAll)
    obj.btn_hints_clear_all.clicked.connect(obj.clearAll)
    obj.btn_hints_swap_choices.clicked.connect(obj.swapChoicesCheckBoxes)

    # Connect phonebook button to show peoplecards
    obj.btn_phone_book.clicked.connect(obj.showMenu)

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

    obj.lbl_datetime.setText(f"{day}:{month}:{year} - {day_name}")

    obj.btn_money_transactions_complete.clicked.connect(obj.updateSalaries)
    obj.btn_money_transactions_cancel.clicked.connect(obj.LoadDashboard)

    obj.tableWidget_item_assignment.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

    obj.btn_long_menu_item_assignments.clicked.connect(obj.LoadItemAssignment)
    obj.btn_item_assignment_add.clicked.connect(obj.add_item)
    obj.btn_item_assignment_back.clicked.connect(obj.backToEmployeeSelection)
    obj.btn_item_assignment_cancel.clicked.connect(obj.cancelItemAssignment)
    obj.btn_item_assignment_complete.clicked.connect(obj.completeAssignment)
    obj.btn_item_assignment_reset.clicked.connect(obj.resetAssignmentList)