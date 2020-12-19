# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_group(Group(
        name="modify_name",
        header="modify_header",
        footer="modify_footer"))
    app.session.logout()
