# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(
            first_name="Для Изменения",
            last_name="Контакт",
            email="modify@mail.com"))

    app.contact.modify_contact(Contact(
        first_name="Иван_modify",
        last_name="Иванов_modify",
        address="Москва, ул. Тестовая, 1 _modify"))
