# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange



def test_delete_some_group(app):
    if app.count('group') == 0:
        app.group.create(Group(name='name_group_for_delete'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert (len(old_groups) - 1) == len(new_groups)
    old_groups[index:index+1] = []  # удаляем  элемент
    assert old_groups == new_groups

