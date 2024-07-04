# # # def separate_sections(data):
# # #     sections = {}
# # #     current_section = []

# # #     for line in data.split('\n'):
# # #         line = line.strip()
# # #         if line:
# # #             current_section.append(line)
# # #         else:
# # #             if current_section:
# # #                 sections[current_section[0]] = current_section[1:]
# # #                 current_section = []

# # #     if current_section:
# # #         sections[current_section[0]] = current_section[1:]

# # #     return sections

# # # if __name__ == "__main__":
# # #     data = '''
# # # Python Tutorial
# # # Python HOME
# # # Python Intro
# # # Python Get Started
# # # Python Syntax
# # # Python Comments
# # # Python Variables
# # # Python Data Types
# # # Python Numbers
# # # Python Casting
# # # Python Strings
# # # Python Booleans
# # # Python Operators
# # # Python Lists
# # # Python Tuples
# # # Python Sets
# # # Python Dictionaries
# # # Python If...Else
# # # Python While Loops
# # # Python For Loops
# # # Python Functions
# # # Python Lambda
# # # Python Arrays
# # # Python Classes/Objects
# # # Python Inheritance
# # # Python Iterators
# # # Python Polymorphism
# # # Python Scope
# # # Python Modules
# # # Python Dates
# # # Python Math
# # # Python JSON
# # # Python RegEx
# # # Python PIP
# # # Python Try...Except
# # # Python User Input
# # # Python String Formatting

# # # File Handling
# # # Python File Handling
# # # Python Read Files
# # # Python Write/Create Files
# # # Python Delete Files

# # # Python Modules
# # # NumPy Tutorial
# # # Pandas Tutorial
# # # SciPy Tutorial
# # # Django Tutorial

# # # Python Matplotlib
# # # Matplotlib Intro
# # # Matplotlib Get Started
# # # Matplotlib Pyplot
# # # Matplotlib Plotting
# # # Matplotlib Markers
# # # Matplotlib Line
# # # Matplotlib Labels
# # # Matplotlib Grid
# # # Matplotlib Subplot
# # # Matplotlib Scatter
# # # Matplotlib Bars
# # # Matplotlib Histograms
# # # Matplotlib Pie Charts

# # # Machine Learning
# # # Getting Started
# # # Mean Median Mode
# # # Standard Deviation
# # # Percentile
# # # Data Distribution
# # # Normal Data Distribution
# # # Scatter Plot
# # # Linear Regression
# # # Polynomial Regression
# # # Multiple Regression
# # # Scale
# # # Train/Test
# # # Decision Tree
# # # Confusion Matrix
# # # Hierarchical Clustering
# # # Logistic Regression
# # # Grid Search
# # # Categorical Data
# # # K-means
# # # Bootstrap Aggregation
# # # Cross Validation
# # # AUC - ROC Curve
# # # K-nearest neighbors

# # # Python MySQL
# # # MySQL Get Started
# # # MySQL Create Database
# # # MySQL Create Table
# # # MySQL Insert
# # # MySQL Select
# # # MySQL Where
# # # MySQL Order By
# # # MySQL Delete
# # # MySQL Drop Table
# # # MySQL Update
# # # MySQL Limit
# # # MySQL Join

# # # Python MongoDB
# # # MongoDB Get Started
# # # MongoDB Create DB
# # # MongoDB Collection
# # # MongoDB Insert
# # # MongoDB Find
# # # MongoDB Query
# # # MongoDB Sort
# # # MongoDB Delete
# # # MongoDB Drop Collection
# # # MongoDB Update
# # # MongoDB Limit

# # # Python Reference
# # # Python Overview
# # # Python Built-in Functions
# # # Python String Methods
# # # Python List Methods
# # # Python Dictionary Methods
# # # Python Tuple Methods
# # # Python Set Methods
# # # Python File Methods
# # # Python Keywords
# # # Python Exceptions
# # # Python Glossary

# # # Module Reference
# # # Random Module
# # # Requests Module
# # # Statistics Module
# # # Math Module
# # # cMath Module

# # # Python How To
# # # Remove List Duplicates
# # # Reverse a String
# # # Add Two Numbers

# # # Python Examples
# # # Python Examples
# # # Python Compiler
# # # Python Exercises
# # # Python Quiz
# # # Python Server
# # # Python Bootcamp
# # # Python Certificate
# # # '''

# # #     sections = separate_sections(data)
# # #     for key, values in sections.items():
# # #         print(key)
# # #         print(values)
# # #         print('-' * 50)

