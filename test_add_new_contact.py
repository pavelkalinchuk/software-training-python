# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time


class TestAddNewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_new_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.authorization(wd, username="admin", password="secret")
        self.add_new_contact(wd, first_name="first_name", last_name="last_name")
        self.return_home_page(wd)
        self.logout(wd)

    def open_home_page(self, wd):
        wd.get("https://localhost/addressbook/")

    def authorization(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def add_new_contact(self, wd, first_name, last_name):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(first_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(last_name)
        wd.find_element_by_name("submit").click()

    def return_home_page(self, wd):
        # Return home page
        wd.find_element_by_link_text("home page").click()
        # Timeout for watching result
        time.sleep(5)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
