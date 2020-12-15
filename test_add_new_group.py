# -*- coding: utf-8 -*-
import pytest
from group import Group
from appgroup import Application


@pytest .fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="automate name", header="automate header", footer="automate footer"))
    app.logout()


def test_add_new_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
