# -*- coding: utf-8 -*-
from model.contact import Contact
import random

# Получение списка контактов из DB, отключаемая проверка UI
def test_del_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="firstname123"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)  # удаляем элемент
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

"""  # Получение списка контактов из UI
def test_del_some_contact(app):
    if app.count('contact') == 0:
        app.contact.create_contact(Contact(firstname="firstname123"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert (len(old_contacts) - 1) == len(new_contacts)
    old_contacts[index:index + 1] = []  # удаляем элемент
    assert old_contacts == new_contacts
"""