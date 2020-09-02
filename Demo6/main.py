from time import sleep

from selenium import webdriver
from test_user_login import Test_User_Login

def main():
    try:
        driver=webdriver.Chrome()
        username='qiuxia_jiang'
        password='aa123456'
        login=Test_User_Login()
        login.test_user_login1(driver,username,password)
        sleep(3)
        login_pass_url = driver.current_url
        assert ('mail163_letter#module=welcome.WelcomeModule%7C%7B%7D' in login_pass_url)
    finally:
        driver.quit()

if __name__ == '__main__':
    main()


