# coding=utf-8
from selenium import webdriver
import unittest

class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.baidu.com")

    def testBaidu(self):
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()

    def tearDown(self):
        self.diriver.quit()

if __name__ == '__main__':
    unittest.main()