# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app, json_groups):  # для выбора источника тестовых данных указать или "data_groups" или "json_groups"
    groups = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(groups)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(groups)
    assert sorted(
        old_groups, key=Group.id_or_max) == sorted(
        new_groups, key=Group.id_or_max)
