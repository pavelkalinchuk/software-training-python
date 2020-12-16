# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.appgroup import Application


@pytest .fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(
        name="automate name",
        header="automate header",
        footer="automate footer"))
    app.session.logout()


def test_add_new_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
