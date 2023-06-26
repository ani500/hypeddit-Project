import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class anil(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='C:/Users/Arnav/workspace_python/drivers/geckodriver')
        self.driver.maximize_window()
        self.driver.get("https://www.hypeddit.com/login")

    def test_mylogin(self):
        self.driver.find_element(By.ID, "login_email").send_keys("anil@baltech.in")
        self.driver.find_element(By.ID, "login_password").send_keys("1234567")
        self.driver.find_element(By.ID, "login_button").click()
        dash = self.driver.find_element(By.XPATH, "//h2[@class='text-uppercase']").text
        self.assertEqual("START YOUR FREE 7-DAY TRIAL", dash)
        self.assertEqual("START YOUR FREE 7-DAY TRIA1L", dash)



