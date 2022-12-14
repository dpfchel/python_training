# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


# Получение списка контактов из DB, отключаемая проверка UI
def test_modificate_group_name_head_foot(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='name_group_for_modify'))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="modificate_name", header="modificate_header", footer="modificate_footer")
    group.id = old_groups[index].id
    app.group.modificate_group_by_id(group)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(app.group.get_group_list(), key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_modificate_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='name_group_for_modify'))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="123456789")
    group.id = old_groups[index].id
    app.group.modificate_group_by_id(group)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(app.group.get_group_list(), key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_modificate_group_head_foot(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='name_group_for_modify'))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(header="987654321", footer="5555555555")
    group.id = old_groups[index].id
    app.group.modificate_group_by_id(group)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(app.group.get_group_list(), key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# # Получение списка контактов из UI
"""def test_modificate_group_head_foot(app):
    if app.count('group') == 0:
        app.group.create(Group(name='name_group_for_modify'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(header="987654321", footer="5555555555")
    group.id = old_groups[index].id
    app.group.modificate_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)"""