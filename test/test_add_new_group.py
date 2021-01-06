# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(
        name="automate name",
        header="automate header",
        footer="automate footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_new_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
