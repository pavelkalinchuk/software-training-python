# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from appcontact import Appcontact


@pytest.fixture
def appcontact(request):
    fixture = Appcontact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(appcontact):
    appcontact.authorization(username="admin", password="secret")
    appcontact.add_new_contact(Contact(
        first_name="Иван",
        last_name="Иванов",
        middle_name="Иванович",
        address="Москва, ул. Тестовая, 1",
        email="test@mail.com",
        phone_mobile="+79161234567"))
    appcontact.logout()
