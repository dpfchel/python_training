# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modificate_contact(app):
    if app.count('contact') == 0:
        app.contact.create_contact(Contact(firstname="firstname123"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="modificate_firstname", middlename="modificate_middlename1", lastname="modificate_lastname",
                                        nickname="modificate_nick", title="modificate_title", company="modificate_comp", address="modificate_address",
                                        home_telephone="999999999", mobile_telephone="8888", work_telephone="7777",
                                        fax_telephone="66666", email="modificate@mod", email2="modificate@2", email3="modificate@3",
                                        homepage="modificate_homepage", day_birthday="2", month_birthday="March",
                                        year_birthday="1000", day_anniversary="10", month_anniversary="February",
                                        year_anniversary="1010", address2="modificate_", home_phone2="11111111",
                                        notes="modificate_notes_sec")
    contact.id = old_contacts[0].id
    app.contact.test_modificate_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modificate_contact_one_field(app):
#    if app.count('contact') == 0:
#        app.contact.create_contact(Contact(firstname="firstname123", day_birthday="20", year_anniversary="2020"))
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(home_telephone="991991991")
#    contact.id = old_contacts[0].id
#    app.contact.test_modificate_contact(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
#    old_contacts[0] = contact
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)