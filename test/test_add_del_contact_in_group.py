from model.group import Group
from model.contact import Contact
import random
from fixture.orm import ORMFixture
from fixture.application import Application as appl

def test_add_contact_in_group(app, db, orm):
    rand_num = appl.random_number("_test_add_contact_to_group_", 5)
    firstname = "test_contact" + rand_num
    name = "test_group" + rand_num
    app.contact.create_contact(Contact(firstname=firstname)) # создаем тестовый контакт с уникальным именем
    app.group.create(Group(name=name))  # создаем тестовую группу с уникальным именем

    list_contact_from_db = db.get_contact_list()
    for i in range(len(list_contact_from_db)):
        if list_contact_from_db[i].firstname == firstname:
            test_contact = list_contact_from_db[i]

    list_group_from_db = db.get_group_list()
    for i in range(len(list_group_from_db)):
        if list_group_from_db[i].name == name:
            test_group = list_group_from_db[i]

    # Добавляем контакт в группу
    app.contact.add_contact_to_group(test_contact, test_group)
    assert len(orm.get_contacts_in_group(test_group)) == 1
    assert orm.get_contacts_in_group(test_group)[0] == test_contact

    # Удаляем контакт из группы
    app.contact.del_contact_from_group(test_contact, test_group)
    assert len(orm.get_contacts_in_group(test_group)) == 0

    # Удалим тестовые контакт и группу
    app.contact.delete_contact_by_id(test_contact.id)
    app.group.delete_group_by_id(test_group.id)