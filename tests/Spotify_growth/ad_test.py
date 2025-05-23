import pytest
import unittest
from pages.Home.login_pages import LoginPage
from pages.Spotify_growth.ad_pages import AdPage
from pages.Home.fangate_pages import FangatePage
from pages.Spotify_growth.edit_pages import EditPage
import os



@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AdTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.lp = LoginPage(self.driver)
        self.ap = AdPage(self.driver)
        self.fp = FangatePage(self.driver)
        self.ep = EditPage(self.driver)

    def test_AdCreate(self):
        print("running createfnagate")
        self.fp.devUnlock("BetterDevTest8675!")
        self.lp.login("arnavangira@mailinator.com", "123456")

        #self.ap.createAd(AdType='track')
        #self.ap.createAd(AdType='playlist')
        #self.ap.createAd(AdType='artist')
        #self.ap.createAd(AdType='fanemail')
        #self.ap.createAd(AdType='presave_reward')
        self.ap.createAd(AdType='presave_smartlink')
        #self.ep.editAd()
