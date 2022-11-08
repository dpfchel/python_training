# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_del_some_contact(app):
    if app.count('contact') == 0:
        app.contact.create_contact(Contact(firstname="firstname123"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert (len(old_contacts) - 1) == len(new_contacts)
    old_contacts[index:index+1] = []  # удаляем элемент
    assert old_contacts == new_contacts