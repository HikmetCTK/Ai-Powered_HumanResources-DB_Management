import re
import unicodedata

def connection_check():
    return True, ""


def load_employee():
    return [[1111, "Fevzi", "FİDAN", "01-01-1900", "Male", "Job 1", "Engineering", 6000.20, "02-02-1920", "fevzi@gmail.com", "0123456789", "password 1", "True"],
            [2222, "John", "DOE", "01-01-1900", "Male", "Job 1", "Engineering", 42120.20, "02-02-1920", "fevzi@gmail.com", "0123456789", "password 1", "True"],
            [3333, "Jane", "DOE", "01-01-1900", "Male", "Job 1", "Engineering", 60000, "02-02-1920", "fevzi@gmail.com", "0123456789", "password 1", "True"],
            [4444, "Hikmet", "Çatak", "01-01-1900", "Male", "Job 1", "Engineering", 60000, "02-02-1920", "fevzi@gmail.com", "0123456789", "password 1", "True"]]

def hiring(*args, **kwargs):
    pass

def load_employee_for_salary_adjustment():
    return [[1111, "Fevzi", "FİDAN", "Engineering", "Job 1", 60000],
            [2222, "John", "DOE", "Engineering", "Job 1", 60000],
            [3333, "Jane", "DOE", "Engineering", "Job 1", 60000],
            [4444, "Hikmet", "ÇATAK", "Engineering", "Job 1", 60000]]

def update_employee_salary(*args, **kwargs):
    pass

def see_message(*args, **kwargs):
    return [[1111, "Fevzi", "FİDAN", "Bu bir deneme mesajıdır. Test amaçlı yazılmıştır.", "01-01-2000", "Subject Test"],
            [2222, "John", "DOE", "Bu bir deneme mesajıdır. Test amaçlı yazılmıştır.", "01-01-2000", "Subject Test 1"],
            [3333, "Jane", "DOE", "Bu bir deneme mesajıdır. Test amaçlı yazılmıştıradasdadasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdaadasdasdasda.", "01-01-2000", "Subject Test 3"],
            [4444, "Hikmet", "ÇATAK", "Bu bir deneme mesajıdır. Test amaçlı yazılmıştır.", "01-01-2000", "Subject Test 4"]]

def send_message_anyone(*args, **kwargs):
    print(args)
    print()
    print(kwargs)

def load_employee_for_message_selection(*args, **kwargs):
    return [[1111, "Fevzi", "FİDAN", "Engineering", "Job 1"],
            [2222, "John", "DOE", "Engineering", "Job 1"]]

def get_pending_leave_requests():
    return ([1111, 10000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [3333, 11000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [4444, 12000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [5555, 13000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [6666, 14000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [7777, 15000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [8888, 16000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [9999, 17000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [1112, 18000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [1113, 19000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [1114, 20000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [1115, 21000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [1116, 22000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [1117, 23000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [1118, 24000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [1119, 25000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [1111, 10000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [3333, 11000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [4444, 12000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [5555, 13000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [6666, 14000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [7777, 15000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [8888, 16000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [9999, 17000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [1112, 18000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [1113, 19000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [1114, 20000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [1115, 21000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [1116, 22000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [1117, 23000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [1118, 24000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"],
            [1119, 25000, "Pending", "01-01-1960", None, None, "Yillik Izin",
            "01-02-1960", "07-02-1960", "Sample description for yillik izin", "7", "01-01-1960"])

def see_events():
    return ([1111, "Meeting 1", "This is a sample meeting that all the employees must attend!", "01-01-1960"],
            [2222, "Meeting 2", "This is a sample meeting that all the invited employees must attend!", "01-01-2000"],
            [3333, "Meeting 3", "This is a sample meeting that all managers must attend!", "01-01-2040"],
            [4444, "Meeting 4", "This is a sample meeting!", "01-01-2080"])

def search(*args, **kwargs) -> tuple[list[str]]:
    return ([3333, "Jane", "DOE", "01-01-1900", "Male", "Job 1", "Engineering", 60000, "02-02-1920", "fevzi@gmail.com", "0123456789", "password 1", "True"],)

def add_event(event_name,event_text,event_date):
    pass

def not_working(selected_employee:int):
    pass

def send_email(from_id:int, employee_ids:list, subject:str, message:str):
    pass

def process_special_request(request_id:int, status:str, approved_by:int):
    pass

def get_pending_special_requests():
    return ([1111, 1000, "Avans", 60000, "Null", "Beklemede", "Null", "Null", "08.12.2024"],
            [2222, 2000, "Avans", 50000, "Null", "Beklemede", "Null", "Null", "06.12.2024"])

def mark_message_as_read(message_id):
    pass

def update_employee(*args, **kwargs):
    pass

def loadInfos(*args, **kwargs):
    return ([1111, "Mobile Phone", 10], [2222, "Gloves", 20],
            [3333, "Laptop", 18], [4444, "Car", 4])

def assign_item_to_employee_no_checking(id,item_id,quantity):
    print(f"ID: {id} | Item ID: {item_id} | Quantity: {quantity}")

def generateRandomPassword(self, length:int) -> str:
    from random import choice
    import string

    characters = string.ascii_letters + string.digits
    password = ''.join(choice(characters) for i in range(length))
    return password

def arrangeText(text:str) -> str:
    text = unicodedata.normalize('NFKD', text).casefold()
    arranged =  re.sub(r'\W+', '', text).casefold()
    return arranged