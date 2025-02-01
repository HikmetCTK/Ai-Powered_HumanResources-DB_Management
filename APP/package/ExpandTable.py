from package.Customs import *
from package.PathHolder import *
import db_man_projectv3_test

"""
When a table cell is selected for full content display, the row data is placed in the
corresponding widgets on the corresponding page of the right pop-up menu (a.k.a. side bar).
"""

def expand_message(obj, row, column, table:QTableWidget|None = None):
    # If the table is not specified, set it to a default
    if table == None: table = obj.tableWidget_table_1

    # m.id,e.first_name,e.last_name,m.message_text,m.message_date,m.subject,e.id
    senderName = table.item(row, 1).text()
    senderSurname = table.item(row, 2).text()
    senderID = table.item(row, 6).text()

    # fromInfo = John DOE - 1111
    fromInfo = senderName + " " + senderSurname + " - " + senderID
    obj.lbl_expand_message_from_content.setText(fromInfo)

    # Get the message subject from the table to the related label
    obj.lbl_expand_message_subject_content.setText(table.item(row, 3).text())

    # Get the message date from the table to the related label
    obj.lbl_expand_message_message_date_content.setText(table.item(row, 5).text())

    # Get the message content to the textEdit
    obj.textEdit_expand_message.setText(table.item(row, 4).text())

    # Open the side menu with the correct page
    obj.stackedWidget_side_menu.setCurrentWidget(obj.page_expand_message)
    obj.stackedWidget_side_menu.setVisible(True)

    # Set the message as read
    db_man_projectv3_test.mark_message_as_read(int(table.item(row, 0).text()))


def expand_event(obj, row, column, table:QTableWidget|None = None):
    # If the table is not specified, set it to a default
    if table == None: table = obj.tableWidget_table_1

    # Get the event id to the related label
    obj.lbl_expand_message_from_content_2.setText(table.item(row, 0).text())

    # Get the event name to the related label
    obj.lbl_expand_message_message_date_content_3.setText(table.item(row, 1).text())

    # Get the event date to the related label
    obj.lbl_expand_message_message_date_content_2.setText(table.item(row, 3).text())

    # Get the event details to the textEdit
    obj.textEdit_expand_event.setText(table.item(row, 2).text())

    # Open the side menu with the correct page
    obj.stackedWidget_side_menu.setCurrentWidget(obj.page_expand_event)
    obj.stackedWidget_side_menu.setVisible(True)

def expand_table(obj, row, column, table:QTableWidget|None = None):
    # If the table is not specified, set it to a default
    if table == None: table = obj.tableWidget_table_1

    row_contents_dict = dict()
    
    for col in range(table.columnCount()):
        activeColumnName = table.horizontalHeaderItem(col).text()
        # In the right pop-up side menu on the right, we ensure that the headers end with a colon
        if not activeColumnName.endswith(":"): activeColumnName = activeColumnName + " :"
        item = table.item(row, col)
        cellWidget = table.cellWidget(row, col)
        if cellWidget:
            continue
        if item is not None:
            row_contents_dict[activeColumnName] = item.text()
        else:
            row_contents_dict[activeColumnName] = ""

    createSideMenuWidgets(obj, row_contents_dict, obj.desiredDynamicButtons)

    obj.stackedWidget_side_menu.setVisible(True)


# END