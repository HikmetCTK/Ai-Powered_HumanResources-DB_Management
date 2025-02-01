import db_man_projectv3_test
from package.Customs import clearDynamicInstances

def LoadDashboard(obj):
    # Open the dashboard page
    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_dashboard)

    # Close the side menu
    obj.closeSideMenu()

    # Get the data
    messages = db_man_projectv3_test.see_messagev2(emp_id=obj.currentEmployeeID)
    specialRequests = db_man_projectv3_test.get_pending_special_requests()
    leaveRequests = db_man_projectv3_test.get_pending_leave_requests()
    upcomingEvents = db_man_projectv3_test.see_events()

    # Get the count values
    msgCount = 0 if messages is None else len(messages)
    parCount = 0 if specialRequests is None else len(specialRequests)
    plpCount = 0 if leaveRequests is None else len(leaveRequests)
    ueCount = 0 if upcomingEvents is None else len(upcomingEvents)

    # Show the count values on the relevant labels
    obj.lbl_count_pending_messages.setText(str(msgCount))
    obj.lbl_count_pending_advance_requests.setText(str(parCount))
    obj.lbl_count_pending_leave_permissions.setText(str(plpCount))
    obj.lbl_count_upcoming_events.setText(str(ueCount))
    
    # When the program loads the dashboard, dynamic objects are no longer needed
    clearDynamicInstances()


# END