# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app, db, json_groups):  # для выбора источника тестовых данных указать или "data_groups" или "json_groups"
    groups = json_groups
    old_groups = db.get_group_list()
    app.group.create(groups)
    new_groups = db.get_group_list()
    old_groups.append(groups)
    assert sorted(
        old_groups, key=Group.id_or_max) == sorted(
        new_groups, key=Group.id_or_max)
