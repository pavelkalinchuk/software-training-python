# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(
            first_name="Для Удаления",
            last_name="Контакт",
            email="delete@mail.com"))
    app.contact.delete_first_contact()
