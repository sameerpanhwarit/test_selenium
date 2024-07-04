import sys
sys.path.append('C:\\Users\\S A M E E R\\Desktop\\net2Apps\\Advanced Task\\advancedTasks')
from gspread_Helper import GSpread
from Task1 import SapSuccessFactorLogin
from Models.rating_scale_models import ONB_Model, ONB_Status
from selenium.webdriver.common.by import By
from controllers import fill_data, load_pending_data, fill_records_into_sheet
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class OneDayList:
    def __init__(self):
        self.login = SapSuccessFactorLogin()
        self.login.login()
        self.helper = self.login.helper
        self.action_chains = ActionChains(self.helper.driver)
    
    #navigate ONB page
    def navigate_to_ONBPage(self):
        homePageURL = self.login.driver.current_url
        scrub_id = homePageURL.split("?")[1]

        onbURL = f'https://hcm41preview.sapsf.com/xi/ui/onboarding2/pages/onb2ManagePrograms.xhtml?&{scrub_id}'
        self.login.driver.get(onbURL)
        self.login.driver.implicitly_wait(20)
        sleep(5)
        self.helper.clickElement('//*[@id="__layout0-anchBar-__section5-anchor"]', 'xpath')

    #scrape data from process pending items
    def scrape_onb_status(self):
        all_objects = []
        all_td = self.helper.getElements('//table[@id="__xmlview5--onb2WhatToBringSettingsTable-listUl"]/tbody//tr//td[2]', By.XPATH)
        
        for td in all_td:
            all_objects.append(ONB_Status(td.text))

        return all_objects
    
    def scrape_pending_data(self, sheet):
        all_records = []
        objects = load_pending_data(sheet)
        all_tr = self.helper.getElements('//table[@id="__xmlview5--onb2WhatToBringSettingsTable-listUl"]/tbody//tr', 'xpath')
        for obj in objects:
            obj.status = obj.status.strip()
            if obj.status == 'pending':
                print('Executed')
                for tr in all_tr:         
                    td = tr.find_elements(By.TAG_NAME, 'td')
                    if td[1].text == obj.itemID:
                        edit_btn = tr.find_element(By.CSS_SELECTOR,'span[aria-label="edit"]')
                        self.helper.driver.execute_script("arguments[0].scrollIntoView(true);", edit_btn)
                        self.action_chains.move_to_element(edit_btn).click().perform()
                        sleep(3)

                        allItems = self.helper.GetListofElementAttributeText('//div[@role="dialog"]//input','value','xpath')
                        IdAndName = allItems[:2]
                        items = allItems[2:]

                        for item in items:
                            record = ONB_Model(IdAndName[0], IdAndName[1], item)
                            all_records.append(record)
                            row_no = objects.index(obj) + 2
                            sheet.update(f'G{row_no}', [['Processed']])
                        
                        self.helper.clickElement('//footer[@class="sapMDialogFooter"]//button[@class="sapMBtnBase sapMBtn sapMBarChild"]','xpath')
                        break

        return all_records

if __name__ == '__main__':

    gs = GSpread()
    spreadsheet = gs.open_spreadsheet('test')
    sheet = gs.change_sheet_by_title(spreadsheet, 'ONB')

    #Navigate ONB page and Fill pending data to gspread
    oneDayList = OneDayList()
    oneDayList.navigate_to_ONBPage()
    all_objects = oneDayList.scrape_onb_status()
    fill_data(all_objects, sheet)

    # records = oneDayList.scrape_pending_data(sheet)
    # fill_records_into_sheet(sheet, records)
    
    
    

    

