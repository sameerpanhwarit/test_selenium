import sys
sys.path.append('C:\\Users\\S A M E E R\\Desktop\\net2Apps\\Advanced Task\\advancedTasks')
from Models.rating_scale_models import tab_elements, tab_permission, tab_Element_status

def load_data(sheet):
    data = sheet.get_all_values()[1:]
    all_records = []
    all_permissions=[]
    
    for row in data:
        obj = tab_elements(row[1], row[2], row[3], row[4], row[5])
        all_records.append(obj)

        obj2 = tab_permission(row[7], row[8], row[9])
        all_permissions.append(obj2)

    return all_records, all_permissions

def load_status(sheet):
    row_no = 2
    row_list = []
    records = []

    while True:
        ID = sheet.cell(row_no, 12).value
        status = sheet.cell(row_no, 13).value

        if status is None:
            break
        record = tab_Element_status(ID, status)
        records.append(record)
        row_list.append(row_no)
        row_no += 1

    return records, row_list