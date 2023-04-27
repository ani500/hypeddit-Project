import time
from base.selenium_driver import SeleniumDriver

class SignupPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

    #Locators
    _login_link = "Login"
    _signup_link = "Sign Up"
    _first_name = "signup_first_name"
    _last_name = "signup_last_name"
    _signup_email = 'signup_email'
    _signup_pwd = "signup_password"
    _confirm_checkbox ="//div[@class='checkbox']//label[@for='confirm_checkbox']"
    _confirm_checkbox_id = "confirm_checkbox"
    _signup_button= "//button[text()='CREATE TRIAL ACCOUNT']"
    _signup_captcha = "recaptcha-anchor-label"
    _trial_text ="//h2[text()='START YOUR FREE 7-DAY TRIAL']"
    _logout_hypeddit="//ul[@class='dropdown-menu']//input[@name='logout']"
    _3_dot_menu = "//img[@alt='three-dot-menu']"

    #fb signup Locators

    _fb_signup_button ="facebookSignup"
    _facebook_email = "email"
    _facebook_pass = "pass"
    _facebook_login_button = "loginbutton"

    # locators Payment

    _7_day_trial_button = "//a[text()='START FREE TRIAL NOW']"
    _radio_annual = "//div[@class='radio']//label[@for='billing_pro-radio-2']"
    _cc_number ="//input[@autocomplete='cc-number']"
    _mm ="//input[@placeholder='MM']"
    _yy="//input[@placeholder='YY']"
    _cvv="//input[@placeholder='CVV']"
    _postal_code="pay_postal_code"
    _first_name="pay_first_name"
    _last_name="pay_last_name"
    _pay_subscribing="pay_subscribing"
    _pro_text="//span[text()='PRO']"
    _sign_up_button ="//div[@class='annually_pro']//div[@class='upgrade-plan-btn']"


    def clickOnLoginLink(self):
        self.elementClick(self._login_link, "link")

    def clickOnSignUpLink(self):
        self.elementClick(self._signup_link, "link")

    def waitFl(self,loc,lid="id"):
        self.waitForElement(loc,lid,20,.5)

    def firstNameSendKeys(self, fName):
        self.sendKeys(fName, self._first_name)

    def lastNameSendKeys(self, lName):
        self.sendKeys(lName, self._last_name)

    def emailSendKeys(self, email):
        self.sendKeys(email, self._signup_email)

    def passwordSendKeys(self, pwd):
        self.sendKeys(pwd, self._signup_pwd)

    def clickConfirm(self):
        self.checkRadioElementClick(self._confirm_checkbox, "xpath", self._confirm_checkbox_id)

    def clickOnSignupButton(self):
        self.elementClick(self._signup_button,'xpath')

    #fb login

    def clickOnFbSignupButton(self):
        self.elementClick(self._fb_signup_button)

    def fbEmailSendKeys(self, fbEmail):
        self.sendKeys(fbEmail, self._facebook_email)

    def fbPassSendKeys(self, fbEmail):
        self.sendKeys(fbEmail, self._facebook_pass)

    def clickFbLoginButton(self):
        self.elementClick(self._facebook_login_button)

    def openPage(self,url):
        self.openUrl(url)

    def clickLogout(self):
        self.elementClick(self._logout_hypeddit,'xpath')

    def click3DotMenu(self):
        self.elementClick(self._3_dot_menu,'xpath')

    # 7 day trial

    def click7trialButton(self):
        self.elementClick(self._7_day_trial_button,'xpath')

    def clickAnnualRadio(self):
        self.elementClick(self._radio_annual,'xpath')

    def ccSendKeys(self, ccNum):
        self.sendKeys(ccNum, self._cc_number,'xpath')

    def mmSendKeys(self, mm):
        self.sendKeys(mm, self._mm, 'xpath')

    def yySendKeys(self, yy):
        self.sendKeys(yy, self._yy, 'xpath')

    def cvvSendKeys(self, cvv):
        self.sendKeys(cvv, self._cvv, 'xpath')

    def postalCodeSendKeys(self, pCode):
        self.sendKeys(pCode, self._postal_code)

    def firstNameSendKeys(self, fName):
        self.sendKeys(fName, self._first_name)

    def lastNameSendKeys(self, lName):
        self.sendKeys(lName, self._last_name)

    def clickPayButton(self):
        self.elementClick(self._pay_subscribing)

    def clickSignupButton(self):
        self.elementClick(self._sign_up_button,'xpath')



    def signup(self, firstname, lastname, email, password):
        self.openPage("https://shift.hypeddit.com/")
        self.waitFl(self._login_link,'link')
        self.clickOnLoginLink()
        self.waitFl(self._signup_link,'link')
        self.clickOnSignUpLink()
        self.waitFl(self._first_name)
        self.firstNameSendKeys(firstname)
        self.lastNameSendKeys(lastname)
        self.emailSendKeys(email)
        self.passwordSendKeys(password)
        time.sleep(5)
        self.clickConfirm()
        self.waitFl(self._signup_button,'xpath')
        self.clickOnSignupButton()
        self.waitFl(self._trial_text, 'xpath')
        self.openUrl("https://shift.hypeddit.com/accountsettings")
        self.waitFl(self._logout_hypeddit,'xpath')
        self.click3DotMenu()
        self.waitFl(self._logout_hypeddit,'xpath')
        self.clickLogout()



    def fbSignup(self, email, pwd):
        self.openPage("https://shift.hypeddit.com/")
        self.waitFl(self._login_link,'link')
        self.clickOnLoginLink()
        self.waitFl(self._signup_link,'link')
        self.clickOnSignUpLink()

        self.clickOnFbSignupButton()
        time.sleep(2)
        self.switchWindowHander(0)
        time.sleep(2)
        self.fbEmailSendKeys(email)
        time.sleep(2)
        self.fbPassSendKeys(pwd)
        time.sleep(2)
        self.clickFbLoginButton()
        self.switchWindowHander(1)
        time.sleep(3)
        self.waitFl(self._trial_text,'xpath')
        self.openUrl("https://shift.hypeddit.com/accountsettings")
        self.click3DotMenu()
        self.waitFl(self._logout_hypeddit, 'xpath')
        self.clickLogout()
        time.sleep(5)

    def upgradetoFreeTrial(self):
        #self.waitFl(self._7_day_trial_button,'xpath')
        self.click7trialButton()
        self.switchWindowHander(0)
        self.clickAnnualRadio()
        self.clickSignupButton()
        self.switchWindowHander(1)
        self.switchWindowHander(0)
        self.waitFl(self._cc_number,'xpath')
        time.sleep(60)
        self.ccSendKeys("4111 1111 1111 1111")
        self.mmSendKeys("10")
        self.yySendKeys("27")
        self.postalCodeSendKeys("10014")
        self.firstNameSendKeys("anil")
        self.lastNameSendKeys("sharma")
        time.sleep(5)
        self.clickPayButton()
        #self.waitFl(self._pro_text,'xpath')






























