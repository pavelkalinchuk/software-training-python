# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from group import Group


def open_home_page(wd):
    wd.get("https://localhost/addressbook/")


def login(wd, username, password):
    open_home_page(wd)
    wd.find_element_by_name("user").click()
    wd.find_element_by_name("user").clear()
    wd.find_element_by_name("user").send_keys(username)
    wd.find_element_by_name("pass").clear()
    wd.find_element_by_name("pass").send_keys(password)
    wd.find_element_by_xpath("//input[@value='Login']").click()


def open_page_with_groups(wd):
    wd.find_element_by_link_text("groups").click()


def create_group(wd, group):
    open_page_with_groups(wd)
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
    return_groups_page(wd)


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
        login(wd, username="admin", password="secret")
        create_group(wd, Group(name="automate name", header="automate header", footer="automate footer"))
        logout(wd)

    def test_add_new_empty_group(self):
        wd = self.wd
        login(wd, username="admin", password="secret")
        create_group(wd, Group(name="", header="", footer=""))
        logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
