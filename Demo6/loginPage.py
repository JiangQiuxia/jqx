from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import os

from po import Page


class LoginPgae(Page):
    url = 'https: // www.126.com'
    username_loc=(By.NAME,"email")
    password_loc=(By.NAME,"password")
    button_loc=(By.ID,"dologin")

    def type_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)

    def click_button(self):
        self.find_element(*self.button_loc).click()

# @pytest.mark.parametrize([{"name":"qiuxia","password":"123"},{}])
# @pytest.mark.demo1
# def test_run(name,password):
#     print("test start")
#     driver =webdriver.Chrome()
#     driver.find_element_by_tag_name("html").is_displayed()
#     driver.get_screenshot_as_file('c:/qiuxia/img.png')
#
# if __name__ == '__main__':
#     pytest.main(['-s', os.path.abspath(__file__)])
