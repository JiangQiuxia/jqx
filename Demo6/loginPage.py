from selenium import webdriver
from selenium.webdriver.common.by import By

from po import Page


class LoginPgae(Page):
    #url='./'
    # driver.switch_to.frame(0)
    url = 'https: // www.126.com'
    username_loc=(By.NAME,"email")
    password_loc=(By.NAME,"password")
    button_loc=(By.ID,"dologin")

    def type_username(self,username):
        self.find_element(self.username_loc).send_keys(username)

    def type_password(self,password):
        self.find_element(self.password_loc).send_keys(password)

    def click_button(self):
        self.find_element(self.button_loc).click()


