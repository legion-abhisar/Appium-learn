# Drag and Drop consists of 4 actions:
#   1.  Moving to point A (starting point)
#   2.  Holding the finger to pick items
#   3.  Draggin to point B (ending point)
#   4.  Release the finger to drop

# -----------------------------------------------------------------------------
#   Drag and Drop using W3C Actions API
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

# Drag and Drop
drag_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='drag-c1')
drop_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='drop-c1')

driver.drag_and_drop(
    origin_el=drag_el,
    destination_el=drop_el
)

# -----------------------------------------------------------------------------
#   Drag and Drop using W3C Gestures Commands
driver.execute_script('mobile: dragGesture', {
    'elementId': drag_el,
    'endX': drop_el.location['x'],
    'endY': drop_el.location['y']
})








