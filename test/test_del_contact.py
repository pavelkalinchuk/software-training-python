# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(
            first_name="Для Удаления",
            last_name="Контакт",
            email="delete@mail.com"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contact = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contact)
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contact
