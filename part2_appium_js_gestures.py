from appium import webdriver
# W3C Mobile Gestures Commands

# In Selenium/Appium, JavaScript commands can be executed using
# driver.execute_script()

# Following are range of commands:
mobile: dragGesture
mobile: flingGesture
mobile: doubleClickGesture
mobile: clickGesture
mobile: longClickGesture
mobile: pinchCloseGesture
mobile: pinchOpenGesture
mobile: swipeGesture
mobile: scrollGesture

# A notable advantage of using these commands is their multi-platform
# compatibility. With a little change in syntax script can run on
# both iOS and Android, eliminating the need for driver-specific
# commands.
appium_server = "http://127.0.0.1:4723"

# Desired capabilities
contacts = {
    "appium:appPackage": "com.android.contacts",
    "appium:appActivity": ".activities.PeopleActivity",
    "platformName": "Android",
    "appium:automationName": "UiAutomator2"
}

driver = webdriver.Remote(appium_server, contacts)

# mobile: longClickGesture
driver.execute_script(
    'mobile: longClickGesture',
    {
        # 'elementId': "Some id"
        'x': 100,   # x-offset coordinate
        'y': 100,   # y-offset coordinate
        'duration': 1000    # Click duration in milliseconds
    }
)

# mobile: doubleClickGesture
driver.execute_script(
    'mobile: doubleClickGesture',
    {
        # 'elementId': "Some id"
        'x': 100,   # x-offset coordinate
        'y': 100    # y-offset coordinate
    }
)

# mobile: clickGesture
driver.execute_script(
    "mobile: clickGesture",
    {
        # 'elementId': "Some id"
        'x': 100,   # x-offset coordinate
        'y': 100    # y-offset coordinate
    }
)

# mobile: pinchOpenGesture
driver.execute_script(
    "mobile: pinchOpenGesture",
    {
        # 'elementId': "Some id"
        'left': 100,
        'top': 100,
        'width': 15,
        'percent': 0.75 # Size of pinch as a percentage of the pinch area size
    }
)

# mobile: pinchCloseGesture
driver.execute_script(
    "mobile: pinchCloseGesture",
    {
        # 'elementId': "Some_id"
        'left': 100,
        'top': 100,
        'percent': 0.75 # Size of pinch as a percentage of the pinch area size
    }
)

# mobile: swipeGesture
driver.execute_script(
    "mobile: swipeGesture",
    {
        'left': 100,
        'top': 100,
        'width': 200,
        'height': 200,
        'direction': 'left', # Accpetable values: up, down, left, right
        'percent': 0.75
    }
)

# mobile: scrollGesture
driver.execute_script(
    "mobile: scrollGesture",
    {
        'left': 100,
        'top': 100,
        'width': 200,
        'height': 200,
        'direction': 'down', # Acceptable values: up, down, left, right
        'percent': 1.0
    }
)


