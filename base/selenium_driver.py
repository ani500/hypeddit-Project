from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import logging
import utilities.custom_logger as c1


class SeleniumDriver():
    log = c1.customLogger(logging.DEBUG)
    def __init__(self, driver):

        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + "  not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found Locator :" + locator + "LocatorType :" + locatorType)
            print("Element Found Locator :" + locator + "LocatorType :" + locatorType)
        except:
            self.log.info("Element Not Found Locator :" + locator + "LocatorType :" + locatorType)
            print("Element not Found Locator :" + locator + "LocatorType :" + locatorType)
        return element

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on the Element Locator :" + locator + "LocatorType :" + locatorType)
        except:
            self.log.info("Cannot clicked on the Element Locator :" + locator + "LocatorType :" + locatorType)
            print_stack()
            # raise RuntimeError("Test Case Aborted")

    def sendKeys(self, text, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(text)
            self.log.info("Send Keys Successfully Locator :" + locator + "LocatorType :" + locatorType)
        except:
            self.log.info("Not Wirte to the Element Locator :" + locator + "LocatorType :" + locatorType)
            print_stack()

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found Locator :" + locator + "LocatorType :" + locatorType)
                return True
            else:
                self.log.info("Element Not Found Locator :" + locator + "LocatorType :" + locatorType)
                return False
        except:
            self.log.info("Element Not Found Locator :" + locator + "LocatorType :" + locatorType)
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found Locator :" + locator + "LocatorType :" + locatorType)
                return True
            else:
                self.log.info("Element Not Found Locator :" + locator + "LocatorType :" + locatorType)
                return False
        except:
            self.log.info("Element Not Found Locator :" + locator + "LocatorType :" + locatorType)
            return False

    def waitForElement(self, locator, locatorType="id", timeout=10, poll_Frequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, poll_Frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     ElementClickInterceptedException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def checkRadioElementClick(self, locator, locatorType, idlocator, idlocatorType="id"):
        try:
            elementxpath = self.getElement(locator, locatorType)
            elementid = self.getElement(idlocator, idlocatorType)
            result = elementid.is_selected()

            if result is not True:
                elementxpath.click()
                self.log.info("Clicked on the Element Locator :" + locator + "LocatorType :" + locatorType)
            else:
                self.log.info("Element already Checked :" + locator + "LocatorType :" + locatorType)

        except:
            self.log.info("Cannot clicked on the Element Locator :" + locator + "LocatorType :" + locatorType)
            print_stack()

    def switchWindowHander(self, m):
        handles = self.driver.window_handles
        print(handles)
        size = len(handles)
        if m != 1:
            for x in range(size):
                if handles[x] != self.driver.current_window_handle:
                    self.driver.switch_to.window(handles[x])
                    print(self.driver.title)

        else:
            print("Hello")
            self.driver.switch_to.window(handles[0])
            print(self.driver.title)

    def openUrl(self,url):
        self.driver.get(url)











