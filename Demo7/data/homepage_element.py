class Homepage_Element():

    #调用类时，自动执行init方法
    def __init__(self):
        self.email_element = "//input[@name='email']"
        self.password_element = "//input[@name='password']"
        self.checkbox = "//input[@id='un-login']"
        self.login = "//a[@id='dologin']"
        self.enterprise_email = "//*[contains(text(),'企业邮箱')]"
