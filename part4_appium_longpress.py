# Long Press gesture is typically used to make the item under press draggable or
# to open modification options like Deletion, Edit or Select

# We have 3 ways:
#   1.  Using W3C Actions API
#   2.  Using W3C Mobile Gestures Commands
#   3.  Using TouchAction class - depreceated

# ------------------------------------------------------------------------------
# Press and Hold using W3C Actions API
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction

appium_server = "http://127.0.0.1:4723"

# Desired capabilities
contacts = {
    "appium:appPackage": "com.android.contacts",
    "appium:appActivity": ".activities.PeopleActivity",
    "platformName": "Android",
    "appium:automationName": "UiAutomator2"
}

driver = webdriver.Remote(appium_server, contacts)

# Get all contacts in the list
contacts = driver.find_elements(by=AppiumBy,
                        value="com.android.contacts:id/cliv_name_textview")

# Create an instance from ActionChains class
actions = ActionChains(driver)

# Create a "touch" type of pointer input. By default it is "mouse"
touch_input = PointerInput(interaction.POINTER_TOUCH, 'touch')

# Override pointer action as 'touch'
actions.w3c_actions = ActionBuilder(mouse=touch_input)

# Press and Hold using W3C actions on first contact
actions.w3c_actions.pointer_action.click_and_hold(contacts[0])
actions.perform()

# Flow of commands:
# Find contacts element -> 
# Create an instance of ActionChains to create w3c_actions ->
# Create a PointerInput as touch ->
# Create an ActionBuilder responsible for using our created PointerInput ->
# Finally, we use the click_and_hold method of PointerActions clas.

# ------------------------------------------------------------------------------
# Press and Hold using W3C Gestures Commands

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

contacts = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="some_id")

# Get element coordinates (position in the page)
element_coord = contacts[0].location

# Long press using W3C Mobile Gestures Commands
driver.execute_script(
    'mobile: longClickGesture', 
    {
        'x': element_coord['x'],
        'y': element_coord['y'],
        'duration': 1000    # 1000 milliseconds = 1 second
    }
)

# ------------------------------------------------------------------------------
# Press and Hold using TouchAction class

contacts = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="some_id")

actions = TouchAction(driver)

actions.press(el=contacts[0]).wait(ms=1000).release().perform()




