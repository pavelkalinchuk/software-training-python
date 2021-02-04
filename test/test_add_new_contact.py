# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_man_contact(app, db,
                         json_contacts):  # для выбора источника тестовых данных указать или "data_groups" или "json_groups"
    contacts = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.add_new_contact(contacts)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contacts)
    assert sorted(
        old_contacts, key=Contact.id_or_max) == sorted(
        new_contacts, key=Contact.id_or_max)
