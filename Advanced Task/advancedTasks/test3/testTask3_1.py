from Task2 import RatingScaleNavigator
from selenium.webdriver.common.by import By

class RatingScaleScraper:
    def __init__(self):
        self.rating_scale_navigator = RatingScaleNavigator()
        self.driver = self.rating_scale_navigator.success_factor_login.driver

    def scrape_rating_scale(self):

        table_data = {}

        self.rating_scale_navigator.navigate_to_rating_scale()

        rating_table = self.driver.find_elements(By.XPATH, '//table[@id="26:m-m-tbl"]/tbody//tr')
        
        for key ,row in enumerate(rating_table):
            cells = row.find_elements(By.TAG_NAME, 'td')
            temp_list = []
            for i,cell in enumerate(cells):
                if i == 1:
                    checkbox = cell.find_element(By.TAG_NAME,"input")
                    value = checkbox.get_attribute('aria-checked')
                    if value.lower() == 'true':
                        temp_list.append('active')
                    else:
                        temp_list.append('non-active')
                if cell.text == '':
                    continue
                temp_list.append(cell.text)
            table_data[key+1]=temp_list
        
        return table_data

if __name__ == "__main__":
    rating_scale_scraper = RatingScaleScraper()
    Data = rating_scale_scraper.scrape_rating_scale()
    for key, value in Data.items():
        print(f'{key} - {value}')
