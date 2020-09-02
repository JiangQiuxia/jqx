from selenium import webdriver

class Page(object):

    login_url="https://www.126.com"

    def __init__(self,selenium_driver,base_url=login_url):
        self.base_url=base_url
        self.driver=selenium_driver
        self.timeout=30
        self.url = './'

    def on_Page(self):
        return self.driver.current_url == (self.base_url+self.url)

    def _open(self,url):
        url=self.base_url+url
        self.driver.get(url)
        assert self.on_Page(),'Did not land on %s' %url

    def open(self):
        self._open(self.url)

    def switch_frame(self):
        self.driver.switch_to.frame(0)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)



