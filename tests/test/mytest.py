import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

class myTestClass():

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.get("https://precisionrenovation.ca/our-philosophy/")
        self.driver.maximize_window()
        el = self.driver.find_element(By.XPATH, "//body")
        self.driver.execute_script("window.scroll(0,1000)")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(2)
        self.driver.execute_script("window.scroll(0,0)")
        time.sleep(5)
        el.screenshot("D:\\workspace_python\\hypeddit-Project\\Files\\f.jpg")
        self.driver.quit()

t = myTestClass()

