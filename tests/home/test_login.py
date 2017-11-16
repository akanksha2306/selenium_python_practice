import unittest

import pytest

from pages.home.login_page import Login_page
from utilities.teststatus import StatusVerify


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = Login_page(self.driver)
        self.ts = StatusVerify(self.driver)



    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("akankshakanjolia@gmail.com", "helloworld")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title Verification")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login Verification")


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("akankshakanjolia@gmail.com", "hellowo23rld")
        result = self.lp.verifyLoginFailed()
        self.ts.markFinal("test_invalidLogin", result, "Invalid login verification")

    @pytest.mark.run(order=3)
    def test_verify_title(self):
        self.lp.verifyLoginTitle()







'''
    def tearDown(self):
        self.driver.quit()
'''
