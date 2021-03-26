from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from Pages.locator import Locator
import allure


class Login(object):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Login with not registered user')
    def login_into_app(self):

        self.email = WebDriverWait(self.driver, 30).until(
            lambda x: x.find_element(MobileBy.ID, Locator.email))
        self.email.send_keys("ahmadilham@gmail.com")

        self.password = WebDriverWait(self.driver, 30).until(
            lambda x: x.find_element(MobileBy.ID, Locator.password))
        self.password.send_keys("password!")

        self.loginbtn = WebDriverWait(self.driver, 30).until(
            lambda x: x.find_element(MobileBy.ID, Locator.loginbtn))
        self.loginbtn.click()

        self.validateLogin = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(MobileBy.ID, Locator.validatelogin))
        assert self.validateLogin.text == "Wrong Email or Password"
        allure.attach(self.driver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=allure.attachment_type.PNG)
