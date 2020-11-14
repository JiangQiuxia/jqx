from time import sleep

from parameterized import parameterized

from po import Page
from loginPage import LoginPgae
from selenium import webdriver
import unittest

data = ('qiuxia_jiang', 'aa123456')
data2 = ('qiuxia_jiang', 'aa123456')

class Test_User_Login(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.close()



    @parameterized.expand([data,data2])
    def test_user_login1(self,username,password):
        login_page=LoginPgae(self.driver)
        login_page.open()
        login_page.switch_frame()
        login_page.type_username(username)
        login_page.type_password(password)
        login_page.click_button()




