import sys
sys.path.append('C:\\Users\\S A M E E R\Desktop\\net2Apps\\Advanced Task\\advancedTasks')
from rating_scale_models import rating_status, rating_scale
from Task2 import RatingScaleNavigator 
from selenium.webdriver.common.by import By
from gspread_Helper import GSpread
from time import sleep
import Task3.controllers_rating_scale as controllers_rating_scale

#controller for scrape names and status
class NamesStatus:
    def __init__(self):
        self.rating_scale_navigator = RatingScaleNavigator()
        self.driver = self.rating_scale_navigator.success_factor_login.helper.driver
        self.helper = self.rating_scale_navigator.success_factor_login.helper
        self.rating_scale_navigator.navigate_to_rating_scale()

    def scrape_names(self):
        all_names = self.helper.getElements('//table[@id="26:m-m-tbl"]/tbody//tr/td[1]//a', 'xpath')
        rating_status_objects = []

        for name_element in all_names:
            name = name_element.text
            rating_status_objects.append(rating_status(name))
        return rating_status_objects

#controller for check status
class scrape_data_info(NamesStatus):
    def __init__(self):
        super().__init__()
        self.rating_scale = []

    def scrape_rating_cells(self,xpath):    
        self.helper.clickElement(xpath,'xpath')
        sleep(2)

        ok_button = self.helper.waitforElementtobevisible('//button[@data-help-id="okButton"]', 'xpath')
        if ok_button is not False:
            ok_button = self.helper.getElement('//button[@data-help-id="okButton"]', 'xpath')
            ok_button.click()

        name = self.helper.getElementAttributeText('//*[@id="48:_txtFld"]','value','xpath')
        description = self.helper.getElement('//*[@id="50:_txtArea"]','xpath')
        description = description.get_attribute('value')

        rows = self.helper.getElements('//table[@id="66:m-m-tbl"]/tbody//tr','xpath')
        rows = rows[:-1]

        for row in rows:

            cells = row.find_elements(By.TAG_NAME, 'td')
            cells = cells[:-1]

            for i, cell in enumerate(cells):
                if i == 0:
                    score = cell.find_element(By.TAG_NAME, 'input')
                    score = score.get_attribute('value')
                elif i == 1:
                    label = cell.find_element(By.TAG_NAME, 'input')
                    label = label.get_attribute('value')
                elif i == 2:
                    score_description = cell.find_element(By.TAG_NAME, 'textarea')
                    score_description = score_description.text                  
                

            self.rating_scale.append(rating_scale(name,description, score,label, score_description))


if __name__ == '__main__':

    gs = GSpread()
    spreadsheet = gs.open_spreadsheet('test')
    sheet = gs.change_sheet_by_title(spreadsheet, 'data')


    nameStatus = NamesStatus()
    objects_list = nameStatus.scrape_names()
    controllers_rating_scale.fill_data(objects_list, sheet)

    # scrapedata = scrape_data_info()
    # rating_scale = controllers_rating_scale.load_pending_data(sheet)
    # controllers_rating_scale.fill_to_gspread(sheet,rating_scale)


    # scrapedata.update_to_gspread(sheet)