# # from HelperMethods import Helper

# # def separate_sections(data):
# #     sections = {}
# #     current_section = []

# #     for line in data.split('\n'):
# #         line = line.strip()
# #         if line:
# #             current_section.append(line)
# #         else:
# #             if current_section:
# #                 sections[current_section[0]] = current_section[1:]
# #                 current_section = []

# #     if current_section:
# #         sections[current_section[0]] = current_section[1:]

# #     return sections


# # if __name__ == '__main__':
# #     helper = Helper()
# #     # helper.driver.get('https://www.w3schools.com/python/python_intro.asp')
# #     sidebar = helper.getElementText('leftmenuinnerinner', 'id')

# #     allHeadings = separate_sections(sidebar)

# #     headingNo = 0
# #     for heading, subHeadings in allHeadings.items():
# #         headingNo = headingNo+1
# #         print(f'{headingNo}.{heading}: {subHeadings}')
# #         print("_"*118)

    


# from HelperMethods import Helper

# class w3School:
#     def __init__(self):
#         self.helper = Helper()
#         self.dictHeadings={}
    
#     def navigate_to_url(self,url):
#         self.helper.driver.get(url)
#         sidebar = self.helper.getElementText('leftmenuinnerinner', 'id')
#         return sidebar
    
#     def separate_sections(self,data):
#         current_section = []

#         for line in data.split('\n'):
#             line = line.strip()
#             if line:
#                 current_section.append(line)
#             else:
#                 if current_section:
#                     self.dictHeading[current_section[0]] = current_section[1:]
#                     current_section = []

#         if current_section:
#             self.dictHeadings[current_section[0]] = current_section[1:]
    
#     def print_headings(self):
#         indexofHeading = 1
#         print(f'{"="*5}Headings{"="*5}')
#         for key in self.dictHeadings.keys():
#             print(f'{indexofHeading}. {key}')
#             indexofHeading = indexofHeading+1

#     def wait_for_input(self):
#         while True:
#             print("_"*20)
#             userInput = input("Enter any Heading for get sub headings: ").title()
#             subHeadings = self.dictHeadings.get(userInput)

#             if subHeadings:
#                 print(f'{userInput} - {subHeadings}')
#                 break
#             else:
#                 print(f'Heading {userInput} not found.')


# w3 = w3School()
# elementsList = w3.navigate_to_url('https://www.w3schools.com/python/python_intro.asp')
# w3.print_headings()
# w3.wait_for_input()


# import gspread
# from google.oauth2.service_account import Credentials


# class GSpread:
#     def __init__(self):
#         self.scopes = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/spreadsheets',
#                        'https://www.googleapis.com/auth/drive.file']
#         self.creds = Credentials.from_service_account_file("credentials.json", scopes=self.scopes)
#         self.client = gspread.authorize(self.creds)
#         self.worksheet_id = "1TOEFIybUneey13EaKB3jJ5Mzst3hwZf7B_JwDILpSOo"

#     def open_sheet(self):
#         try:
#             worksheet = self.client.open_by_key(self.worksheet_id).sheet1
#             return worksheet

#         except gspread.exceptions as e:
#             print(f'Sheet not exists {e}.')

#     def get_last_row(self, worksheet):
#         all_values = worksheet.get_all_values()
#         return len(all_values) + 1

#     def insert_data(self, worksheet, data):
#         for dataa in data:
#             last_row = self.get_last_row(worksheet)
#             worksheet.insert_row(dataa, last_row)
#             self.check_and_format_last_row(worksheet)
            
#         print(f'{data} inserted successfully.')

#     def retrive_data(self, worksheet):
#         values = worksheet.get_all_values()
#         if values:
#             for i, value in enumerate(values):
#                 print(f'{i + 1}.{value}')
#         else:
#             print(f'{worksheet} is empty.')

#     def check_and_format_last_row(self, worksheet):
#         last_row = self.get_last_row(worksheet)
#         last_row = last_row - 1
#         marks = worksheet.cell(last_row, 3).value
#         marks = int(marks)

#         if marks >= 50:
#             cell_color = {"backgroundColor": {"green": 1.0, "red": 0.0, "blue": 0.0}}
#         else:
#             cell_color = {"backgroundColor": {"green": 0.0, "red": 1.0, "blue": 0.0}}

#         marks_cell_range = f"C{last_row}"
#         worksheet.format(marks_cell_range, cell_color)

