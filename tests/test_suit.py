import unittest
from tests.Home.fangate_test import CreateFangateTests
from tests.Spotify_growth.ad_test import AdTests
from tests.test.mytest import myTestClass

tc1 = unittest.TestLoader().loadTestsFromTestCase(CreateFangateTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(AdTests)
tc3 = unittest.defaultTestLoader.loadTestsFromTestCase(myTestClass)

test = unittest.TestSuite([tc3,tc2])

unittest.TextTestRunner(verbosity=2).run(test)



