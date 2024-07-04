import sys
sys.path.append('C:\\Users\\S A M E E R\\Desktop\\net2Apps\\Advanced Task\\advancedTasks')
from gspread_Helper import GSpread
from time import sleep
from Task2 import RatingScaleNavigator 
from selenium.webdriver.common.by import By
from selenium import webdriver
from controllers import load_data, load_status
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

class Automation:
    def __init__(self):
        self.rating_scale_navigator = RatingScaleNavigator()
        self.driver = self.rating_scale_navigator.success_factor_login.helper.driver
        self.helper = self.rating_scale_navigator.success_factor_login.helper
        self.rating_scale_navigator.navigate_to_rating_scale()

    def automate(self, objects):
        scrapePage = self.helper.driver.current_url
        obj_status, row_list = load_status(sheet)

        for obj in objects:
            for row_no, status in enumerate(obj_status):
                if status.scale_name == obj.name:
                    if status.status == 'pending':

                        xpath = f'//table[@id="26:m-m-tbl"]//tr//td[1]//a[text()="{obj.name}"]'
                        isElement = self.helper.isElementPresent(xpath, 'xpath')

                        if not isElement:

                            self.helper.clickElement('//span[text()="Create New Rating Scale"]', 'xpath')
                            self.helper.clickElement('//li[4]//input[@type="radio"]', 'xpath')
                            self.helper.clickElement('//div[@class="sfDlgCntr fd-dialog__content fd-dialog__content--compact"]//button', 'xpath')


                            self.helper.getElement('//*[@id="48:_txtFld"]','xpath').send_keys(obj.name)
                            self.helper.getElement('//*[@id="50:_txtArea"]','xpath').send_keys(obj.description)


                            self.helper.getElement('//input[@value="Score"]', 'xpath').send_keys(obj.score)
                            self.helper.getElement('//input[@value="Give a short label for the score..."]','xpath').send_keys(obj.label)
                            self.helper.getElement('//textarea[text()="Give detailed description..."]','xpath').send_keys(obj.score_description)

                            self.helper.clickElement('//span[@class="left"]//span[@class="right"]//a//span[text()="Save"]', 'xpath')
                            sleep(3)

                            sheet.update(range_name=f'I{row_list[row_no]}', values=[['Processed']])
                            self.driver.get(scrapePage)
                            break


                        self.helper.clickElement(xpath, 'xpath')
                        sleep(2)

                        ok_button = self.helper.waitforElementtobevisible('//button[@data-help-id="okButton"]', 'xpath')
                        if ok_button is not False:
                            ok_button = self.helper.getElement('//button[@data-help-id="okButton"]', 'xpath')
                            ok_button.click()

                        all_td = self.helper.getElements('//table[@id="66:m-m-tbl"]//tr//td[1]','xpath')
                        all_td = all_td[:-1]

                        tr_score_list= []

                        for td in all_td:
                            score = td.find_element(By.TAG_NAME, 'input').get_attribute('value')

                            tr_score_list.append(score)

                        if obj.score in tr_score_list:
                            self.driver.get(scrapePage)
                            continue

                        addNewScore = '//a[text()="Add New Score"]'
                        self.helper.clickElement(addNewScore, 'xpath')
                        sleep(2)

                        self.helper.getElement('//input[@value="Score"]', 'xpath').send_keys(obj.score)
                        self.helper.getElement('//input[@value="Give a short label for the score..."]', 'xpath').send_keys(obj.label)
                        self.helper.getElement('//textarea[text()="Give detailed description..."]', 'xpath').send_keys(obj.score_description)

                        self.helper.clickElement('//span[@class="left"]//span[@class="right"]//a//span[text()="Save"]', 'xpath')
                        sleep(2)

                        print(row_list[row_no])
                        sheet.update(range_name=f'I{row_list[row_no]}', values=[['Processed']])
                        self.driver.get(scrapePage)

if __name__ == '__main__':

    gs = GSpread()
    spreadsheet = gs.open_spreadsheet('test')
    sheet = gs.change_sheet_by_title(spreadsheet, 'data')

    objects = load_data(sheet)

    automation = Automation()
    automation.automate(objects)
