from HelperMethods import Helper
from selenium import webdriver
from selenium.webdriver.common.by import By
class w3School:
    driver = webdriver.Firefox()
    def __init__(self):
        self.helper = Helper()
        self.dictHeadings={}
    
    def navigate_to_url(self,url):
        self.helper.driver.get(url)
        sidebar = self.helper.getElement('leftmenuinnerinner', 'id')
        return sidebar
    
    def separate_sections(self,data):
        elements = data.find_elements(By.TAG_NAME, 'h2')
        for element in elements:
            heading = element.text
            sub_headings = []

            siblings = element.find_elements(By.XPATH, 'following-sibling::*')
            for sibling in siblings:
                if sibling.tag_name == 'h2':
                    break
                elif sibling.tag_name == 'a':
                    sub_headings.append(sibling.text)

            self.dictHeadings[heading] = sub_headings
    
    def print_headings(self):
        indexofHeading = 0
        print(f'{"="*5}Headings{"="*5}')
        for key in self.dictHeadings.keys():
            indexofHeading = indexofHeading+1
            print(f'{indexofHeading}. {key}')   

    def wait_for_input(self):
        while True:
            print("_"*20)
            userInput = input("Enter any Heading for get sub headings: ").title()
            subHeadings = self.dictHeadings.get(userInput)

            if subHeadings:
                print(f'{userInput} - {subHeadings}')
                break
            else:
                print(f'Heading {userInput} not found.')


url = 'https://www.w3schools.com/python/python_intro.asp'

w3 = w3School()
elementsList = w3.navigate_to_url(url)
w3.separate_sections(elementsList)
w3.print_headings()
w3.wait_for_input()