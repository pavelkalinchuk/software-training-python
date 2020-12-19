# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contact(Contact(
        first_name="Иван_modify",
        last_name="Иванов_modify",
        middle_name="",
        address="Москва, ул. Тестовая, 1 _modify",
        email="",
        phone_mobile=""))
    app.session.logout()
