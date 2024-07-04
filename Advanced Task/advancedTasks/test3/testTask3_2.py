from Task2 import RatingScaleNavigator
from selenium.webdriver.common.by import By
from time import sleep
from gspread_Helper import GSpread

class RatingDataScraper:
    def __init__(self):
        self.rating_scale_navigator = RatingScaleNavigator()
        self.driver = self.rating_scale_navigator.success_factor_login.helper.driver
        self.helper = self.rating_scale_navigator.success_factor_login.helper

    def scrape_rating_cells(self):
        self.rating_scale_navigator.navigate_to_rating_scale()
        current_url = self.driver.current_url

        all_rating_data = ['SNO', 'Name', 'Description', 'Score', 'Label', 'Description']

        rating_rows = self.helper.getElements('//table[@id="26:m-m-tbl"]/tbody//tr//td[1]//a', 'xpath')

        for row_index in range(len(rating_rows)):
            self.driver.get(current_url)
            self.driver.implicitly_wait(10)

            row_element = self.helper.getElement(f'//table[@id="26:m-m-tbl"]/tbody//tr[{row_index + 1}]//td[1]//a', 'xpath')
            row_element.click()

            ok_button = self.helper.waitforElementtobevisible('//button[@data-help-id="okButton"]', 'xpath')
            if ok_button is not False:
                ok_button = self.helper.getElement('//button[@data-help-id="okButton"]', 'xpath')
                ok_button.click()
    
            name = self.helper.getElementAttributeText('//*[@id="48:_txtFld"]','value','xpath')
            description = self.helper.getElement('//*[@id="50:_txtArea"]','xpath')

            rows = self.helper.getElements('//table[@id="66:m-m-tbl"]/tbody//tr','xpath')
            rows = rows[:-1]

            for row in rows:
                temp_data = []

                temp_data.append(name)
                temp_data.append(description.get_attribute('value'))

                cells = row.find_elements(By.TAG_NAME, 'td')
                cells = cells[:-1]

                for i, cell in enumerate(cells):
                    if i == 2:
                        text_area = cell.find_element(By.TAG_NAME, 'textarea')
                        temp_data.append(text_area.text)
                    else:
                        tag = cell.find_element(By.TAG_NAME, 'input')
                        temp_data.append(tag.get_attribute('value'))

                gs.insert_data(sheet, temp_data)
                
        return all_rating_data


gs = GSpread()
spreadsheet = gs.open_spreadsheet('https://docs.google.com/spreadsheets/d/1TOEFIybUneey13EaKB3jJ5Mzst3hwZf7B_JwDILpSOo/edit#gid=0')
sheet = gs.change_sheet_by_title(spreadsheet, 'Sheet1')

RDS = RatingDataScraper()
rating_data = RDS.scrape_rating_cells()
