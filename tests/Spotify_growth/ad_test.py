import pytest
import unittest
from pages.Home.login_pages import LoginPage
from pages.Spotify_growth.ad_pages import AdPage
from pages.Home.fangate_pages import FangatePage
from pages.Spotify_growth.edit_pages import EditPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AdTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.lp = LoginPage(self.driver)
        self.ap = AdPage(self.driver)
        self.fp = FangatePage(self.driver)
        self.ep = EditPage(self.driver)

    @pytest.mark.order2
    def test_AdCreate(self):
        print("running createfnagate")
        self.fp.devUnlock("BetterDevTest8675!")
        self.lp.login("anil@baltech.in", "1234567")


        self.ap.createAd(AdType='track')
        self.ap.createAd(AdType='playlist')
        self.ap.createAd(AdType='artist')
        #self.ep.editAd()

