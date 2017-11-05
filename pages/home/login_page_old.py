import logging

from selenium.webdriver.common.by import By

import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver


class Login_page(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    # Locators
    # putting _ means I am making these variables as private

    _login_Link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_Button = "commit"

    '''
    def getLoginLink(self):
        return self.driver.find_element(By.LINK_TEXT, self._login_Link)

    def getEmailField(self):
        return self.driver.find_element(By.ID, self._email_field)

    def getPasswordField(self):
        return self.driver.find_element(By.ID, self._password_field)

    def getLoginButton(self):
        return self.driver.find_element(By.NAME, self._login_Button)    
    '''

    def clickLoginLink(self):
        self.elementClick(self._login_Link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType=id)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType=id)

    def clickLoginButton(self):
        self.elementClick(self._login_Button, locatorType="name")

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyloginSuccessful(self):
        userIcon = driver.find_element(By.ID, "search-courses")
