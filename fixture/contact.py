import re
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
        self.contact_cache = None
        time.sleep(2)

    def modify_contact(self, contact):
        wd = self.appcontact.wd
        self.open_page_with_contacts()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_firm(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_home_page()
        self.contact_cache = None

    def modify_contact_by_index(self, index, contact):
        wd = self.appcontact.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_firm(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id_, contact_update):
        wd = self.appcontact.wd
        self.open_contact_to_edit_by_id(id_)
        self.fill_contact_firm(contact_update)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_home_page()
        self.contact_cache = None

    def fill_contact_firm(self, contact):
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("address", contact.address)
        self.change_field_value("email", contact.email)
        self.change_field_value("mobile", contact.phone_mobile)
        self.change_field_value("home", contact.phone_home)
        self.change_field_value("work", contact.phone_work)
        self.change_field_value("phone2", contact.phone_secondary)

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

    def select_contact_by_id(self, id_):
        wd = self.appcontact.wd
        wd.find_element_by_css_selector("input[value = '%s' ]" % id_).click()

    def delete_first_contact(self):
        wd = self.appcontact.wd
        self.open_page_with_contacts()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None
        time.sleep(2)

    def delete_contact_by_index(self, index):
        wd = self.appcontact.wd
        self.open_page_with_contacts()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None
        time.sleep(2)

    def delete_contact_by_id(self, id_):
        wd = self.appcontact.wd
        self.open_page_with_contacts()
        self.select_contact_by_id(id_)
        # wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")  # ожидание появления окна с сообщением об удалении
        self.contact_cache = None

    def delete_all_contacts(self):
        wd = self.appcontact.wd
        self.open_page_with_contacts()
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None
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

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.appcontact.wd
            self.open_page_with_contacts()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                first_name = cells[2].text
                last_name = cells[1].text
                address = cells[3].text
                id_ = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_mails = cells[4].text
                self.contact_cache.append(Contact(
                    first_name=first_name,
                    last_name=last_name,
                    address=address,
                    id=id_,
                    all_mails_from_home_page=all_mails,
                    all_phones_from_home_page=all_phones))
        return list(self.contact_cache)  # возвращаем копию кэша

    def get_contact_info_from_edit_page(self, index):
        wd = self.appcontact.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        id_ = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(
            first_name=firstname,
            last_name=lastname,
            address=address,
            id=id_,
            email=email,
            email2=email2,
            email3=email3,
            phone_home=homephone,
            phone_mobile=mobilephone,
            phone_work=workphone,
            phone_secondary=secondaryphone)

    def get_contact_info_from_view_page(self, index):
        wd = self.appcontact.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(
            phone_home=homephone,
            phone_mobile=mobilephone,
            phone_work=workphone,
            phone_secondary=secondaryphone)

    def open_contact_to_edit_by_index(self, index):
        wd = self.appcontact.wd
        self.open_page_with_contacts()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_id(self, id_):
        wd = self.appcontact.wd
        self.open_page_with_contacts()
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % id_).click()
        # wd.find_element_by_partial_link_text("Next")
        # row = wd.find_elements_by_name("entry")[id_]
        # cell = row.find_elements_by_tag_name("td")[7]
        # cell.find_element_by_tag_name("a").click()

    def open_contact_to_view_by_index(self, index):
        wd = self.appcontact.wd
        self.open_page_with_contacts()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()
