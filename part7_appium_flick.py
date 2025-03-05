# -----------------------------------------------------------------------------
# Flick using W3C Actions API

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

# Flick up
buttons_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Buttons')
grid_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Grid')

driver.flick(
    start_x=grid_el.location['x'],
    start_y=grid_el.location['y'],
    end_x=buttons_el.location['x'],
    end_y=buttons_el.location['y']
)

# Flick down
driver.flick(
    start_x=buttons_el.location['x'],
    start_y=buttons_el.location['y'],
    end_x=grid_el.location['x'],
    end_y=grid_el.location['y']
)

# -----------------------------------------------------------------------------
# Flick using W3C Gestures Commands

list_view = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='android:id/list')
list_view_rect = list_view.rect

# Flick/fling using elementId
driver.execute_script('mobile: flingGesture', {
    'elementId': list_view,
    'direction': 'down',
    'percent': 1
})

# Flick/fling using coordinates
driver.execute_script('mobile: flingGesture', {
    'left': list_view_rect['x'],
    'right': list_view_rect['y'],
    'direction': 'up',
    'width': list_view_rect['width'],
    'height': list_view_rect['height'],
    'percent': 2
})

