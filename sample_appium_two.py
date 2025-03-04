from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder


desired_caps = {
    'platformName': 'Android',
    'platformVersion': '10.0',
    'deviceName': 'Android Emulator',
    'app': '/path/to/apk'
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

actions = ActionChains(driver)

actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))

actions.w3c_actions.pointer_action.move_to_location(0, 10)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(2)
actions.w3c_actions.pointer_action.move_to_location(20,20)
actions.w3c_actions.pointer_action.release()
actions.perform()






