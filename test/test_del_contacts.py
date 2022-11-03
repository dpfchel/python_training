# -*- coding: utf-8 -*-
from model.contact import Contact

def test_del_contact(app):
    if app.count('contact') == 0:
        app.contact.create_contact(Contact(firstname="firstname123"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert (len(old_contacts) - 1) == len(new_contacts)
    old_contacts[0:1] = []  # удаляем первый элемент
    assert old_contacts == new_contacts