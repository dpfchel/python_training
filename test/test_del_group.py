# -*- coding: utf-8 -*-
import random

from model.group import Group
import random



# получаем инфо из БД, перешли на выбор по id
def test_delete_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='name_group_for_delete'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert (len(old_groups) - 1) == len(new_groups)
    old_groups.remove(group)  # удаляем  элемент
    assert old_groups == new_groups


# тест с UI
"""def test_delete_some_group(app):
    if app.count('group') == 0:
        app.group.create(Group(name='name_group_for_delete'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert (len(old_groups) - 1) == len(new_groups)
    old_groups[index:index+1] = []  # удаляем  элемент
    assert old_groups == new_groups"""

