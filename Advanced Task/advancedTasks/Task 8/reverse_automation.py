import sys
sys.path.append('C:\\Users\\S A M E E R\\Desktop\\net2Apps\\Advanced Task\\advancedTasks')
from gspread_Helper import GSpread
from Task1 import SapSuccessFactorLogin
from Models.rating_scale_models import ONB_Model, ONB_Status
from selenium.webdriver.common.by import By
from controller import *
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
        self.login.driver.implicitly_wait(60)
        self.helper.clickElement('//*[@id="__layout0-anchBar-__section5-anchor"]', 'xpath')
        self.helper.driver.implicitly_wait(10)
        

    def automation(self):
        objects = load_data(sheet)
        all_records_status, row_list = load_status(sheet)
        sleep(3)
        # all_tr = self.helper.getElements('//table[@id="__xmlview5--onb2WhatToBringSettingsTable-listUl"]/tbody//tr', 'xpath')

        for obj in objects:

            for row_no, record_status in enumerate(all_records_status):
                # all_tr = self.helper.getElements('//table[@id="__xmlview5--onb2WhatToBringSettingsTable-listUl"]/tbody//tr', 'xpath')
                if record_status.itemID == obj.id:
                    if record_status.status == 'pending':

                        all_tr = self.helper.getElements(
                            '//table[@id="__xmlview5--onb2WhatToBringSettingsTable-listUl"]/tbody//tr', 'xpath')
                        obj.id = obj.id.strip()

                        all_texts_td2 = []
                        for tr in all_tr:
                            td = tr.find_elements(By.TAG_NAME, 'td')
                            if len(td) >= 3:
                                text_td2 = td[1].text
                                all_texts_td2.append(text_td2)
                        print(obj.id)
                        if obj.id.upper() in all_texts_td2:
                            for tr, text_td2 in zip(all_tr, all_texts_td2):
                                if obj.id.upper() == text_td2:
                                    tr.find_element(By.CSS_SELECTOR,'span[aria-label="edit"]').click()
                                    sleep(3)

                                    allItems = self.helper.GetListofElementAttributeText('//div[@role="dialog"]//input','value','xpath')
                                    items = allItems[2:]
                                    print(allItems)

                                    if obj.item not in items:
                                        self.helper.clickElement('//div[@role="dialog"]//section//button', 'xpath')
                                        sleep(5)
                                        addItem = self.helper.getElements('//div[@role="dialog"]//input','xpath')
                                        print(len(addItem))
                                        addItem = addItem[-1]
                                        addItem.send_keys(obj.item)
                                        self.helper.clickElement('//footer//button[1]','xpath')
                                        sleep(3)
                                        self.helper.clickElement('//footer//button[2]','xpath')
                                        break

                                    else:
                                        self.helper.clickElement('//footer//button[2]','xpath')
                                        ignoreBtn = self.helper.waitforElementtobevisible('//footer//button[1][@class="sapMBtnBase sapMBtn sapMBarChild"]','xpath')
                                        if ignoreBtn is not False:
                                            self.helper.clickElement('//footer//button[1][@class="sapMBtnBase sapMBtn sapMBarChild"]','xpath')
                                        sleep(2)
                                        break
                        else:
                            print('Add new Executed')
                            self.helper.clickElement('//button[@id="__button5"]','xpath')
                            inputs = self.helper.getElements('//div[@role="dialog"]//input','xpath')

                            inputs[0].send_keys(obj.id)
                            inputs[1].send_keys(obj.listName)

                            self.helper.clickElement('//div[@role="dialog"]//button[@title="Add"]', 'xpath')

                            addItemInput = self.helper.getElements('//div[@role="dialog"]//input', 'xpath')
                            addItemInput[-1].send_keys(obj.item)

                            self.helper.clickElement('//div[@role="dialog"]//button[@id="onb2WhatToBringSettingsAddModifyDialogFragment--onb2WhatToBringSettingsSubmitButton"]','xpath')
                            sleep(4)
                            self.helper.clickElement('//footer//button[2]','xpath')
                            sleep(5)

                        sheet.update(range_name=f'G{row_list[row_no]}', values=[['Processed']])

if __name__ == '__main__':
    gs = GSpread()
    spreadsheet = gs.open_spreadsheet('test')
    sheet = gs.change_sheet_by_title(spreadsheet, 'ONB')

    oneDayList = OneDayList()
    oneDayList.navigate_to_ONBPage()
    oneDayList.automation()

    
    