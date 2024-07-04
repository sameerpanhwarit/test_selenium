import sys
sys.path.append('C:\\Users\\S A M E E R\\Desktop\\net2Apps\\Advanced Task\\advancedTasks')
from gspread_Helper import GSpread
from Task1 import SapSuccessFactorLogin
from Models.rating_scale_models import ONB_Model, ONB_Status
from selenium.webdriver.common.by import By
from controller import *
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep
import color_helpers

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
        self.login.driver.implicitly_wait(60)
        self.helper.clickElement('//*[@id="__layout0-anchBar-__section5-anchor"]', 'xpath')
        self.helper.driver.implicitly_wait(10)
        

    def validation(self,sheet):
        objects = load_data(sheet)
        sleep(3)
        all_tr = self.helper.getElements('//table[@id="__xmlview5--onb2WhatToBringSettingsTable-listUl"]/tbody//tr', 'xpath')

        all_records, row_list = load_status(sheet)
        for rowNum, obj in enumerate(objects):
            for row_no, record in enumerate(all_records):
                if record.itemID == obj.id:
                    if record.status == 'pending':
                        obj.id = obj.id.strip()
                        all_texts_td2 = []
                        for tr in all_tr:
                            td = tr.find_elements(By.TAG_NAME, 'td')
                            if len(td) >= 3:
                                text_td2 = td[1].text
                                all_texts_td2.append(text_td2)

                        if obj.id in all_texts_td2:
                            for tr, text_td2 in zip(all_tr, all_texts_td2):
                                if obj.id == text_td2:
                                    tr.find_element(By.CSS_SELECTOR,'span[aria-label="edit"]').click()
                                    sleep(3)

                                    allItems = self.helper.GetListofElementAttributeText('//div[@role="dialog"]//input','value','xpath')
                                    items = allItems[2:]
                                    idAndName = allItems[:2]

                                    if obj.id == idAndName[0]:
                                        color_helpers.set_cell_color_green(sheet,rowNum+1,'B')
                                    else: color_helpers.set_cell_color_red(sheet,rowNum+1,'B')

                                    if obj.listName == idAndName[1]:
                                        color_helpers.set_cell_color_green(sheet,rowNum+1,'C')
                                    else: color_helpers.set_cell_color_red(sheet,rowNum+1,'C')

                                    if obj.item not in items:
                                        color_helpers.set_cell_color_red(sheet,rowNum+1,'D')
                                        self.helper.clickElement('//footer//button[1]','xpath')
                                        sleep(3)
                                        self.helper.clickElement('//footer//button[2]','xpath')
                                        break

                                    else:
                                        color_helpers.set_cell_color_green(sheet,rowNum+1,'D')
                                        self.helper.clickElement('//footer//button[2]','xpath')
                                        ignoreBtn = self.helper.waitforElementtobevisible('//footer//button[1][@class="sapMBtnBase sapMBtn sapMBarChild"]','xpath')
                                        if ignoreBtn is not False:
                                            self.helper.clickElement('//footer//button[1][@class="sapMBtnBase sapMBtn sapMBarChild"]','xpath')
                                        sleep(2)
                                        # break
                        else:
                            color_helpers.color_cells_a_google_sheet(obj, sheet)

                        sheet.update(range_name=f'G{row_list[row_no]}', values=[['Processed']])



if __name__ == '__main__':
    gs = GSpread()
    spreadsheet = gs.open_spreadsheet('test')
    sheet = gs.change_sheet_by_title(spreadsheet, 'ONB')

    oneDayList = OneDayList()
    oneDayList.navigate_to_ONBPage()
    oneDayList.validation(sheet)

    