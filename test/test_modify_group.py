# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    app.group.modify_group(Group(name="modify_name"))
