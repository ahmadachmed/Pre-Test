from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from Pages.locator import Locator
import allure


class Register(object):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Register with valid user')
    def register_into_app(self):

        self.register = WebDriverWait(self.driver, 30).until(
            lambda x: x.find_element(MobileBy.ID, Locator.register))
        self.register.click()

        self.namefield = WebDriverWait(self.driver, 30).until(
            lambda x: x.find_element(MobileBy.ID, Locator.namefield))
        self.namefield.send_keys("ahmad ilham")

        self.emailfield = WebDriverWait(self.driver, 30).until(
            lambda x: x.find_element(MobileBy.ID, Locator.emailfield))
        self.emailfield.send_keys("ahmadilham@gmail.com")

        self.passwordfield = WebDriverWait(self.driver, 30).until(
            lambda x: x.find_element(MobileBy.ID, Locator.passwordfield))
        self.passwordfield.send_keys("password!")

        self.repasswordfield = WebDriverWait(self.driver, 30).until(
            lambda x: x.find_element(MobileBy.ID, Locator.repasswordfield))
        self.repasswordfield.send_keys("password!")

        self.registerbtn = WebDriverWait(self.driver, 30).until(
            lambda x: x.find_element(MobileBy.ID, Locator.registerbtn))
        self.registerbtn.click()

        self.validateregister = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(MobileBy.ID, Locator.validateregister))
        assert self.validateregister.text == "Registration Successful"
        allure.attach(self.driver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=allure.attachment_type.PNG)
