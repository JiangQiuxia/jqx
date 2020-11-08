import unittest

import pytest
from parameterized import parameterized

from driver.driver import chrome_driver
from page.homepage import Homepage


@pytest.mark.login
class Test_login_in(unittest.TestCase):
    def setUp(self):
        self.driver = chrome_driver()
        self.driver.get("https://mail.163.com/")
        self.homepage = Homepage()

    def tearDown(self):
        self.driver.close()

    # @pytest.mark.parametrize("email, password", [("123", "aaa")])
    @parameterized.expand([("123", "aaa"),("456", "bbb")])
    def test_login_in(self, email, password):
        self.homepage.login_in(self.driver, email, password)
