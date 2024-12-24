from customs import *
import datetime


def approval(senderButtonType, id):
    placeHolderLabel = DoubleButtonWidget.getInstance("dynamicPlaceholderLabel"+"_"+id)
    if placeHolderLabel and placeHolderLabel.isVisible():
        # Once the related placeholder label appeared, it cannot be updated.
        return

    # Merge the parts and create the button's name
    buttonName = "dynamic" + senderButtonType + "_" + id

    button = DoubleButtonWidget.getInstance(buttonName)

    if button: button.click() # Trigger the button

def update(originalQueryResult, newInputs):
    for index in range(1, len(newInputs)):
        # Index 0 belongs to dynamic button
        # Actual data starts at index 1

        if originalQueryResult[0][index - 1] == None:
            newInputs[index] = None
        elif isinstance(originalQueryResult[0][index - 1], datetime.date):
            newInputs[index] = datetime.datetime.strptime(newInputs[index], r"%Y-%m-%d")
        else:
            data_type = type(originalQueryResult[0][index - 1])
            # In the original query result, data starts at index 0

            # Set the new data type to the original data type
            newInputs[index] = data_type(newInputs[index])
    
    db_man_projectv3_test.update_employee(employee_id = newInputs[1],
                                     first_name = newInputs[2],
                                     last_name = newInputs[3],
                                     date_of_birth = newInputs[4],
                                     gender = newInputs[5],
                                     job_title = newInputs[6],
                                     department = newInputs[7],
                                     salary = newInputs[8],
                                     hire_date = newInputs[9],
                                     email = newInputs[10],
                                     phone_number = newInputs[11],
                                     password = newInputs[12],
                                     is_active = newInputs[13])