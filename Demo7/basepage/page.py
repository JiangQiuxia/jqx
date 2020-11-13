import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page():

    def webdriver_wait(self,driver,time,element):
        webdriverWait = WebDriverWait(driver, time).until(EC.visibility_of(driver.find_element_by_xpath(element)))
        return webdriverWait

    def take_screenshot(self,driver,pagename):
        driver.get_screenshot_as_file(r"C:/aQiuxia/Practise/Demo7/image/"+time.strftime("%Y-%m-%d %H_%M_%S-") + pagename)

    def switch_frame_index(self,driver,index):
        driver.switch_to.frame(index)

