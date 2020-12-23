# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    app.group.create(Group(
        name="automate name",
        header="automate header",
        footer="automate footer"))


def test_add_new_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
