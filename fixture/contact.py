import time
from model.contact import Contact


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
        time.sleep(2)

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
        if not (wd.current_url.endswith("/addressbook/") and len(
                wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
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

    def count(self):
        wd = self.appcontact.wd
        self.open_page_with_contacts()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.appcontact.wd
        self.open_page_with_contacts()
        contacts = []
        for element1, element2, element3 in zip(
                wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr/td[3]"),
                wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr/td[2]"),
                wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr/td[@class='center']//input")):
            first_name = element1.text
            last_name = element2.text
            id_ = element3.get_attribute("value")
            contacts.append(Contact(first_name=first_name, last_name=last_name, id=id_))
        return contacts
