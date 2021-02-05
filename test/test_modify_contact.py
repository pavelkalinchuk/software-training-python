# -*- coding: utf-8 -*-
import random

from model.contact import Contact


def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new_contact(Contact(
            first_name="Для Изменения",
            last_name="Контакт",
            email="modify@mail.com"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    contact_update = Contact(
        first_name="first_name modify",
        last_name="last_name modify",
        address="address _modify")
    contact_update.id = contact.id
    app.contact.modify_contact_by_id(contact.id, contact_update)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact_update
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
