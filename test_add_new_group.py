# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from group import Group


def open_home_page(wd):
    wd.get("https://localhost/addressbook/")


def login(wd, username, password):
    wd.find_element_by_name("user").click()
    wd.find_element_by_name("user").clear()
    wd.find_element_by_name("user").send_keys(username)
    wd.find_element_by_name("pass").clear()
    wd.find_element_by_name("pass").send_keys(password)
    wd.find_element_by_xpath("//input[@value='Login']").click()


def open_page_with_groups(wd):
    wd.find_element_by_link_text("groups").click()


def create_group(wd, group):
    # Creating new group
    wd.find_element_by_name("new").click()
    # Fill group firm
    wd.find_element_by_name("group_name").click()
    wd.find_element_by_name("group_name").clear()
    wd.find_element_by_name("group_name").send_keys(group.name)
    wd.find_element_by_name("group_header").clear()
    wd.find_element_by_name("group_header").send_keys(group.header)
    wd.find_element_by_name("group_footer").clear()
    wd.find_element_by_name("group_footer").send_keys(group.footer)
    # Submit group creation
    wd.find_element_by_name("submit").click()


def return_groups_page(wd):
    wd.find_element_by_link_text("group page").click()


def logout(wd):
    wd.find_element_by_link_text("Logout").click()


class TestAddNewGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_new_group(self):
        wd = self.wd
        open_home_page(wd)
        login(wd, username="admin", password="secret")
        open_page_with_groups(wd)
        create_group(wd, Group(name="automat name", header="automat header", footer="automat footer"))
        return_groups_page(wd)
        logout(wd)

    def test_add_new_empty_group(self):
        wd = self.wd
        open_home_page(wd)
        login(wd, username="admin", password="secret")
        open_page_with_groups(wd)
        create_group(wd, Group(name="", header="", footer=""))
        return_groups_page(wd)
        logout(wd)

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    @property
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
