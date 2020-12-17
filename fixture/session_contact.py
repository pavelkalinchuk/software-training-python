class SessionContHelper:

    def __init__(self, appcontact):
        self.appcontact = appcontact

    def authorization(self, username, password):
        wd = self.appcontact.wd
        self.appcontact.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.appcontact.wd
        wd.find_element_by_link_text("Logout").click()
