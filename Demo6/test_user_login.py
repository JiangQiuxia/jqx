from time import sleep

from po import Page
from loginPage import LoginPgae
from selenium import webdriver




class Test_User_Login():

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.close()

    def test_user_login1(self,driver,username,password):
        login_page=LoginPgae(driver)
        login_page.open()
        login_page.switch_frame()
        login_page.type_username(username)
        login_page.type_password(password)
        login_page.click_button()




