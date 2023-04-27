import pytest
import unittest
from pages.Home.login_pages import LoginPage
from pages.Home.fangate_pages import FangatePage
from pages.Home.signup_pages import SignupPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CreateFangateTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.fp = FangatePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.sp = SignupPage(self.driver)


    @pytest.mark.order2
    def test_CreateFangate(self):
        print("running createfnagate")
        self.fp.devUnlock("BetterDevTest8675!")
        self.lp.login("harry@baltech.in", "123456")
        #self.fp.createFangate(Fg="fangate")
        #self.fp.createFangate(Fg="linkgate")
        self.fp.createFangate(Fg="smartlink")


        # result = self.lp.verifyLoginSuccessful()
        # assert result == True

    #@pytest.mark.order1
    #def test_Login(self):
        #self.lp.login("data123@gmail.com", "123456")
        # result = self.lp.verifyLoginSuccessful()
        # assert result == True





