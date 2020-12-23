# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_man_contact(app):
    app.contact.add_new_contact(Contact(
        first_name="Иван",
        last_name="Иванов",
        middle_name="Иванович",
        address="Москва, ул. Тестовая, 1",
        email="ivan@mail.com",
        phone_mobile="+79161234567"))


def test_add_women_contact(app):
    app.contact.add_new_contact(Contact(
        first_name="Ольга",
        last_name="Ласточка",
        middle_name="Батьковна",
        address="Москва, ул. Тестовая, 2",
        email="olga@mail.com",
        phone_mobile="+79161112233"))
