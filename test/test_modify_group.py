# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_for_modify_group"))

    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    group_update = Group(name="modify_name")
    group_update.id = group.id
    app.group.modify_group_by_id(group.id, group_update)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group_update
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
