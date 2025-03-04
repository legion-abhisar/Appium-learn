from appium import webdriver
from appium.options.android import uiautomator2
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

el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='some value')
el.click()

driver.quit()





