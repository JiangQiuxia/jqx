from basepage.page import Page
from driver.driver import chrome_driver
from data.homepage_element import Homepage_Element


class Homepage(Page, Homepage_Element):

    # def __init__(self):
    #     Homepage_Element = ()
    # 类中的所有方法里面第一个参数需要传入self
    def login_in(self, driver, email, password):
        # 隐式等待；显示等待和隐式等待两个中只需要用一个方法，显式等待提高脚本性能，一般使用显式等待；
        # driver.implicitly_wait(10)

        self.switch_frame_index(driver, 0)
        # 显式等待；self代表类本身，所以类继承了其他类时，其他类的方法就属于这个类，可以直接用self调用
        # 显式等待只等待某一个具体元素，而隐式等待属于全局等待，每一步都要等待，所以显式等待可以提高脚本性能
        self.webdriver_wait(driver, 20, self.email_element).send_keys(email)

        self.webdriver_wait(driver, 20, self.password_element).send_keys(password)

        checkBox = driver.find_element_by_xpath(self.checkbox).is_selected()
        if not checkBox:
            driver.find_element_by_xpath(self.checkbox).click()

        self.take_screenshot(driver, "homepage.png")

        driver.find_element_by_xpath(self.login).click()

        assert ("success" in driver.current_url), "login failed"

# main函数只有在当前文件才会执行
if __name__ == '__main__':
    TestDemo7 = Homepage()
    TestDemo7.login_in(chrome_driver())
