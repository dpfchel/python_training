# -*- coding: utf-8 -*-
from model.group import Group

def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modificate(Group(name="modificate_name", header="modificate_header", footer="modificate_footer"))
    app.session.logout()