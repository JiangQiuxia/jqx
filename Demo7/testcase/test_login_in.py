import unittest

import pytest
from parameterized import parameterized

from driver.driver import chrome_driver
from page.homepage import Homepage


@pytest.mark.login
class Test_login_in(unittest.TestCase):
    def setUp(self):
        self.driver = chrome_driver()
        self.driver.get("")
        self.homepage = Homepage()

    def tearDown(self):
        self.driver.close()

    @pytest.mark.parametrize("email, password", [("123", "aaa")])
    # @parameterized.expand([("123", "aaa"),("456", "bbb")])
    def test_login_in(self, email, password):
        self.homepage.login_in(self.driver, email, password)

    @pytest.mark.checklink
    def test_page_link(self):
        self.homepage.page_link(self.driver)
