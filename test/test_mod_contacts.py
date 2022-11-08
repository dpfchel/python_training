# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange



def test_modificate_contact_home_telephone(app):
    if app.count('contact') == 0:
        app.contact.create_contact(Contact(firstname="firstname123", day_birthday="20", year_anniversary="2020"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(home_telephone="991991991")
    contact.id = old_contacts[index].id
    app.contact.modificate_contact_by_id(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



"""
def test_modificate_contact_all_param(app):
    if app.count('contact') == 0:
        app.contact.create_contact(Contact(firstname="firstname123"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="modificate_firstname", middlename="modificate_middlename1", lastname="modificate_lastname",
                                        nickname="modificate_nick", title="modificate_title", company="modificate_comp", address="modificate_address",
                                        home_telephone="999999999", mobile_telephone="8888", work_telephone="7777",
                                        fax_telephone="66666", email="modificate@mod", email2="modificate@2", email3="modificate@3",
                                        homepage="modificate_homepage", day_birthday="2", month_birthday="March",
                                        year_birthday="1000", day_anniversary="10", month_anniversary="February",
                                        year_anniversary="1010", address2="modificate_", home_phone2="11111111",
                                        notes="modificate_notes_sec")
    contact.id = old_contacts[index].id
    app.contact.modificate_contact_by_id(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    
    """