# -*- coding: utf-8 -*-
from model.group import Group
import random
from fixture.application import Application as appl


testdata = [
    Group(name='name1', header='header1', footer='footer1'),
    Group(name='name2', header='header2', footer='footer2')
]

"""   # полный перебор комбинаций
testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", (appl.random_string("name", 10)).strip()]   # strip - удалить пробел с начала и конца строки. Для краевых случаев с пробелами в начале и в конце строки - создаем отдельные тесты.
    for header in ["", appl.random_string("header", 20)]
    for footer in ["", appl.random_string("footer", 20)]
]
"""
