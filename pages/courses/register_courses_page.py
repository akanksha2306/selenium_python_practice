import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver


class Register_courses_page(BasePage):

    log = cl.customLogger(logging.DEBUG)

    #Locators

    _search_box_id = "search-courses"
    _course_xpath = "/html/body/div/div/div/div[2]/div/div/div[1]/a/div/div[2]"
    _search_btn_id = "search-course-button"
    _enroll_button_id = "enroll-button-top" # type is id
    _cc_id= "payment_method_credit_card" #type is id
    _credit_card_num_name = "cardnumber" #type is id
    _cc_exp_name = "exp-date"
    _cc_cvc_name = "cvc"
    _postal_field_name = "postal"
    _submit_enroll_id = "confirm-purchase" #id
    _enroll_error_message_class = "cc__error alert-danger" # class


    def __init__(self, driver):
        super(Register_courses_page, self).__init__(driver)
        self.driver = driver

    def enterCourseToEnroll(self, Name):
        self.sendKeys(Name, self._search_box_id, "id")
        self.elementClick(self._search_btn_id, "id")
        #put a wait command here,becoz it will load

    def selectCourseToEnroll(self):
        # not sure about the link text
        self.elementClick(self._course_xpath, "xpath")
        #put wait statements
        self.elementClick(self._enroll_button_id, "id")

    def enterCardNumber(self, cardNumber):
        #__privateStripeFrame6

        self.webScroll("down", self._postal_field_name, "name")
        #self.webScroll("down")
        #switch to frame using id
        time.sleep(1)
        self.driver.switch_to_frame(self.getElement("__privateStripeFrame3", "name"))
        time.sleep(2)
        self.sendKeys(cardNumber, self._credit_card_num_name, "name")
        self.driver.switch_to_default_content()

    def enterCardExp(self,exp):
        #time.sleep(1)
        self.driver.switch_to_frame(self.getElement("__privateStripeFrame4", "name"))
        time.sleep(2)
        self.sendKeys(exp, self._cc_exp_name,"name")
        self.driver.switch_to_default_content()

    def enterCardCvc(self,cvc):
        #time.sleep(1)
        self.driver.switch_to_frame(self.getElement("__privateStripeFrame5", "name"))
        time.sleep(2)
        self.sendKeys(cvc, self._cc_cvc_name,"name")
        self.driver.switch_to_default_content()

    def enterpostalcode(self,postalcode):
        self.driver.switch_to_frame(self.getElement("__privateStripeFrame6", "name"))
        time.sleep(2)
        self.sendKeys(postalcode, self._postal_field_name,"name")
        self.driver.switch_to_default_content()

    def enrollInCourse(self):
        self.elementClick(self._submit_enroll_id, "id")

    def enterCreditCardinformation(self, cardNumber, exp, cvc, postal_code):
        self.enterCardNumber(cardNumber)
        self.enterCardExp(exp)
        self.enterCardCvc(cvc)
        self.enterpostalcode(postal_code)

    def captureErrorMsg(self):
        error_msg = "Hint : check for exception"
        try:
            error_msg = self.getElement(self._enroll_error_message_class, "class")
        except:
            raise
        return error_msg


















