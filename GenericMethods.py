from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.common.exceptions as Exceptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *


class Helper:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window

    def checkType(self, locatorType):
        locatorType = locatorType.lower()

        try:
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
            else:
                print(f"Element {locatorType} Type is invalid.")
                return False
        except Exceptions as e:
            pass

    def getElement(self, locator, locatorType):
        byType = self.checkType(locatorType)
        try:
            if byType:
                element = self.driver.find_element(byType, locator)
                return element
            else:
                return False
        except Exception as e:
            pass

    def getElementText(self, locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            if element:
                return element.text
        except Exception as e:
            print(e)

    def getElementAttributeText(self, locator, Attribute, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            if element:
                attribute = Attribute.lower()
                return element.get_attribute(attribute)
        except Exception as e:
            print(e)

    def clickElement(self, locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            if element:
                element.click()
                return True
            else:
                print("Element not found")
                return False
        except Exception as e:
            print(e)
            return False

    def getElements(self, locator, locatorType):
        byType = self.checkType(locatorType)
        try:
            if byType:
                elements = self.driver.find_elements(byType, locator)
                if elements:
                    print(f"Element found with locator {locator}")
                    return elements
            else:
                return None
        except Exception as e:
            print(e)

    def getListofElementText(self, locator, locatorType):
        listElementsText = []
        try:
            elements = self.getElements(locator, locatorType)
            if len(elements) > 0:
                for element in elements:
                    listElementsText.append(element.text)
                return listElementsText
            else:
                print("No any element found.")
        except Exception as e:
            print(e)

    def GetListofElementAttributeText(self, locator, Attribute, locatorType):
        listElements = []
        try:
            elements = self.getElements(locator, locatorType)
            if len(elements) > 0:
                for element in elements:
                    attributeText = element.get_attribute(Attribute)
                    if attributeText:
                        listElements.append(attributeText)
                return listElements
            else:
                print("No Element Found.")
                return listElements
        except Exception as e:
            print(e)

    def isElementPresent(self, locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            if element:
                return True
            else:
                return False
        except Exception as e:
            print(e)
        
    def waitforElementtobevisible(self, locator, locatorType):
        byType = self.checkType(locatorType)
        if byType:
            try:
                wait = WebDriverWait(self.driver, 60, 0.5, [NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
                element = wait.until(EC.visibility_of_element_located((byType, locator)))
                if element:
                    return True
            except:
                print("Element not found.")
                return False
        else:
            print(f"Locator {locatorType} is invalid.")
