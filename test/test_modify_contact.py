# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    app.contact.modify_contact(Contact(
        first_name="Иван_modify",
        last_name="Иванов_modify",
        address="Москва, ул. Тестовая, 1 _modify"))
