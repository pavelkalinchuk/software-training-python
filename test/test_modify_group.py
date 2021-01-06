# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_for_delete_group"))
    old_groups = app.group.get_group_list()
    app.group.modify_group(Group(name="modify_name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
