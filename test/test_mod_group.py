# -*- coding: utf-8 -*-
from model.group import Group

def test_modificate_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modificate_first_group(Group(name="modificate_name", header="modificate_header", footer="modificate_footer"))
    app.session.logout()