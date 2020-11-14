import logging
from time import sleep

from Public import loginPage
from selenium import webdriver

class loginTest():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.126.com")


    def test_admin_login(self):
        username='qiuxia_jiang'
        password='aa123456'
        loginPage().user_login(self.driver,username,password)
        sleep(3)
        login_pass_url=self.driver.current_url
        # print(login_pass_url)
        assert('mail163_letter#module=welcome.WelcomeModule%7C%7B%7D'in login_pass_url)
        self.logger.info('login successfully')
        # self.driver.quit()

    # def test_guest_login(self):
    #     username='qiuxia_jiang'
    #     password='aa123456'
    #     loginPage().user_login(self.driver,username,password)
    #     self.driver.quit()

if __name__ == '__main__':
    login=loginTest()
    login.test_admin_login()


    # login.test_guest_login()
