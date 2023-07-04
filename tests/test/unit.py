import logging
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.chrome import service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import utilities.custom_logger as t1
from PIL import Image, ImageChops


class anil():
    # testlog = t1.customLogger(logging.DEBUG)

    def setUp(self):

        self.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://precisionrenovation.ca")
        self.driver.implicitly_wait(3)

    # def test_mylogin(self):
    #     self.driver.find_element(By.ID, "login_email").send_keys("arnavangira@gmail.com")
    #     self.driver.find_element(By.ID, "login_password").send_keys("Uid@1234567")
    #     self.driver.find_element(By.ID, "login_button").click()
    #     #dash = self.driver.find_element(By.XPATH, "//h2[@class='text-uppercase']").text
    #     #self.assertEqual("START YOUR FREE 7-DAY TRIAL", dash)
    #     #self.assertEqual("START YOUR FREE 7-DAY TRIA1L", dash)
    #     self.driver.get("https://hypeddit.com/loudlinks/create")
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, "//button[@data-id='loudlink_fangate']//span[contains(text(),'Please "
    #                                        "select music')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(text(),'Automatically show my newest download gate')]").click()

    def test_getLInks(self):

        global morelinks
        ad_url_list = []
        ad_url_list_final =[]

        # Save all a elements
        links = self.driver.find_elements(By.XPATH, "//a")

        # Save all the href in the list
        for link in links:
            ad_url_list.append(link.get_attribute("href"))

        # Remove the duplicate Urls from the list
        ad_url_list = list(set(ad_url_list))

        # Hit all links of the list name ad_url_list, grab all a elements and put the href in the ad_url_list_final
        # list.
        for k in ad_url_list:
            try:
                self.driver.get(k)

                morelinks = self.driver.find_elements(By.XPATH, "//a")
            except:
                print("except block")

            for morelink in morelinks:
                ad_url_list_final.append(morelink.get_attribute("href"))
            morelinks.clear()

            for a in ad_url_list_final:
                el = self.driver.find_element(By.XPATH, "//body")
                print("hello")
                self.driver.execute_script("window.scroll(0,1000)")
                time.sleep(2)
                self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
                time.sleep(2)
                self.driver.execute_script("window.scroll(0,0)")
                time.sleep(5)
                el.screenshot("D:\\workspace_python\\hypeddit-Project\\Files" + "\\" + a + ".png")
                print(a)


        # Remove duplicate Urls from the list
        ad_url_list_final = list(set(ad_url_list_final))

        # Open each url from the list, take the Screenshot and put it in the folder.
        for f in ad_url_list_final:
            self.driver.get(f)
            time.sleep(5)
            el = self.driver.find_element(By.XPATH, "//body")
            print("hello")
            self.driver.execute_script("window.scroll(0,1000)")
            time.sleep(2)
            self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
            time.sleep(2)
            self.driver.execute_script("window.scroll(0,0)")
            time.sleep(5)
            el.screenshot("D:\\workspace_python\\hypeddit-Project\\Files\\".join(f).join(".jpg"))


ob = anil()
ob.setUp()
ob.test_getLInks()










    # def test_imageDiff(self):
    #     img1 = Image.open("D:\\workspace_python\\hypeddit-Project\\Files\\share.png")
    #     img2 = Image.open("D:\\workspace_python\\hypeddit-Project\\Files\\promote.png")
    #     diff = ImageChops.overlay(img1, img2)
    #     diff.save("D:\\workspace_python\\hypeddit-Project\\Files\\pexels-photo-new1.jpg")
