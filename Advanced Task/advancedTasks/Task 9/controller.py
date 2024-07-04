import sys
sys.path.append('C:\\Users\\S A M E E R\\Desktop\\net2Apps\\Advanced Task\\advancedTasks')
from Models.rating_scale_models import ONB_Model, ONB_Status

#get data and create objects
def load_data(sheet):
    data = sheet.get_all_values()[1:]
    objects = []
    for row in data:
        obj = ONB_Model(row[1], row[2], row[3])
        objects.append(obj)
    return objects

def load_status(sheet):
    row_no = 2
    row_list = []
    records = []

    while True:
        ID = sheet.cell(row_no, 6).value
        status = sheet.cell(row_no, 7).value

        if status is None:
            break
        record = ONB_Status(ID, status)
        records.append(record)
        row_list.append(row_no)
        row_no += 1

    return records, row_list
