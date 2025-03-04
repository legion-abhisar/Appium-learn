from appium import webdriver
from appium.options.android.uiautomator2 import 
from appium.webdriver.common.appiumby import AppiumBy

des_cap = {
    'platformName': 'Android',
    'platformVersion': '10.0',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings'
}

appium_server_url = 'http://localhost:4723'

driver = webdriver.Remote(appium_server_url, des_cap)

