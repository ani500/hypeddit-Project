"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver
import os
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome import service


class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser

    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = "https://hypeddit.com/"
        if self.browser == "edge":
            # Set ie driver
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
            #edgedriver = "C:/workspace_python/drivers/msedgedriver.exe"
            #os.environ["webdriver.edge.driver"] = edgedriver
            #driver = webdriver.Edge(edgedriver)
            driver.set_window_size(1440, 900)
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            #driver = webdriver.Firefox(executable_path='C:/workspace_python/drivers/drivers/geckodriver')
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

            #chromedriver = "D:/workspace_python/drivers/chromedriver.exe"
            #os.environ["webdriver.chrome.driver"] = chromedriver
            #driver = webdriver.Chrome(chromedriver)
            driver.set_window_size(1440, 900)
        else:
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            #driver = webdriver.Firefox(executable_path='C:/workspace_python/drivers/drivers/geckodriver')
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver
