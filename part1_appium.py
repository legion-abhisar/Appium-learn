# Main appium driver
from appium import webdriver

# It is used to locate elements
from appium.webdriver.common.appiumby import AppiumBy

# It is used to create a UiAutomator2 driver instance
from appium.options.android import uiautomator2

# W3C compatible gestures helper library created to update driver's default gestures
from appium.webdriver.extensions.action_helpers import ActionHelpers

# W3C compatible libraries to create any gestures rather than driver's default gestures
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction

# Old touch action libraries (Deprecated)
# from appium.webdriver.common.touch_action import TouchAction
# from appium.webdriver.common.multi_action import MultiAction

from time import sleep

appium_server = "http://127.0.0.1:4723"

# Desired capabilities
contacts = {
    "appium:appPackage": "com.android.contacts",
    "appium:appActivity": ".activities.PeopleActivity",
    "platformName": "Android",
    "appium:automationName": "UiAutomator2"
}



