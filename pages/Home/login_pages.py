import time
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as c1
import logging
from pages.Home.locators import Locators


class LoginPage(SeleniumDriver,Locators):
    log = c1.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "login_email"
    _password_field = "login_password"
    _login_button = "login_button"
    _stats_visits = "stats_visit_total"
    # locators for signup page
    _email_field_signup = "signup_email"
    _password_field_signup = "signup_password"
    _firstname_signup = "signup_first_name"
    _lastname_signup = "signup_last_name"
    _signup_link = "Sign Up"
    _signup_button = "/html/body/section[2]/section/section/section/section/div/div[2]/div[3]/form/div[7]/button"
    _signup_CheckBox = "/html/body/section[2]/section/section/section/section/div/div[2]/div[3]/form/div[6]/div[1]/label"

    def clickOnTheLink(self):
        self.elementClick(self._login_link, "link")

    def clickOnTheCheckBox(self):
        self.elementClick(self._signup_CheckBox,"xpath")

    def firstNameSendKeys(self, firstname):
        self.sendKeys(firstname, self._firstname_signup)

    def lastNameSendKeys(self, lastname):
        self.sendKeys(lastname, self._lastname_signup)

    def emailSendKeys(self, email):
        self.sendKeys(email, self._email_field)

    def passwordSendKeys(self, password):
        self.sendKeys(password, self._password_field)

    def emailSendKeys_Signup(self, email):
        self.sendKeys(email, self._email_field_signup)

    def passwordSendKeys_Signup(self, password):
        self.sendKeys(password, self._password_field_signup)

    def clickOnTheSignupLink(self):
        self.elementClick(self._signup_link, "link")

    def clickOnTheLoginButton(self):
        self.elementClick(self._login_button)

    def clickOnTheSignUpButton(self):
        self.elementClick(self._signup_button, "xpath")

    def waitFl(self,loc,lid="id"):
        self.waitForElement(loc,lid,50,.5)

    def clickLogout(self):
        self.elementClick(self.logout_hypeddit(),'xpath')

    def login(self, email="", password="",tag=0):

        if tag in ("simple",0):
            time.sleep(2)
            time.sleep(2)
            self.waitFl(self._login_link, "link")
            self.clickOnTheLink()
            self.clearFields()
            self.emailSendKeys(email)
            self.passwordSendKeys(password)
            self.clickOnTheLoginButton()
            time.sleep(10)
        if tag == "simple":
            self.clickLogout()

            self.waitFl(self._trial_text, 'xpath')
            self.openUrl("https://hypeddit.com/accountsettings")
            self.click3DotMenu()
            self.waitFl(self._logout_hypeddit, 'xpath')
            self.clickLogout()



    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self._stats_visits)
        return result

    def verifyInvalidLoginSuccessful(self):
        result = self.isElementPresent(self._stats_visits)
        return result

    def clearFields(self):
        element = self.getElement(self._email_field)
        element.clear()

        element = self.getElement(self._password_field)
        element.clear()

    def signup(self, firstname, lastname, email, password):
        self.driver.get("https://hypeddit.com/")
        time.sleep(10)
        self.driver.get("https://hypeddit.com/")
        self.clickOnTheLink()
        self.clickOnTheSignupLink()
        self.clearFields_signup()
        self.firstNameSendKeys(firstname)
        self.lastNameSendKeys((lastname))
        self.emailSendKeys_Signup(email)
        self.passwordSendKeys_Signup(password)
        self.clickOnTheCheckBox()
        time.sleep(5)
        self.clickOnTheSignUpButton()

    def clearFields_signup(self):
        element = self.getElement(self._firstname_signup).clear()
        element = self.getElement(self._lastname_signup).clear()
        element = self.getElement(self._email_field_signup).clear()
        element = self.getElement(self._password_field_signup).clear()
