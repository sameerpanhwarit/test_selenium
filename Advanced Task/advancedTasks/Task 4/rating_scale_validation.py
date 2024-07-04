import sys
sys.path.append('C:\\Users\\S A M E E R\\Desktop\\net2Apps\\Advanced Task\\advancedTasks')
from gspread_Helper import GSpread
from time import sleep
from Task2 import RatingScaleNavigator 
from selenium.webdriver.common.by import By
from selenium import webdriver
from controllers import load_data,load_status
from colorHelpers import set_cell_color_red, set_cell_color_green, color_cells_a_google_sheet


class CheckPresence:
    def __init__(self):
        self.rating_scale_navigator = RatingScaleNavigator()
        self.driver = self.rating_scale_navigator.success_factor_login.helper.driver
        self.helper = self.rating_scale_navigator.success_factor_login.helper
        self.rating_scale_navigator.navigate_to_rating_scale()

    def check_cell_data_on_webpage(self, all_objects):
        sleep(2) 

        scrapePage = self.helper.driver.current_url
        tr_now = 1

        name_column = 'B'
        description_column = 'C'
        score_column = 'D'
        label_column = 'E'
        score_description_column = 'F'

        all_records, row_list = load_status(sheet)
        for row_number, obj in enumerate(all_objects, start=2):
            for row_no, record in enumerate(all_records):
                if record.scale_name == obj.name:
                    if record.status =='pending':
                        xpath = f'//table[@id="26:m-m-tbl"]//tr//td[1]//a[text()="{obj.name}"]'
                        isElement = self.helper.isElementPresent(xpath, 'xpath')

                        if not isElement:
                            color_cells_a_google_sheet(obj, sheet)
                            sheet.update(range_name=f'I{row_list[row_no]}', values=[['Processed']])
                            continue

                        self.helper.clickElement(xpath, 'xpath')
                        sleep(2)

                        ok_button = self.helper.waitforElementtobevisible('//button[@data-help-id="okButton"]', 'xpath')
                        if ok_button is not False:
                            ok_button = self.helper.getElement('//button[@data-help-id="okButton"]', 'xpath')
                            ok_button.click()

                        name = self.helper.getElementAttributeText('//*[@id="48:_txtFld"]', 'value', 'xpath')
                        description = self.helper.getElement('//*[@id="50:_txtArea"]', 'xpath')
                        description = description.get_attribute('value')

                        xpath = f'//table[@id="66:m-m-tbl"]/tbody//tr[{tr_now}]//td'
                        all_td = self.helper.getElements(xpath,'xpath')
                        all_td = all_td[:-1]

                        a = self.helper.isElementPresent(f'{xpath}//a[text()="Add New Score"]','xpath')
                        if a is True:
                            tr_now = 1
                            sheet.format(f'B{row_number}:F{row_number}',  {'backgroundColor': {'red': 1.0}})
                            self.helper.driver.get(scrapePage)
                            self.helper.driver.implicitly_wait(10)
                            continue

                        score = ''
                        score_label = ''
                        score_description = ''

                        for i,td in enumerate(all_td):
                            if i == 0:
                                score = td.find_element(By.TAG_NAME, 'input')
                                score = score.get_attribute('value')
                                print(score)
                            elif i == 1:
                                score_label = td.find_element(By.TAG_NAME, 'input')
                                score_label = score_label.get_attribute('value')
                            elif i == 2:
                                score_description = td.find_element(By.TAG_NAME, 'textarea')
                                score_description = score_description.text


                        if obj.name == name:
                            set_cell_color_green(sheet, row_number, name_column)
                        else:
                            set_cell_color_red(sheet, row_number, name_column)

                        if obj.description == description:
                            set_cell_color_green(sheet, row_number, description_column)
                        else:
                            set_cell_color_red(sheet, row_number, description_column)
                        if obj.score == score:
                            set_cell_color_green(sheet, row_number, score_column)
                        else:
                            set_cell_color_red(sheet, row_number, score_column)
                        if obj.label == score_label:
                            set_cell_color_green(sheet, row_number, label_column)
                        else:
                            set_cell_color_red(sheet, row_number, label_column)
                        if obj.score_description == score_description:
                            set_cell_color_green(sheet, row_number, score_description_column)
                        else:
                            set_cell_color_red(sheet, row_number, score_description_column)

                        next_row_number = row_number + 1
                        if next_row_number < len(all_objects) + 2:
                            next_obj = all_objects[next_row_number - 2]
                            if obj.name == next_obj.name:
                                tr_now +=1
                            else:
                                tr_now = 1

                        sheet.update(range_name=f'I{row_list[row_no]}', values=[['Processed']])

                        self.helper.driver.get(scrapePage)
                        self.helper.driver.implicitly_wait(10)


if __name__ == '__main__':
    gs = GSpread()
    spreadsheet = gs.open_spreadsheet('test')
    sheet = gs.change_sheet_by_title(spreadsheet, 'data')

    cp = CheckPresence()
    all_objects = load_data(sheet)
    cp.check_cell_data_on_webpage(all_objects)
