import inspect
from package.Customs import *
from package.PathHolder import *
from package import StandardMessageBox
import db_man_projectv3_test

def search(obj):
    tableMatchTable = {
        "Employees"       :"employees",
        "Special_requests":"special_requests",
        "Items"           :"items",
        "Messages"        :"messages",
        "Events_"         :"events_",
        "Employee_leaves" :"employee_leaves"
    }
    
    columnMatchTable = {
        "Employees"       :"first_name",
        "Special_requests":"request_type",
        "Items"           :"item_name",
        "Messages"        :"subject",
        "Events_"         :"event_name",
        "Employee_leaves" :"leave_type"
        }
    
    # Text: @Employees | John
    text = obj.textEdit_page_search_search.toPlainText()
    filterArea = text[text.find("@")+1:text.find(" ")]

    searchKeyword = text[text.find("|")+1:].strip()
    searchTable = tableMatchTable[filterArea]
    searchColumn = columnMatchTable[filterArea]

    if filterArea == "Messages":
        # If the filter is for messages
        # Filtering is done based on sender name which corresponds to column with index 1
        result = db_man_projectv3_test.see_messagev2(emp_id = obj.currentEmployeeID)
        if not result:
            StandardMessageBox.NoResultsFound(obj).exec()
            return
        filteredResult = list()

        for record in result:
            if db_man_projectv3_test.arrangeText(searchKeyword) in db_man_projectv3_test.arrangeText(record[1]):
                filteredResult.append(record,)        

        obj.LoadIncomingMessages(externalResult=filteredResult)
    
    else:
        result = None
        # Use special search functions for special requests and leave requests
        if filterArea == "Special_requests":
            result = db_man_projectv3_test.search_special_requests(first_name=searchKeyword)
        elif filterArea == "Employee_leaves":
            result = db_man_projectv3_test.search_employee_leaves(first_name=searchKeyword)
        else:
            # Remaining filter types use a common search function
            result = db_man_projectv3_test.search(keyword = searchKeyword,
                                                  table_name = searchTable,
                                                  column_name = searchColumn)

        # If no results found, notify the user
        if not result:
            StandardMessageBox.NoResultsFound(obj).exec()
            return
        
        # Show the results to the user
        if filterArea == "Employees":
            obj.LoadViewEmployees(externalResult = result)

        elif filterArea == "Special_requests":
            obj.LoadTableView(externalResult = result,
                              tableHeaders = ["Employee ID", "First Name", "Last Name", "Department", "Job Title",
                                              "Request ID", "Request Type", "Request Amount", "Request Date", "Status",
                                              "Evaluated By", "Description", "Answer Date"],
                              header = "Special Request History")

            StandardMessageBox.NoActionForRequests(obj).exec()

        elif filterArea == "Events_":
            obj.LoadUpcomingEvents(externalResult = result)

        elif filterArea == "Employee_leaves":
            obj.LoadTableView(externalResult = result,
                              tableHeaders = ["Employee ID", "First Name", "Last Name", "Department", "Job Title",
                                              "Request ID", "Status", "Request Date", "Evaluated By", "Answer Date",
                                              "Leave Type", "Start Day", "End Date", "Total Dates", "Description"],
                              header = "Leave Request History")

            StandardMessageBox.NoActionForRequests(obj).exec()

        elif filterArea == "Items":
            obj.LoadTableView(externalResult = result,
                              tableHeaders = ["Item ID", "Item Name", "Quantity"],
                              header = "Items")
        else:
            return
        
    pass

def search_table(obj, search_text:str, columnNumber:int|None = None):
    """
    columnNumber for searching in a specific column will be added
    in a future update...
    """

    # Search in the main table

    frame = inspect.currentframe()
    caller_frame = frame.f_back
    caller_name = caller_frame.f_code.co_name
    if db_man_projectv3_test.arrangeText(caller_name) != db_man_projectv3_test.arrangeText("search_table"):
        # If it is not a recursive call, we start searching from scratch. Make all rows visible.
        makeAllRowsVisible(obj.mainTable)
    
    # Remove leading and trailing unnecessary space characters
    search_text = search_text.strip()
    
    if search_text == "" or search_text == " ":
        return
    
    if search_text == obj.textEdit_page_search_search.placeHolderText:
        # If the expression in the search box becomes the default placeholder
        # expression, remove the filter and make all lines visible
        for row in range(obj.mainTable.rowCount()):
            obj.mainTable.setRowHidden(row, False)
        
        return
    
    if len(search_text.split(" ")) == 1:
        # If search_text is a one-word search...
        for row in range(obj.mainTable.rowCount()):
            if obj.mainTable.isRowHidden(row):
                # If the row is already hidden, skip the current row
                continue
            
            # We initialize row_hidden with True because if we
            # cannot find a match then we will hide the current
            # row
            row_hidden = True
            for column in range(obj.mainTable.columnCount()):
                if columnNumber != None and columnNumber != column:
                    # If a column number is specified and the current
                    # column is not the desired column, skip the current
                    # column
                    continue

                item = obj.mainTable.item(row, column)
                if item:
                    item = db_man_projectv3_test.arrangeText(item.text())
                    search_text = db_man_projectv3_test.arrangeText(search_text)
                    if search_text in item:
                        # If match, show the row
                        row_hidden = False
                        break
            
            obj.mainTable.setRowHidden(row, row_hidden)
    
    else:
        # If search_text is a multi-word search...
        for word in search_text.split(" "):
            obj.search_table(word)


# END