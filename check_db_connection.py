# Var4 - get_contacts in group (ORM)

from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')

try:
    l = db.get_contacts_in_group(Group(id="1"))       # получим список контактов
    #l = db.get_contacts_not_in_groups(Group(id="479"))  # получим список контактов
    for item in l:
        print(item)
    print(len(l))
finally:
    pass



# Третий вариант - для доступа через ORM
"""from fixture.orm import ORMFixture

db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')

try:
    # l = db.get_group_list()       # получим список групп
    l = db.get_contact_list()       # получим список контактов
    for item in l:
        print(item)
    print(len(l))
finally:
    pass

"""


# Второй вариант - для доступа напрямую в БД
"""from fixture.db import DbFixture

db = DbFixture(host='127.0.0.1', name='addressbook', user='root', password='')

try:
    groups = db.get_group_list()
    for group in groups:
        print(group)
    print(len(groups))
finally:
    db.destroy()"""


# Первый вариант - доступ через UI
"""import mysql.connector

connection =  mysql.connector.connect(host='127.0.0.1', database='addressbook', user='root', password='')

try:
    cursor =connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()"""