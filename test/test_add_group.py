# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    old_groups = app.group.get_group_list()  # список групп до проведения шагов
    group = Group(name="new_2", header="header_2", footer="footer_2")
    app.group.create(group)  # создали группу
    assert (len(old_groups)+1) == app.count('group')   # кол-во групп до теста + 1 = кол-ву групп после теста
    new_groups = app.group.get_group_list()  # список групп после проведения шагов
    old_groups.append(group)  # к списку групп до теста добавили группу которую создавали и сравним со списком после теста
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    assert (len(old_groups)+1) == app.count('group')    # метод app.count('group') в роли хэш от get_group_list()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_add_some_name_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="some_name", header="", footer="")
    app.group.create(group)
    assert (len(old_groups)+1) == app.count('group')    # метод app.count('group') в роли хэш от get_group_list()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)