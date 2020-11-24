from appium import webdriver
from time import sleep
def app_driver():
    desired_caps = {"automationName": "UiAutomator2",
                "platformName": "Android",
                "platformVersion": "11",
                "deviceName": "emulator-5554",
                "appPackage": "com.android.chrome",
                "appActivity": "com.google.android.apps.chrome.Main",
                "noReset": "true"}
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    return driver

if __name__ == '__main__':
    app_driver()


