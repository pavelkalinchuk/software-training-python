# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app, data_groups):
    old_groups = app.group.get_group_list()
    app.group.create(data_groups)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(data_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
