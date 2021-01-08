# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_man_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(
        first_name="Иван",
        last_name="Иванов",
        middle_name="Иванович",
        address="Москва, ул. Тестовая, 1",
        email="ivan@mail.com",
        phone_mobile="+79161234567")
    app.contact.add_new_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_women_contact(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact(
        first_name="Ольга",
        last_name="Ласточка",
        middle_name="Батьковна",
        address="Москва, ул. Тестовая, 2",
        email="olga@mail.com",
        phone_mobile="+79161112233")
    app.contact.add_new_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
