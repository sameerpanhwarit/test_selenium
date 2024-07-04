import sys
sys.path.append('C:\\Users\\S A M E E R\\Desktop\\net2Apps\\Advanced Task\\advancedTasks')

from gspread_Helper import GSpread
from Task1 import SapSuccessFactorLogin
from selenium.webdriver.common.by import By
from controller import load_data, load_status
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

    def find_test_objects(self,permissions, check_obj):
        found_objects = []
        for obj in permissions:
            if obj.identifier == check_obj:
                found_objects.append(obj)
        return found_objects
    
    def automation(self):
        all_records, all_permissions = load_data(sheet)
        all_records_status, row_list = load_status(sheet)
        permission_supported =  ["processedapprovals","ectbenefitsfocus","varpaystatement", "pendingapprovals", "varpayindview", "compstatement", "personalInfoTab", "employmentInfoTab", "combinedstatement"]


        for obj in all_records:

            if obj.identifier == '':
                break

            for row_no, record_status in enumerate(all_records_status):
                if record_status.tabElement == obj.identifier:
                    if record_status.status == 'pending':
                        isPresent = self.helper.isElementPresent(f'//a[text()="{obj.identifier}"]', 'xpath')
                        if isPresent is True:
                            self.helper.clickElement(f'//a[text()="{obj.identifier}"]', 'xpath')
                            sleep(3)

                            self.helper.clickElement('//div[@class="ectFCTitle"]//button', 'xpath')
                            sleep(3)
                            self.helper.clickElement('//div[@class="sfOverlayMgr"]//a','xpath')
                            sleep(2)

                            tab_element_tr = self.helper.getElements('//table[@role="none"]/tbody/tr//td[2]', 'xpath')

                            for i, tr in enumerate(tab_element_tr):

                                if i == 1:
                                    default_label = tr.text
                                    if default_label != obj.default_label:
                                        valueInput = tr.find_element(By.TAG_NAME, 'input')
                                        valueInput.clear()
                                        valueInput.send_keys(obj.default_label)
                                elif i == 2:
                                    label = tr.text
                                    if label != obj.label:
                                        valueInput = tr.find_element(By.TAG_NAME, 'input')
                                        valueInput.clear()
                                        valueInput.send_keys(obj.label)
                                elif i == 3:
                                    enabled = tr.text
                                    if enabled != obj.enabled:
                                        span = self.helper.getElement(
                                            '//table[@role="none"]/tbody/tr[4]//td[2]//span[contains(@class,"toggle")]','xpath')
                                        span.click()

                                        options = self.helper.getElements('//div[@class="scrolling-page first-page"]//a','xpath')
                                        if obj.enabled == 'Yes':
                                            options[1].click()
                                        else:
                                            options[0].click()
                                elif i == 4:
                                    description = tr.text
                                    if description != obj.description:
                                        valueInput = tr.find_element(By.TAG_NAME, 'input')
                                        valueInput.clear()
                                        valueInput.send_keys(obj.description)

                            # permission automation statements
                            if obj.identifier in permission_supported:
                                foundObjects = self.find_test_objects(all_permissions, obj.identifier)

                                permission_tr = self.helper.getElements('//table[@role="none"]/tbody/tr[6]//table/tbody//tr', 'xpath')
                                permission_tr = permission_tr[1:-1] if permission_tr else []

                                if len(permission_tr) > 0:

                                    existing_permissions = []

                                    for tr in permission_tr:
                                        inputs = tr.find_elements(By.TAG_NAME, 'input')
                                        permission = inputs[0].get_attribute('value')
                                        role = inputs[1].get_attribute('value')
                                        existing_permissions.append((permission, role))

                                        if len(foundObjects) > 0:
                                            for obj in foundObjects:
                                                found = False
                                                for permission, role in existing_permissions:
                                                    if obj.permission == permission and obj.role == role:
                                                        found = True
                                                        break

                                                if not found:
                                                    addTr = self.helper.getElement(
                                                        '//table[@role="none"]/tbody/tr[6]//table/tbody/tr[last()]',
                                                        'xpath')

                                                    if addTr:
                                                        inp = addTr.find_element(By.XPATH, './/input[@type="text"]')
                                                        inp.send_keys(obj.role)

                                                        permissionSpan = addTr.find_element(By.XPATH,
                                                                                            './/input[@role="combobox"]//following-sibling::span[2]')
                                                        permissionSpan.click()
                                                        allOptions = self.helper.getElements(
                                                            '//div[@class="resizer-wrapper"]//a', 'xpath')

                                                        if obj.permission == 'none':
                                                            allOptions[0].click()
                                                        elif obj.permission == 'read':
                                                            allOptions[1].click()
                                                        elif obj.permission == 'write':
                                                            allOptions[2].click()

                                                        existing_permissions.append((obj.permission, obj.role))



                                else:
                                    for objct in foundObjects:
                                        addTr = self.helper.getElements('//table[@role="none"]/tbody/tr[6]//table/tbody//tr', 'xpath')
                                        addTrlen = len(addTr)

                                        inp = self.helper.getElement(f'//table[@role="none"]/tbody/tr[6]//table/tbody//tr[{addTrlen}]//input[@type="text"]','xpath')

                                        inp.send_keys(objct.role)

                                        permissionSpan = self.helper.getElement(f'//table[@role="none"]/tbody/tr[6]//table/tbody//tr[{addTrlen}]//input[@role="combobox"]//following-sibling::span[2]','xpath')
                                        permissionSpan.click()
                                        allOptions = self.helper.getElements('//div[@class="resizer-wrapper"]//a', 'xpath')

                                        if objct.permission == 'none':
                                            allOptions[0].click()

                                        elif objct.permission == 'read':
                                            allOptions[1].click()

                                        elif objct.permission == 'write':
                                            allOptions[2].click()

                            saveBtn = self.helper.getElement('//div[@class="buttons"]//button', 'xpath')
                            saveBtn.click()
                            sleep(10)
                            # continue

                        else:
                            self.helper.clickElement('//a[text()="Create New"]', 'xpath')
                            sleep(5)

                            allFields = self.helper.getElements('//table[@role="none"]/tbody/tr//td[2]//input', 'xpath')
                            for i, field in enumerate(allFields):
                                if i == 1:
                                    field.send_keys(obj.identifier)
                                elif i == 2:
                                    field.send_keys(obj.default_label)
                                elif i==3:
                                    field.send_keys(obj.label)
                                elif i==4:
                                    span = self.helper.getElement('//table[@role="none"]/tbody/tr[4]//td[2]//span[contains(@class,"toggle")]','xpath')
                                    span.click()
                                    options = self.helper.getElements('//div[@class="scrolling-page first-page"]//a', 'xpath')
                                    if obj.enabled == 'Yes':
                                        options[1].click()
                                elif i==5:
                                    field.send_keys(obj.description)

                                if obj.identifier in permission_supported:
                                    foundObjects = self.find_test_objects(all_permissions, obj.identifier)
                                    if len(foundObjects) > 0:
                                        for objct in foundObjects:
                                            addTr = self.helper.getElements('//table[@role="none"]/tbody/tr[6]//table/tbody//tr', 'xpath')
                                            addTrlen = len(addTr)

                                            inp = self.helper.getElement(f'//table[@role="none"]/tbody/tr[6]//table/tbody//tr[{addTrlen}]//input[@type="text"]','xpath')

                                            inp.send_keys(objct.role)

                                            permissionSpan = self.helper.getElement(f'//table[@role="none"]/tbody/tr[6]//table/tbody//tr[{addTrlen}]//input[@role="combobox"]//following-sibling::span[2]','xpath')
                                            permissionSpan.click()
                                            allOptions = self.helper.getElements('//div[@class="resizer-wrapper"]//a', 'xpath')

                                            if objct.permission == 'none':
                                                allOptions[0].click()

                                            elif objct.permission == 'read':
                                                allOptions[1].click()

                                            elif objct.permission == 'write':
                                                allOptions[2].click()

                                saveBtn = self.helper.getElement('//div[@class="buttons"]//button', 'xpath')
                                saveBtn.click()
                                sleep(5)

                        sheet.update(range_name=f'M{row_list[row_no]}', values=[['Processed']])

if __name__ == '__main__':
    gs = GSpread()
    spreadsheet = gs.open_spreadsheet('test')
    sheet = gs.change_sheet_by_title(spreadsheet, 'Task 10 to 13')

    employeeElements = EmployeeElements()
    employeeElements.automation()