#     def clear_sheet(self, worksheet):
#         all_values = worksheet.get_all_values()
#         header = all_values[0]

#         cell_color = {"backgroundColor": {"green": 1.0, "red": 1.0, "blue": 1.0}}
#         for i, _ in enumerate(all_values[1:], start=1):
#             marks_cell_range = f"C{i + 1}"
#             worksheet.format(marks_cell_range, cell_color)

#         worksheet.clear()
#         worksheet.append_row(header)
#         print("Worksheet Cleared Successfully.")


# data = [['Sameer', 112, 60],['Sameer', 112, 40],['Sameer', 112, 70]]
# gs = GSpread()
# worksheet = gs.open_sheet()
# gs.insert_data(worksheet, data)
# gs.retrive_data(worksheet)
# # gs.clear_sheet(worksheet)

# import requests

# class Request:
#     def __init__(self, baseURL):
#         self.baseURL = baseURL

#     @staticmethod
#     def userData():

#         email = input("Enter user email: ")
#         first = input("Enter user first name: ")
#         last = input("Enter user last name: ")

#         json = {
#             'email': email,
#             'first': first,
#             'last': last
#         }

#         return json


#     def get(self, params=None):
#         response = requests.get(self.baseURL, params=str(params))
#         if response.status_code == 200:
#             print(response.json())
#         else:
#             print(f"Request failed with status code {response.status_code}")

#     def post(self, data=None):
#         response = requests.post(self.baseURL, json=data)
#         if response.status_code == 201:
#             print(f'User created successfully: {response.json()}')
#         else:
#             print(f"Request failed with status code {response.status_code}")

#     def put(self, endpoint, data=None):
#         url = f'{self.baseURL}/{endpoint}'
#         response = requests.put(url, json=data)
#         if response.status_code == 200:
#             print(f"User updated successfully: {response.json()}")
#         else:
#             print(f"Request failed with status code {response.status_code}")

# if __name__ == '__main__':
#     request = Request('https://reqres.in/api/users')

#     requestOption = input('Which Request you want to made? GET, PUT,POST: ').upper()

#     while True:
#         if requestOption == 'GET':
#             request.get(params=1)
#             break

#         elif requestOption == 'POST':
#             json = request.userData()
#             request.post(data=json)
#             break
        
#         elif requestOption == 'PUT':
#             userID= input('Enter user ID you want to update: ')
#             json = request.userData()
#             request.put(endpoint=userID, data=json)
#             break

#         else:
#             print('Invalid Request Option!!!')


# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()
# driver.get('https://www.w3schools.com/python/python_intro.asp')
# sidebar = driver.find_element(By.ID, 'leftmenuinnerinner')
# elements = sidebar.find_elements(By.TAG_NAME, 'h2')

# headings_subHeadings = {}

# for element in elements:
#     heading = element.text
#     temp_sub_headings =[]

#     sub_headings = element.find_elements(By.TAG_NAME, 'a')
#     for sub_heading in sub_headings:
#         h2 = sub_heading.find_element(By.XPATH, 'following-sibling::h2')
#         print(h2)
#         if h2 is None:
#             temp_sub_headings.append(sub_heading.text)
#         else:
#             break
#     headings_subHeadings[heading] = temp_sub_headings

# for hheading, sheading in headings_subHeadings.items():
#     print(f'{hheading} - {sheading}')


# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()
# driver.get('https://www.w3schools.com/python/python_intro.asp')
# sidebar = driver.find_element(By.ID, 'leftmenuinnerinner')
# elements = sidebar.find_elements(By.TAG_NAME, 'h2')

# headings_subHeadings = {}

# for element in elements:
#     heading = element.text
#     sub_headings = []

#     siblings = element.find_elements(By.XPATH, 'following-sibling::*')
#     for sibling in siblings:
#         if sibling.tag_name == 'h2':
#             break
#         elif sibling.tag_name == 'a':
#             sub_headings.append(sibling.text)

#     headings_subHeadings[heading] = sub_headings

# for hheading, sheading in headings_subHeadings.items():
#     print(f'{hheading} - {sheading}')

# driver.quit()

# task 7

# import gspread
# from google.oauth2.service_account import Credentials

# class GSpread:
#     def __init__(self):
#         self.scopes = [
#             'https://spreadsheets.google.com/feeds',
#             'https://www.googleapis.com/auth/spreadsheets',
#             'https://www.googleapis.com/auth/drive.file',
#             'https://www.googleapis.com/auth/drive'
#         ]
#         self.creds = Credentials.from_service_account_file("credentials.json", scopes=self.scopes)
#         self.client = gspread.authorize(self.creds)
#         self.current_spreadsheet = None
#         self.current_sheet = None

