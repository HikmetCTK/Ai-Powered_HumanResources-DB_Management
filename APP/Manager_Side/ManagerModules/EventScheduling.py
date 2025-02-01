from package import StandardMessageBox
import db_man_projectv3_test
from PyQt6.QtCore import QDate
import datetime

def LoadEventScheduling(obj):
    # Clear the input boxes
    obj.lineEdit_event_name.clear()
    obj.dateEdit_event_date.clear()
    obj.textEdit_event_description.clear()
    
    # Set the initial date of the event date to the current date
    obj.dateEdit_event_date.setDate(QDate.currentDate())
    
    # Open the related page
    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_create_event)
    
    # Set focus on the line edit related to event name
    obj.lineEdit_event_name.setFocus()

def ScheduleEvent(obj):
    eventName = obj.lineEdit_event_name.text()
    eventText = obj.textEdit_event_description.toPlainText()
    eventDate = obj.dateEdit_event_date.text()

    if eventName == None or eventName == "":
        StandardMessageBox.Warning(obj, "Invalid Event Name", "Please provide a valid event name to proceed.").exec()
        return
    
    if eventText == None or eventText == "":
        StandardMessageBox.Warning(obj, "Invalid Event Description", "Please provide a valid event description to proceed.").exec()
        return
    
    eventDate = datetime.datetime.strptime(eventDate, r"%Y-%m-%d")
    
    ret = db_man_projectv3_test.add_event(event_name = eventName,
                                          event_text = eventText,
                                          event_date = eventDate)
    
    if ret == True:
        StandardMessageBox.Successful(obj).exec()
        return
    
    if isinstance(ret, str):
        StandardMessageBox.Error(obj, "Event Scheduling Failure", f"{ret}").exec()
        return
    
    if ret == None:
        StandardMessageBox.Error(obj, "Event Scheduling Failure", "add_event returned None!").exec()
        return


# END