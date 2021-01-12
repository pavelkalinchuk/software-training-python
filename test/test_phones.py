# -*- coding: utf-8 -*-
from model.contact import Contact
import re


def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(
            first_name="Тестовый",
            last_name="Контакт",
            address="Москва, ул. Тестовая, 2",
            phone_mobile="+79161112233",
            phone_home="+74951234567",
            phone_work="+74990980908",
            phone_secondary="+78900909090",
            email="test@mail.com"))
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


# def test_phones_on_view_page(app):
#     contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.phone_mobile == contact_from_edit_page.phone_mobile
#     assert contact_from_view_page.phone_home == contact_from_edit_page.phone_home
#     assert contact_from_view_page.phone_work == contact_from_edit_page.phone_work
#     assert contact_from_view_page.phone_secondary == contact_from_edit_page.phone_secondary


def clear(a):
    return re.sub("[() -]", "", a)


def merge_phones_like_on_home_page(contact):
    return "\n".join(
        filter(lambda x: x != "",
               map(lambda x: clear(x),
                   filter(lambda x: x is not None,
                          [contact.phone_home, contact.phone_mobile, contact.phone_work, contact.phone_secondary]))))
