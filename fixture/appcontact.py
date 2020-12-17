from selenium import webdriver
from fixture.session_contact import SessionContHelper
from fixture.contact import ContactHelper


class Appcontact:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session_contact = SessionContHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
