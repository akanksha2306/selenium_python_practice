from pages.courses.register_courses_page import Register_courses_page
import unittest

import pytest
from utilities.teststatus import StatusVerify

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Register_course_tests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.rcp = Register_courses_page(self.driver)
        self.ts = StatusVerify(self.driver)




    @pytest.mark.run(order=1)
    def test_Invalid_Enrollment(self):
        self.rcp.enterCourseToEnroll ("Javascript")
        self.rcp.selectCourseToEnroll()
        self.rcp.enterCreditCardinformation("4900000000000086", "1218", "123", "560102")
        # self.rcp.enterCardNumber("4900000000000086")
        # self.rcp.enterCardExp("1218")
        # self.rcp.enterCardCvc("123")
        # self.rcp.enterpostalcode("560102")
        self.rcp.enrollInCourse()
        result = self.rcp.captureErrorMsg()
        self.ts.markFinal("test_Invalid_Enrollment", result, "The card was declined.")






