from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class myTestClass():

    def __init__(self):


    def myLogin(self):

        driver.find_element(By.ID, "login_email").send_keys("anil@baltech.in")
        driver.find_element(By.ID, "login_password").send_keys("1234567")
        driver.find_element(By.ID, "login_button").click()

