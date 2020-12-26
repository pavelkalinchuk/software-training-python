import time


class GroupHelper:

    def __init__(self, appgroup):
        self.appgroup = appgroup

    def fill_group_firm(self, group):
        # wd = self.appgroup.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.appgroup.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_page_with_groups(self):
        wd = self.appgroup.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.appgroup.wd
        self.open_page_with_groups()
        # Creating new group
        wd.find_element_by_name("new").click()
        self.fill_group_firm(group)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.return_groups_page()
        time.sleep(2)

    def modify_group(self, group):
        wd = self.appgroup.wd
        self.open_page_with_groups()
        # Choosing a group in list
        self.select_first_group()
        # Pressing Edit button
        wd.find_element_by_xpath("(//input[@name='edit'])[2]").click()
        self.fill_group_firm(group)
        # Apply changes
        wd.find_element_by_name("update").click()
        self.return_groups_page()
        time.sleep(2)

    def select_first_group(self):
        wd = self.appgroup.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_group(self):
        wd = self.appgroup.wd
        self.open_page_with_groups()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.return_groups_page()
        time.sleep(2)

    def return_groups_page(self):
        wd = self.appgroup.wd
        wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.appgroup.wd
        self.open_page_with_groups()
        return len(wd.find_elements_by_name("selected[]"))