#     def open_spreadsheet_by_title(self, spreadsheet_title):
#         try:
#             self.current_spreadsheet = self.client.open(spreadsheet_title)
#             self.current_sheet = self.current_spreadsheet.sheet1
#             print(f"Spreadsheet '{spreadsheet_title}' opened successfully.")
#         except gspread.exceptions.SpreadsheetNotFound:
#             print(f'Spreadsheet with title "{spreadsheet_title}" not found.')

#     def change_sheet_by_title(self, sheet_title):
#         if not self.current_spreadsheet:
#             print("No spreadsheet selected. Please select a spreadsheet first.")
#             return

#         try:
#             self.current_sheet = self.current_spreadsheet.worksheet(sheet_title)
#             print(f"Sheet changed to '{sheet_title}'")
#         except gspread.exceptions.WorksheetNotFound:
#             print(f"Sheet with title '{sheet_title}' not found.")
#             print("Available sheet titles:")
#             for sheet in self.current_spreadsheet.worksheets():
#                 print(sheet.title)

#     def get_last_row(self, sheet):
#         all_values = sheet.get_all_values()
#         return len(all_values) + 1

#     def insert_data(self, data):
#         if not self.current_sheet:
#             print("No sheet selected. Please select a sheet.")
#             return

#         for row_data in data:
#             last_row = self.get_last_row(self.current_sheet)
#             self.current_sheet.insert_row(row_data, last_row)
#             self.check_and_format_last_row()
            
#         print(f'{data} inserted successfully.')

#     def retrieve_data(self):
#         if not self.current_sheet:
#             print("No sheet selected. Please select a sheet.")
#             return

#         values = self.current_sheet.get_all_values()
#         if values:
#             for i, value in enumerate(values):
#                 print(f'{i + 1}. {value}')
#         else:
#             print(f'{self.current_sheet.title} is empty.')

#     def check_and_format_last_row(self):
#         if not self.current_sheet:
#             print("No sheet selected. Please select a sheet.")
#             return

#         last_row = self.get_last_row(self.current_sheet) - 1
#         marks = int(self.current_sheet.cell(last_row, 3).value)

#         if marks >= 50:
#             cell_color = {"backgroundColor": {"green": 1.0, "red": 0.0, "blue": 0.0}}
#         else:
#             cell_color = {"backgroundColor": {"green": 0.0, "red": 1.0, "blue": 0.0}}

#         marks_cell_range = f"C{last_row}"
#         self.current_sheet.format(marks_cell_range, cell_color)

#     def clear_sheet(self):
#         if not self.current_sheet:
#             print("No sheet selected. Please select a sheet.")
#             return

#         all_values = self.current_sheet.get_all_values()
#         if not all_values:
#             print("The sheet is already empty.")
#             return

#         header = all_values[0]

#         cell_color = {"backgroundColor": {"green": 1.0, "red": 1.0, "blue": 1.0}}
#         for i, _ in enumerate(all_values[1:], start=1):
#             marks_cell_range = f"C{i + 1}"
#             self.current_sheet.format(marks_cell_range, cell_color)

#         self.current_sheet.clear()
#         self.current_sheet.append_row(header)
#         print("Sheet Cleared Successfully.")

# # Example usage
# data = [['Sameer', 112, 65], ['Awais', 78, 45], ['Taha', 91, 51]]
# gs = GSpread()
# gs.open_spreadsheet_by_title("test")
# print(gs.change_sheet_by_title("s2"))
# gs.insert_data(data)
# gs.retrieve_data()
# gs.clear_sheet()

# task 7 regex
# import gspread
# from google.oauth2.service_account import Credentials
# import re

# class GSpread:
#     def __init__(self):
#         self.scopes = [
#             'https://spreadsheets.google.com/feeds',
#             'https://www.googleapis.com/auth/spreadsheets',
#             'https://www.googleapis.com/auth/drive.file',
#             'https://www.googleapis.com/auth/drive'
#         ]
#         self.creds = Credentials.from_service_account_file("credentials.json", scopes=self.scopes)
#         self.client = gspread.authorize(self.creds)
#         self.current_spreadsheet = None
#         self.current_sheet = None

