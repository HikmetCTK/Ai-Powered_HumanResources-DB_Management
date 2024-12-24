
from customs import *
from path_holder import *


def expand_message(obj, row, column):
    # m.id,e.first_name,e.last_name,m.message_text,m.message_date,m.subject
    # fromInfo = John DOE
    fromInfo = obj.tableWidget_table_1.item(row, 1).text() + " " + obj.tableWidget_table_1.item(row, 2).text() + " - " + obj.tableWidget_table_1.item(row, 6).text()
    obj.lbl_expand_message_from_content.setText(fromInfo)

    # Get the message subject from the table to the related label
    obj.lbl_expand_message_subject_content.setText(obj.tableWidget_table_1.item(row, 3).text())

    # Get the message date from the table to the related label
    obj.lbl_expand_message_message_date_content.setText(obj.tableWidget_table_1.item(row, 5).text())

    # Get the message content to the textEdit
    obj.textEdit_expand_message.setText(obj.tableWidget_table_1.item(row, 4).text())

    # Open the side menu with the correct page
    obj.stackedWidget_side_menu.setCurrentWidget(obj.page_expand_message)
    obj.stackedWidget_side_menu.setVisible(True)

    # Set the message as read
    db_man_projectv3_test.mark_message_as_read(int(obj.tableWidget_table_1.item(row, 0).text()))


def expand_event(obj, row, column):
    # Get the event id to the related label
    obj.lbl_expand_message_from_content_2.setText(obj.tableWidget_table_1.item(row, 0).text())

    # Get the event name to the related label
    obj.lbl_expand_message_message_date_content_3.setText(obj.tableWidget_table_1.item(row, 1).text())

    # Get the event date to the related label
    obj.lbl_expand_message_message_date_content_2.setText(obj.tableWidget_table_1.item(row, 3).text())

    # Get the event details to the textEdit
    obj.textEdit_expand_event.setText(obj.tableWidget_table_1.item(row, 2).text())

    # Open the side menu with the correct page
    obj.stackedWidget_side_menu.setCurrentWidget(obj.page_expand_event)
    obj.stackedWidget_side_menu.setVisible(True)

def expand_table(obj, row, column):
    row_contents_dict = dict()
    
    for col in range(obj.tableWidget_table_1.columnCount()):
        activeColumnName = obj.tableWidget_table_1.horizontalHeaderItem(col).text()
        if not activeColumnName.endswith(":"): activeColumnName = activeColumnName + " :"
        item = obj.tableWidget_table_1.item(row, col)
        cellWidget = obj.tableWidget_table_1.cellWidget(row, col)
        if cellWidget:
            continue
        if item is not None:
            row_contents_dict[activeColumnName] = item.text()
        else:
            row_contents_dict[activeColumnName] = ""

    createSideMenuWidgets(obj, row_contents_dict, obj.desiredDynamicButtons)

    obj.stackedWidget_side_menu.setVisible(True)