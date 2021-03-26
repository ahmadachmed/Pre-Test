from appium import webdriver as AppiumDriver
from Pages.login import Login
import allure

@allure.severity(severity_level='CRITICAL')
def test_login_UnregisteredUser():
    Desired_Capabilities = {
        'automationName': 'UIAutomator2',
        'platformName': 'Android',
        'platformVersion': '9',
        'udid': 'c488dea0',
        'deviceName': 'test',
        'appActivity': 'com.loginmodule.learning.activities.LoginActivity',
        'appPackage': 'com.loginmodule.learning',
        'newCommandTimeout': 60,
    }
    driver = AppiumDriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=Desired_Capabilities)
    login = Login(driver)

    login.login_into_app()

    driver.quit()