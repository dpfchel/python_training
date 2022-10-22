# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="new_2", header="header_2", footer="footer_2"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
