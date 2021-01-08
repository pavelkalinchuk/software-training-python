# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(
            first_name="Для Изменения",
            last_name="Контакт",
            email="modify@mail.com"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(
        first_name="Иван_modify",
        last_name="Иванов_modify",
        address="Москва, ул. Тестовая, 1 _modify")
    contact.id = old_contacts[0].id
    app.contact.modify_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
