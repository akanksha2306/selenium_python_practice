"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
import logging
from traceback import print_stack

import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver


class StatusVerify(SeleniumDriver):
    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        """
        Inits CheckPoint class
        """
        super(StatusVerify, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result == True:
                self.resultList.append("PASS")
                self.log.info("### VERIFICATION SUCCESSFUL :: + " + resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                self.screenShot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception Occurred !!!")
            self.screenShot(resultMessage)
            print_stack()

    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.setResult(result, resultMessage)

        print self.resultList

        if "FAIL" in self.resultList:
            self.log.error(testName + " ### TEST FAILED")
            del self.resultList[:]
            assert False
        else:
            self.log.info(testName + " ### TEST SUCCESSFUL")
            del self.resultList[:]
            assert True
