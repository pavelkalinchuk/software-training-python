# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import string
import random


def random_string_fio(maxlen):
    symbols = string.ascii_letters
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_address(maxlen):
    symbols = string.ascii_letters + string.digits + " " * 5
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_email():
    symbols = string.ascii_lowercase + string.digits
    return "".join([random.choice(symbols) for i in range(5)]) + "@" + "".join(
        [random.choice(symbols) for i in range(5)]) + "." + "".join([random.choice(symbols) for i in range(3)])


def random_string_phone():
    symbols = string.digits
    return "+" + "".join([random.choice(symbols) for i in range(11)])


testdata = [
    Contact(
        first_name=random_string_fio(10),
        last_name=random_string_fio(10),
        middle_name=random_string_fio(10),
        address=random_string_address(30),
        email=random_string_email(),
        phone_mobile=random_string_phone(),
        phone_home=random_string_phone(),
        phone_work=random_string_phone(),
        phone_secondary=random_string_phone())
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_man_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    # contact = Contact(
    #     first_name="Иван",
    #     last_name="Иванов",
    #     middle_name="Иванович",
    #     address="Москва, ул. Тестовая, 1",
    #     email="ivan@mail.com",
    #     phone_mobile="+79161234567",
    #     phone_home="+74951234567",
    #     phone_work="+74990980908",
    #     phone_secondary="+78900909090")
    app.contact.add_new_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_women_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(
#         first_name="Ольга",
#         last_name="Ласточка",
#         middle_name="Батьковна",
#         address="Москва, ул. Тестовая, 2",
#         email="olga@mail.com",
#         phone_mobile="+79161112233",
#         phone_home="+74951234567",
#         phone_work="+74990980908",
#         phone_secondary="+78900909090")
#     app.contact.add_new_contact(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
