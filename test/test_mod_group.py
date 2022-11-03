# -*- coding: utf-8 -*-
from model.group import Group

def test_modificate_first_group(app):
    if app.count('group') == 0:
        app.group.create(Group(name='name_group_for_modify'))
    old_groups = app.group.get_group_list()
    group = Group(name="modificate_name", header="modificate_header", footer="modificate_footer")
    group.id = old_groups[0].id
    app.group.modificate_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_modificate_name_in_first_group(app):
    if app.count('group') == 0:
        app.group.create(Group(name='name_group_for_modify'))
    old_groups = app.group.get_group_list()
    group = Group(name="123456789")
    app.group.modificate_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_modificate_header_and_footer_in_first_group(app):
    if app.count('group') == 0:
        app.group.create(Group(name='name_group_for_modify'))
    old_groups = app.group.get_group_list()
    group = Group(header="987654321", footer="5555555555")
    app.group.modificate_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

