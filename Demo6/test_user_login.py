from time import sleep

from po import Page
from loginPage import LoginPgae



class Test_User_Login():

    def test_user_login1(self,driver,username,password):
        login_page=LoginPgae(driver)
        login_page.open()
        login_page.switch_frame()
        sleep(5)
        login_page.type_username(username)
        login_page.type_password(password)
        login_page.click_button()
