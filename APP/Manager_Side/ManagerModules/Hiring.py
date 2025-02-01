from package import StandardMessageBox
from PyQt6.QtWidgets import QWidget, QLineEdit
import db_man_projectv3_test
import datetime
from PyQt6.QtCore import QDate

def _clearInputs(obj):
    page = obj.page_new_staff_registration

    # Find the widgets in the current page
    # Personal and business information parts
    # are separated from each other by widgets
    widgets = page.findChildren(QWidget)

    # Loop through widgets and find the lineEdits
    for widget in widgets:
        lineEdits = widget.findChildren(QLineEdit)
        for lineEdit in lineEdits:
            lineEdit.clear()

def _checkInputs(obj):
    page = obj.page_new_staff_registration

    # Find the widgets in the current page
    # Personal and business information parts
    # are separated from each other by widgets
    widgets = page.findChildren(QWidget)

    # Loop through widgets and find the lineEdits
    for widget in widgets:
        lineEdits = widget.findChildren(QLineEdit)
        for lineEdit in lineEdits:
            if lineEdit.text() == None or lineEdit.text() == "":
                return False
    
    return True

def LoadHiring(obj):
    _clearInputs(obj)
    
    obj.dateEdit_hiring_date_of_birth.clear()
    obj.comboBox_hiring_gender.setCurrentIndex(0)
    obj.comboBox_hiring_password_sending_preference.setCurrentIndex(0)

    obj.dateEdit_hiring_date_of_birth.setDate(QDate.currentDate())

    obj.stackedWidget_main_screen.setCurrentWidget(obj.page_new_staff_registration)

def hire(obj):
    if not _checkInputs(obj):
        StandardMessageBox.Warning(obj, "Missing Information",
                                   "Please fill in all required information!").exec()
        return
    
    name = obj.lineEdit_hiring_name.text()
    surname = obj.lineEdit_hiring_surname.text()
    birth = obj.dateEdit_hiring_date_of_birth.text()
    gender = obj.comboBox_hiring_gender.currentText()
    jobTitle = obj.lineEdit_hiring_job_title.text()
    department = obj.lineEdit_hiring_department.text()
    salary = obj.lineEdit_hiring_salary.text()
    hireDate = datetime.datetime.now().strftime(r"%Y-%m-%d")
    email = obj.lineEdit_hiring_email.text()
    phoneNo = obj.lineEdit_hiring_phone_number.text()
    employeePassword = db_man_projectv3_test.generateRandomPassword(8)

    try:
        db_man_projectv3_test.hiring(name = name, surname = surname, birth = birth, gender = gender,
                                     job_title = jobTitle, department = department, salary = salary,
                                     hire_date = hireDate, email = email, phone_no = phoneNo,
                                     password = employeePassword)
    
    except Exception as e:
        StandardMessageBox.Error(obj, "Hiring Error",
                                 f"An error occurred while hiring! | {str(e)}").exec()
    
    else:
        # Get the password sending preference
        pref = obj.comboBox_hiring_password_sending_preference.currentText()
        
        if pref == "Just Show":
            msg = f"Hiring successful! Employee's initial password: {employeePassword}"
        
        else:
            if pref == "Show and Send Email":
                msg = f"Hiring successful! Employee's initial password: {employeePassword}\n\n"\
                    "Email including password has also been sent."
            
            else:
                msg = f"Hiring successful! Employee's initial password has been sent to them by email."
            
            try:                
                # Send email
                ret = db_man_projectv3_test.send_email(records=((None, obj.lineEdit_hiring_email.text()),),
                                                       email_title="Your Initial Password",
                                                       email_description=f"Your initial password: {employeePassword}",
                                                       from_emp_id=obj.currentEmployeeID,
                                                       from_name=obj.name, from_surname=obj.surname,
                                                       from_role=obj.role)            
            
            except:
                StandardMessageBox.Error(obj, "Error",
                                         f"Email could not be sent!\n\nInitial Password: {employeePassword}").exec()
                
                return
            
            else:
                if ret != True:
                    StandardMessageBox.Error(obj, "Error",
                                             f"Email could not be sent!\n\nErr: {ret}\n\nInitial Password: {employeePassword}").exec()
                    
                    return
        
        StandardMessageBox.Information(obj, "Employee Password", msg).exec()
        
        obj.reload()


# END