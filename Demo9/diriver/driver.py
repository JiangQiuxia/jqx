from selenium import webdriver

def chrome_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def firefox_driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    return driver

def ie_driver():
    driver = webdriver.Ie()
    driver.maximize_window()
    return driver