from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as c1
import logging
import time
import pyautogui


class exchangePage(SeleniumDriver):
    log = c1.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _click_ready_button = "//a[@class='button exchange-dw-tooltip button-primary download-ready']"
    _click_notready_button = "//a[@class='button button-light white-tooltip exchange-dw-tooltip']"
    _find_uid = "//div[@id='i_0']"

    # Fangate
    _download_button = "downloadProcess"

    _email_name = "email_name"
    _email_address = "email_address"
    _email_to_download = "email_to_downloads_next"

    _sp_button = "//div[@id='step_sp']//a[@id='login_to_sp']"

    _sp_username = "login-username"
    _sp_password = "login-password"
    _sp_login_button = "//span[contains(text(),'Log In')]"
    _sp_agree_button = "//p[contains(text(),'Agree')]"

    _final_download_button = "//a[@onclick='return downloadUnlimitedGate()']"

    def searchButtonsClick(self):
        return self.getElements(self._click_ready_button, 'xpath')

    def findUids(self):
        return self.getElements(self._find_uid, 'xpath')

    def exchangeCheck(self):
        self.driver.get("https://dev2.hypeddit.com/exchange")
        time.sleep(10)
        uids = self.findUids()
        selects = self.searchButtonsClick()
        if selects:
            # for select in selects:
            # print(select)
            # self.driver.execute_script(
            #   "arguments[0].setAttribute('class', 'button exchange-dw-tooltip button-primary download-ready')",
            #  selects[0])

            self.driver.execute_script(
                "arguments[0].classList.remove('data-toggle')",
                selects[0])

            self.driver.execute_script(
                "arguments[0].classList.remove('data-placement')",
                selects[0])

            self.driver.execute_script(
                "arguments[0].classList.add('data-code')",
                selects[0])

            self.driver.execute_script(
                "arguments[0].setAttribute('data-code', 'ophqbj')",
                selects[0])

            self.driver.execute_script(
                "arguments[0].classList.add('data-played')",
                selects[0])

            self.driver.execute_script(
                "arguments[0].setAttribute('data-played', '1')",
                selects[0])

            self.driver.execute_script(
                "arguments[0].classList.remove('class')",
                selects[0])

            self.driver.execute_script(
                "arguments[0].classList.add('class')",
                selects[0])

            self.driver.execute_script(
                "arguments[0].setAttribute('class', 'button button-primary download-ready')",
                selects[0])
            self.driver.execute_script(
                "arguments[0].classList.remove('title')",
                selects[0])

            self.driver.execute_script(
                "arguments[0].classList.remove('data-original-title')",
                selects[0])

        time.sleep(30)

    def openExchangePage(self):
        self.driver.get("https://dev2.hypeddit.com/exchange")
        time.sleep(10)

    def exchangeClickButton(self):
        print(pyautogui.size())
        time.sleep(5)
        # pyautogui.moveTo(100, 100, duration=1)
        if not self.searchButtonsClick():
            pyautogui.click(791, 501)  # Click Yt track
            # time.sleep(1)
        if not self.searchButtonsClick():
            pyautogui.click(564, 452)  # Click Mixcloud track
            # time.sleep(1)
        if not self.searchButtonsClick():
            pyautogui.click(461, 456)  # Click Sc track
            # time.sleep(1)
        if not self.searchButtonsClick():
            pyautogui.click(616, 465)  # Click Spotify track

        print(pyautogui.position())
        time.sleep(2)

        elements = self.searchButtonsClick()
        if elements:
            elements[0].click()

    def fangatePreview(self, email):
        time.sleep(5)

        self.switchWindowHander(0)
        print("handler switched")

        self.waitFl(self._download_button)
        self.firstDownloadButtonClick()

        if self.waitFl(self._email_to_download):
            self.waitFl(self._email_name)
            self.fNameSendKeys("anil")
            self.emailSendKeys(email)
            self.emailButtonClick()

        if self.waitFl(self._sp_button, 'xpath'):
            print('in sp')
            self.spButtonClick()
            self.switchWindowHander(0)
            self.waitFl(self._sp_username)
            self.spUserNameSendKeys("ashu121@baltech.in")
            self.spPasswordSendKeys("test123456")
            self.waitFl(self._sp_login_button, 'xpath')
            self.spIframeButtonClick()
            self.waitFl(self._sp_agree_button, 'xpath')
            self.spAgreeClick()
            time.sleep(5)
            self.switchWindowHander(1)
            time.sleep(5)

        self.waitFl(self._final_download_button, "xpath")
        self.finalDownloadButtonClick()
        time.sleep(5)
        self.switchWindowHander(1)
        print("final switched")



    def firstDownloadButtonClick(self):
        self.elementClick(self._download_button)

    def waitFl(self, loc, lid="id"):
        return self.waitForElement(loc, lid, 20, .5)

    def fNameSendKeys(self, name):
        self.sendKeys(name, self._email_name)

    def emailSendKeys(self, email):
        self.sendKeys(email, self._email_address)

    def emailButtonClick(self):
        self.elementClick(self._email_to_download)

    def finalDownloadButtonClick(self):
        self.elementClick(self._final_download_button, "xpath")

    def spButtonClick(self):
        self.elementClick(self._sp_button, 'xpath')

    def spUserNameSendKeys(self, uname):
        self.sendKeys(uname,self._sp_username)

    def spPasswordSendKeys(self, pwd):
        self.sendKeys(pwd,self._sp_password)

    def spIframeButtonClick(self):
        self.elementClick(self._sp_login_button, 'xpath')

    def spAgreeClick(self):
        self.elementClick(self._sp_agree_button, 'xpath')
