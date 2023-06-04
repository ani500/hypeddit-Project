import pytest
import unittest
from pages.Home.login_pages import LoginPage
from pages.Spotify_growth.ad_pages import AdPage
from pages.Home.fangate_pages import FangatePage
from pages.Spotify_growth.edit_pages import EditPage
from pages.Exchange.exchange_pages import exchangePage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ExchangeTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.lp = LoginPage(self.driver)
        self.ep = exchangePage(self.driver)
        self.fp = FangatePage(self.driver)


    @pytest.mark.order2
    def test_Exchange(self):
        print("running exchange")
        self.fp.devUnlock("BetterDevTest8675!")
        self.lp.login("dinu@baltech.in", "123456")
        self.ep.openExchangePage()

        self.ep.exchangeClickButton()
        self.ep.fangatePreview("testing009web@gmail.com")

        self.ep.exchangeClickButton()
        self.ep.fangatePreview("testing009web@gmail.com")

        # self.ep.exchangeClickButton()
        # self.ep.fangatePreview("testing008web@gmail.com")
        #
        # self.ep.exchangeClickButton()
        # self.ep.fangatePreview("testing008web@gmail.com")


        # self.ep.exchangeClickButton()
        # self.ep.fangatePreview()



