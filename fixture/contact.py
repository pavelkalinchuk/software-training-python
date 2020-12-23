import time


class ContactHelper:

    def __init__(self, appcontact):
        self.appcontact = appcontact

    def add_new_contact(self, contact):
        wd = self.appcontact.wd
        self.open_page_with_contacts()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_firm(contact)
        wd.find_element_by_name("submit").click()
        self.return_home_page()

    def modify_contact(self, contact):
        wd = self.appcontact.wd
        self.open_page_with_contacts()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_firm(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_home_page()

    def fill_contact_firm(self, contact):
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("address", contact.address)
        self.change_field_value("email", contact.email)
        self.change_field_value("mobile", contact.phone_mobile)

    def change_field_value(self, field_name, text):
        wd = self.appcontact.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_page_with_contacts(self):
        wd = self.appcontact.wd
        wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        wd = self.appcontact.wd
        self.open_page_with_contacts()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        time.sleep(2)

    def delete_all_contacts(self):
        wd = self.appcontact.wd
        self.open_page_with_contacts()
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        time.sleep(2)

    def return_home_page(self):
        wd = self.appcontact.wd
        # Return home page
        wd.find_element_by_link_text("home page").click()
        # Timeout for watching result
        time.sleep(2)
