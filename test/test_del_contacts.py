# -*- coding: utf-8 -*-
from model.contact import Contact

def test_del_contact(app):
    if app.count('contact') == 0:
        app.contact.create_contact(Contact(firstname="firstname123"))
    app.contact.delete_first_contact()
