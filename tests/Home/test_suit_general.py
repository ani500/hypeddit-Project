import unittest
from tests.Home.signup_test import GeneralTests
from tests.Home.fangate_test import CreateFangateTests

tc1 = unittest.TestLoader().loadTestsFromTestCase(GeneralTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(CreateFangateTests)


test = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(test)