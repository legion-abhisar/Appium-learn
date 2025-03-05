# Scroll Up and Down using W3C Actions API
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

appium_server = "http://127.0.0.1:4723"

# Desired capabilities
contacts = {
    "appium:appPackage": "com.android.contacts",
    "appium:appActivity": ".activities.PeopleActivity",
    "platformName": "Android",
    "appium:automationName": "UiAutomator2"
}

driver = webdriver.Remote(appium_server, contacts)

# Scroll Down
# Get origin element (Starting point)
buttons_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Buttons")

# Get destination element (Ending point)
grid_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Grid")

# Perform scroll using driver.scroll()
driver.scroll(origin_el=buttons_el, destination_el=grid_el)

sleep(1)

# Scroll Up
grid_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Grid")
picker_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Picker')
driver.scroll(grid_el, picker_el)

# -----------------------------------------------------------------------------
# Scroll Up and Down using W3C Mobile Gestures Commands

# Scroll Down - with Element
list_view = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="android:id/list")
driver.execute_script('mobile: scrollGesture', {
    'elementId': list_view,
    'direction': 'down',
    'percent': 2
})

# Scroll Up - with Element
list_view = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='android:id/list')
driver.execute_script('mobile: scrollGesture', {
    'elementId': list_view,
    'direction': 'up',
    'percent': 0.5,
    'speed': 1000
})
# -----------------------------------------------------------------------------
# Scroll Bounding Area refers to the allowed aread we can scroll on a scrollable 
# element.
# -----------------------------------------------------------------------------
# Scroll using TouchAction class

from appium.webdriver.common.touch_action import TouchAction

actions = TouchAction(driver)

# Scroll Down (Passing element coordination)
up_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Buttons')
down_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Grid')
actions \
    .press(el=down_el) \
    .move_to(x=up_el.location['x'], y=up_el.location['y']) \
    .release() \
    .perform()

# Scroll Up (Passing element object)
grid_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Grid')
picker_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Picker')
actions \
    .press(el=grid_el) \
    .move_to(el=picker_el) \
    .release() \
    .perform()


















