# What is the difference between Scroll, Swipe and Flick?
#
# Scroll: Moving contents of the page within a container (scroll bounding area) to
# 4 main directions (up, down, left, right). It is performed slowly and in a
# controlled manner. We release our finger at the end of the gesture, after we've 
# moved the contents we're searching for into view. We scroll to view content that
# extends beyond the visible area of a screen.

# Swipe: A quick but continuous movement of the finger across the screen in a
# particular direction (usually up/down/right/left as a scroll). It is very close to 
# scrolling but is much faster than it. It is commonly used for various interactions,
# such as navigating between screens or pages in an app, revealing additional
# options or actions (eg. swiping to delete an item in iOS) or switching between 
# different views or tabs

# Flick: It is a rapid movement of the finger across the screen as fast as possible.
# We release our finger while performing a Flick. For example, flicking up quickly
# while paying games like Fruit Ninja Game or Subway Surfer.

# -----------------------------------------------------------------------------
# Swipe Up and Down using W3C Actions API
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

# Swipe Up
buttons_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Buttons")
grid_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Grid')

driver.swipe(
    start_x=buttons_el.location['x'],
    start_y=buttons_el.location['y'],
    end_x=grid_el.location['x'],
    end_y=grid_el.location['y']
)

# Same for Swipe Down - Reverse the start and end.

# -----------------------------------------------------------------------------
# Swipe Up and Down using W3C Gestures Commands

# Swipe Up - With Element
list_view = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='android:id/list')
driver.execute_script('mobile: swipeGesture', {
    'elementId': list_view,
    'direction': 'up',
    'percent': 0.3,
    'speed': 5000
})

# Swipe Down - With Element
driver.execute_script('mobile: swipeGesture', {
    'elementId': list_view,
    'direction': 'down',
    'percent': 0.3,
    'speed': 3000
})








