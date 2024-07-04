import sys
sys.path.append('C:\\Users\\S A M E E R\\Desktop\\net2Apps\\Advanced Task\\advancedTasks')

from gspread_Helper import GSpread
from Task1 import SapSuccessFactorLogin
from Models.rating_scale_models import tab_Element_status, tab_elements, tab_permission
from selenium.webdriver.common.by import By
from controller import fill_pending_data, load_pending_data, fill_main_section, fill_permission_section
from time import sleep

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

    # scrape data for fill into pending section
    def scrape_tab_elements_pending(self):
        status_objects = []
        all_tr = self.helper.getElements('//table[@cellspacing="10"]//tbody//tr//table[@cellspacing="10"]//tr', 'xpath')
        all_tr = all_tr[:-1]

        for tr in all_tr:
            status_objects.append(tab_Element_status(tr.text, 'pending'))

        return status_objects
                

    def scrape_tab_elements(self):
        all_records = []
        all_permission = []

        objects = load_pending_data(sheet)
        for obj in objects:
            if obj.status == 'pending':
                self.helper.clickElement(f'//a[text()="{obj.tabElement}"]', 'xpath')
                sleep(5)

                identifier = ''
                default_label = ''
                label = ''
                enabled = ''
                description = ''

                permission_type = '-'
                role = '-'

                tab_element_tr = self.helper.getElements('//table[@role="none"]/tbody/tr//td[2]', 'xpath')

                for i, tr in enumerate(tab_element_tr):

                    if i == 0:
                        identifier = tr.text
                    elif i == 1:
                        default_label = tr.text
                    elif i == 2:
                        label = tr.text
                    elif i == 3:
                        enabled = tr.text
                    elif i == 4:
                        description = tr.text
                    else:
                        permission_tr = self.helper.getElements('//table[@role="none"]/tbody/tr[6]//table/tbody//tr', 'xpath')
                        permission_tr = permission_tr[1:-1] if permission_tr else []  # Check if permission table exists

                        if len(permission_tr) > 0:
                            for tr in permission_tr:
                                tds = tr.find_elements(By.TAG_NAME, 'td')
                                permission_type = tds[0].text
                                role = tds[1].text
                                all_permission.append(tab_permission(identifier, permission_type, role))
                                row_no = objects.index(obj) + 2
                                sheet.update(f'M{row_no}', [['Processed']])
                            break
                        else:
                            row_no = objects.index(obj) + 2
                            sheet.update(f'M{row_no}', [['Processed']])
                            break

                all_records.append(tab_elements(identifier, default_label, label, enabled, description))

        return all_records, all_permission

if __name__ == '__main__':
    gs = GSpread()
    spreadsheet = gs.open_spreadsheet('test')
    sheet = gs.change_sheet_by_title(spreadsheet, 'Task 10 to 13')

    employeeElements = EmployeeElements()

    # status_objects = employeeElements.scrape_tab_elements_pending()
    # fill_pending_data(status_objects, sheet)

    all_records, permissions = employeeElements.scrape_tab_elements()

    # fill_main_section(sheet, all_records)
    fill_permission_section(sheet, permissions)

