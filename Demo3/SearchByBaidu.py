from selenium import webdriver

search_text=["selenium","apple","orange"]
for text in search_text:
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(text)
    driver.find_element_by_id("su").click()