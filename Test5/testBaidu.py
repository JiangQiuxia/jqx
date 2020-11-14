import unittest
import time
from selenium import webdriver
from BeautifulReport import BeautifulReport


class Testbaidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.baidu.com")

    def testBaidu(self):
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        title=self.driver.title
        self.assertEqual(title,"unittest_百度搜索")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite_cases=unittest.defaultTestLoader.discover("./",pattern="test*.py")
    BeautifulReport(suite_cases).report(filename=time.strftime("%Y-%m-%d %H_%M_%S")+"百度搜索报告",description="搜索关键字",log_path=".")

