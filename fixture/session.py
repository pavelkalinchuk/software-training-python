class SessionHelper:

    def __init__(self, appgroup):
        self.appgroup = appgroup

    def login(self, username, password):
        wd = self.appgroup.wd
        self.appgroup.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.appgroup.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")
