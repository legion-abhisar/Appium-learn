from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Desired capabilities
des_cap = {
    'platformName': 'Android',
    'platformVersion': '10.0',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings'
}

# Appium Driver Initialization
driver = webdriver.Remote('http://localhost:4723', options=des_cap)

# Locator Strategies
el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="id_value")
el2 = driver.find_element(by=AppiumBy.ID, value="id_value")
el3 = driver.find_element(by=AppiumBy.XPATH, value="xpath")
el4 = driver.find_element(by=AppiumBy.CLASS_NAME, value="class_name")

# Element Interaction
el1.click()
el2.send_keys()

##### Advanced ######
from appium.webdriver.extensions.android.activities import Activities

# Retrieves current activity running on the device
Activities.current_activity() 

# Wait for an activity: block until target activity presents or time out
Activities.wait_activity(activity="name_of_activity",
                        timeout=10)
#-------------------------------------------------------------
from appium.webdriver.extensions.android.common import Common

# Retrieves the current package running on the device
Common.current_package()
#-------------------------------------------------------------
from appium.webdriver.extensions.android.network import Network

# Returns an integer bitmask specifying the network connection type
# This API only works reliably on emulators
Network.network_connection()

# Set the network connection type. Android only.
# Possible values:

    # +--------------------+------+------+---------------+
    # | Value (Alias)      | Data | Wifi | Airplane Mode |
    # +====================+======+======+===============+
    # | 0 (None)           | 0    | 0    | 0             |
    # +--------------------+------+------+---------------+
    # | 1 (Airplane Mode)  | 0    | 0    | 1             |
    # +--------------------+------+------+---------------+
    # | 2 (Wifi only)      | 0    | 1    | 0             |
    # +--------------------+------+------+---------------+
    # | 4 (Data only)      | 1    | 0    | 0             |
    # +--------------------+------+------+---------------+
    # | 6 (All network on) | 1    | 1    | 0             |
    # +--------------------+------+------+---------------+
Network.set_network_connection("b001")

# Toggle wifi
Network.toggle_wifi()
#-------------------------------------------------------------
from appium.webdriver.extensions.android.performance import Performance

# Returns the information data types of the system state which is supported
# to read like cpu, memory, network traffic and battery.
Performance.get_performance_data_types()

# Returns the information of the system state which is supported to
# read as like cpu, memory, network traffic and battery
Performance.get_performance_data(package_name="Some name",
                                data_type="cpu",
                                data_read_timeout=10)
#-------------------------------------------------------------
from appium.webdriver.extensions.android.power import Power

# Emulate power capacity change on the connected emulator
Power.set_power_capacity(50)

#-------------------------------------------------------------
from appium.webdriver.extensions.android.sms import Sms

# Emulate send SMS event on the connected emulator
Sms.send_sms(phone_number="9876543210",
            message="Hello Appium")

#-------------------------------------------------------------
from appium.webdriver.extensions.action_helpers import ActionHelpers

action_help = ActionHelpers(driver)

action_help.

# Drag the origin element to the destination element
action_help.drag_and_drop(origin_el="Element to drag",
                            destination_el="Element to drag to",
                            pause=5)

# Scrolls from one element to another
action_help.scroll(origin_el="Element from which to begin scrolling",
            destination_el="element to scroll to",
            duration=5)

# Swipe from one point to another point
action_help.swipe(start_x=10,
                start_y=10,
                end_x=50
                end_y=50,
                duration=400)

# Tap on a particular place with up to five fingers, holding for a certain time
action_help.tap(positions=[(100,20),(100,60),(100,100)],
                duration=500)








