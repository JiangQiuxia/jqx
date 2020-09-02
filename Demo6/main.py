import logging
from time import sleep
import unittest
from selenium import webdriver
from test_user_login import Test_User_Login
from BeautifulReport import BeautifulReport
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

class Main(unittest.TestCase):
    def main1(self):
        try:
            driver = webdriver.Chrome()
            username = 'qiuxia_jiang'
            password = 'aa123456'
            login = Test_User_Login()
            login.test_user_login1(driver, username, password)
            sleep(3)
            login_pass_url = driver.current_url
            assert ('mail163_letter#module=welcome.WelcomeModule%7C%7B%7D' in login_pass_url)
            logger.info('login successfully')
        finally:
            driver.quit()

if __name__ == '__main__':
    suite_cases=unittest.defaultTestLoader.discover(".",pattern="test*.py")
    BeautifulReport(suite_cases).report(filename=time.strftime("%Y-%m-%d %H_%M_%S")+"登录126邮箱报告",description="登录126邮箱",log_path=".")



