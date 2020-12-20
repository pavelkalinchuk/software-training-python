import time


class GroupHelper:

    def __init__(self, appgroup):
        self.appgroup = appgroup

    def fill_group_firm(self, group, wd):
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def open_page_with_groups(self):
        wd = self.appgroup.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.appgroup.wd
        self.open_page_with_groups()
        # Creating new group
        wd.find_element_by_name("new").click()
        self.fill_group_firm(group, wd)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.return_groups_page()
        time.sleep(2)

    def modify_group(self, group):
        wd = self.appgroup.wd
        self.open_page_with_groups()
        # Choosing a group in list
        wd.find_element_by_name("selected[]").click()
        # Pressing Edit button
        wd.find_element_by_xpath("(//input[@name='edit'])[2]").click()
        # Enter modify
        self.fill_group_firm(group, wd)
        # Apply changes
        wd.find_element_by_name("update").click()
        self.return_groups_page()
        time.sleep(2)

    def delete_first_group(self):
        wd = self.appgroup.wd
        self.open_page_with_groups()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.return_groups_page()
        time.sleep(2)

    def return_groups_page(self):
        wd = self.appgroup.wd
        wd.find_element_by_link_text("group page").click()