#     def open_spreadsheet(self, identifier):
#         url_pattern = re.compile(r'https://docs.google.com/spreadsheets/d/([a-zA-Z0-9-_]+)')
#         id_pattern = re.compile(r'^[a-zA-Z0-9-_]{15,}$')

#         try:
#             match = url_pattern.match(identifier)
#             if match:
#                 print("Detected URL.")
#                 self.current_spreadsheet = self.client.open_by_url(identifier)
#                 self.current_sheet = self.current_spreadsheet.sheet1
#                 print(f"Spreadsheet opened by URL: {identifier}")
#                 return
            
#             if id_pattern.match(identifier):
#                 print("Detected ID.")
#                 self.current_spreadsheet = self.client.open_by_key(identifier)
#                 self.current_sheet = self.current_spreadsheet.sheet1
#                 print(f"Spreadsheet opened by ID: {identifier}")
#                 return

#             print("Assuming Title.")
#             self.current_spreadsheet = self.client.open(identifier)
#             self.current_sheet = self.current_spreadsheet.sheet1
#             print(f"Spreadsheet opened by Title: {identifier}")

#         except gspread.exceptions.SpreadsheetNotFound:
#             print(f'Spreadsheet with title "{identifier}" not found.')

#     def change_sheet_by_title(self, sheet_title):
#         if not self.current_spreadsheet:
#             print("No spreadsheet selected. Please select a spreadsheet first.")
#             return

#         try:
#             self.current_sheet = self.current_spreadsheet.worksheet(sheet_title)
#             print(f"Sheet changed to '{sheet_title}'")
#         except gspread.exceptions.WorksheetNotFound:
#             print(f"Sheet with title '{sheet_title}' not found.")
#             print("Available sheet titles:")
#             for sheet in self.current_spreadsheet.worksheets():
#                 print(sheet.title)

#     def get_last_row(self, sheet):
#         all_values = sheet.get_all_values()
#         return len(all_values) + 1

#     def insert_data(self, data):
#         if not self.current_sheet:
#             print("No sheet selected. Please select a sheet.")
#             return

#         for row_data in data:
#             last_row = self.get_last_row(self.current_sheet)
#             self.current_sheet.insert_row(row_data, last_row)
#             self.check_and_format_last_row()
            
#         print(f'{data} inserted successfully.')

#     def retrieve_data(self):
#         if not self.current_sheet:
#             print("No sheet selected. Please select a sheet.")
#             return

#         values = self.current_sheet.get_all_values()
#         if values:
#             for i, value in enumerate(values):
#                 print(f'{i + 1}. {value}')
#         else:
#             print(f'{self.current_sheet.title} is empty.')

#     def check_and_format_last_row(self):
#         if not self.current_sheet:
#             print("No sheet selected. Please select a sheet.")
#             return

#         last_row = self.get_last_row(self.current_sheet) - 1
#         marks = int(self.current_sheet.cell(last_row, 3).value)

#         if marks >= 50:
#             cell_color = {"backgroundColor": {"green": 1.0, "red": 0.0, "blue": 0.0}}
#         else:
#             cell_color = {"backgroundColor": {"green": 0.0, "red": 1.0, "blue": 0.0}}

#         marks_cell_range = f"C{last_row}"
#         self.current_sheet.format(marks_cell_range, cell_color)

#     def clear_sheet(self):
#         if not self.current_sheet:
#             print("No sheet selected. Please select a sheet.")
#             return

#         all_values = self.current_sheet.get_all_values()
#         if not all_values:
#             print("The sheet is already empty.")
#             return

#         header = all_values[0]

#         cell_color = {"backgroundColor": {"green": 1.0, "red": 1.0, "blue": 1.0}}
#         for i, _ in enumerate(all_values[1:], start=1):
#             marks_cell_range = f"C{i + 1}"
#             self.current_sheet.format(marks_cell_range, cell_color)

#         self.current_sheet.clear()
#         self.current_sheet.append_row(header)
#         print("Sheet Cleared Successfully.")


# data = [['Sameer', 112, 65], ['Awais', 78, 45], ['Taha', 91, 51]]
# gs = GSpread()
# gs.open_spreadsheet('test')
# print(gs.change_sheet_by_title("s2"))
# gs.insert_data(data)
# gs.retrieve_data()
# gs.clear_sheet()


from gspread_Helper import GSpread

gs = GSpread()

worksheet = gs.open_spreadsheet('test')
sheet = gs.change_sheet_by_title(worksheet,'s2')
print(sheet)