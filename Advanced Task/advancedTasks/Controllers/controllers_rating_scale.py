import sys
sys.path.append('C:\\Users\\S A M E E R\Desktop\\net2Apps\\Advanced Task\\advancedTasks')
from ..Models.rating_scale_models import rating_status
from Task3.rating_scale_reverse import scrape_data_info as SC
sc = SC()


# insert scale name and status 
def insert_into_gspread(objects_list, sheet):
    row_no = 2 
    for obj in objects_list:
        sheet.update(f'H{row_no}', [[obj.scale_name, obj.status]])
        row_no += 1 

#scrape pending data
def scrape_pending_data(sheet):
    row_no = 2
    records = []
        
    while True:
        name = sheet.cell(row_no, 8).value
        status = sheet.cell(row_no, 9).value
        scalePage = sc.helper.driver.current_url  
        if status is None:
            break
        record = rating_status(name, status)
        records.append(record)
        row_no += 1

    for record in records:
        if record.status == 'pending':
            xpath = f'//table[@id="26:m-m-tbl"]/tbody//tr//a[text()="{record.scale_name}"]'
            element = sc.helper.getElement(xpath, 'xpath')

            if element is not None:
                sc.scrape_rating_cells(xpath)
                row_no = records.index(record) + 2
                sheet.update(f'I{row_no}', [['Processed']])   

        elif status is None:
            break
        sc.helper.driver.get(scalePage)
        sc.helper.driver.implicitly_wait(10)
        row_no += 1

    return sc.rating_scale

#update rating scale into gspread
def update_to_gspread(sheet, rating_scale):
    row_no = 2
    item_id = 1
    for obj in rating_scale:
        row_data = [
            [item_id],
            [obj.name],
            [obj.description],
            [obj.score],
            [obj.label],
            [obj.score_description]
        ]

        column_names = ['A', 'B', 'C', 'D', 'E', 'F']
        for i, value in enumerate(row_data):
            cell_range = f'{column_names[i]}{row_no}'
            sheet.update(cell_range, [value])

        item_id += 1
        row_no += 1