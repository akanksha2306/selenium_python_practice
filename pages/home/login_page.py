import logging

import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver


class Login_page(SeleniumDriver):
    '''
    All these locators and log is a class property ,it wont change with every page,(until we want to do),so
    making it s a class property.(static variables they all are)wont change until we change them.
    '''

    log = cl.customLogger(logging.DEBUG)

    # Locators
    _login_Link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_Button = "commit"

    def __init__(self, driver):
        super(Login_page, self).__init__(driver)
        self.driver = driver

    def clickLoginLink(self):
        # self.getLoginLink().click()
        self.elementClick(Login_page._login_Link, "link")

    def enterEmail(self, email):
        # self.getEmailField().send_keys(email)
        self.sendKeys(email, self._email_field, "id")

    def enterPassword(self, password):
        # self.getPasswordField().send_keys(password)
        self.sendKeys(password, self._password_field, "id")

    def clickLoginButton(self):
        # self.getLoginButton().click()
        self.elementClick(self._login_Button, "name")

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("search-courses", locatorType="id")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password')]", locatorType="xpath")
        return result

    def verifyTitle(self):
        if "Let's Kode It" in self.getTitle():
            return True
        else:
            return False
