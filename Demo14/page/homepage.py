from data.driver import app_driver
import selenium
from appium import webdriver

class Open_Baidu():
    driver = app_driver()
    driver.find_element_by_id("com.android.chrome:id/search_box_text").send_keys("https://www.baidu.com")
    # driver.find_element_by_id("com.android.chrome:id/tile_grid_layout").click()



if __name__ == '__main__':
    Open_Baidu

