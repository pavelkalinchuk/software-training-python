# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_man_contact(app, data_contacts):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new_contact(data_contacts)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(data_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
