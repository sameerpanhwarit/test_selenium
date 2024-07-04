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
        self.current_spreadsheet = None
        self.current_sheet = None

    def open_spreadsheet(self, identifier):
        url_pattern = re.compile(r'https://docs.google.com/spreadsheets/d/([a-zA-Z0-9-_]+)')
        id_pattern = re.compile(r'^[a-zA-Z0-9-_]{15,}$')

        try:
            match = url_pattern.match(identifier)
            if match:
                print("Detected URL.")
                self.current_spreadsheet = self.client.open_by_url(identifier)
                self.current_sheet = self.current_spreadsheet.sheet1
                print(f"Spreadsheet opened by URL: {identifier}")
                return
            
            if id_pattern.match(identifier):
                print("Detected ID.")
                self.current_spreadsheet = self.client.open_by_key(identifier)
                self.current_sheet = self.current_spreadsheet.sheet1
                print(f"Spreadsheet opened by ID: {identifier}")
                return

            print("Assuming Title.")
            self.current_spreadsheet = self.client.open(identifier)
            self.current_sheet = self.current_spreadsheet.sheet1
            print(f"Spreadsheet opened by Title: {identifier}")

        except gspread.exceptions.SpreadsheetNotFound:
            print(f'Spreadsheet with title "{identifier}" not found.')

    def change_sheet_by_title(self, sheet_title):
        if not self.current_spreadsheet:
            print("No spreadsheet selected. Please select a spreadsheet first.")
            return

        try:
            self.current_sheet = self.current_spreadsheet.worksheet(sheet_title)
            print(f"Sheet changed to '{sheet_title}'")
        except gspread.exceptions.WorksheetNotFound:
            print(f"Sheet with title '{sheet_title}' not found.")
            print("Available sheet titles:")
            for sheet in self.current_spreadsheet.worksheets():
                print(sheet.title)

    def get_last_row(self, sheet):
        all_values = sheet.get_all_values()
        return len(all_values) + 1

    def insert_data(self, data):
        if not self.current_sheet:
            print("No sheet selected. Please select a sheet.")
            return

        for row_data in data:
            last_row = self.get_last_row(self.current_sheet)
            self.current_sheet.insert_row(row_data, last_row)
            self.check_and_format_last_row()
            
        print(f'{data} inserted successfully.')

    def retrieve_data(self):
        if not self.current_sheet:
            print("No sheet selected. Please select a sheet.")
            return

        values = self.current_sheet.get_all_values()
        if values:
            for i, value in enumerate(values):
                print(f'{i + 1}. {value}')
        else:
            print(f'{self.current_sheet.title} is empty.')

    def check_and_format_last_row(self):
        if not self.current_sheet:
            print("No sheet selected. Please select a sheet.")
            return

        last_row = self.get_last_row(self.current_sheet) - 1
        marks = int(self.current_sheet.cell(last_row, 3).value)

        if marks >= 50:
            cell_color = {"backgroundColor": {"green": 1.0, "red": 0.0, "blue": 0.0}}
        else:
            cell_color = {"backgroundColor": {"green": 0.0, "red": 1.0, "blue": 0.0}}

        marks_cell_range = f"C{last_row}"
        self.current_sheet.format(marks_cell_range, cell_color)

    def clear_sheet(self):
        if not self.current_sheet:
            print("No sheet selected. Please select a sheet.")
            return

        all_values = self.current_sheet.get_all_values()
        if not all_values:
            print("The sheet is already empty.")
            return

        cell_color = {"backgroundColor": {"green": 1.0, "red": 1.0, "blue": 1.0}}
        for i, _ in enumerate(all_values[0:], start=0):
            marks_cell_range = f"C{i + 1}"
            self.current_sheet.format(marks_cell_range, cell_color)

        self.current_sheet.clear()
        print("Sheet Cleared Successfully.")


data = [['Sameer', 112, 65], ['Awais', 78, 45], ['Taha', 91, 51]]
gs = GSpread()
gs.open_spreadsheet('test')
# print(gs.change_sheet_by_title("s2"))
# gs.insert_data(data)
gs.retrieve_data()
gs.clear_sheet()
