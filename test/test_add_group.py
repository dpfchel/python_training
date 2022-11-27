# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
from fixture.application import Application as appl
#from data.add_group import testdata
#from data.group import constant as testdata


#@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])

# Получение списка контактов из DB, отключаемая проверка UI
def test_add_group(app, db, json_dataset_group, check_ui):
    group = json_dataset_group
    old_groups = db.get_group_list()  # список групп до проведения шагов
    app.group.create(group)  # создали группу
    #assert (len(old_groups)+1) == app.count('group')   # кол-во групп до теста + 1 = кол-ву групп после теста
    new_groups = db.get_group_list()  # список групп после проведения шагов
    old_groups.append(group)  # к списку групп до теста добавили группу которую создавали и сравним со списком после теста
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(app.group.get_group_list(), key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


"""
def test_add_group_groupname_have_space_in_border(app, db):
    group = Group(name="     name1     ", header="   header1    ", footer="    footer1    ")
    #old_groups = app.group.get_group_list()  # список групп до проведения шагов
    old_groups = db.get_group_list()
    app.group.create(group)  # создали группу
    # хеширование не нужно, тк. работаем с БД
    #assert (len(old_groups)+1) == app.count('group')   # кол-во групп до теста + 1 = кол-ву групп после теста
    #new_groups = app.group.get_group_list()  # список групп после проведения шагов
    new_groups = db.get_group_list()
    #group.name = (group.name)[5:-5] # для проверкок через UI - пробелы удаляются
    group.name = (group.name)  # для проверкок через DB - пробелы не удаляются
    old_groups.append(group)  # к списку групп до теста добавили группу которую создавали и сравним со списком после теста
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    
"""
#из набора данных удалил пробелы в середине слов.
# При работе с БД из набора данных удалил двойной обратный слеш  \\
