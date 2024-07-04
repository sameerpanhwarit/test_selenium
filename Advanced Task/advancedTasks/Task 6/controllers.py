import sys
sys.path.append('C:\\Users\\S A M E E R\\Desktop\\net2Apps\\Advanced Task\\advancedTasks')
from Models.rating_scale_models import ONB_Status

# fill pending data 
def fill_data(objects_list, sheet):
    row_no = 2 
    for obj in objects_list:
        sheet.update(f'F{row_no}', [[obj.itemID, obj.status]])
        row_no += 1 

#process pending data 
def load_pending_data(sheet):
    row_no = 2
    records = []
        
    while True:
        name = sheet.cell(row_no, 6).value
        status = sheet.cell(row_no, 7).value
        if status is None:
            break
        record = ONB_Status(name, status)
        records.append(record)
        row_no += 1

    return records

#fill Proccessed Data into Sheet
def fill_records_into_sheet(sheet, records):
    row_no = 2
    item_id = 1
    for obj in records:
        row_data = [
            [item_id],
            [obj.id],
            [obj.listName],
            [obj.item]
        ]

        column_names = ['A', 'B', 'C', 'D']
        for i, value in enumerate(row_data):
            cell_range = f'{column_names[i]}{row_no}'
            sheet.update(cell_range, [value])

        item_id += 1
        row_no += 1
    