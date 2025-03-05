# What is tapping?
# Tapping is quickly touching the device with a bit of pressure, similar to clicking
# with a mouse.

# What is the difference between Tap, Click and Press?
# Tap involves use of our fingers to touch the screen, where as click involves using
# input devices like a Mouse or Trackpad. Press can mean two different things:
# pressing a keyboard button or holding down on the touch screen.
# In iOS devices, the amount of pressure applied also matters, as it can perform extra
# actions on the pressed element.

# --------------------------------------------------------------------------------
# Tap (Single | Multi-finger) using W3C Actions API #
# Here we use driver.tap() which is a part of ActionHelpers class.
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
# Using click here
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
# Using tap here - one finger
driver.tap([(0, 500)])
# Using tap here - multi-finger - Max 5
driver.tap([(0,200),(0,300),(0,400),(0,500),(0,600)])

# --------------------------------------------------------------------------------
# Tap using TouchAction class and MultiAction class - depreceated in latest appium

# --------------------------------------------------------------------------------
# Double Tap using W3C Actions API
el_coords = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Add").location

# Perform quickly two taps
driver.tap([(el_coords['x'], el_coords['y'])])
driver.tap([(el_coords['x'], el_coords['y'])])

# --------------------------------------------------------------------------------
# Double Tap using W3C Mobile Gesture Commands - JavaScript
el_coords = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Add").location

# Perform double tap using mobile gestures commands
driver.execute_script(
    'mobile: doubleClickGesture',
    {
        'x': el_coords["x"],
        'y': el_coords['y']
    }
)



















