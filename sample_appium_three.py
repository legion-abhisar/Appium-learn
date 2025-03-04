from selenium.webdriver.common.by import By
from appium import webdriver

des_cap = {
    'platformName': 'Android',
    'platformVersion': '10.0',
    'deviceName': 'Android Emulator',
    'app': 'path/to/apk'
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", des_cap)

driver.implicitly_wait(20)
driver.find_element(By.ID, "com.flipkart.android:id/select_btn").click()
driver.find_element(By.ID, "com.flipkart.android:id/phone_input").send_keys('9876543210')




