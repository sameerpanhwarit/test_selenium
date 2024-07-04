import sys
sys.path.append('C:\\Users\\S A M E E R\\Desktop\\net2Apps\\Advanced Task\\advancedTasks')
from Models.rating_scale_models import rating_scale,rating_status

#get data and create objects
def load_data(sheet):
    data = sheet.get_all_values()[1:]
    objects = []
    for row in data:
        obj = rating_scale(row[1], row[2], row[3], row[4], row[5])
        objects.append(obj)
    return objects

def load_status(sheet):
    row_no = 2
    row_list = []
    records = []

    while True:
        name = sheet.cell(row_no, 8).value
        status = sheet.cell(row_no, 9).value
        if status is None:
            break
        record = rating_status(name, status)
        records.append(record)
        row_list.append(row_no)
        row_no += 1

    return records, row_list
