from pages.Home.screen import ScreenSave
import pytest
import unittest

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class ScreenTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.scv = ScreenSave(self.driver)

    @pytest.mark.order2
    def test_case_100(self):
        self.scv.takeScreen("https://hypeddit.com/")


