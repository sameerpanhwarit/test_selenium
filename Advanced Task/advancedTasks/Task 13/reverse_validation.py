import sys
sys.path.append('C:\\Users\\S A M E E R\\Desktop\\net2Apps\\Advanced Task\\advancedTasks')

from gspread_Helper import GSpread
from Task1 import SapSuccessFactorLogin
from selenium.webdriver.common.by import By
from controller import load_data, load_status
from time import sleep
from colors_helper import color_cells_a_google_sheet,set_cell_color_green,set_cell_color_red

class EmployeeElements:
    def __init__(self):
        self.login = SapSuccessFactorLogin()
        self.login.login()
        self.helper = self.login.helper
        self.navigate_to_tab_elements()
    
    # navigate Manage Business Configuration page
    def navigate_to_tab_elements(self):
        homePageURL = self.login.driver.current_url
        scrub_id = homePageURL.split("?")[1]

        onbURL = f'https://hcm41preview.sapsf.com/xi/ui/businessconfig/pages/adminConfiguration.xhtml?&{scrub_id}'
        self.login.driver.get(onbURL)
        self.login.driver.implicitly_wait(60)

        sleep(2)
        click = self.helper.clickElement('//a[text()="Employee Profile"]', 'xpath')
        
        while click is not True:
            click = self.helper.clickElement('//a[text()="Employee Profile"]', 'xpath')

        sleep(2)
        self.helper.clickElement('//table//div//img', 'xpath')
        sleep(2)
        self.helper.clickElement('//a[text()="Tab Elements"]', 'xpath')
        sleep(2)

    def find_test_objects(self,permissions, check_obj):
        found_objects = []
        for obj in permissions:
            if obj.identifier == check_obj:
                found_objects.append(obj)
        return found_objects
    
    def validation(self):
       all_records, all_permissions = load_data(sheet)
       all_records_status, row_list = load_status(sheet)
       permission_supported =  ["ectbenefitsfocus","varpaystatement", "pendingapprovals", "varpayindview", "compstatement", "personalInfoTab", "employmentInfoTab", "combinedstatement"]


       for rowNo,obj in enumerate(all_records):
           rowNo = rowNo + 1

           if obj.identifier == '':
               break

           for row_no, record_status in enumerate(all_records_status):
               if record_status.tabElement == obj.identifier:
                   if record_status.status == 'pending':
                        isPresent = self.helper.isElementPresent(f'//a[text()="{obj.identifier}"]', 'xpath')
                        if isPresent is False:
                            color_cells_a_google_sheet(obj, sheet)
                            if obj.identifier in permission_supported:
                                all_values = sheet.findall(obj.identifier)
                                records_list = []
                                row_numbers = []

                                for value in all_values:
                                    if value.col == 8:
                                        row_numbers.append(value.row)
                                        record_i = sheet.cell(row=value.row, col=9).value.strip()
                                        record_h = sheet.cell(row=value.row, col=10).value.strip()
                                        records_list.append((record_i, record_h))

                                for index, (record_i, record_h) in enumerate(records_list):
                                    row = row_numbers[index]
                                    print(row+1)
                                    set_cell_color_red(sheet, row=row - 1, column='I')
                                    set_cell_color_red(sheet, row=row - 1, column='J')

                        if isPresent is True:

                            self.helper.clickElement(f'//a[text()="{obj.identifier}"]', 'xpath')
                            sleep(3)

                            self.helper.clickElement('//div[@class="ectFCTitle"]//button', 'xpath')
                            sleep(3)
                            self.helper.clickElement('//div[@class="sfOverlayMgr"]//a','xpath')
                            sleep(2)


                            tab_element_tr = self.helper.getElements('//table[@role="none"]/tbody/tr//td[2]', 'xpath')

                            for i, tr in enumerate(tab_element_tr):

                                if i == 0:
                                    set_cell_color_green(sheet,rowNo,'B')
                                elif i == 1:
                                    default_label = tr.find_element(By.TAG_NAME,'input').get_attribute('value')
                                    if default_label != obj.default_label:
                                       set_cell_color_red(sheet,rowNo,'C')
                                    else: set_cell_color_green(sheet,rowNo,'C')
                                elif i == 2:
                                    label = tr.find_element(By.TAG_NAME,'input').get_attribute('value')
                                    if label != obj.label:
                                        set_cell_color_red(sheet,rowNo,'D')
                                    else: set_cell_color_green(sheet,rowNo,'D')
                                elif i == 3:
                                    enabled = tr.text
                                    if enabled != obj.enabled:
                                        set_cell_color_red(sheet,rowNo,'E')
                                    else: set_cell_color_green(sheet,rowNo,'E')
                                elif i == 4:
                                    description = tr.find_element(By.TAG_NAME,'input').get_attribute('value')
                                    if description.strip() != obj.description.strip():
                                        set_cell_color_red(sheet,rowNo,'F')
                                    else: set_cell_color_green(sheet,rowNo,'F')


                            if obj.identifier in permission_supported:
                                all_values = sheet.findall(obj.identifier)
                                records_list = []
                                row_numbers = []

                                for value in all_values:
                                    if value.col == 8:
                                        row_numbers.append(value.row)
                                        record_i = sheet.cell(row=value.row, col=9).value.strip()
                                        record_h = sheet.cell(row=value.row, col=10).value.strip()
                                        records_list.append((record_i, record_h))

                                permission_tr = self.helper.getElements('//table[@role="none"]/tbody/tr[6]//table/tbody//tr', 'xpath')
                                permission_tr = permission_tr[1:-1] if permission_tr else []

                                permissions_roles = set()

                                for tr in permission_tr:
                                    inputs = tr.find_elements(By.TAG_NAME, 'input')
                                    permission = inputs[0].get_attribute('value').strip()
                                    role = inputs[1].get_attribute('value').strip()
                                    permissions_roles.add((permission, role))

                                for index, (record_i, record_h) in enumerate(records_list):
                                    row=row_numbers[index]
                                    if (record_i, record_h) in permissions_roles:
                                        set_cell_color_green(sheet,row=row-1,column='I')
                                        set_cell_color_green(sheet,row=row-1,column='J')
                                    else:
                                        set_cell_color_red(sheet,row=row-1,column='I')
                                        set_cell_color_red(sheet,row=row-1,column='J')
                        sheet.update(range_name=f'M{row_list[row_no]}', values=[['Processed']])


if __name__ == '__main__':
    gs = GSpread()
    spreadsheet = gs.open_spreadsheet('test')
    sheet = gs.change_sheet_by_title(spreadsheet, 'Task 10 to 13')

    employeeElements = EmployeeElements()
    employeeElements.validation()
