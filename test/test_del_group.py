# -*- coding: utf-8 -*-
from model.group import Group



def test_delete_first_group(app):
    if app.count('group') == 0:
        app.group.create(Group(name='name_group_for_delete'))
    app.group.delete_first_group()
