"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""

import os
from selenium import webdriver


class WebDriverFactory():
    def __init__(self, browser, osType, baseUrl):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
        self.osType = osType
        self.baseUrl = baseUrl

    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        #baseURL = "https://letskodeit.teachable.com/"

        if (self.osType not in ["win", "mac", "linux"]):
            self.osType = "mac"


        base_dir = os.path.dirname(__file__)
        resources_dir = os.path.join(base_dir, '../resources/selenium_drivers/%s/'%(self.osType,))

        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver_path = os.path.join(resources_dir, 'geckodriver')
            driver = webdriver.Firefox(executable_path=driver_path)
        elif self.browser == "chrome":
            # Set chrome driver
            driver_path = os.path.join(resources_dir, 'chromedriver')
            driver = webdriver.Chrome(executable_path=driver_path)
        else:
            driver_path = os.path.join(resources_dir, 'geckodriver')
            driver = webdriver.Firefox(executable_path=driver_path)
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(self.baseUrl)
        return driver
