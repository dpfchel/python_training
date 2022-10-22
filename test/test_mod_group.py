# -*- coding: utf-8 -*-
from model.group import Group

def test_modificate_first_group(app):
    app.group.modificate_first_group(Group(name="modificate_name", header="modificate_header", footer="modificate_footer"))

def test_modificate_name_in_first_group(app):
    app.group.modificate_first_group(Group(name="123456789"))

def test_modificate_header_and_footer_in_first_group(app):
    app.group.modificate_first_group(Group(header="987654321", footer="5555555555"))
