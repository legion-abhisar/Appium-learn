# To perform Zoom In/Out:
# We put two fingers on the screen and then drag them in opposite directions.
# We need 4 points on the screen:
#   1.  Finger 1 starting point
#   2.  Finger 1 ending point
#   3.  Finger 2 starting point
#   4.  Finger 2 ending point

# Zoom In/Out using W3C Mobile Gestures Commands
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

appium_server = "http://127.0.0.1:4723"

# Desired capabilities
contacts = {
    "appium:appPackage": "com.android.contacts",
    "appium:appActivity": ".activities.PeopleActivity",
    "platformName": "Android",
    "appium:automationName": "UiAutomator2"
}

driver = webdriver.Remote(appium_server, contacts)

# Zoom In
driver.execute_script('mobile: pinchOpenGesture', {
    'left': 200,
    'top': 800,
    'width': 1000,
    'height': 1000,
    'percent': 0.5
})

# Zoom out
driver.execute_script('mobile: pinchCloseGesture', {
    'left': 200,
    'top': 800,
    'width': 1000,
    'height': 1000,
    'percent': 0.5
})

