import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.Home.fangate_pages import FangatePage
from pages.Home.login_pages import LoginPage
from pages.Spotify_growth.ad_pages import AdPage
import unittest
import time
from selenium.webdriver.common.by import By


class myTestClass(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://dev2.hypeddit.com/")
        self.driver.maximize_window()

        #self.lp = LoginPage(self.driver)
        #self.fp = FangatePage(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    @classmethod
    def setUp(self):
        self.fp = FangatePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ap = AdPage(self.driver)
    def test_CreateFangate(self):

        self.fp.devUnlock("BetterDevTest8675!")
        self.lp.login("regression126-100@baltech.in", "123456")
        #self.ap.createAd(AdType='track')
        self.driver.get("https://dev2.hypeddit.com/videomaker")
        time.sleep(10)
        self.driver.find_element(By.XPATH,"//div[@class='radio-option-box']//label[@for='video_size-radio-3'][@class='optionLabel']").click()
        time.sleep(15)










