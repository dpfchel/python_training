import pytest

from model.group import Group
from timeit import timeit


def test_group_list(app, db):
    err_list = []
    #print(timeit((lambda: app.group.get_group_list()), number=1))
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    #print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
    #assert False
    ui_list = app.group.get_group_list()
    db_list = map(clean, db.get_group_list())    #  Убираем лишние пробелы с инфы, полученной с БД

    assert_1 = " Sravni without sorting"
    try:
        assert ui_list != db_list, assert_1
    except(AssertionError):
        err_list.append(assert_1)

    assert_2 = "Sravni with zero"
    try:
        assert ui_list != 0, assert_2
    except(AssertionError):
        err_list.append(assert_2)

    assert_3 = "main assert"
    try:
        assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max), assert_3
    except(AssertionError):
        err_list.append(assert_3)

    print(str(err_list))

