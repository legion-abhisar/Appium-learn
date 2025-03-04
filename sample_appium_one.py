from appium import webdriver
from appium.webdriver.common.appiumby import ByType
from appium.webdriver.extensions.hw_actions import HardwareActions
import time
from appium.webdriver.extensions.action_helpers import ActionHelpers

# Host and Port where Appium is running
HOST = "localhost"
PORT = "4723"

# Desired capabilities
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '13',
    'deviceName': 'Google Pixel 7pro',
    'app': '/apk/com.slot.spin.game.play.apk',
    'appPackage': 'com.slot.spin.game.play',
    'appActivity': 'com.slot.spin.game.play.MainActivity',
    'automationName': 'UiAutomator2'
}

# Appium server URL
appium_server_url = 'http://' + HOST + ':' + PORT + 'wd/hub'

# Initalize driver
driver = webdriver.Remote(appium_server_url, desired_caps)

# try:
    time.sleep(5)

touch_action = ActionHelpers(driver)


