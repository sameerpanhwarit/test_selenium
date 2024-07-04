from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import selenium.common.exceptions as Exceptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *


class Helper:
    def __init__(self, driver = None):
        # options = Options()
        # options.headless = True
        # self.driver = webdriver.Chrome(options=options)
        if driver is not None:
            self.driver = driver
        else:
            self.driver = webdriver.Firefox()

    def byType(self, locatorType):
        locatorType = locatorType.lower()

        if locatorType == "id":
            return By.ID
        elif locatorType == "class_name":
            return By.CLASS_NAME
        elif locatorType == "css_selector":
            return By.CSS_SELECTOR
        elif locatorType == "tag_name":
            return By.TAG_NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "link_text":
            return By.LINK_TEXT
        elif locatorType == "partial_link_text":
            return By.PARTIAL_LINK_TEXT
        else:
            print(f'Element{locatorType} is not valid.')
            return None

    def getElement(self, locator, locatorType):

        byType = self.byType(locatorType)
        element = None

        if byType is not None:
            try:
                element = self.driver.find_element(byType, locator)
            except Exception as e:
                print(e)
        return element

    def getElementText(self, locator, locatorType):

        elementText = ""
        element = self.getElement(locator, locatorType)
        if element is not None:
            elementText = element.text
            
        return elementText 

    def getElementAttributeText(self, locator, Attribute, locatorType):
       
       Attrtext = ""
       element = self.getElement(locator, locatorType)

       if element is not None:
           Attrtext = element.get_attribute(Attribute)   
       else:
           print(f'{Attribute} Attribute text not found.')

       return Attrtext

    def clickElement(self, locator, locatorType):

        element = self.getElement(locator, locatorType)

        if element is not None:
            try:
                element.click()
                return True
            except:
                return False
        else:
            return False

    def getElements(self, locator, locatorType):

        elements = []
        byType = self.byType(locatorType)

        if byType is not None:
            try:
                elements = self.driver.find_elements(byType, locator)

            except Exception as e:
                print(e)

        return elements

    def getListofElementText(self, locator, locatorType):

        listElementsText = []
        elements = self.getElements(locator, locatorType)

        if len(elements) > 0:
                for element in elements:
                    listElementsText.append(element.text)

        return listElementsText
            

    def GetListofElementAttributeText(self, locator, Attribute, locatorType):
        listElements = []
        elements = self.getElements(locator, locatorType)
        if len(elements) > 0:
            for element in elements:
                attributeText = element.get_attribute(Attribute)
                if attributeText is not None:
                    listElements.append(attributeText)
        return listElements


    def isElementPresent(self, locator, locatorType):
        element = self.getElement(locator, locatorType)
        if element is not None:
            return True
        else:
            return False
        
    def waitforElementtobevisible(self, locator, locatorType):
        byType = self.byType(locatorType)
        if byType is not None:
            try:
                wait = WebDriverWait(self.driver, 60, 0.5, [NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
                element = wait.until(EC.visibility_of_element_located((byType, locator)))
                if element is not None:
                    return True
            except:
                # print(f'Element with - {locator} and {locatorType} is not found.')
                return False