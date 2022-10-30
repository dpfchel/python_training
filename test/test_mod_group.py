# -*- coding: utf-8 -*-
from model.group import Group

def test_modificate_first_group(app):
    if app.count('group') == 0:
        app.group.create(Group(name='name_group_for_modify'))
    old_groups = app.group.get_group_list()
    app.group.modificate_first_group(Group(name="modificate_name", header="modificate_header", footer="modificate_footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modificate_name_in_first_group(app):
    if app.count('group') == 0:
        app.group.create(Group(name='name_group_for_modify'))
    old_groups = app.group.get_group_list()
    app.group.modificate_first_group(Group(name="123456789"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modificate_header_and_footer_in_first_group(app):
    if app.count('group') == 0:
        app.group.create(Group(name='name_group_for_modify'))
    old_groups = app.group.get_group_list()
    app.group.modificate_first_group(Group(header="987654321", footer="5555555555"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


