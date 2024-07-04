import sys
sys.path.append('C:\\Users\\S A M E E R\\Desktop\\net2Apps\\Advanced Task\\advancedTasks')
from Models.rating_scale_models import tab_Element_status

# fill pending data into sheet
def fill_pending_data(objects_list, sheet):
    row_no = 2 
    for obj in objects_list:
        sheet.update(f'L{row_no}', [[obj.tabElement, obj.status]])
        row_no += 1 

#load pending data
def load_pending_data(sheet):
    row_no = 2
    records = []
        
    while True:
        element = sheet.cell(row_no, 12).value
        status = sheet.cell(row_no, 13).value
        if status is None:
            break
        record = tab_Element_status(element, status)
        records.append(record)
        row_no += 1

    return records

# fill main section 
def fill_main_section(sheet, all_records):
    row_no = 2
    item_id = 1
    for obj in all_records:
        row_data = [
            [item_id],
            [obj.identifier],
            [obj.default_label],
            [obj.label],
            [obj.enabled],
            [obj.description]
        ]

        column_names = ['A', 'B', 'C', 'D','E','F']
        for i, value in enumerate(row_data):
            cell_range = f'{column_names[i]}{row_no}'
            sheet.update(cell_range, [value])

        item_id += 1
        row_no += 1

#fill permission section
def fill_permission_section(sheet, permissions):
    row_no = 2
    for obj in permissions:
        row_data = [
            [obj.identifier],
            [obj.permission],
            [obj.role]
        ]

        column_names = ['H', 'I', 'J']
        for i, value in enumerate(row_data):
            cell_range = f'{column_names[i]}{row_no}'
            sheet.update(cell_range, [value])

        row_no += 1
