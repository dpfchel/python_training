# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
from fixture.application import Application as appl


   # полный перебор комбинаций
testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", (appl.random_string("name", 10)).strip()]   # strip - удалить пробел с начала и конца строки. Для краевых случаев с пробелами в начале и в конце строки - создаем отдельные тесты.
    for header in ["", appl.random_string("header", 20)]
    for footer in ["", appl.random_string("footer", 20)]
]
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()  # список групп до проведения шагов
    app.group.create(group)  # создали группу
    assert (len(old_groups)+1) == app.count('group')   # кол-во групп до теста + 1 = кол-ву групп после теста
    new_groups = app.group.get_group_list()  # список групп после проведения шагов
    old_groups.append(group)  # к списку групп до теста добавили группу которую создавали и сравним со списком после теста
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_group_groupname_have_space_in_border(app):
    group = Group(name="     name     ", header="   header    ", footer="    footer    ")
    old_groups = app.group.get_group_list()  # список групп до проведения шагов
    app.group.create(group)  # создали группу
    assert (len(old_groups)+1) == app.count('group')   # кол-во групп до теста + 1 = кол-ву групп после теста
    new_groups = app.group.get_group_list()  # список групп после проведения шагов
    group.name = (group.name)[5:-5]
    old_groups.append(group)  # к списку групп до теста добавили группу которую создавали и сравним со списком после теста
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)