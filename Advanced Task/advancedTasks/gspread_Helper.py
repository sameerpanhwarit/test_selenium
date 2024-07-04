import gspread
from google.oauth2.service_account import Credentials
import re

class GSpread:
    def __init__(self):
        self.scopes = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive.file',
            'https://www.googleapis.com/auth/drive'
        ]
        self.creds = Credentials.from_service_account_file("credentials.json", scopes=self.scopes)
        self.client = gspread.authorize(self.creds)
        
    def open_spreadsheet(self, identifier):
        url_pattern = re.compile(r'https://docs.google.com/spreadsheets/d/([a-zA-Z0-9-_]+)')
        id_pattern = re.compile(r'^[a-zA-Z0-9-_]{15,}$')

        try:
            match = url_pattern.match(identifier)
            if match:
                print("Detected URL.")
                return self.client.open_by_url(identifier)
            
            if id_pattern.match(identifier):
                print("Detected ID.")
                return self.client.open_by_key(identifier)

            print("Assuming Title.")
            return self.client.open(identifier)

        except gspread.exceptions.SpreadsheetNotFound:
            print(f'Spreadsheet with title/ID/URL "{identifier}" not found.')
            return None

    def change_sheet_by_title(self, spreadsheet, sheet_title):
        try:
            sheet = spreadsheet.worksheet(sheet_title)
            print(f'Sheet {sheet_title} is changed.')
            return sheet
        except gspread.exceptions.WorksheetNotFound:
            print(f"Sheet with title '{sheet_title}' not found.")
            print("Available sheet titles:")
            for sheet in spreadsheet.worksheets():
                print(sheet.title)
            return None

    def get_last_row(self, sheet):
        all_values = sheet.get_all_values()
        return len(all_values)+1

    def insert_data(self, sheet, data):
        last_row = self.get_last_row(sheet)
        sheet.insert_row(data, last_row)
            # self.check_and_format_last_row(sheet, last_row)
            
        print(f'{data} inserted successfully.')
    
    # using it for model
    def update(self, sheet, obj):
        last_row = self.get_last_row(sheet)
        col_count = sheet.col_count
        new_row = [None] * col_count
        new_row[7] = obj.scale_name  
        new_row[8] = obj.status
        sheet.insert_row(new_row, last_row)
        print(f'{obj.scale_name} and {obj.status} updated successfully.')

    # def update(self, sheet, obj, column_char):
    #     last_row = self.get_last_row(sheet)
    #     col_count = sheet.col_count
    #     new_row = [None] * col_count
        
    #     # Convert column char to index (assuming A=1, B=2, ..., Z=26)
    #     column_index = ord(column_char.upper()) - ord('A') + 1
        
    #     new_row[column_index - 1] = obj.scale_name
    #       # Adjusting index to start from 0
    #     sheet.insert_row(new_row, last_row)
    #     print(f'{obj.scale_name} and {obj.status} updated successfully.')



    def retrieve_data(self, sheet):
        all_values = []
        values = sheet.get_all_values()
        if values:
            all_values = values

        return all_values

    def check_and_format_last_row(self, sheet, last_row):
        marks = int(sheet.cell(last_row, 3).value)

        if marks >= 50:
            cell_color = {"backgroundColor": {"green": 1.0, "red": 0.0, "blue": 0.0}}
        else:
            cell_color = {"backgroundColor": {"green": 0.0, "red": 1.0, "blue": 0.0}}

        marks_cell_range = f"C{last_row}"
        sheet.format(marks_cell_range, cell_color)

    def clear_sheet(self, sheet):
        all_values = sheet.get_all_values()
        if not all_values:
            print("The sheet is already empty.")
            return

        cell_color = {"backgroundColor": {"green": 1.0, "red": 1.0, "blue": 1.0}}
        for i, _ in enumerate(all_values[0:], start=0):
            marks_cell_range = f"C{i + 1}"
            sheet.format(marks_cell_range, cell_color)

        sheet.clear()
        print("Sheet Cleared Successfully.")


# data = [['Sameer', 112, 65], ['Awais', 78, 45], ['Taha', 91, 51]]
# gs = GSpread()
# spreadsheet = gs.open_spreadsheet('test')
# if spreadsheet:
#     sheet = gs.change_sheet_by_title(spreadsheet, "s2")
#     if sheet:
#         gs.insert_data(sheet, data)
#         gs.retrieve_data(sheet)
#         gs.clear_sheet(sheet)
