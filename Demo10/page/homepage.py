from basepage.page import Page
from data.homepage_element import Homepage_Element


class Homepage(Page,Homepage_Element):
    def login_in(self,driver,email,password):
        self.switch_frame_index(driver,0)
        self.webdriver_wait(driver,20,self.email_element).send_keys(email)
        driver.find_element_by_xpath(self.password_element).send_keys(password)
        checkbox = driver.find_element_by_xpath(self.checkbox).is_selected()
        if not checkbox:
            driver.find_element_by_xpath(self.checkbox).click()
        self.take_screenshot(driver,"homgepage.png")
        driver.find_element_by_xpath(self.login_button).click()
        assert ("success" in driver.current_url),"login failed"